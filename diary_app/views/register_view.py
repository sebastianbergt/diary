from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate



# class NewEntryView(LoginRequiredMixin, View):
#     def post(self, request):
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary_entries')
    else:
        form = UserCreationForm()
    return render(request, 'diary_app/register.html', {'form': form})
