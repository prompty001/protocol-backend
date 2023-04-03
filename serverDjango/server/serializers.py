from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'cpf', 'birthday', 'guid', 'androidId']

        extra_kwargs = {
            'password': {'write_only': True},
            'cpf': {'write_only': True},
            'guid': {'write_only': True},
            'androidId': {'write_only': True},
            'birthday': {'write_only': True},
            'email': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance