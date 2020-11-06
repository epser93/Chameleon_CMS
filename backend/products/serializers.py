from accounts.serializers import UserSerializer
from rest_framework import serializers
from .models import Category, CategoryDescription, CopyOfItemDescription, CopyOfItemImage, Item, ItemDescription, ItemImage, Template

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


class CategoryJoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['id', 'item_image', 'is_thumbnail', 'priority', 'created_date', 'update_date']


class ItemDescriptionSerializer(serializers.ModelSerializer):
    category_description = CategoryDescriptionSerializer()
    class Meta:
        model = ItemDescription
        fields = ['content', 'item', 'category_description']


class ItemSerializer(serializers.ModelSerializer):
    cms_user = UserSerializer(required=False)
    images = ItemImageSerializer(required=False, many=True)
    descriptions = ItemDescriptionSerializer(required=False, many=True)
    category = CategoryJoinSerializer()
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'is_temp', 'is_active', 'category','template','created_date', 'update_date', 'cms_user','descriptions', 'images']


class CopyItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopyOfItemImage
        fields = ['id', 'item_image', 'is_thumbnail', 'priority', 'created_date', 'update_date']


class CopyItemDescriptionSerializer(serializers.ModelSerializer):
    category_description = CategoryDescriptionSerializer()
    class Meta:
        model = CopyOfItemDescription
        fields = ['content', 'category_description']


class CopyItemSerializer(serializers.ModelSerializer):
    cms_user = UserSerializer(required=False)
    copy_images = CopyItemImageSerializer(required=False, many=True)
    copy_descriptions = CopyItemDescriptionSerializer(required=False, many=True)
    category = CategoryJoinSerializer()
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'is_temp', 'is_active', 'category','template','created_date', 'update_date', 'cms_user', 'copy_descriptions', 'copy_images']


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['id', 'name', 'type']