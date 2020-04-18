from rest_framework import serializers

from .models import List, Card

class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = ['name']


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['title', 'description', 'the_list', 'story_points', 'business_value'] 