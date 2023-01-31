from django.contrib import admin

from .models import *


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'daily_payment', 'num_guests')
    list_display_links = ('title',)
    search_fields = ('daily_payment', 'num_guests')
    list_filter = ('daily_payment', 'num_guests')


admin.site.register(RoomType, RoomTypeAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_type')
    list_display_links = ('room_type',)
    search_fields = ('room_type',)
    list_filter = ('room_type',)


admin.site.register(Room, RoomAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_id', 'user_id', 'start_time', 'end_time')
    list_display_links = ('room_id', 'user_id')
    search_fields = ('room_id', 'user_id', 'start_time', 'end_time')
    list_filter = ('room_id', 'user_id', 'start_time', 'end_time')


admin.site.register(Order, OrderAdmin)
