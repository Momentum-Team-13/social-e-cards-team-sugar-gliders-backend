from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from ecards_api.models import GreetingCard, Follow
from ecards_api.serializers import CardSerializer, FollowSerializer
from rest_framework.response import Response
import requests
from django.contrib.auth.models import User


class GreetingCardCreate(generics.ListCreateAPIView):
    queryset = GreetingCard.objects.all()
    serializer_class = CardSerializer 


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
GET /followers - get list of users they are following
POST /followers - follow a user 
"""
class FollowersListCreate(generics.ListCreateAPIView):
	queryset = Follow.objects.all()
	serializer_class = FollowSerializer	
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		user_following = User.objects.get(pk=self.request.data['following'])
		if user_following.id is not self.request.user.id:
			serializer.save(user=self.request.user, following=user_following)
		else:
			return Response({"message": "Users cannot follow themselves"})

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset()).filter(user=request.user)
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)


"""
DELETE /followers/<int:pk/ - remove user from followers list
"""

class FollowersRemove(generics.DestroyAPIView):
	queryset = Follow.objects.all()
	serializer_class = FollowSerializer
	permission_classes = [permissions.IsAuthenticated]

	
