from django.urls import path
from app_basic_1 import views


app_name = 'app_basic_1'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login,  name='user_login'),
]