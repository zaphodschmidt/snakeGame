# snakeGame/urls.py
from django.urls import path
from .views import my_datastar_view

urlpatterns = [
    # Point directly to the view function you just wrote
    path('', my_datastar_view, name='game-stream'),
]