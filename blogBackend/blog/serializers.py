# Serializes Entry Data Model
from .models import Entry
from rest_framework import serializers


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry