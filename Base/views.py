from django.shortcuts import render
from django.http import HttpResponse
from Base.models import Contact
from django.contrib import messages
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return render(request, 'home.html', {'form': ContactForm()})
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return render(request, 'home.html', {'form': ContactForm()})
        else:
            messages.error(request, "Please correct the errors in the form.")
            return render(request, 'home.html', {'form': form})
    
    form = ContactForm()
    return render(request, 'home.html', {'form': form})