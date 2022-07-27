from rest_framework import serializers
from ecards_api.models import Follow

class FollowSerializer(serializers.ModelSerializer):
	follower = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = Follow
		field = "__all__"

