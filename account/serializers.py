from rest_framework import serializers

from . import models


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли не совпадают')
        return data

    def create(self, validated_data):
        user = models.User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        try:
            author = models.Author.objects.create(
                user=user,
            )
        except Exception as e:
            user.delete()
            raise e
        else:
            author.username = user.username
        return author
