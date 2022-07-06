from django.shortcuts import redirect, render
from .models import Contact
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.

def home(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        
        return redirect('contact')
       

    return render(request, 'contact/index.html')

class Contact_list(ListView):
    model = Contact
    template_name = 'contact/list_contact.html'