from django.http import request
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item, ItemImage, ItemDescription, Category, CategoryDescription, Template, CopyOfItem, CopyOfItemDescription, CopyOfItemImage
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
        item = Item()
        copy_of_item = CopyOfItem()
        template = Template.objects.get(pk=request.data['template'])
        category = Category.objects.get(pk=request.data['category'])
        item.create(request.data, request.user, category, template)
        copy_of_item.copy_create(request.data, request.user, category, template, item)

        for description in request.data.get('descriptions', []):
            item_description = ItemDescription()
            copy_item_description = CopyOfItemDescription()
            category_description = CategoryDescription.objects.get(pk=description['id'])
            item_description.create(description['content'], request.user, item, category_description)
            copy_item_description.create(description['content'], request.user, copy_of_item, category_description)
        images = request.FILES.getlist('images')
        is_thumbnails = request.data.get('is_thumbnails', [False for _ in range(len(images))])
        prioritys = request.data.get('prioritys', [i+1 for i in range(len(images))])
        for i in range(len(images)):
            item_image = ItemImage()
            copy_item_image = CopyOfItemImage()
            item_image.create(images[i], item, is_thumbnails[i], prioritys[i])
            copy_item_image.copy(item_image, copy_of_item)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


    def post(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.recovery()
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    

    def put(self, request, pk):
        item = Item.objects.get(pk=pk)
        images = ItemImage.objects.filter(item=item)
        descriptions = ItemDescription.objects.filter(item=item)
        images.delete()
        descriptions.delete()
        copy_of_item = CopyOfItem.objects.get(pk=request.data['id'], item=item)
        copy_of_images = CopyOfItemImage.objects.filter(item=copy_of_item)
        copy_descriptions = CopyOfItemDescription.objects.filter(item=copy_of_item)
        item.copy(copy_of_item)
        for copy_image in copy_of_images:
            image = ItemImage()
            image.copy(copy_image, item)
        for copy_description in copy_descriptions:
            description = ItemDescription()
            description.copy(copy_description, item)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def delete(self, reqeust, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        answer = {'message': "비활성화 되었습니다."}
        return Response(answer)


class CopyProduct(APIView):

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        copy_items = CopyOfItem.objects.filter(item=item)
        serializer = ItemSerializer(copy_items, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        print(request.data)
        item = Item.objects.get(pk=pk)
        copy_of_item = CopyOfItem()
        template = Template.objects.get(pk=request.data['template'])
        category = Category.objects.get(pk=request.data['category'])
        copy_of_item.copy_create(request.data, request.user, category, template, item)
        for description in request.data.get('descriptions', []):
            copy_item_description = CopyOfItemDescription()
            category_description = CategoryDescription.objects.get(pk=description['id'])
            copy_item_description.create(description['content'], request.user, copy_of_item, category_description)
        images = request.FILES.getlist('images')
        is_original = request.data.get('is_original', 'True') == 'True'
        images_type = list(map(int, request.data.getlist('images_type')))
        if not images_type:
            images_type = [-1 for _ in range(len(images))]
        is_thumbnails = list(map(bool, request.data.getlist('is_thumbnails')))
        if not is_thumbnails:
            is_thumbnails = [False for _ in range(len(images))]
        prioritys = list(map(int, request.data.getlist('prioritys')))
        if not prioritys:
            prioritys = [i+1 for i in range(len(images))]
        idx = 0
        for i in images_type:
            copy_item_image = CopyOfItemImage()
            if i == -1:
                copy_item_image.create(images[idx], copy_of_item, is_thumbnails[idx], prioritys[idx])
                idx += 1
            else:
                if is_original:
                    item_image = ItemImage.objects.get(pk=i)
                else:
                    item_image = CopyOfItemImage.objects.get(pk=i)
                copy_item_image.copy(item_image, copy_of_item)

        serializer = ItemSerializer(copy_of_item)
        return Response(serializer.data)