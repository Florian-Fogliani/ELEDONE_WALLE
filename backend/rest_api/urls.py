from django.urls import path
from .views import StartView, StopView

urlpatterns = [
    path('start/', StartView.as_view(), name='start'),
    path('stop/', StopView.as_view(), name='stop'),
]