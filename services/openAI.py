from openai import OpenAI
from utils.config import OPEN_AI_KEY
# Provide your OpenAI API key during client initialization
client = OpenAI(api_key=OPEN_AI_KEY)