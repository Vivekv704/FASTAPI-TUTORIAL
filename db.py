from pymongo import MongoClient
client = MongoClient()

db = client["fastapi_tut_db"]
msg_collection = db["test_collection"]