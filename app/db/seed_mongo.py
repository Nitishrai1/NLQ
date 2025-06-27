

from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")

db = client["wealth_portfolio"]


users_collection = db["users"]


sample_users = [
    {
        "userId": 101,
        "name": "Virat Kohli",
        "address": "Mumbai, India",
        "riskAppetite": "high",
        "investmentPreferences": ["stocks", "real estate"]
    },
    {
        "userId": 102,
        "name": "MS Dhoni",
        "address": "Ranchi, India",
        "riskAppetite": "medium",
        "investmentPreferences": ["mutual funds", "gold"]
    },
    {
        "userId": 103,
        "name": "Rohit Sharma",
        "address": "Nagpur, India",
        "riskAppetite": "low",
        "investmentPreferences": ["bonds", "fixed deposits"]
    }
]

users_collection.delete_many({})

users_collection.insert_many(sample_users)

print("✅ Sample users inserted into MongoDB.")
