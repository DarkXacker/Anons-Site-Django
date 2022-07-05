from django.shortcuts import redirect, render
from contact.forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email': email,
                'content': content
            })

            send_mail('The contact from subject','This is the message', 
                'noreply@codewithstein.com', ['fulstackandgamerprogrammer@gmail.com'],
                fail_silently=False,
                html_message=html)

    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {
        'form': form
    })
