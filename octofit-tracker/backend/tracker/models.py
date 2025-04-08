from pymongo import MongoClient
from django.conf import settings

# Establish MongoDB connection
client = MongoClient(settings.MONGO_CLIENT['host'])
db = client[settings.MONGO_CLIENT['db_name']]

# Models are now collections in MongoDB
users_collection = db['users']
teams_collection = db['teams']
activities_collection = db['activity']
leaderboard_collection = db['leaderboard']
workouts_collection = db['workouts']
