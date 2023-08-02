from django.urls import path
from .views import ListBook,CreateBook,ViewBook,UpdateBook,DeleteBook,LoginUser,SignupUser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',ListBook.as_view(),name="index"),
    path('create_book/',CreateBook.as_view(),name="Create"),
    path('view_book/<int:pk>/',ViewBook.as_view(),name="view"),
    path('update_book/<int:pk>/',UpdateBook.as_view(),name="update"),
    path('delete_book/<int:pk>/',DeleteBook.as_view(),name="delete"),
    path('login/',LoginUser.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page="login"),name="logout"),
    path('register/',SignupUser.as_view(),name="register"),

]