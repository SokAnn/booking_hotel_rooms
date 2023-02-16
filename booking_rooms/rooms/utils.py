
menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Типы номеров', 'url_name': 'types'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
