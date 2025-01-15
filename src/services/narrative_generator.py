import openai
import os

openai.api_base = "https://openai.vocareum.com/v1"

# Define OpenAI API key 
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

class NarrativeGenerator:
    def __init__(self):
        # Call the generate_listings method to generate real estate listings and store the response in the file
        # Listing.txt
        relative_path = 'data/Listings.txt'
        absolute_path = os.path.abspath(relative_path)
        
        # Check if the file exists and if it is empty
        if not os.path.exists(absolute_path) or os.path.getsize(absolute_path) == 0:
            with open(absolute_path, "w") as file:
                file.write(self.generate_listings())

    def generate_listings(self):
        # Logic to generate a real estate listing based on buyer preferences    
        prompt = """
        Objective:
        Generate 10 real estate listings based on the following example and in the format of csv (comma-separated values) with the following columns: Neighborhood, Price, Bedrooms, Bathrooms, House Size, Description.

        Details:
        Don't start each listing with the number, this is not a numbered list.
        Don't end each listing with two or more newlines. Only one newline is allowed at the end of each listing.
        Don't include: Neighborhood Description: or any other text that is not part of the listing.

        Examples:

        Neighborhood,Price,Bedrooms,Bathrooms,House Size,Description
        Green OaksPrice, 800000, 3, 2, 2000, Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem.\nNeighborhood Description: Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze.
        Lakeside Manor,1200000,5,4,3500,Experience luxury living in Lakeside Manor with this stunning 5-bedroom, 4-bathroom estate. The grand entrance leads to a formal living room with a fireplace, a gourmet kitchen with top-of-the-line appliances, and a master suite with a spa-like bathroom. The backyard features a pool, spa, and built-in BBQ for outdoor entertaining.
        """
        
        response = openai.ChatCompletion.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a real estate agent looking to generate listings for potential buyers."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gpt-3.5-turbo",
            temperature=1,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        print(response.choices[0].message)

        return response.choices[0].message.content

    def convert_to_embeddings(self, listing):
        # Logic to convert LLM-generated listings into embeddings
        pass

    def augment_description(self, listing, buyer_preferences):
        # Logic to augment descriptions based on buyer preferences
        pass