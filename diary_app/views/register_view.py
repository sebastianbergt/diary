from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View

class RegisterView(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary_entries')
        
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'diary_app/register.html', {'form': form})
