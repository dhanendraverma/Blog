from django.urls import path,re_path
from blog import views

urlpatterns = [
    re_path(r'^$',views.PostListView.as_view(),name='post_list'),
    re_path(r'^$',views.AboutView.as_view(),name='about'),
    re_path(r'post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
]