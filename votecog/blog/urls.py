from django.conf.urls import url
from django.urls import path
from . import views
from .views import DeletePostView, like_post
from django.conf import settings
from django.conf.urls.static import static
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', DeletePostView.as_view(), name='post_delete'),
    path('like/', like_post, name='like_post'),
    path('stat/', views.stat, name='stat'),
    # url(r'^post/(?P<pk>[0-9]+)/comment/$', views.AddCommentView, name='add_comment'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
