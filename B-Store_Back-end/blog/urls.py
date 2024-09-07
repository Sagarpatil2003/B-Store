from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("create/", views.create_book, name="create_book"),
    path("<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("<int:book_id>/delete/", views.delete_book, name="delete_book"),
    path('register/',views.register, name='register'),

]
