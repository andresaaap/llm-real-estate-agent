# main.py
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.models.model import Listing, Buyer
from src.services.narrative_generator import NarrativeGenerator
from src.config.settings import get_settings

def main():
    settings = get_settings()
    print("Welcome to the LLM Real Estate Agent!")
    
    # Collect buyer preferences
    
    # Initialize the narrative generator
    narrative_generator = NarrativeGenerator()

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