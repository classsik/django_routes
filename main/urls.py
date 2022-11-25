from django.urls import path, include

from . import views

posts_urls = [
    path('', views.all_posts),
    path('popular', views.popular_posts),
    path('latest', views.latest_posts),
    path('<int:post_id>/likes', views.post_likes),
    path('<int:post_id>/comments', views.post_comments)
]

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('contacts', views.contacts),
    path('access/', views.access),
    path('json/', views.json),
    path('set/', views.set),
    path('get/', views.get),
    path('posts/', include(posts_urls))
]
