from django.http import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item, ItemImage, ItemDescription, Category, CategoryDescription, Template
from .serializers import ItemSerializer, CategorySerializer

class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
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
        items = Item.objects.filter(category=category)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.is_active = True
        category.save()
        serializer = CategorySerializer(category)
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
        return Response('삭제완료')

    
    def descriptions_update(self, data, category):
        for description in data.get('descriptions_update', []):
            category_description = CategoryDescription.objects.get(pk=description['id'])
            category_description.update(description['name']) 

    # 위에 코드와 중복됨 나중에 리팩토링
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
        print(request.data)
        # return Response(1)
        item = Item()
        template = Template.objects.get(pk=request.data['template'])
        category = Category.objects.get(pk=request.data['category'])
        item.create(request.data, request.user, category, template)
        for description in request.data.get('descriptions', []):
            item_description = ItemDescription()
            category_description = CategoryDescription.objects.get(pk=description['id'])
            item_description.create(description['content'], request.user, item, category_description)
        # 임시저장 테이블 추가, 임시저장 데이터 추가 기능 

        # 이미지 추가 코드 넣기
        images = request.FILES.getlist('images')
        is_thumbnails = request.data.get('is_thumbnails', [False for _ in range(len(images))])
        prioritys = request.data.get('prioritys', [i+1 for i in range(len(images))])
        for i in range(len(images)):
            item_image = ItemImage()
            item_image.create(images[i], item, is_thumbnails[i], prioritys[i])
        serializer = ItemSerializer(item)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


    def post(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.is_active = True
        item.save()
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    def put(self, request, pk):
        item = Item.objects.get(pk=pk)
        template = Template.objects.get(id=request.data['template'])
        item.update(request.data, template)
        self.descriptions_add(request.data, item, request.user)
        self.descriptions_update(request.data)
        self.descriptions_delete(request.data)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
        

    def descriptions_update(self, data):
        for description in data.get('descriptions_update', []):
            item_description = ItemDescription.objects.get(id=description['id'])
            item_description.update(description['content'])

    # 위에 코드와 중복됨 나중에 리팩토링(상속 or 외부로 함수빼기)
    def descriptions_add(self, data, item, user):
        for description in data.get('descriptions_add', []):
            category_description = CategoryDescription.objects.get(id=description['id'])
            item_description = ItemDescription()
            item_description.create(description['content'], user, item, category_description)

    def descriptions_delete(self, data):
        for description in data.get('descriptions_delete', []):
            item_description = ItemDescription.objects.get(pk=description)
            item_description.delete()