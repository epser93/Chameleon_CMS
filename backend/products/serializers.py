from accounts.serializers import UserSerializer
from rest_framework import serializers
from accounts.serializers import UserSerializer
#from services.models import TemplateSerializer
#from accounts.models import DepartmentSerializer
from .models import Category, CategoryDescription, Item, ItemDescription, ItemImage

class CategorySerializer(serializers.ModelSerializer):
    #template = TemplateSerializer()
    cms_user = UserSerializer(required=False)
    #department = DepartmentSerializer()
    class Meta:
        model = Category
        # fields = ['name', 'is_active', 'priority', 'created_date', 'update_date', 'template', 'cms_user', 'department']
        fields = ['id', 'name', 'is_active', 'priority', 'created_date', 'update_date', 'cms_user']


class CategoryDescriptionSerializer(serializers.ModelSerializer):
    cms_user = UserSerializer(required=False)
    #department = DepartmentSerializer()
    class Meta:
        model = CategoryDescription
        fields = ['name', 'cms_user']


class ItemSerializer(serializers.ModelSerializer):
    cms_user = UserSerializer(required=False)
    # item_image = ItemImageSerializer()
    # item_description = ItemDescriptionSerializer()
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'is_temp', 'is_active', 'created_date', 'update_date', 'cms_user']


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['id', 'item_image', 'is_thumbnail', 'priority', 'is_active', 'created_date', 'update_date']


class ItemDescriptionSerializer(serializers.ModelSerializer):
    category_description = CategoryDescriptionSerializer()
    cms_user = UserSerializer(required=False)
    category_description = CategoryDescription
    class Meta:
        model = ItemDescription
        fields = ['content', 'item', 'is_active', 'created_date', 'update_date', 'category_description', 'cms_user']


# class ProductsSerializer(serializers.ModelSerializer):
#     item = ItemSerializer()
#     item_image = ItemImageSerializer()
#     itme_description = ItemDescriptionSerializer()
#     class Meta: