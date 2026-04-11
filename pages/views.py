from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home_view(request):
    return render(request, "pages/home.html")

def about_me_view(request):
    return render(request, 'pages/about_me.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def projects_view(request):
    return render(request, 'pages/projects.html')

def contact_view(request):
    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})
