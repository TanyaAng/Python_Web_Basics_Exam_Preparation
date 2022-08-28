from django.urls import path

from Notes.app.views import home_page, create_note, edit_note, delete_note, details_note, profile, delete_profile, \
    create_profile

urlpatterns = (
    path('', home_page, name='home page'),

    path('add/', create_note, name='note create'),
    path('edit/<int:pk>/', edit_note, name='note edit'),
    path('delete/<int:pk>/', delete_note, name='note delete'),
    path('details/<int:pk>/', details_note, name='note details'),

    path('profile/', profile, name='profile'),
    path('profile/create/', create_profile, name='profile create'),
    path('profile/delete/', delete_profile, name='profile delete'),

)
