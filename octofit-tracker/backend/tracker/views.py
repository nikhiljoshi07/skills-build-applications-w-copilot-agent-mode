from django.shortcuts import render
from rest_framework import viewsets
from tracker.models import users_collection, teams_collection, activities_collection, leaderboard_collection, workouts_collection
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = list(users_collection.find())
        return Response(users)

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        teams = list(teams_collection.find())
        return Response(teams)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        activities = list(activities_collection.find())
        return Response(activities)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboard = list(leaderboard_collection.find())
        return Response(leaderboard)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        workouts = list(workouts_collection.find())
        return Response(workouts)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activity': '/api/activity/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/',
    })
