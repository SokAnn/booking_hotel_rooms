from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .utils import DataMixin, menu

add_menu = [
    {'title': 'Поиск комнаты', 'url_name': 'find'},
    # {'title': 'Забронировать номер', 'url_name': 'add'},
    {'title': 'Мои брони', 'url_name': 'my_rooms'},
]


def new_menu(request):
    context_menu = menu.copy()
    if request.user.is_authenticated:
        for i in add_menu:
            context_menu.append(i)
    return context_menu


def index(request):
    context_menu = new_menu(request)
    context = {
        'menu': context_menu,
        'title': 'Главная страница'
    }
    return render(request, 'rooms/index.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found :( </h1>")


def room_types(request):
    context_menu = new_menu(request)
    form1 = TypePaymentFilterForm()
    form2 = TypeGuestsFilterForm()
    form3 = TypePaymentSortingForm()
    form4 = TypeGuestsSortingForm()
    req = request.POST
    context = {
        'menu': context_menu,
        'title': 'Типы номеров',
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'req': req
    }
    return render(request, 'rooms/room_types.html', context=context)


def find_rooms(request):
    form = FindRoomForm()
    context_menu = new_menu(request)
    context = {
        'menu': context_menu,
        'title': 'Добавление брони',
        'form': form,
        'req': request.POST
    }
    return render(request, 'rooms/find_rooms.html', context=context)


def add_room(request):
    req = request.POST
    form = AddRoomForm()

    if request.method == 'POST':
        form = AddRoomForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['start_time'], type(form.cleaned_data['start_time']))
            print(form.cleaned_data['end_time'], type(form.cleaned_data['end_time']))
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка заполнения формы')

    context_menu = new_menu(request)
    print(req)
    context = {
        'menu': context_menu,
        'title': 'Добавление брони',
        'form': form,
        'req': req,
        'text': 'Параметры брони:'
    }

    return render(request, 'rooms/add_room.html', context=context)


def my_rooms(request):
    context_menu = new_menu(request)
    context = {
        'menu': context_menu,
        'title': 'Список забронированных номеров'
    }
    return render(request, 'rooms/my_rooms.html', context=context)


def show_order(request, pk):
    req = request.POST
    if request.method == 'POST':
        try:
            record = Order.objects.get(id=pk)
            record.delete()
            return redirect('home')
        except:
            return redirect('my_rooms')

    context_menu = new_menu(request)
    context = {
        'menu': context_menu,
        'title': 'Редактирование брони',
        'text': 'Вы точно хотите сохранить изменения (отменить бронь)? '
                'Если это не то, что Вы хотите, то перейдите на любую другую страницу'
    }
    return render(request, 'rooms/add_room.html', context=context)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'rooms/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'rooms/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login')
