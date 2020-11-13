from products.models import Item
from accounts.serializers import UserSerializer
from products.serializers import CustomerItemSerializer, ItemSerializer, MainItemJoinSerializer
from django.db.models import Q
from accounts.models import User
from services.models import Event
from rest_framework import serializers
from .models import Event, EventDetail, MainCarouselItem, MainItem, Notices


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetail
        fields = ['id', 'image', 'priority']


class EventSerializer(serializers.ModelSerializer):
    images = EventDetailSerializer(required=False, many=True)
    class Meta:
        model = Event
        fields = ['id', 'title', 'content','start_date', 'is_active', 'end_date', 'thumbnail_image', 'create_date', 'update_date', 'priority', 'user', 'images', 'url']


class NoticesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = ['id','title', 'content', 'start_date', 'end_date','create_date', 'update_date', 'is_active', 'is_temp','user', 'image']


class MainItemSerializer(serializers.ModelSerializer):
    item = MainItemJoinSerializer()
    user = UserSerializer()
    class Meta:
        model = MainItem
        fields = ['id', 'priority', 'is_active','create_date', 'update_date', 'item', 'user']


class MainCarouselItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = MainCarouselItem
        fields = ['id', 'title', 'priority', 'image', 'is_active', 'url', 'create_date', 'update_date', 'user']


class CustomerMainItemSerializer(serializers.ModelSerializer):
    item = MainItemJoinSerializer()
    class Meta:
        model = MainItem
        fields = ['id', 'priority', 'item']


class CustomerCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCarouselItem
        fields = ['id', 'image', 'url']


class CustomerEventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'content', 'start_date', 'end_date', 'thumbnail_image', 'priority']


class CustomerEventDetailSerializer(serializers.ModelSerializer):
    images = EventDetailSerializer(required=False, many=True)
    class Meta:
        model = Event
        fields = ['id', 'title', 'start_date', 'end_date', 'thumbnail_image', 'priority', 'content', 'url', 'images']


class SearchSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['items', 'events']

    def get_events(self, obj):
        content = self.context.get('content', '')
        events = Event.objects.filter(Q(title__contains=content) | Q(content__contains=content)).exclude(is_active=False)
        serializer = CustomerEventListSerializer(events, many=True)
        return serializer.data
    
    def get_items(self, obj):
        content = self.context.get('content', '')
        items = Item.objects.filter(name__contains=content).exclude(is_temp=True).exclude(is_active=False)
        serializer = CustomerItemSerializer(items, many=True)
        return serializer.data


class CustomerNoticeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = ['id', 'title', 'content', 'start_date', 'image']