from django.shortcuts import render
from rest_framework import generics
from ecards_api.models import Follow

# Create your views here.
class FollowersListCreate(generics.ListCreateAPIView):
	queryset = Follow.objects.all()
	
