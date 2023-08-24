from django.urls import path
from . import views

urlpatterns = [
    path('', views.diabetic, name='diabetic'),
]