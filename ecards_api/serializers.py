from rest_framework import serializers
from ecards_api.models import GreetingCard, Follow
from rest_framework.decorators import api_view
import requests


class CardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = GreetingCard
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Follow
        fields = "__all__"
