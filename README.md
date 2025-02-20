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

Install pyenv and pyenv-virtualenv:

```
brew update
brew install pyenv
brew install pyenv-virtualenv
```

Add the following lines to your shell profile (e.g., ~/.bash_profile, ~/.zshrc, ~/.profile, or ~/.bashrc):

```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Restart your shell:

```
source ~/.zshrc   # For zsh
```

Create and Activate Virtual Environment:

```
pyenv install 3.12.0  # Install the desired Python version if not already installed
pyenv virtualenv 3.12.0 myproject-env
pyenv activate myproject-env
```

3. Install the required dependencies:
   ```
   pip3 install -r requirements.txt
   ```

4. Set environment variables:
   ```
   export OPENAI_API_KEY="your_api_key_here"
   ```

## Usage
To run the application, execute the following command:
```
streamlit run src/HomeMatch.py
```
Follow the prompts to input buyer preferences and generate personalized real estate narratives.

## Reviewing instructions

The real estate listings can be found in the `data/Listings.txt` file.

The following is a demo video of the application:

[![Demo Video](https://i9.ytimg.com/vi/aF_hqQUwjlk/mqdefault.jpg?sqp=CJTc3r0G-oaymwEmCMACELQB8quKqQMa8AEB-AHUBoAC2AOKAgwIABABGGUgZShlMA8=&rs=AOn4CLBNbRGYqVSzBkSZXE5tXwvqO2tTxQ)](https://youtu.be/aF_hqQUwjlk)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.