from django.urls import path

from .views import home_view, list_view, detail_view

app_name = 'blogs'

urlpatterns = [
	path('', home_view, name='home'),
	path('list/', list_view, name='list'),
	path('<int:id>/detail/', detail_view, name='detail'),
]
