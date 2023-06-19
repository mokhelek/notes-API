from django.urls import path
from .import views


urlpatterns = [
    path("", views.showEndpoints),
    path("books", views.getBooks),
    path("add-book/", views.addBook),
    path("book/<str:pk>/", views.getBook),
    path("edit-book/<str:pk>/", views.editBook),
    path("delete-book/<str:pk>/", views.deleteBook),

]