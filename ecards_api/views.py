from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from ecards_api.models import GreetingCard, Follow
from ecards_api.serializers import CardSerializer, FollowSerializer
from ecards_api.serializers import UserSerializer
from ecards_api.filters import IsOwnerFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from ecards_api.permissions import IsOwner
from rest_framework.response import Response
import requests
from django.contrib.auth.models import User


"""
GET /ecards/ - get list of all greeting cards
POST /ecards/ - create a new greeting card
"""
class GreetingCardCreate(generics.ListCreateAPIView):
    queryset = GreetingCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(card_owner=self.request.user)

    def get_queryset(self):
      queryset = GreetingCard.objects.all()
      list_param = self.request.query_params.get("list")

      if list_param == 'me':
        queryset = GreetingCard.objects.all().filter(card_owner=self.request.user)
      
      if list_param == 'following':
        following_qs = Follow.objects.all().filter(user=self.request.user)
        for ob in following_qs:
            queryset = GreetingCard.objects.all().filter(card_owner=ob.following).exclude(card_owner=self.request.user)

      return queryset


"""
Get /ecards/me/ - show greeting cards created for that user
"""
class GreetingCardMe(generics.ListCreateAPIView):
    queryset = GreetingCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GreetingCard.objects.all().filter(card_owner=self.request.user)


"""
Patch /ecards/<int:pk - edit the chosen greeting card
Delete /ecards/<int:pk - delete the chosen greeting card
Get /ecards/<int:pk - show the chosen greeting card
"""
class GreetingCardEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = GreetingCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(card_owner=self.request.user)


class FollowingCards(generics.ListAPIView):
    queryset = GreetingCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GreetingCard.objects.all().filter(card_owner=User.objects.get(pk=self.request.data['following']))


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
	filter_backends = [DjangoFilterBackend, IsOwnerFilterBackend]

	def perform_create(self, serializer):
		user_following = User.objects.get(pk=self.request.data['following'])
		if user_following.id is not self.request.user.id:
			serializer.save(user=self.request.user, following=user_following)
		else:
			return Response({"message": "Users cannot follow themselves"})


"""
DELETE /followers/<int:pk/ - remove user from followers list
"""
class FollowersRemove(generics.DestroyAPIView):
	queryset = Follow.objects.all()
	serializer_class = FollowSerializer
	permission_classes = [permissions.IsAuthenticated, IsOwner]


"""
GET /users - get list of all users
"""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
