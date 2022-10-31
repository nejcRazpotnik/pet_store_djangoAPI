#TODO move to animals folder

from rest_framework import serializers

from animals.models import Categories, Status, Tags, Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = [
            'name',
            'category',
            'pictures',
            'status',
            'tags'
        ]

