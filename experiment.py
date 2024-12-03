import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if the variables are loaded correctly
print("TWILIO_ACCOUNT_SID:", os.getenv("TWILIO_ACCOUNT_SID"))
print("TWILIO_AUTH_TOKEN:", os.getenv("TWILIO_AUTH_TOKEN"))
print("NGROK_URL:", os.getenv("NGROK_URL"))