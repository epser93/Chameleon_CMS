from django.http import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, EventDetail, Notices
from .serializers import EventSerializer, NoticesSerializer

message = 'message'

# 이벤트
class EventList(APIView):
    
    def get(self, request):
        events = Event.objects.filter(is_active=True)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        event = Event()
        is_success, answer = event.create(request.data, request.user, request.FILES['thumbnail'])
        if is_success == False:
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        images = request.FILES.getlist('images')
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