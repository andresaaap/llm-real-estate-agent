import unittest
from src.services.narrative_generator import NarrativeGenerator
from src.models.model import Listing, Buyer

class TestNarrativeGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = NarrativeGenerator()
        self.listing = Listing(
            Neighborhood="Downtown",
            Price=500000,
            Bedrooms=3,
            Bathrooms=2,
            House_Size=1500,
            Description="A beautiful home in the heart of the city.",
            Neighborhood_Description="Vibrant area with lots of amenities."
        )
        self.buyer = Buyer(
            Neighborhood="Downtown",
            Price=450000,
            Bedrooms=2,
            Bathrooms=1,
            House_Size=1000
        )

    def test_generate_listing_narrative(self):
        narrative = self.generator.generate_listing_narrative(self.listing)
        self.assertIn("beautiful home", narrative)
        self.assertIn("Downtown", narrative)

    def test_convert_to_embeddings(self):
        embeddings = self.generator.convert_to_embeddings(self.listing)
        self.assertIsNotNone(embeddings)

    def test_augment_description(self):
        augmented_description = self.generator.augment_description(self.listing.Description, self.buyer)
        self.assertIn("heart of the city", augmented_description)

if __name__ == '__main__':
    unittest.main()