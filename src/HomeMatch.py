# main.py
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.models.model import Listing
from src.services.narrative_generator import NarrativeGenerator
from src.config.settings import get_settings
from src.utils.embedding_utils import generate_embeddings

def main():
    input_data = ["This is a test sentence.", "Here is another sentence."]
    embeddings = generate_embeddings(input_data)
    
    settings = get_settings()
    print("Welcome to the LLM Real Estate Agent!")
    
    # Collect buyer preferences
    
    # Initialize the narrative generator
    narrative_generator = NarrativeGenerator()

    # Read listings from file
    relative_path = 'data/Listings.txt'
    absolute_path = os.path.abspath(relative_path)
    listings = read_listings_from_file(absolute_path)
    print("Listings:")
    for listing in listings:
        print(listing)


def collect_buyer_preferences():
    # This function would ideally collect preferences from user input
    # For now, we will return a mock preference dictionary
    return {
        "Neighborhood": "Downtown",
        "Price": 500000,
        "Bedrooms": 2,
        "Bathrooms": 2,
        "House Size": 1200
    }

def read_listings_from_file(file_path):
    listings = []
    with open(file_path, 'r') as file:
        line_count = 0
        for line in file:
            if line_count > 0:
                # Assuming each line is a comma-separated value string
                neighborhood, price, bedrooms, bathrooms, house_size, description = line.strip().split(',')
                listing_string = f"{neighborhood}, {price}, {bedrooms}, {bathrooms}, {house_size}, {description}"
                print(listing_string)

                # use the properties to create an embedding
                listing_embedding = generate_embeddings(listing_string)

                listing = Listing(
                    neighborhood=neighborhood,
                    price=int(price),
                    bedrooms=int(bedrooms),
                    bathrooms=int(bathrooms),
                    house_size=int(house_size),
                    description=description,
                    vector=listing_embedding
                )
                listings.append(listing)
            line_count += 1
    return listings

if __name__ == "__main__":
    main()