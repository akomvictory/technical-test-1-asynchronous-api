from django.urls import path
from api_async_app import views

urlpatterns = [
    path('quotes/', views.get_quotes, name='get_quotes'),
    path('randomuser/', views.get_random_user, name='get_random_user'),
]