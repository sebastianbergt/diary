from django.shortcuts import redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('diary_entries')
    else:
        return redirect('login')