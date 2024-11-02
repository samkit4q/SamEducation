from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login  # Import necessary functions for authentication

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Your account has been created!')
        return redirect('login')  # Redirect to the login page
    return render(request, 'users/register.html')  # Render the registration template

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # Authenticate the user
        if user is not None:
            auth_login(request, user)  # Log in the user
            return redirect('dashboard')  # Redirect to a dashboard or another page after login
        else:
            messages.error(request, 'Invalid username or password.')  # Display an error message
    return render(request, 'users/login.html')  # Render the login template


