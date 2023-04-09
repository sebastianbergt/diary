from django.urls import path
from . import views

urlpatterns = [
    path('', views.diary_entries, name='diary_entries'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('search/', views.search, name='search'),
]
