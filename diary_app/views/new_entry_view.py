from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from ..forms import DiaryEntryForm

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
