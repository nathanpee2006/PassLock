from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("get-form", views.get_form, name="get_form"),
    path("add/<str:type>", views.add, name="add"),
    path("get-credentials", views.get_credentials, name="get_credentials"),
    path("edit/credential/<int:uuid>", views.edit, name="edit"),
    path("delete/credential/<str:uuid>", views.delete, name="delete"),
    path("favorites", views.favorites, name="favorites"),
    path("favorite", views.favorite, name="favorite"),
    path("unfavorite", views.unfavorite, name="unfavorite"),
    path("type/<str:type>", views.type, name="type")
]