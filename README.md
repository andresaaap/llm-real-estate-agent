# LLM Real Estate Agent

## Overview
The LLM Real Estate Agent project leverages large language models and vector databases to generate personalized real estate narratives based on buyer preferences. This application aims to enhance the home-buying experience by providing tailored property descriptions that align with individual buyer needs.

## Features
- Generate real estate listings based on buyer preferences.
- Utilize large language models to create engaging narratives.
- Store and retrieve property embeddings using a vector database.
- Augment property descriptions based on specific buyer criteria.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/llm-real-estate-agent.git
   ```
2. Navigate to the project directory:
   ```
   cd llm-real-estate-agent
   ```

Create a virtual environment: Use the python -m venv command to create a virtual environment.

```
python3 -m venv realstateagent
```

Activate the virtual environment: Activate the virtual environment using the following command:

```
source realstateagent/bin/activate
```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set environment variables:
   ```
   export OPENAI_API_KEY="your_api_key_here"
   ```

## Usage
To run the application, execute the following command:
```
python src/HomeMatch.py
```
Follow the prompts to input buyer preferences and generate personalized real estate narratives.

## Testing
To run the unit tests, use the following command:
```
pytest tests/
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.