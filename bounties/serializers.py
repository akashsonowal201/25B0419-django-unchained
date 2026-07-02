from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Bounty


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password"]

        extra_kwargs = {

            "password": {

                "write_only": True

            }

        }

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)


class BountySerializer(serializers.ModelSerializer):

    class Meta:
        model = Bounty
        fields = [
            "id",
            "target_name",
            "reward",
            "status",
            "owner",
            "created_at",
        ]

        read_only_fields = [
            "owner",
            "created_at",
        ]

    class Meta:
        model = Bounty

        fields = "__all__"

        read_only_fields = ["owner"]
