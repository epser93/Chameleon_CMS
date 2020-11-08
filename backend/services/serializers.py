from products.serializers import ItemSerializer
from products.models import Item
from django.db.models import Q
from accounts.models import User
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


class SearchSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['items', 'events']

    def get_events(self, obj):
        content = self.context.get('content', '0000')
        events = Event.objects.filter(Q(title__contains=content) | Q(content__contains=content)).exclude(is_active=False)
        serializer = EventSerializer(events, many=True).data
        return serializer
    
    def get_items(self, obj):
        content = self.context.get('content', '0000')
        items = Item.objects.filter(name__contains=content).exclude(is_temp=True).exclude(is_active=False)
        serializer = ItemSerializer(items, many=True).data
        return serializer