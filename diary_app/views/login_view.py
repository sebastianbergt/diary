from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views import View

class LoginView(View):
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('diary_entries')
        
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'diary_app/login.html', {'form': form})
