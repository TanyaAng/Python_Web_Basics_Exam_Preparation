from django.contrib import admin
from django.urls import path

from Expenses_tracker.main.views import home_page, create_expense_page, edit_expense_page, delete_expense_page, profile, \
    edit_profile, delete_profile, create_profile

urlpatterns = (
    path('', home_page, name='index'),

    path('create/', create_expense_page, name='create expense'),
    path('edit/<int:pk>/', edit_expense_page, name='edit expense'),
    path('delete/<int:pk>/', delete_expense_page, name='delete expense'),

    path('profile/', profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile')

)
