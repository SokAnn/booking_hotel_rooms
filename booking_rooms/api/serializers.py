from rest_framework import serializers
from rooms.models import RoomType, Room, Order


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ('id', 'title', 'daily_payment', 'num_guests')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'room_type')


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ('id', 'room', 'user', 'start_time', 'end_time')

