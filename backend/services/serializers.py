from services.models import Event
from rest_framework import serializers
from .models import Event, EventDetail, Notices


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetail
        fields = ['id', 'image', 'priority']


class EventSerializer(serializers.ModelSerializer):
    detail = EventDetailSerializer(required=False, many=True)
    class Meta:
        model = Event
        fields = ['id', 'title', 'content','start_date', 'is_active', 'end_date', 'thumbnail_image', 'create_date', 'update_date', 'priority', 'user', 'detail', 'url']


class NoticesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = ['id','title', 'content', 'start_date', 'end_date','create_date', 'update_date', 'is_active', 'is_temp','user', 'image']