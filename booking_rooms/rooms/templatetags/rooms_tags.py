from django import template
from django.contrib.auth.models import User
from django.db.models import Q
import datetime
from rooms.models import RoomType, Order, Room

register = template.Library()


@register.inclusion_tag('rooms/list_types.html')
def show_room_types(request):
    if not request:
        room_types = RoomType.objects.all()
    else:
        if 'daily_payment' in request:
            temp = float(request['daily_payment'])
            room_types = RoomType.objects.filter(daily_payment__gte=temp)
        else:
            if 'num_guests' in request:
                temp = int(request['num_guests'])
                room_types = RoomType.objects.filter(num_guests__gte=temp)
            else:
                if 'order_payment' in request:
                    room_types = RoomType.objects.order_by('-daily_payment')
                else:
                    if 'order_guests' in request:
                        room_types = RoomType.objects.order_by('-num_guests')
                    else:
                        room_types = RoomType.objects.all()
    return {'types': room_types}


@register.inclusion_tag('rooms/my_orders.html')
def show_my_rooms(user_id):
    current_user = User.objects.get(pk=user_id)
    orders = current_user.order_set.all()
    return {'orders': orders}


@register.inclusion_tag('rooms/list_rooms.html')
def show_rooms(request):
    if not request:
        curr_rooms = {}
    else:
        start_time = datetime.date.fromisoformat(request['start_time'])
        end_time = datetime.date.fromisoformat(request['end_time'])
        find_rooms = Order.objects.filter(~((Q(start_time__lt=start_time) & Q(end_time__lt=start_time)) |
                                          (Q(start_time__gt=end_time) & Q(end_time__gt=end_time))))
        if not find_rooms:
            curr_rooms = Room.objects.all()
        else:
            curr_rooms = Room.objects.filter(~Q(id__in=find_rooms.values('room_id')))
    return {'rooms': curr_rooms}



