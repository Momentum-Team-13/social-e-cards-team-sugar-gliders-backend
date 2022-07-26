from rest_framework import serializers
from ecards_api.models import GreetingCard


class CardSerializer(serializers.ModelSerializer):

	class Meta:
		model = GreetingCard
		fields = ['id', 'card_color_list', 'card_color', 'card_owner', 'card_inner_message', 'card_outer_message', 'card_image']
