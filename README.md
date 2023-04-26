## Table of Contents  
- [Project Dependencies](#project-dependencies) 
- [Prerequisites](#prerequisites)
-  [Installing](#installing) 
- [Project Structure](#project-structure) 
- [Usage](#usage)
# Discord Teaching Assistant Bot

  

This is a Discord bot implemented in Python that acts as a teaching assistant, providing answers to questions asked by users in a Discord server. The bot uses OpenAI's GPT-3.5-turbo model for generating responses, as well as the Canvas API for fetching course information. You can use the `!help` command inside your Discord server to explore and learn more about all the available commands, as well as their use cases.

  

## Project Dependencies

  

The dependencies required for running the Discord Teaching Assistant Bot are listed in the `requirements.txt` file.

  

### Prerequisites

  

Before you proceed with the installation, make sure you have the following software installed:

  

- [Python 3](https://www.python.org/downloads/)

- [pip3](https://pip.pypa.io/en/stable/installing/) (Python package manager)

  

### Installing

  

To install the dependencies, follow these steps:

  

1. Clone the repository from GitHub: [https://github.com/OGulsan/TABot.git](https://github.com/OGulsan/TABot.git)

2. Navigate to the project directory in your terminal.

3. Run the following command to create a virtual environment:

  

	For Windows:

	```python3 -m venv env```

	  

	For macOS/Linux:

	```python3 -m venv env```

4. Activate the virtual environment:
	
	  

	For Windows:

	```env\Scripts\activate.bat```

	  

	For macOS/Linux:

	```source env/bin/activate```

5. Finally, run the following command to install the dependencies:

	```pip3 install -r requirements.txt```

  

This will create and activate a virtual environment, and then install the dependencies listed in the `requirements.txt` file into the virtual environment. Note: It is recommended to use a virtual environment to manage the dependencies of this project.

  

## Project Structure

  

The project consists of the following files:

  

- `ta_bot.py`: This is the main entry point of the Discord Teaching Assistant Bot. It handles the bot's connection to Discord, message events, and response generation using the OpenAI API.

- `helpers.py`: This file contains helper functions for interacting with Discord, such as getting the general text channel from guilds and checking if a message is a command.

- `ta_bot_ai.py`: This file contains the class `TABotAI` which represents the AI component of the bot. It uses the OpenAI API to generate responses to user questions.

- `token_counter.py`: This file contains a function `num_tokens_from_messages` which calculates the number of tokens used in a list of messages. It is used for tracking the token count for API usage.

- `canvas.py`: This file contains functions for interacting with the Canvas API, such as fetching course information.
- `requirments.txt`: This file contains a list of all the dependencies required for running the Discord Teaching Assistant Bot.

  

## Usage

1. Install the project dependencies using `pip3 install -r requirements.txt` in a virtual environment.

2. Set up a Discord bot and obtain the bot token.

3. Set the `DISCORD_BOT_TOKEN` and `OPEN_AI_TOKEN` environment variables in a `.env` file or in your environment.

4. Set up the `CANVAS_API_KEY` and `CANVAS_BASE_URL`  environment variables for the Canvas API in the `.env` file or in your environment.

5. Run the `main.py` file to start the Discord Teaching Assistant Bot.

6. Invite the bot to your Discord server and interact with it by sending messages prefixed with "!" to ask questions or fetch course information.

7. Use the `!help` command to explore and learn more about all the available commands and their use cases. The bot provides detailed information on how to use different commands and their functionalities, helping users navigate and make the most out of the Discord Teaching Assistant Bot.

9. Happy Learning!