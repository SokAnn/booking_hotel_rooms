from django.urls import path
from rooms.views import index, room_types, find_rooms, add_room, RegisterUser, LoginUser, logout_user, my_rooms, \
    show_order

urlpatterns = [
    path('', index, name='home'),
    path('room_types/', room_types, name='types'),
    path('find_rooms/', find_rooms, name='find'),
    path('add_room/', add_room, name='add'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('my_rooms/', my_rooms, name='my_rooms'),
    path('order/<int:pk>/', show_order, name='order')
]
