from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from ecards_api.models import GreetingCard
from ecards_api.serializers import CardSerializer


class GreetingCardCreate(generics.ListCreateAPIView):
    queryset = GreetingCard.objects.all()
    serializer_class = CardSerializer 

