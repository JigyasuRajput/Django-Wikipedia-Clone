from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.title, name="title"),
    path("search/", views.search, name="search"),
    path("new_page/", views.new_page, name="new_page"),
    path("edit/<str:title>/", views.edit_page, name="edit_page"),
    path("entry/<str:title>/", views.title, name="entry"),
    path("random/", views.random_page, name="random_page"),
] 
