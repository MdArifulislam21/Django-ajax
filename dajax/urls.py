from django.urls import path
from .views import *
app_name= 'dajax'

urlpatterns = [
    path('', DajaxHome.as_view(), name='home'),
    path('create/', UserCreate.as_view(), name='user_create'),
]
