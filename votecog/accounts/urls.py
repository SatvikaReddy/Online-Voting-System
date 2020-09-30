from django.urls import path
from . import views
from .views import home
# from .views import PersonCreateView
from django.conf.urls import url

app_name = 'accounts'
urlpatterns = [
   path('home-page/', views.home, name='home-page'),
   path('profile/', views.profile, name='profile'),
   path('cform/', views.cform, name='person_form'),
    path('success/', views.success, name='success'),
    path('dash/', views.dashboard, name='dashboard'),
    url(r'^dash/(?P<pk>[0-9]+)/cstatus/$', views.cstatus, name='cstatus'),
    url(r'^dash/(?P<pk>[0-9]+)/$', views.sdetails, name='sdetails'),
]