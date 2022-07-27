from rest_framework import serializers
from ecards_api.models import GreetingCard, Follow
from rest_framework.decorators import api_view
import requests


class CardSerializer(serializers.ModelSerializer):

	class Meta:
		model = GreetingCard
		fields = ['id', 'card_color_list', 'card_color', 'card_owner', 'card_inner_message', 'card_outer_message', 'card_image']



class FollowSerializer(serializers.ModelSerializer):
	follower = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = Follow
		field = "__all__"
