from django.urls import path
from .views import register, login_view  # Import the views

urlpatterns = [
    path('register/', register, name='register'),  # Use 'register_view' if renamed
    path('login/', login_view, name='login'),  # Use 'login_view' if renamed
]


