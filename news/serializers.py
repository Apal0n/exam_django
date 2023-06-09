from rest_framework import serializers

from . import models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    model = models.Comment
    fields = '__all__'
