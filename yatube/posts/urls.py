from django.urls import path

from . import views

app_name = 'posts'


urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('group_posts/<slug:slug>/', views.group_posts, name='group_post'),
]
