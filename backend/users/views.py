from supabase import create_client, Client
from django.shortcuts import render, redirect
from django.contrib import messages

# Supabase credentials
SUPABASE_URL = "https://xgfiwkjivlinillbdrei.supabase.co"  
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhnZml3a2ppdmxpbmlsbGJkcmVpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzE3OTU3NDIsImV4cCI6MjA0NzM3MTc0Mn0.oQgbKc5ftIDro5E1DQTf1-3BcNNV-MAbAVmjFiaRh20"  # Replace with your Anon Key

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'register.html')

        try:
            # Use Supabase to register the user
            response = supabase.auth.sign_up({
                "email": email,
                "password": password
            })

            # Check if registration was successful
            if "error" in response:
                messages.error(request, response["error"]["message"])
                return render(request, 'register.html')

            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'register.html')

    return render(request, 'register.html')
