from src.models.model import Listing, Buyer
import unittest

class TestListing(unittest.TestCase):
    def setUp(self):
        self.listing = Listing(
            Neighborhood="Downtown",
            Price=500000,
            Bedrooms=3,
            Bathrooms=2,
            House_Size=1500,
            Description="A beautiful home in the heart of the city.",
            Neighborhood_Description="Vibrant area with lots of amenities."
        )

    def test_listing_attributes(self):
        self.assertEqual(self.listing.Neighborhood, "Downtown")
        self.assertEqual(self.listing.Price, 500000)
        self.assertEqual(self.listing.Bedrooms, 3)
        self.assertEqual(self.listing.Bathrooms, 2)
        self.assertEqual(self.listing.House_Size, 1500)
        self.assertEqual(self.listing.Description, "A beautiful home in the heart of the city.")
        self.assertEqual(self.listing.Neighborhood_Description, "Vibrant area with lots of amenities.")

class TestBuyer(unittest.TestCase):
    def setUp(self):
        self.buyer = Buyer(
            Neighborhood="Uptown",
            Price=600000,
            Bedrooms=4,
            Bathrooms=3,
            House_Size=2000
        )

    def test_buyer_preferences(self):
        self.assertEqual(self.buyer.Neighborhood, "Uptown")
        self.assertEqual(self.buyer.Price, 600000)
        self.assertEqual(self.buyer.Bedrooms, 4)
        self.assertEqual(self.buyer.Bathrooms, 3)
        self.assertEqual(self.buyer.House_Size, 2000)

if __name__ == '__main__':
    unittest.main()