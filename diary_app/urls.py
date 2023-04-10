from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('entries/', views.DiaryListView.as_view(), name='diary_entries'),
    path('new_entry/', views.NewEntryView.as_view(), name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.EditEntryView.as_view(), name='edit_entry'),
    path('search/', views.SearchView.as_view(), name='search'),
]
