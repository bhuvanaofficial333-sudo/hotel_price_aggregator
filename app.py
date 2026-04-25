from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from data_source import aggregate_prices
from datetime import datetime
import sqlite3
import os
import matplotlib.pyplot as plt
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "supersecretkey"

DATABASE = "database.db"


def init_db():

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT,
        password TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS search_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        location TEXT,
        checkin TEXT,
        checkout TEXT,
        guests INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS bookings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        hotel TEXT,
        location TEXT,
        final_price REAL
    )
    """)

    conn.commit()
    conn.close()


init_db()

# EMAIL FUNCTION
def send_email(to_email, subject, body):

    sender = "your_email@gmail.com"
    password = "your_app_password"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(sender,password)
        server.sendmail(sender,to_email,msg.as_string())
        server.quit()
    except:
        print("Email failed")


# REGISTER
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        try:
            c.execute(
                "INSERT INTO users(username,email,password) VALUES(?,?,?)",
                (username,email,password)
            )
            conn.commit()
        except:
            return "Username already exists"

        conn.close()

        return redirect("/login")

    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        if "robot_check" not in request.form:
            return "Confirm robot check"

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()

        conn.close()

        if user and check_password_hash(user[3], password):

            session["user"] = username
            return redirect("/")

        return "Invalid login"

    return render_template("login.html")


# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# HOME
@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

    return render_template("index.html")


# SEARCH
@app.route("/search", methods=["POST"])
def search():

    username = session["user"]

    location = request.form["location"]
    checkin = request.form["checkin"]
    checkout = request.form["checkout"]
    guests = int(request.form["guests"])
    min_rating = float(request.form["min_rating"])
    sort_option = request.form["sort_option"]

    checkin_date = datetime.strptime(checkin,"%Y-%m-%d")
    checkout_date = datetime.strptime(checkout,"%Y-%m-%d")

    nights = (checkout_date - checkin_date).days

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute("""
    INSERT INTO search_history(username,location,checkin,checkout,guests)
    VALUES(?,?,?,?,?)
    """,(username,location,checkin,checkout,guests))

    conn.commit()
    conn.close()

    data = aggregate_prices()

    filtered = data[data["location"] == location]
    filtered = filtered[filtered["rating"] >= min_rating]

    filtered["original_price"] = filtered["price"] * nights * guests

    discount = 0
    if nights >= 3:
        discount += 10
    if guests >= 4:
        discount += 5

    discount = min(discount,15)

    filtered["final_price"] = filtered["original_price"] * (1-discount/100)

    if sort_option == "price_low":
        filtered = filtered.sort_values(by="final_price")

    if sort_option == "price_high":
        filtered = filtered.sort_values(by="final_price",ascending=False)

    if sort_option == "rating_high":
        filtered = filtered.sort_values(by="rating",ascending=False)

    hotels = filtered.to_dict(orient="records")

    best_deal = filtered.sort_values(by="final_price").iloc[0]["hotel"]

    plt.figure()
    plt.bar(filtered["hotel"], filtered["final_price"])
    plt.xticks(rotation=45)
    plt.tight_layout()

    if not os.path.exists("static"):
        os.makedirs("static")

    plt.savefig("static/chart.png")
    plt.close()

    return render_template(
        "results.html",
        hotels=hotels,
        location=location,
        nights=nights,
        guests=guests,
        best_deal=best_deal
    )


# HOTEL GALLERY PAGE
@app.route("/hotel/<hotel_name>")
def hotel_page(hotel_name):

    data = aggregate_prices()

    hotel = data[data["hotel"] == hotel_name].iloc[0]

    return render_template("hotel.html", hotel=hotel)


# BOOK
@app.route("/book", methods=["POST"])
def book():

    username = session["user"]

    hotel = request.form["hotel"]
    location = request.form["location"]
    price = request.form["final_price"]

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute("SELECT email FROM users WHERE username=?", (username,))
    email = c.fetchone()[0]

    c.execute("""
    INSERT INTO bookings(username,email,hotel,location,final_price)
    VALUES(?,?,?,?,?)
    """,(username,email,hotel,location,price))

    conn.commit()
    conn.close()

    send_email(
        email,
        "Hotel Booking Confirmed",
        f"Your booking at {hotel} in {location} is confirmed.\nTotal Price: ₹{price}"
    )

    return render_template(
        "booking_success.html",
        hotel=hotel,
        location=location,
        price=price
    )


if __name__ == "__main__":
    app.run(debug=True)