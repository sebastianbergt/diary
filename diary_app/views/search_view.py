from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from ..models import DiaryEntry
from django.db.models import Q

class SearchView(LoginRequiredMixin, View):
    def get(self, request):
        query = request.GET.get('q', '')
        entries = DiaryEntry.objects.filter(Q(content__icontains=query)).order_by('-created_at')[:20]
        return render(request, 'diary_app/search.html', {'entries': entries, 'query': query})
