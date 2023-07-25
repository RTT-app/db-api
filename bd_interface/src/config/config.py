from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

dotenv_path = find_dotenv(filename='.env')
print(dotenv_path)
if not Path(dotenv_path).exists():
    os.system("touch .env")

load_dotenv(dotenv_path)

DB = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

MONGO_URI = f'mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB}'
