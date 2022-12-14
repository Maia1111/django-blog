from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    
    path("home2", views.home2, name="home2"),
    path("home3", views.home3, name="home3"),
    path("home4", views.home4, name="home4"),
    path("home5", views.home5, name="home5"),
    path("home6", views.home6, name="home6"),
    path("home7", views.home7, name="home7"),
    path("colapse", views.colapse, name="colapse"),
    path("flexbox", views.flexbox, name="flexbox"),
    path("flexbox2", views.flexbox2, name="flexbox2"),
    path('post/<int:post_id>/post_detail', views.post_detail, name='post_detail'),
]
