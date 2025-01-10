class Listing:
    def __init__(self, neighborhood, price, bedrooms, bathrooms, house_size, description, neighborhood_description):
        self.neighborhood = neighborhood
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.house_size = house_size
        self.description = description
        self.neighborhood_description = neighborhood_description


class Buyer:
    def __init__(self, neighborhood, price, bedrooms, bathrooms, house_size):
        self.preferences = {
            "neighborhood": neighborhood,
            "price": price,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "house_size": house_size
        }