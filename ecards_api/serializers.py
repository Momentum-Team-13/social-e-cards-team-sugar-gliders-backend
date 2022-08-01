from multiprocessing import managers
from rest_framework import serializers
from ecards_api.models import GreetingCard, Follow
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id', 'username', 'email']


class CardSerializer(serializers.ModelSerializer):
	card_owner = UserSerializer(read_only=True)

	class Meta:
		model = GreetingCard
		fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
	following = serializers.ReadOnlyField(source='following.id')
	user_following = UserSerializer(source='following', read_only=True)

	class Meta:
		model = Follow
		fields = ['id', 'user_following', 'following']
