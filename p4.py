import google.genai as genai
import os
from dotenv import load_dotenv
#load the API keys from .env file
load_dotenv()
genai.configure(api_key=os.environ.get("GENAI_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-3.8-flash",generation_config={"temperature": 0.7, "max_output_tokens": 150},system_instruction="You are a concise AI tutor. Answer in 2-3 sentences.")

result = model.generate_content("what is a vector database?")
print(result.text)
print(f"Tokens used:{result.token_usage.total_tokens}")

GEMINI_API_KEY=text

APP_NAME= GENAI_Workshop
LOG_LEVEL = INFO
