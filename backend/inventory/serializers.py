from rest_framework import serializers
from .models import Category, Item, UserProfile
from django.contrib.auth.models import User
from django.db import transaction

# === Category Serializer ===
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# === Item Serializer ===
class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # for GET/display only
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Item
        fields = [
            'id', 'name', 'category', 'category_id',
            'quantity', 'date_added', 'status', 'owner'
        ]
        read_only_fields = ['owner']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        item = super().create(validated_data)
        item.update_status()
        item.save()
        return item

    def update(self, instance, validated_data):
        item = super().update(instance, validated_data)
        item.update_status()
        item.save()
        return item

# === UserProfile Serializer ===
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'account_type']

# === User Serializer (handles missing profile safely) ===
class UserSerializer(serializers.ModelSerializer):
    userprofile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'userprofile']

    def get_userprofile(self, user):
        try:
            profile = user.profile  # based on related_name='profile'
            return UserProfileSerializer(profile).data
        except UserProfile.DoesNotExist:
            return {
                "phone_number": "",
                "account_type": ""
            }

# === User Registration Serializer ===
class UserRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(write_only=True)
    account_type = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'password', 'confirm_password', 'phone_number', 'account_type'
        ]

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    @transaction.atomic
    def create(self, validated_data):
        phone_number = validated_data.pop('phone_number')
        account_type = validated_data.pop('account_type')
        validated_data.pop('confirm_password')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )

        # ✅ Update the auto-created profile (from signals)
        user.profile.phone_number = phone_number
        user.profile.account_type = account_type
        user.profile.save()

        return user
