from django.shortcuts import render
from Base.models import Contact
from django.contrib import messages

def home(request):
    return render(request, 'home.html')
    
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        
        # Validate inputs
        if len(name) < 2 or len(name) > 30:
            messages.error(request, "Name must be between 2 and 30 characters.")
            return render(request, 'home.html')
        
        if len(email) < 5 or len(email) > 50:
            messages.error(request, "Invalid email.")
            return render(request, 'home.html')
        
        if len(number) < 3 or len(number) > 10:
            messages.error(request, "Invalid phone number.")
            return render(request, 'home.html')
        
        
        Contact.objects.create(name=name, email=email, number=number, message=message)
        messages.success(request, "Your message has been sent successfully.")
        return render(request, 'home.html')
    
    return render(request, 'home.html')
