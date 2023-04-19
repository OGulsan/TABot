import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

token = os.getenv("DISCORD_BOT_TOKEN")
