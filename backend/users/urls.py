from django.urls import path
from . import views

urlpatterns = [
    path("fetch-users/", views.fetch_users, name="fetch_users"),
]
