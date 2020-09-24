from django.urls import path
from . import views
from .views import home
from .views import PersonCreateView

app_name = 'accounts'
urlpatterns = [
   path('home-page/', views.home, name='home-page'),
   path('profile/', views.profile, name='profile'),
   path('cform/', PersonCreateView.as_view(), name='person_form'),
    path('success/', views.success, name='success'),
]