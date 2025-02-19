from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry

embeddings = get_registry().get("openai").create()

class Listing(LanceModel):
    vector: Vector(384)
    neighborhood: str
    price: int
    bedrooms: int
    bathrooms: int
    house_size: int
    description: str

class BuyerPreferences:
    def __init__(self, neighborhood, price, bedrooms, bathrooms, house_size, amenities, priorities):
        self.neighborhood = neighborhood
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.house_size = house_size
        self.amenities = amenities
        self.priorities = priorities

    def __str__(self):
        return (f"Neighborhood: {self.neighborhood}, Price: {self.price}, Bedrooms: {self.bedrooms}, "
                f"Bathrooms: {self.bathrooms}, House Size: {self.house_size}, "
                f"Amenities: {self.amenities}, Priorities: {self.priorities}")