from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from ecards_api.models import GreetingCard, Follow
from ecards_api.serializers import CardSerializer, FollowSerializer
from ecards_api.serializers import UserSerializer
from ecards_api.filters import IsOwnerFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from ecards_api.permissions import IsOwner, TheOwner, IsOwnerOrReadOnly
from rest_framework.response import Response
import requests
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


"""
POST /ecards/ - create a new greeting card
GET /ecards/ - get list of all greeting cards
GET /ecards?list=me - get list of all users cards
GET /ecards?list=following - get list of all user following cards 
"""
class GreetingCardCreate(generics.ListCreateAPIView):
    queryset = GreetingCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def perform_create(self, serializer):
        serializer.save(card_owner=self.request.user)

    def get_queryset(self):
      queryset = GreetingCard.objects.all()
      list_param = self.request.query_params.get("list")

      if list_param == 'me':
        queryset = GreetingCard.objects.all().filter(card_owner=self.request.user)
      
      if list_param == 'following':
        following_qs = Follow.objects.all().filter(user=self.request.user)

        if len(following_qs) == 0:
            return []

        following_ids = []
        for ob in following_qs:
            filtered_qs = GreetingCard.objects.all().filter(card_owner=ob.following)
            following_ids = following_ids + list(filtered_qs.values_list('id', flat=True))
            queryset = GreetingCard.objects.filter(id__in=following_ids)

      return queryset


"""
Patch /ecards/<int:pk - edit the chosen greeting card
Delete /ecards/<int:pk - delete the chosen greeting card
Get /ecards/<int:pk - show the chosen greeting card
"""
class GreetingCardEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = GreetingCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    permissions.IsAuthenticatedOrReadOnly


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


"""
PATCH /users/me/ - edit your user
"""
class UserEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj
