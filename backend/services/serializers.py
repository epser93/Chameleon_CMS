from services.models import Event
from rest_framework import serializers
from .models import Event, EventDetail, Notices


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetail
        fields = ['image', 'content', 'priority']
        # fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    detail = EventDetailSerializer(required=False, many=True)
    class Meta:
        model = Event
        fields = ['id', 'title', 'start_date', 'end_date', 'thumbnail_image', 'create_date', 'update_date', 'priority', 'user', 'detail']


class NoticesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = ['id','title', 'content', 'create_date', 'update_date', 'is_active', 'user', 'image']