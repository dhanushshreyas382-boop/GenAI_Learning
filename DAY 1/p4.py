import os
from dotenv import load_dotenv
load_dotenv()

config = dotenv_values(".env")
api_key = config.get("GEMINI_API_KEY")
api_key = os.get("GEMINI_API_KEY","")
api_key = os.environ["GEMINI_API_KEY"]
