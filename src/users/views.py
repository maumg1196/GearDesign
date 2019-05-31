"""Users Views."""
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from users.forms import SignUpForm


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('design:first')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def logout_view(request):
    """Logout users."""
    logout(request)
    return redirect('design:first')
