from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from ..models import DiaryEntry
from ..forms import DiaryEntryForm


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