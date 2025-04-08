print("Importing pymongo library...")
from pymongo import MongoClient

# Enhanced error handling to capture exceptions
try:
    print("Attempting to connect to MongoDB...")
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    print("Connection attempt completed.")
    # List databases
    databases = client.list_database_names()
    print("Databases:", databases)
except Exception as e:
    print("Error occurred while connecting to MongoDB:", e)

print("Script execution completed.")
