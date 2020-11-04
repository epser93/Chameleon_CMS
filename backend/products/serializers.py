from accounts.serializers import UserSerializer
from rest_framework import serializers
from .models import Category, CategoryDescription, Item, ItemDescription, ItemImage

class CategoryDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDescription
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    cms_user = UserSerializer(required=False)
    description = CategoryDescriptionSerializer(required=False, many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'is_active', 'priority', 'created_date', 'update_date', 'cms_user', 'description']


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['id', 'item_image', 'is_thumbnail', 'priority', 'is_active', 'created_date', 'update_date']


class ItemDescriptionSerializer(serializers.ModelSerializer):
    category_description = CategoryDescriptionSerializer()
    class Meta:
        model = ItemDescription
        fields = ['content', 'item', 'category_description']


class ItemSerializer(serializers.ModelSerializer):
    cms_user = UserSerializer(required=False)
    images = ItemImageSerializer(required=False, many=True)
    descriptions = ItemDescriptionSerializer(required=False, many=True)
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'is_temp', 'is_active', 'created_date', 'update_date', 'cms_user','descriptions', 'images']