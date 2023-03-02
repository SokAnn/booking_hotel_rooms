from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import RoomType, Room, Order
from .permissions import IsOwnerOrReadOnly
from .serializers import RoomTypeSerializer, RoomSerializer, OrderSerializer
from .filters import RoomTypeFilter, OrderFilter, RoomFilter


class RoomTypeAPIList(generics.ListAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('daily_payment', 'num_guests')
    filterset_class = RoomTypeFilter


class RoomAPIList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = RoomFilter


class OrderAPIList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filterset_class = OrderFilter


class OrderAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
