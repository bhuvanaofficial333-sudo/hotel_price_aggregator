import pandas as pd


def fetch_booking_data():

    data = [
        {
            "hotel": "Taj Hotel",
            "location": "Hyderabad",
            "price": 5000,
            "rating": 4.5,
            "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945"
        },

        {
            "hotel": "Novotel",
            "location": "Hyderabad",
            "price": 4500,
            "rating": 4.2,
            "image": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa"
        },

        {
            "hotel": "ITC Kohenur",
            "location": "Hyderabad",
            "price": 6000,
            "rating": 4.7,
            "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4"
        },

        {
            "hotel": "The Leela",
            "location": "Mumbai",
            "price": 7500,
            "rating": 4.8,
            "image": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb"
        },

        {
            "hotel": "Trident",
            "location": "Mumbai",
            "price": 6800,
            "rating": 4.4,
            "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd"
        },

        {
            "hotel": "Radisson Blu",
            "location": "Delhi",
            "price": 5500,
            "rating": 4.3,
            "image": "https://images.unsplash.com/photo-1564501049412-61c2a3083791"
        },

        {
            "hotel": "The Oberoi",
            "location": "Delhi",
            "price": 8200,
            "rating": 4.9,
            "image": "https://images.unsplash.com/photo-1501117716987-c8e1ecb210c1"
        },

        {
            "hotel": "ITC Gardenia",
            "location": "Bangalore",
            "price": 6200,
            "rating": 4.6,
            "image": "https://images.unsplash.com/photo-1590490360182-c33d57733427"
        },

        {
            "hotel": "The Park",
            "location": "Bangalore",
            "price": 4800,
            "rating": 4.1,
            "image": "https://images.unsplash.com/photo-1559599238-308793637427"
        },

        {
            "hotel": "Marriott",
            "location": "Hyderabad",
            "price": 6500,
            "rating": 4.6,
            "image": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2"
        },

{
    "hotel": "Hyatt Regency",
    "location": "Hyderabad",
    "price": 7000,
    "rating": 4.7,
    "image": "https://images.unsplash.com/photo-1551776235-dde6d482980b"
},

{
    "hotel": "Lemon Tree",
    "location": "Hyderabad",
    "price": 3500,
    "rating": 4.0,
    "image": "https://images.unsplash.com/photo-1584132967334-10e028bd69f7"
},

{
    "hotel": "JW Marriott",
    "location": "Mumbai",
    "price": 9000,
    "rating": 4.8,
    "image": "https://images.unsplash.com/photo-1521783593447-5702b9bfd267"
},

{
    "hotel": "Holiday Inn",
    "location": "Delhi",
    "price": 5200,
    "rating": 4.2,
    "image": "https://images.unsplash.com/photo-1590490360182-c33d57733427"
},

{
    "hotel": "Vivanta",
    "location": "Bangalore",
    "price": 5800,
    "rating": 4.5,
    "image": "https://images.unsplash.com/photo-1501117716987-c8e1ecb210c1"
}
    ]

    return pd.DataFrame(data)


def fetch_expedia_data():

    data = [
        {
            "hotel": "Taj Hotel",
            "location": "Hyderabad",
            "price": 4800,
            "rating": 4.5,
            "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945"
        },

        {
            "hotel": "Novotel",
            "location": "Hyderabad",
            "price": 4700,
            "rating": 4.2,
            "image": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa"
        },

        {
            "hotel": "ITC Kohenur",
            "location": "Hyderabad",
            "price": 5900,
            "rating": 4.7,
            "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4"
        },

        {
            "hotel": "The Leela",
            "location": "Mumbai",
            "price": 7200,
            "rating": 4.8,
            "image": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb"
        },

        {
            "hotel": "Trident",
            "location": "Mumbai",
            "price": 7000,
            "rating": 4.4,
            "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd"
        },

        {
            "hotel": "Radisson Blu",
            "location": "Delhi",
            "price": 5300,
            "rating": 4.3,
            "image": "https://images.unsplash.com/photo-1564501049412-61c2a3083791"
        },

        {
            "hotel": "The Oberoi",
            "location": "Delhi",
            "price": 8000,
            "rating": 4.9,
            "image": "https://images.unsplash.com/photo-1501117716987-c8e1ecb210c1"
        },

        {
            "hotel": "ITC Gardenia",
            "location": "Bangalore",
            "price": 6000,
            "rating": 4.6,
            "image": "https://images.unsplash.com/photo-1590490360182-c33d57733427"
        },

        {
            "hotel": "The Park",
            "location": "Bangalore",
            "price": 5000,
            "rating": 4.1,
            "image": "https://images.unsplash.com/photo-1559599238-308793637427"
        }
    ]

    return pd.DataFrame(data)


def fetch_expedia_data():

    data = [
        {
    "hotel": "Marriott",
    "location": "Hyderabad",
    "price": 6500,
    "rating": 4.6,
    "image": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2"
},

{
    "hotel": "Hyatt Regency",
    "location": "Hyderabad",
    "price": 7000,
    "rating": 4.7,
    "image": "https://images.unsplash.com/photo-1551776235-dde6d482980b"
},

{
    "hotel": "Lemon Tree",
    "location": "Hyderabad",
    "price": 3500,
    "rating": 4.0,
    "image": "https://images.unsplash.com/photo-1584132967334-10e028bd69f7"
},

{
    "hotel": "JW Marriott",
    "location": "Mumbai",
    "price": 9000,
    "rating": 4.8,
    "image": "https://images.unsplash.com/photo-1521783593447-5702b9bfd267"
},

{
    "hotel": "Holiday Inn",
    "location": "Delhi",
    "price": 5200,
    "rating": 4.2,
    "image": "https://images.unsplash.com/photo-1590490360182-c33d57733427"
},

{
    "hotel": "Vivanta",
    "location": "Bangalore",
    "price": 5800,
    "rating": 4.5,
    "image": "https://images.unsplash.com/photo-1501117716987-c8e1ecb210c1"
}
    ]

    return pd.DataFrame(data)


def aggregate_prices():

    booking = fetch_booking_data()
    expedia = fetch_expedia_data()

    combined = pd.concat([booking, expedia])

    result = combined.sort_values("price").groupby(
        ["hotel", "location"], as_index=False
    ).first()

    return result