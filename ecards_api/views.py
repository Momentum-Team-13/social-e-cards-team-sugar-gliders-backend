from django.shortcuts import render
from rest_framework import generics, permissions
from ecards_api.models import Follow
from ecards_api.serializers import FollowSerializer
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
"""
  Home page, get's you a free meme
"""
@api_view(['GET'])
def getDankMeme(request):
	res = requests.get('https://meme-api.herokuapp.com/gimme')
	data = res.json()

	return Response({
		'team': 'Team Sugar Gliders',
		'description': 'We got this team 😎, if you"re feeling down there"s a link here where you can see a funny Meme. Use it to lift your spirit.',
		'dank_meme_image': data['url']
		})


"""
GET /followers - get all list of users you follow
"""
class FollowersListCreate(generics.ListCreateAPIView):
	queryset = Follow.objects.all()
	serializer_class = FollowSerializer	
	permission_classes = []

