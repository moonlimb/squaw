from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    # validates user input
    # converts JSON to Django ORM object (deserialize) for post/put request
    # converts Django ORM object to JSON (serialize) for GET request
    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Post

    

