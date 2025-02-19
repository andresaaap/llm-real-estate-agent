# main.py
import sys
import os
import streamlit as st
import openai

openai.api_base = "https://openai.vocareum.com/v1"

# Define OpenAI API key 
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.models.model import Listing, BuyerPreferences
from src.services.narrative_generator import NarrativeGenerator
from src.config.settings import get_settings
from src.utils.embedding_utils import generate_embeddings
from src.config.db_init import initialize_db, get_db_table

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
    
    if "neighborhood" not in st.session_state:
        st.session_state.neighborhood = False

    if "neighborhood_values" not in st.session_state:
        st.session_state.neighborhood_values = False

    if "amenities" not in st.session_state:
        st.session_state.amenities = False

    if "amenities_values" not in st.session_state:
        st.session_state.amenities_values = False

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        user_input_classification = classify_user_input(prompt)
        
        ## Get the users preferences about neighborhood, price, bedrooms, bathrooms, and house size
        if st.session_state.neighborhood == False:
            with st.chat_message("assistant"):
                st.markdown("What neighborhood, price, bedrooms, bathrooms and house size are you looking for?")
                st.session_state.neighborhood = True
                st.session_state.messages.append({"role": "assistant", "content": "What neighborhood, price, bedrooms, bathrooms and house size are you looking for?"})

        if st.session_state.neighborhood_values == False and st.session_state.neighborhood == True:
            # Logic to generate a real estate listing based on buyer preferences    
            
            # If the user input is classified as Neighborhood
            if "Neighborhood" in user_input_classification:
                # Logic to generate a real estate listing based on buyer preferences
                prompt_template = f"""
                Objective:
                Extract the neighborhood, price, number of bedrooms, number of bathrooms and house size from the following text and output the values in the format: Neighborhood,Price,Bedrooms,Bathrooms,House Size.

                Details:
                bedrooms, bathrooms, and house size are integers.
                price is an integer.
                Neighborhood is a string.
                The values are separated by commas.

                Examples:

                Bel Air,1000000,5,4,3000

                Text:
                {prompt}
                """
                extract_data_neighborhood = extract_information_from_user_input(prompt_template, prompt)
                st.session_state.neighborhood_values = True
                st.session_state.data_neighborhood = extract_data_neighborhood

        ## Get the users prefences related to amenities
        if st.session_state.amenities == False and st.session_state.neighborhood_values == True:
            with st.chat_message("assistant"):
                st.markdown("Which amenities would you like?")
                st.session_state.amenities = True
                st.session_state.messages.append({"role": "assistant", "content": "Which amenities would you like?"})

        if st.session_state.amenities_values == False and st.session_state.amenities == True:
            # Logic to generate a real estate listing based on buyer preferences    
            
            # If the user input is classified as Neighborhood
            if "Amenities" in user_input_classification:
                # Logic to generate a real estate listing based on buyer preferences
                prompt_template = f"""
                Objective:
                Extract the amenities from the following text.

                Details:
                The amenities are separated by commas.
                The amenities are strings.

                Examples:

                overlooking the golf course, luxurious master suite, home theater, outdoor kitchen, golfing

                Text:
                {prompt}
                """
                extract_data_amenities = extract_information_from_user_input(prompt_template, prompt)
                st.session_state.amenities_values = True
                st.session_state.data_amenities = extract_data_amenities

            # if neighborhood_values and amenities_values are True, then use them to create the buyer preferences
            if st.session_state.neighborhood_values == True and st.session_state.amenities_values == True:
                data_neighborhood_split = st.session_state.data_neighborhood.split(",")
                # Logic to generate a real estate listing based on buyer preferences
                buyer_preferences = BuyerPreferences(
                    neighborhood=data_neighborhood_split[0],
                    price=data_neighborhood_split[1],
                    bedrooms=data_neighborhood_split[2],
                    bathrooms=data_neighborhood_split[3],
                    house_size=data_neighborhood_split[4],
                    amenities=st.session_state.data_amenities,
                    priorities="safe neighborhood, close to a mall, classic style home"
                )
                print(buyer_preferences)
                table = get_db_table()
                # Generate embeddings for the buyer preferences
                buyer_preferences_vector = generate_embeddings(str(buyer_preferences))
                # Perform a semantic search
                search_results = table.search(buyer_preferences_vector).limit(2).where(f"neighborhood='{buyer_preferences.neighborhood}'").to_df()
                print(search_results)

        ## Get the users preferences related to 3 most important things when making the decision
        #if "important_decision_criteria" not in st.session_state:
        #    with st.chat_message("assistant"):
        #        st.markdown("What are 3 most important things for you in choosing this property?")
        #        st.session_state.important_decision_criteria = True
        #        st.session_state.messages.append({"role": "assistant", "content": "What are 3 most important things for you in choosing this property?"})
        
        # Display assistant response

def extract_information_from_user_input(prompt_template, user_input):
    # Format the prompt_template with the user_input
    formatted_prompt = prompt_template.format(prompt=user_input)
    
    response = openai.ChatCompletion.create(
        messages=[
            {
                "role": "system",
                "content": "You are a real estate agent looking to extract relevant information from potential buyers."
            },
            {
                "role": "user",
                "content": formatted_prompt
            }
        ],
        model="gpt-3.5-turbo",
        temperature=1,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content

def classify_user_input(user_input):
    prompt_template_function_classification = f"""
    Objective:
    Classify the user input into the following categories: Neighborhood, Amenities, Important Decision Criteria, Other.

    Details:
    If the user input is a response for the question "What neighborhood, price, bedrooms, bathrooms and house size are you looking for?", classify it as Neighborhood.
    If the user input is a response for the question "Which amenities would you like?", classify it as Amenities.
    If the user input is a response for the question "What are 3 most important things for you in choosing this property?", classify it as Important Decision Criteria.
    Otherwise, classify it as Other.

    Examples:

    I am looking for a house in Downtown with 2 bedrooms, 2 bathrooms, and a house size of 1200 sqft.
    Neighborhood

    User input:
    {user_input}
    """

    response = openai.ChatCompletion.create(
        messages=[
            {
                "role": "system",
                "content": prompt_template_function_classification
            }
        ],
        model="gpt-3.5-turbo",
        temperature=1,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response.choices[0].message.content


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