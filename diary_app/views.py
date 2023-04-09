from django.shortcuts import render, redirect, get_object_or_404
from .models import DiaryEntry
from .forms import DiaryEntryForm
from datetime import date, timedelta
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.views import LogoutView


def home(request):
    if request.user.is_authenticated:
        return redirect('diary_entries')
    else:
        return redirect('login')
    
class DiaryListView(LoginRequiredMixin, View):
    def get(self, request, input_date=None):
        if not input_date:
            input_date = date.today()
        entries = DiaryEntry.objects.filter(user=request.user, date=input_date).order_by('-created_at')[:20]
        return render(request, 'diary_app/diary_entries.html', {'entries': entries, 'date': input_date})

class NewEntryView(LoginRequiredMixin, View):
    def post(self, request):
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('diary_entries')
            
    def get(self, request):
        form = DiaryEntryForm()
        return render(request, 'diary_app/new_entry.html', {'form': form})

class EditEntryView(LoginRequiredMixin, View):
    def get(self, request, entry_id):
        entry = get_object_or_404(DiaryEntry, id=entry_id)
        form = DiaryEntryForm(instance=entry)
        return render(request, 'diary_app/edit_entry.html', {'form': form})

    def post(self, request, entry_id):
        entry = get_object_or_404(DiaryEntry, id=entry_id)
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('diary_entries')    

class SearchView(LoginRequiredMixin, View):
    def get(self, request):
        query = request.GET.get('q', '')
        entries = DiaryEntry.objects.filter(Q(content__icontains=query)).order_by('-created_at')[:20]
        return render(request, 'diary_app/search.html', {'entries': entries, 'query': query})

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary_entries')
    else:
        form = UserCreationForm()
    return render(request, 'diary_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('diary_entries')
    else:
        form = AuthenticationForm()
    return render(request, 'diary_app/login.html', {'form': form})

class CustomLogoutView(LogoutView):
    next_page = 'login'