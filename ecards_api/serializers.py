from rest_framework import serializers
from ecards_api.models import GreetingCard, Follow
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id', 'username', 'email']


class CardSerializer(serializers.ModelSerializer):

	class Meta:
		model = GreetingCard
		fields = ['id', 'card_color_list', 'card_color', 'card_owner', 'card_inner_message', 'card_outer_message', 'card_image']



class FollowSerializer(serializers.ModelSerializer):
	following = serializers.ReadOnlyField(source='following.id')
	user_following = UserSerializer(source='following', read_only=True)

	class Meta:
		model = Follow
		fields = ['id', 'user_following', 'following']

