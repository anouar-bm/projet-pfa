from django.shortcuts import render, redirect

from .forms import SignupForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('user_app:login')
    else:
        form = SignupForm()

    return render(request, 'user/signup.html', {
        'form': form
    })