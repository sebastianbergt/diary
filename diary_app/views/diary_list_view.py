from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from ..models import DiaryEntry
from datetime import date

class DiaryListView(LoginRequiredMixin, View):
    def get(self, request, input_date=None):
        if not input_date:
            input_date = date.today()
        entries = DiaryEntry.objects.filter(user=request.user, date=input_date).order_by('-created_at')[:20]
        return render(request, 'diary_app/diary_entries.html', {'entries': entries, 'date': input_date})
