from products.models import Item
from accounts.models import TotalLog, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, EventDetail, MainCarouselItem, MainItem, Notices
from .serializers import CustomerCarouselSerializer, CustomerEventDetailSerializer, CustomerEventListSerializer, CustomerMainItemSerializer, EventSerializer, MainCarouselItemSerializer, MainItemSerializer, NoticesSerializer, SearchSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.views import forbidden_message


message = 'message'

# 이벤트
class EventList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_superuser == False and request.user.is_eventer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        event = Event()
        is_success, answer = event.create(request.data, user, request.FILES.get('thumbnail', None))
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
            event_detail.create(images[i], prioritys[i], event, user)
        log = TotalLog()
        log.update('\'{}\' 이벤트 생성'.format(event.title), None, user)
        event = Event.objects.get(pk=event.pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)


class EventDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def post(self, request, pk):
        if request.user.is_superuser == False and request.user.is_eventer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        event = Event.objects.using('master').get(pk=pk)
        event.activate()
        log = TotalLog()
        log.update('\'{}\' 이벤트 활성화'.format(event.title), None, user)
        event = Event.objects.get(pk=event.pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk):
        if request.user.is_superuser == False and request.user.is_eventer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        event = Event.objects.using('master').get(is_active=True, pk=pk)
        before_title = event.title
        event.update(request.data, user, request.FILES.get('thumbnail', None))
        # 이미지 수정로직 넣기

        log = TotalLog()
        log.update('\'{} -> {}\' 이벤트 수정'.format(before_title, event.title), None, user)
        event = Event.objects.get(pk=event.pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def delete(self, request, pk):
        if request.user.is_superuser == False and request.user.is_eventer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        event = Event.objects.using('master').get(is_active=True, pk=pk)
        event.delete()
        log = TotalLog()
        log.update('\'{}\' 이벤트 비활성화'.format(event.title), None, user)
        answer = {message: '이벤트가 비활성화 되었습니다.'}
        return Response(answer, status=status.HTTP_200_OK)

# 공지
class NoticesList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notices = Notices.objects.all()
        serializer = NoticesSerializer(notices, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        notice = Notices()
        is_success, answer = notice.create(request.data, user, request.FILES.get('image'))
        if is_success == False:
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        log = TotalLog()
        log.update('\'{}\' 공지 생성'.format(notice.title), None, user)
        notice = Notices.objects.get(pk=notice.pk)
        serializer = NoticesSerializer(notice)
        return Response(serializer.data)


class NoticesDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        notice = Notices.objects.get(pk=pk)
        serializer = NoticesSerializer(notice)
        return Response(serializer.data)

    def post(self, request, pk):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        notice = Notices.objects.using('master').get(pk=pk)
        notice.start()
        log = TotalLog()
        log.update('\'{}\' 공지 활성화'.format(notice.title), None, user)
        notice = Notices.objects.get(pk=notice.pk)
        serializer = NoticesSerializer(notice)
        return Response(serializer.data)

    def put(self, request, pk):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        notice = Notices.objects.using('master').get(pk=pk)
        before_title = notice.title
        notice.update(request.data, user, request.FILES.get('image'))
        log = TotalLog()
        log.update('\'{} -> {}\' 공지 수정'.format(before_title, notice.title), None, user)
        notice = Notices.objects.get(pk=notice.pk)
        serializer = NoticesSerializer(notice)
        return Response(serializer.data)

    def delete(self, request, pk):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        notice = Notices.objects.get(is_active=True, pk=pk)
        _type = '비활성화'
        if notice.is_temp == True:
            _type = '삭제'
        notice.delete()
        log = TotalLog()
        log.update('\'{}\' 공지 {}'.format(notice.title, _type), None, user)
        answer = {message: '공지가 {} 되었습니다.'.format(_type)}
        return Response(answer, status=status.HTTP_200_OK)


class CustomerSearchAPI(APIView):
    def get(self, request):
        serializer = SearchSerializer(request.user, context = {'content': request.GET.get('content', None)})
        return Response(serializer.data)


class MainItemAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        main_items = MainItem.objects.all()
        serializer = MainItemSerializer(main_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        priority = request.data['priority']
        is_active = request.data.get('is_active', 'True') == 'True'
        if is_active and MainItem.objects.filter(priority=priority).filter(is_active=True).exists():
            answer = {message: '해당위치에 아이템이 등록되어 있습니다. '}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        item = Item.objects.using('master').get(pk=request.data['id'])
        main_item = MainItem()
        main_item.create(item, user, priority, is_active)
        log = TotalLog()        
        log.update('\'{}\' 메인아이템 생성'.format(main_item.item.name), None, user)
        main_item = MainItem.objects.get(pk=main_item.pk)
        serializer = MainItemSerializer(main_item)
        return Response(serializer.data)



class MainItemDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        main_item = MainItem.objects.get(pk=pk)
        serializer = MainItemSerializer(main_item)
        return Response(serializer.data)

    def post(self, request, pk):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        main_item = MainItem.objects.using('master').get(pk=pk)
        if MainItem.objects.filter(priority=main_item.priority).filter(is_active=True).exists():
            answer = {message: '해당위치에 아이템이 등록되어 있습니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        main_item.activate()
        log = TotalLog()        
        log.update('\'{}\' 메인아이템 활성화'.format(main_item.item.name), None, user)
        main_item = MainItem.objects.get(pk=main_item.pk)
        serializer = MainItemSerializer(main_item)
        return Response(serializer.data)

    def put(self, request, pk):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        main_item = MainItem.objects.using('master').get(pk=pk)
        before_name = main_item.item.name
        priority = request.data.get('priority', main_item.priority)
        if priority != main_item.priority and MainItem.objects.filter(priority=priority).filter(is_active=True).exists():
            answer = {message: '해당위치에 아이템이 등록되어 있습니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        item = None
        if request.data.get('id', None):
            item = Item.objects.using('master').get(pk=request.data['id'])
        main_item.update(item, user, priority, request.data.get('is_active', main_item.is_active))
        log = TotalLog()
        log.update('\'{} ->{}\' 메인아이템 수정'.format(before_name, main_item.item.name), None, user)
        main_item = MainItem.objects.get(pk=main_item.pk)
        serializer = MainItemSerializer(main_item)
        return Response(serializer.data)

    def delete(self, request, pk):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        main_item = MainItem.objects.using('master').get(pk=pk)
        main_item.delete()
        log = TotalLog()
        log.update('\'{}\' 메인아이템 비활성화'.format(main_item.item.name), None, user)
        answer = {message: '해당 메인 아이템을 비활성화 했습니다.'}
        return Response(answer)


class MainCarouselItemAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        main_carousel_items = MainCarouselItem.objects.all()
        serializer = MainCarouselItemSerializer(main_carousel_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        main_carousel = MainCarouselItem()
        main_carousel.update(request.data, user, request.FILES.get('image', None))
        log = TotalLog()
        log.update('\'{}\' 케로셀 아이템 생성'.format(main_carousel.title), None, user)
        main_carousel = MainCarouselItem.objects.get(pk=main_carousel.pk)
        serializer = MainCarouselItemSerializer(main_carousel)
        return Response(serializer.data)


class MainCarouselItemDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, reqeust, pk):
        main_carousel = MainCarouselItem.objects.get(pk=pk)
        serializer = MainCarouselItemSerializer(main_carousel)
        return Response(serializer.data)


    def post(self, request, pk):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        main_carousel = MainCarouselItem.objects.using('master').get(pk=pk)
        main_carousel.activate()
        log = TotalLog()
        log.update('\'{}\' 케로셀 아이템 활성화'.format(main_carousel.title), None, user)
        main_carousel = MainCarouselItem.objects.get(pk=main_carousel.pk)
        serializer = MainCarouselItemSerializer(main_carousel)
        return Response(serializer.data)


    def put(self, request, pk):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        main_carousel = MainCarouselItem.objects.using('master').get(pk=pk)
        before_name = main_carousel.title
        main_carousel.update(request.data, user, request.FILES.get('image', None))
        log = TotalLog()
        log.update('\'{} -> {}\' 케로셀 아이템 변경'.format(before_name, main_carousel.title), None, user)
        main_carousel = MainCarouselItem.objects.get(pk=main_carousel.pk)
        serializer = MainCarouselItemSerializer(main_carousel)
        return Response(serializer.data)


    def delete(self, request, pk):
        if request.user.is_superuser == False and request.user.is_marketer == False :
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        user = User.objects.using('master').get(pk=request.user.pk)
        main_carousel = MainCarouselItem.objects.using('master').get(pk=pk)
        main_carousel.delete()
        log = TotalLog()
        log.update('\'{}\' 케로셀 아이템 비활성화'.format(main_carousel.title), None, user)
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