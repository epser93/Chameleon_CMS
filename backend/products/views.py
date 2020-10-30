from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item, ItemImage, ItemDescription, Category, CategoryDescription, Template
from .serializers import ItemSerializer, CategorySerializer

class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.filter(is_active=True)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        if Category.objects.filter(name=request.data['name']).exists():
            return Response('존재하는 카테고리 입니다.', status=status.HTTP_400_BAD_REQUEST)
        category = Category()
        template = Template.objects.get(pk=request.data['template'])
        category.create(request.data, request.user, template)
        for description in request.data['descriptions']:
            category_description = CategoryDescription()
            category_description.create(description, category)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class CategoryDetail(APIView):

    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        items = Item.objects.filter(category=category).filter(is_active=True)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    # 테스트
    def put(self, request, pk):
        template = Template.objects.get(pk=request.data['template'])
        category = Category.objects.get(pk=pk)
        category.update(request.data, template)
        self.descriptions_add(request.data, category)
        self.descriptions_update(request.data, category)
        self.descriptions_delete(request.data)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    
    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()

    
    def descriptions_update(self, data, category):
        for description in data.get('descriptions_update', []):
            category_description = CategoryDescription.objects.get(pk=description['id'])
            category_description.update(description['name']) 

    def descriptions_add(self, data, category):
        for description in data.get('descriptions_add', []):
            category_description = CategoryDescription()
            category_description.create(description, category)

    def descriptions_delete(self, data):
        for description in data.get('descriptions_delete', []):
            category_description = CategoryDescription.objects.get(pk=description)
            category_description.delete()


class ProductsList(APIView):
    
    def post(self, request, format=None):
        item = Item()
        template = Template.objects.get(pk=request.data['template'])
        category = Category.objects.get(pk=request.data['category'])
        item.create(request.data, request.user, category, template)
        for description in request.data['descriptions']:
            item_description = ItemDescription()
            category_description = CategoryDescription.objects.get(pk=description['id'])
            item_description.create(description['content'], request.user, item, category_description)
        # 임시저장 테이블 추가, 임시저장 데이터 추가 기능 

        # 이미지 추가 코드 넣기
        serializer = ItemSerializer(item)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk, is_active=True)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    def put(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.update(request.data)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
        