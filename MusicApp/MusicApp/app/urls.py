from django.urls import path

from MusicApp.app.views import home_page, create_album, details_album, edit_album, delete_album, details_profile, \
    delete_profile, create_profile

urlpatterns = (
    path('', home_page, name='home page'),

    path('album/add/', create_album, name=' album create'),
    path('album/details/<int:pk>/', details_album, name=' album details'),
    path('album/edit/<int:pk>/', edit_album, name=' album edit'),
    path('album/delete/<int:pk>/', delete_album, name=' album delete'),

    path('profile/create/', create_profile, name='profile create'),
    path('profile/details/', details_profile, name=' profile details'),
    path('profile/delete/', delete_profile, name=' profile delete'),

)
