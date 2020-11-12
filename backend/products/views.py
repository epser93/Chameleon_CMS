from accounts.models import TotalLog, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item, ItemImage, ItemDescription, Category, CategoryDescription, Template, CopyOfItem, CopyOfItemDescription, CopyOfItemImage
from .serializers import CopyItemSerializer, CustomerCategoryJoinSerializer, CustomerCategorySerializer, CustomerItemSerializer, ItemSerializer, CategorySerializer, TemplateSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.views import forbidden_message
from django.core.cache import cache
from cms_pjt.redis_key import RedisKey


message = 'message'
existing_category_message = {message: '존재하는 카테고리 입니다.'}

class CategoryList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_superuser == False and request.user.is_producter == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(username=request.user.username)
        if Category.objects.filter(name=request.data['name']).exists():
            return Response(existing_category_message, status=status.HTTP_400_BAD_REQUEST)
        category = Category()
        template = Template.objects.using('master').get(pk=int(request.data['template']))
        category.create(request.data, user, template, request.FILES.get('image', None))
        for description in request.data.getlist('descriptions'):
            category_description = CategoryDescription()
            category_description.create(description, category)
        log = TotalLog()
        log.update('\'{}\' 카테고리 생성'.format(category.name), None, user)
        category = Category.objects.get(pk=category.pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class CategoryDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        items = Item.objects.filter(category=category)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        if request.user.is_superuser == False and request.user.is_producter == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(username=request.user.username)
        category = Category.objects.using('master').get(pk=pk)
        category.activate()
        log = TotalLog()
        log.update('\'{}\' 카테고리 활성화'.format(category.name), None, user)
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    # 테스트
    def put(self, request, pk):
        if request.user.is_superuser == False and request.user.is_producter == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        if request.data.get('name', None) and Category.objects.filter(name=request.data['name']).exclude(pk=pk).exists():
            return Response(existing_category_message, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.using('master').get(username=request.user.username)
        template = Template.objects.using('master').get(pk=int(request.data['template']))
        category = Category.objects.using('master').get(pk=pk)
        before_name = category.name
        category.update(request.data, user, template, request.FILES.get('image', None))
        self.descriptions_add(request.data, category)
        self.descriptions_update(request.data, category)
        self.descriptions_delete(request.data)
        log = TotalLog()
        log.update('\'{} -> {}\' 카테고리 수정'.format(before_name, category.name), None, user)
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    
    def delete(self, request, pk):
        if request.user.is_superuser == False and request.user.is_producter == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(username=request.user.username)
        category = Category.objects.get(pk=pk)
        category.delete()
        log = TotalLog()
        log.update('\'{}\' 카테고리 비활성화'.format(category.name), None, user)
        answer = {message: "비활성화 되었습니다."}
        return Response(answer)

    
    def descriptions_update(self, data, category):
        descriptions_update_id = list(map(int, data.getlist('descriptions_update_id')))
        descriptions_update_name = data.getlist('descriptions_update_name')
        for i in range(len(descriptions_update_id)):
            category_description = CategoryDescription.objects.using('master').get(pk=descriptions_update_id[i])
            category_description.update(descriptions_update_name[i]) 

    # 위에 코드와 중복됨 나중에 리팩토링
    def descriptions_add(self, data, category):
        for description in data.getlist('descriptions_add'):
            category_description = CategoryDescription()
            category_description.create(description, category)

    def descriptions_delete(self, data):
        for description in data.getlist('descriptions_delete'):
            category_description = CategoryDescription.objects.using('master').get(pk=int(description))
            category_description.delete()


class ProductsList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.is_superuser == False and request.user.is_producter == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        item = Item()
        copy_of_item = CopyOfItem()
        user = User.objects.using('master').get(pk=request.user.pk)
        template = Template.objects.using('master').get(pk=request.data['template'])
        category = Category.objects.using('master').get(pk=request.data['category'])
        item.create(request.data, user, category, template)
        copy_of_item.copy_create(request.data, user, category, template, item)
        item.copy(copy_of_item)
        description_id = list(map(int, request.data.getlist('descriptions_id')))
        descriptions_content = request.data.getlist('descriptions_content')
        for i in range(len(descriptions_content)):
            item_description = ItemDescription()
            copy_item_description = CopyOfItemDescription()
            category_description = CategoryDescription.objects.using('master').get(pk=description_id[i])
            copy_item_description.create(descriptions_content[i], user, copy_of_item, category_description)
            item_description.copy(copy_item_description, item)
        images = []
        number = int(request.data['number'])
        for i in range(number):
            images.append(request.FILES['image{}'.format(i)])
        is_thumbnails = request.data.getlist('is_thumbnails')
        if len(is_thumbnails) == 0:
            is_thumbnails = [False for _ in range(len(images))]
        prioritys = request.data.get('prioritys', [i+1 for i in range(len(images))])
        for i in range(len(images)):
            item_image = ItemImage()
            copy_item_image = CopyOfItemImage()
            item_image.create(images[i], item, is_thumbnails[i], prioritys[i])
            copy_item_image.copy(item_image, copy_of_item)
        log = TotalLog()
        log.update('\'{}\' 아이템 생성'.format(item.name), None, user)
        item = Item.objects.get(pk=item.pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


class ProductDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


    def post(self, request, pk):
        if request.user.is_superuser == False and request.user.is_producter == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        item = Item.objects.using('master').get(pk=pk)
        user = User.objects.using('master').get(username=request.user.username)
        item.activate()
        log = TotalLog()
        log.update('\'{}\' 아이템 활성화'.format(item.name), None, user)
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    

    def put(self, request, pk):
        if request.user.is_superuser == False and request.user.is_producter == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(username=request.user.username)
        item = Item.objects.using('master').get(pk=pk)
        before_name = item.name
        images = ItemImage.objects.using('master').filter(item=item)
        descriptions = ItemDescription.objects.using('master').filter(item=item)
        images.delete()
        descriptions.delete()
        copy_of_item = CopyOfItem.objects.using('master').get(pk=request.data['id'], item=item)
        copy_of_images = CopyOfItemImage.objects.using('master').filter(item=copy_of_item)
        copy_descriptions = CopyOfItemDescription.objects.using('master').filter(item=copy_of_item)
        item.copy(copy_of_item)
        for copy_image in copy_of_images:
            image = ItemImage()
            image.copy(copy_image, item)
        for copy_description in copy_descriptions:
            description = ItemDescription()
            description.copy(copy_description, item)
        log = TotalLog()
        log.update('\'{} -> {}\' 아이템 수정'.format(before_name, item.name), None, user)
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def delete(self, request, pk):
        if request.user.is_superuser == False and request.user.is_producter == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        item = Item.objects.get(pk=pk)
        item.delete()
        log = TotalLog()
        log.update('\'{}\' 아이템 비활성화'.format(item.name), None, user)
        answer = {'message': "비활성화 되었습니다."}
        return Response(answer)


class CopyProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        copy_items = CopyOfItem.objects.filter(item=item)
        serializer = CopyItemSerializer(copy_items, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        if request.user.is_superuser == False and request.user.is_producter == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        item = Item.objects.using('master').get(pk=pk)
        copy_of_item = CopyOfItem()
        template = Template.objects.using('master').get(pk=request.data['template'])
        category = Category.objects.using('master').get(pk=request.data['category'])
        copy_of_item.copy_create(request.data, user, category, template, item)
        description_id = list(map(int, request.data.getlist('descriptions_id')))
        descriptions_content = request.data.getlist('descriptions_content')
        for i in range(len(descriptions_content)):
            copy_item_description = CopyOfItemDescription()
            category_description = CategoryDescription.objects.using('master').get(pk=description_id[i])
            copy_item_description.create(descriptions_content[i], user, copy_of_item, category_description)
        images = []
        number = int(request.data['number'])
        for i in range(number):
            images.append(request.FILES['image{}'.format(i)])
        is_original = request.data.get('is_original', 'True') == 'True'
        images_type = list(map(int, request.data.getlist('images_type')))
        if not images_type:
            images_type = [-1 for _ in range(len(images))]
        is_thumbnails = request.data.getlist('is_thumbnails')
        for i in range(len(is_thumbnails)):
            is_thumbnails[i] = is_thumbnails[i] == 'True'
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
                print(copy_item_image)
                idx += 1
            else:
                if is_original:
                    item_image = ItemImage.objects.using('master').get(pk=i)
                else:
                    item_image = CopyOfItemImage.objects.using('master').get(pk=i)
                copy_item_image.copy(item_image, copy_of_item)
        log = TotalLog()
        log.update('\'{}\' 아이템 히스토리 생성'.format(item.name), None, user)
        copy_of_item = CopyOfItem.objects.get(pk=copy_of_item.pk)
        serializer = CopyItemSerializer(copy_of_item)
        return Response(serializer.data)


class TemplateAPI(APIView):
    
    def get(self, request):
        key = RedisKey.template
        if cache.has_key(RedisKey.template):
            return Response(cache.get(key))
        templates = Template.objects.all()
        serializer = TemplateSerializer(templates, many=True)
        cache.set(key, serializer.data)
        return Response(serializer.data)


class CustomerCategoryAPI(APIView):
    def get(self, request):
        key = RedisKey.category_customer+'all'
        if cache.has_key(key):
            return Response(cache.get(key))
        categories = Category.objects.filter(is_active=True).order_by('priority', '-update_date')
        serializer = CustomerCategorySerializer(categories, many=True)
        cache.set(key, serializer.data)
        return Response(serializer.data)


class CustomerCategoryDetailAPI(APIView):
    def get(self, request, pk):
        key = RedisKey.category_customer + str(pk)
        if cache.has_key(key):
            return Response(cache.get(key))
        category = Category.objects.get(pk=pk, is_active=True)
        serializer = CustomerCategoryJoinSerializer(category)
        cache.set(key, serializer.data)
        return Response(serializer.data)


class CustomerItemAPI(APIView):
    def get(self, request, pk):
        key = RedisKey.item_customer + str(pk)
        if cache.has_key(key):
            return Response(cache.get(key))
        item = Item.objects.get(pk=pk, is_active=True, is_temp=False)
        serializer = CustomerItemSerializer(item)
        cache.set(key, serializer.data)
        return Response(serializer.data)