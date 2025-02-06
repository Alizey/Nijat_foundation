from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('' , views.index , name='index'),
    path('signup' , views.signup , name='signup'),
    path('login' , views.login, name='login')
]