# main.py
import sys
import os
import streamlit as st

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.models.model import Listing
from src.services.narrative_generator import NarrativeGenerator
from src.config.settings import get_settings
from src.utils.embedding_utils import generate_embeddings
from src.config.db_init import initialize_db

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
    listings = read_listings_from_file(absolute_path, settings["LISTINGS_SEPARATOR"])
    print("Listings:")
    for listing in listings:
        print(listing)

    table = initialize_db()
    # Store the embeddings in the vector database
    table.add(listings)
    print("Listings added to the database.")
    table.head().to_pandas()

    # Perform a semantic search
    print(table.search(listings[4].vector).limit(2).where("neighborhood='Mountain View Haven'").to_df())

def start_chat():
    # Streamlit UI
    st.title("Bedrock Chat Application")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

            response = "hola"
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

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

def read_listings_from_file(file_path, separator):
    listings = []
    with open(file_path, 'r') as file:
        line_count = 0
        for line in file:
            if line_count > 0:
                # Assuming each line is a comma-separated value string
                neighborhood, price, bedrooms, bathrooms, house_size, description = line.strip().split(separator)
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
    if "initialized" not in st.session_state:
        st.session_state.initialized = False
    if not st.session_state.initialized:
        main()
        # Set the initialized flag to True
        st.session_state.initialized = True
    start_chat()