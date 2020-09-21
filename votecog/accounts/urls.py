from django.urls import path
from . import views
from .views import home

app_name = 'accounts'
urlpatterns = [
   path('home-page/', views.home, name='home-page'),
   path('profile/', views.profile, name='profile')
]