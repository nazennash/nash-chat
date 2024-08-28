from django.shortcuts import render
from . forms import RegisterForm
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})