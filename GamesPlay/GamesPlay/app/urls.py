from django.urls import path

from GamesPlay.app.views import home_page, dashboard, create_game, details_game, edit_game, delete_game, create_profile, \
    details_profile, edit_profile, delete_profile

urlpatterns=(
    path('', home_page, name='home page'),

    path('dashboard/', dashboard, name='dashboard'),

    path('game/create/', create_game, name='game create'),
    path('game/details/<int:pk>', details_game, name='game details'),
    path('game/edit/<int:pk>/', edit_game, name='game edit'),
    path('game/delete/<int:pk>/', delete_game, name='game delete'),

    path('profile/create/', create_profile, name='profile create'),
    path('profile/details/', details_profile, name='profile details'),
    path('profile/edit/', edit_profile, name='profile edit'),
    path('profile/delete/', delete_profile, name='profile delete'),


)