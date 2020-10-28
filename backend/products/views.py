from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item, ItemImage, ItemDescription, Category, CategoryDescription
from .serializers import ItemSerializer, CategorySerializer

class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        category = Category()
        category_description = CategoryDescription()
        category.create(request.data, request.user, request.template)
        categorydetail.create(request.data, category)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        items = item.objects.filter(category=category)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.update(request.data, request.template)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def delete(self, request, pk):


class ProductsList(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        item = Item()
        item_image = ItemImage()
        item_description = ItemDescription()
        item.create(request.data, request.user, request.category, request.template)
        item_image.create(request.data, item)
        item_description.create(request.data, request.user, item, request.category_description)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    def put(self, request, pk):
        item = Item.objects.get(pk=pk)
        item_image = Item.objects.filter(item=item)
        item_description = Item.objects.filter(item=item)
        item.update(request.data, request.template)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    def delete(self, request, pk):