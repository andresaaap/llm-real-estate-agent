# main.py

from src.models.model import Listing, Buyer
from src.services.narrative_generator import NarrativeGenerator
from src.config.settings import get_settings

def main():
    settings = get_settings()
    print("Welcome to the LLM Real Estate Agent!")
    
    # Collect buyer preferences
    buyer_preferences = collect_buyer_preferences()
    buyer = Buyer(**buyer_preferences)
    
    # Initialize the narrative generator
    narrative_generator = NarrativeGenerator(settings)
    
    # Generate listings based on buyer preferences
    listings = narrative_generator.generate_listings(buyer)
    
    # Display the generated narratives
    for listing in listings:
        print(listing.description)

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

if __name__ == "__main__":
    main()