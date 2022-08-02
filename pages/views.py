from django.shortcuts import render

from .models import (
    Files,
    Admission,
    Member,
)
from .forms import FileForm

# Create your views here.

def index(request):
    
    return render(request, 'pages/index.html')


def apply(request):
    
    return render(request, 'pages/apply.html')


def wait(request):
    
    return render(request, 'pages/wait.html')
    
    
def admission(request):
    
    return render(request, 'pages/admission.html')