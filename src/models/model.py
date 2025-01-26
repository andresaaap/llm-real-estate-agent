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
