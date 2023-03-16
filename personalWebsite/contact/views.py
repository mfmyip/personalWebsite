from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

from .models import Contact
from .forms import ContactForm

# Create your views here.

def index(request):
    template_name = 'contact/contact.html'

    me = Contact.objects.get(pk=1) # get first obj in contact
    context = {
        'contact': me
    }
    return render(request, template_name, context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry From: " + form.cleaned_data['your_name']
            body = {
                'name': form.cleaned_data['your_name'],
                'email': form.cleaned_data['your_email'],
                'message': form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())
            try:
                # 'from', ['to']
                send_mail(subject, message, 'murphyyip49@gmail.com', ['murphyyip49@gmail.com'])
                messages.success(request, 'Form submission successful!')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact:contact')
        
    form = ContactForm()
    me = Contact.objects.get(pk=1) # get first obj in contact
    context = {
        'contact': me,
        'form': form
    }
    return render(request, 'contact/contact.html', context)

