from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        if 'email' in validated_data:
            user.email=validated_data['email']
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user