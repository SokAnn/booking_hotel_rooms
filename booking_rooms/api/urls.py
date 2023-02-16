from django.urls import path, include
from api.views import RoomTypeAPIList, RoomAPIList, OrderAPIList, OrderAPIDestroy

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('room_types/', RoomTypeAPIList.as_view()),
    path('rooms/', RoomAPIList.as_view()),
    path('orders/', OrderAPIList.as_view()),
    path('orders_delete/<int:pk>/', OrderAPIDestroy.as_view()),
]
