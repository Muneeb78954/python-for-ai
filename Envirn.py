import os
from dotenv import load_dotenv
# Read from environment

load_dotenv()
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_URL')

print(f"Using API key: {api_key}")
print(f"Using database: {database}")