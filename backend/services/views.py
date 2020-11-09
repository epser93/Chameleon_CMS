from django.http import request
from products.models import Item
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, EventDetail, MainCarouselItem, MainItem, Notices
from .serializers import CustomerCarouselSerializer, CustomerEventDetailSerializer, CustomerEventListSerializer, CustomerMainItemSerializer, EventSerializer, MainCarouselItemSerializer, MainItemSerializer, NoticesSerializer, SearchSerializer

message = 'message'

# 이벤트
class EventList(APIView):
    
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        event = Event()
        is_success, answer = event.create(request.data, request.user, request.FILES.get('thumbnail', None))
        if is_success == False:
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        images = []
        number = int(request.data['number'])
        for i in range(number):
            images.append(request.FILES['image{}'.format(i)])
        prioritys = request.data.getlist('prioritys')
        if len(prioritys) == 0:
            prioritys = [i+1 for i in range(len(images))]
        for i in range(len(images)):
            event_detail = EventDetail()
            event_detail.create(images[i], prioritys[i], event, request.user)
        # 이미지 처리로직 넣기
        serializer = EventSerializer(event)
        return Response(serializer.data)


class EventDetailAPI(APIView):

    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def post(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.activate()
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk):
        event = Event.objects.get(is_active=True, pk=pk)
        event.update(request.data, request.user, request.FILES.get('thumbnail', None))
        # 이미지 수정로직 넣기
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def delete(self, request, pk):
        event = Event.objects.get(is_active=True, pk=pk)
        event.delete()
        answer = {message: '이벤트가 비활성화 되었습니다.'}
        return Response(answer, status=status.HTTP_200_OK)

# 공지
class NoticesList(APIView):
    
    def get(self, request):
        notices = Notices.objects.all()
        serializer = NoticesSerializer(notices, many=True)
        return Response(serializer.data)

    def post(self, request):
        notice = Notices()
        is_success, answer = notice.create(request.data, request.user, request.FILES.get('image'))
        if is_success == False:
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        serializer = NoticesSerializer(notice)
        return Response(serializer.data)


class NoticesDetail(APIView):

    def get(self, request, pk):
        notice = Notices.objects.get(pk=pk)
        serializer = NoticesSerializer(notice)
        return Response(serializer.data)

    def post(self, request, pk):
        notice = Notices.objects.get(pk=pk)
        notice.start()
        serializer = NoticesSerializer(notice)
        return Response(serializer.data)

    def put(self, request, pk):
        notice = Notices.objects.get(pk=pk)
        notice.update(request.data, request.user, request.FILES.get('image'))
        serializer = NoticesSerializer(notice)
        return Response(serializer.data)

    def delete(self, request, pk):
        notice = Notices.objects.get(is_active=True, pk=pk)
        notice.delete()
        answer = {message: '공지가 비활성화 되었습니다.'}
        return Response(answer, status=status.HTTP_200_OK)


class CustomerSearchAPI(APIView):
    def get(self, request):
        serializer = SearchSerializer(request.user, context = {'content': request.GET.get('content', None)})
        return Response(serializer.data)


class MainItemAPI(APIView):
    def get(self, request):
        main_items = MainItem.objects.all()
        serializer = MainItemSerializer(main_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        priority = request.data['priority']
        is_active = request.data.get('is_active', 'True') == 'True'
        if is_active and MainItem.objects.filter(priority=priority).filter(is_active=True).exists():
            answer = {message: '해당위치에 아이템이 등록되어 있습니다. '}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        item = Item.objects.get(pk=request.data['id'])
        main_item = MainItem()
        main_item.create(item, request.user, priority, is_active)
        serializer = MainItemSerializer(main_item)
        return Response(serializer.data)



class MainItemDetailAPI(APIView):
    def get(self, request, pk):
        main_item = MainItem.objects.get(pk=pk)
        serializer = MainItemSerializer(main_item)
        return Response(serializer.data)

    def post(self, request, pk):
        main_item = MainItem.objects.get(pk=pk)
        if MainItem.objects.filter(priority=main_item.priority).filter(is_active=True).exists():
            answer = {message: '해당위치에 아이템이 등록되어 있습니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        main_item.activate()
        serializer = MainItemSerializer(main_item)
        return Response(serializer.data)

    def put(self, request, pk):
        main_item = MainItem.objects.get(pk=pk)
        priority = request.data.get('priority', main_item.priority)
        if priority != main_item.priority and MainItem.objects.filter(priority=priority).filter(is_active=True).exists():
            answer = {message: '해당위치에 아이템이 등록되어 있습니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        item = None
        if request.data.get('id', None):
            item = Item.objects.get(pk=request.data['id'])
        main_item.update(item, request.user, priority, request.data.get('is_active', main_item.is_active))
        serializer = MainItemSerializer(main_item)
        return Response(serializer.data)

    def delete(self, request, pk):
        main_item = MainItem.objects.get(pk=pk)
        main_item.delete()
        answer = {message: '해당 메인 아이템을 비활성화 했습니다.'}
        return Response(answer)


class MainCarouselItemAPI(APIView):
    def get(self, request):
        main_carousel_items = MainCarouselItem.objects.all()
        serializer = MainCarouselItemSerializer(main_carousel_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        main_carousel_item = MainCarouselItem()
        main_carousel_item.update(request.data, request.user, request.FILES.get('image', None))
        serializer = MainCarouselItemSerializer(main_carousel_item)
        return Response(serializer.data)


class MainCarouselItemDetailAPI(APIView):
    def get(self, reqeust, pk):
        main_carousel = MainCarouselItem.objects.get(pk=pk)
        serializer = MainCarouselItemSerializer(main_carousel)
        return Response(serializer.data)


    def post(self, request, pk):
        main_carousel = MainCarouselItem.objects.get(pk=pk)
        main_carousel.activate()
        serializer = MainCarouselItemSerializer(main_carousel)
        return Response(serializer.data)


    def put(self, request, pk):
        main_carousel = MainCarouselItem.objects.get(pk=pk)
        main_carousel.update(request.data, request.user, request.FILES.get('image', None))
        serializer = MainCarouselItemSerializer(main_carousel)
        return Response(serializer.data)


    def delete(self, request, pk):
        main_carousel = MainCarouselItem.objects.get(pk=pk)
        main_carousel.delete()
        answer = {message: '케로셀 아이템이 비활성화 되었습니다.'}
        return Response(answer)


class CustomerMainItemAPI(APIView):
    def get(self, request):
        main_item = MainItem.objects.filter(is_active=True).order_by('priority', '-update_date')
        serializer = CustomerMainItemSerializer(main_item, many=True)
        return Response(serializer.data)


class CustomerCarouselAPI(APIView):
    def get(self, request):
        carousel_item = MainCarouselItem.objects.filter(is_active=True).order_by('priority', '-update_date')
        serializer = CustomerCarouselSerializer(carousel_item, many=True)
        return Response(serializer.data)


class CustomerEventAPI(APIView):
    def get(self, request):
        events = Event.objects.filter(is_active=True).order_by('priority', 'update_date')
        serializer = CustomerEventListSerializer(events, many=True)
        return Response(serializer.data)


class CustomerEventDetailAPI(APIView):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk, is_active=True)
        serializer = CustomerEventDetailSerializer(event)
        return Response(serializer.data)