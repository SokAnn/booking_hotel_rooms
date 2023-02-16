from django.db.models import Q
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rooms.models import RoomType, Room, Order
from .permissions import IsOwnerOrReadOnly
from .serializers import RoomTypeSerializer, RoomSerializer, OrderSerializer


class RoomTypeAPIList(generics.ListAPIView):
    serializer_class = RoomTypeSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('daily_payment', 'num_guests')

    def get_queryset(self):
        queryset = RoomType.objects.all()

        min_guests = self.request.query_params.get('min_guests')
        max_guests = self.request.query_params.get('max_guests')

        min_payment = self.request.query_params.get('min_payment')
        max_payment = self.request.query_params.get('max_payment')

        if min_guests is not None:
            queryset = queryset.filter(num_guests__gte=min_guests)
        if max_guests is not None:
            queryset = queryset.filter(num_guests__lte=max_guests)

        if min_payment is not None:
            queryset = queryset.filter(daily_payment__gte=min_payment)
        if max_payment is not None:
            queryset = queryset.filter(daily_payment__lte=max_payment)

        return queryset


class RoomAPIList(generics.ListAPIView):
    serializer_class = RoomSerializer
    filter_backends = (DjangoFilterBackend, )

    def get_queryset(self):
        queryset = Room.objects.all()

        min_date = self.request.query_params.get('min_date')
        max_date = self.request.query_params.get('max_date')

        if min_date is not None and max_date is not None:
            find_rooms = Order.objects.filter(~((Q(start_time__lt=min_date) & Q(end_time__lt=min_date)) |
                                                (Q(start_time__gt=max_date) & Q(end_time__gt=max_date))))
            queryset = Room.objects.filter(~Q(id__in=find_rooms.values('room_id')))

        return queryset


class OrderAPIList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)


class OrderAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )

