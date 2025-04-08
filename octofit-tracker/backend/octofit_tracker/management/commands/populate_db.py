from django.core.management.base import BaseCommand
from tracker.models import users_collection, teams_collection, activities_collection, leaderboard_collection, workouts_collection
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Drop existing collections
        users_collection.drop()
        teams_collection.drop()
        activities_collection.drop()
        leaderboard_collection.drop()
        workouts_collection.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "email": "thundergod@mhigh.edu", "name": "Thor"},
            {"_id": ObjectId(), "email": "metalgeek@mhigh.edu", "name": "Tony Stark"},
            {"_id": ObjectId(), "email": "zerocool@mhigh.edu", "name": "Steve Rogers"},
            {"_id": ObjectId(), "email": "crashoverride@mhigh.edu", "name": "Natasha Romanoff"},
            {"_id": ObjectId(), "email": "sleeptoken@mhigh.edu", "name": "Bruce Banner"},
        ]
        users_collection.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[2]["_id"], users[3]["_id"], users[4]["_id"]]},
        ]
        teams_collection.insert_many(teams)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": 60},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": 120},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": 90},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": 30},
            {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": 75},
        ]
        activities_collection.insert_many(activities)

        # Create leaderboard entries
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "points": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "points": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "points": 95},
            {"_id": ObjectId(), "user": users[3]["_id"], "points": 85},
            {"_id": ObjectId(), "user": users[4]["_id"], "points": 80},
        ]
        leaderboard_collection.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        workouts_collection.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
