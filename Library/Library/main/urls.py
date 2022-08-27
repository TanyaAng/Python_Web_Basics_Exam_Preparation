from django.urls import path

from Library.main.views import home_page, create_book, edit_book, book_details, profile_page, edit_profile, \
    delete_profile, create_profile, delete_book

urlpatterns = (
    path('', home_page, name='home page'),

    path('add/', create_book, name='book create'),
    path('edit/<int:pk>/', edit_book, name='book edit'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('delete/<int:pk>/', delete_book, name='book delete'),

    path('profile/', profile_page, name='profile page'),
    path('profile/create/', create_profile, name='profile create'),
    path('profile/edit/', edit_profile, name='profile edit'),
    path('profile/delete/', delete_profile, name='profile delete')

)
