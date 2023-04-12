from rest_framework import serializers

from apps.organizations.models import Organization
from apps.users.serializers import RegisterSerializer, LoginSerializer, UserUpdateSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    admin = RegisterSerializer(write_only=True)
    admin_data = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ["id",
                  "name",
                  "field",
                  "description",
                  "email",
                  "phone_number",
                  "admin",
                  "admin_data"]

    def get_admin_data(self, obj):
        admin = obj.admin
        serializer = RegisterSerializer(admin)
        return serializer.data

    def create(self, validated_data):
        admin_data = validated_data.pop("admin")
        register_serializer = RegisterSerializer(data=admin_data)
        register_serializer.is_valid(raise_exception=True)
        admin_user = register_serializer.save()

        organization = Organization.objects.create(admin=admin_user, **validated_data)

        return organization

