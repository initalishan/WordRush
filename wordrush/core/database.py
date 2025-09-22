from pymongo import MongoClient
from os import environ 
from dotenv import load_dotenv


load_dotenv()

MONGO_URL = environ["MONGO_URL"]

mongo_client = MongoClient(MONGO_URL)
db = mongo_client["WordRush"]

users_col = db["users"]
groups_col = db["groups"]
scores_col = db["scores"]