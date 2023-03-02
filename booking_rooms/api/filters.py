from django.db.models import Q
from django_filters import rest_framework as filters
from .models import RoomType, Order, Room


class RoomTypeFilter(filters.FilterSet):
    daily_payment = filters.RangeFilter()
    num_guests = filters.RangeFilter()

    class Meta:
        model = RoomType
        fields = ['daily_payment', 'num_guests']


class RoomFilter(filters.FilterSet):
    class Meta:
        model = Room
        fields = ['room_type']

    @property
    def qs(self):
        parent = super().qs

        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')

        if start_time is not None and end_time is not None:
            return parent.exclude(id__in=Order.objects.filter(~((Q(start_time__lt=start_time) &
                                                                 Q(end_time__lt=start_time)) |
                                                                (Q(start_time__gt=end_time) &
                                                                 Q(end_time__gt=end_time)))).values('room_id'))
        else:
            return parent.all()


class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = ['user', ]

    @property
    def qs(self):
        parent = super().qs
        user = getattr(self.request, 'user', None)

        return parent.filter(user=user)
