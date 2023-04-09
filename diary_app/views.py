from django.shortcuts import render, redirect, get_object_or_404
from .models import DiaryEntry
from .forms import DiaryEntryForm
from datetime import date, timedelta
from django.db.models import Q

def diary_entries(request, input_date=None):
    if not input_date:
        input_date = date.today()
    entries = DiaryEntry.objects.filter(date=input_date).order_by('-created_at')[:20]
    return render(request, 'diary_app/diary_entries.html', {'entries': entries, 'date': input_date})

def new_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary_entries')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary_app/new_entry.html', {'form': form})

def edit_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id)
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('diary_entries')
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'diary_app/edit_entry.html', {'form': form})

def search(request):
    query = request.GET.get('q', '')
    entries = DiaryEntry.objects.filter(Q(content__icontains=query)).order_by('-created_at')[:20]
    return render(request, 'diary_app/search.html', {'entries': entries, 'query': query})
