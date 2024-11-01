# sam_education/views.py
from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')  # Make sure 'index.html' exists in your templates folder
