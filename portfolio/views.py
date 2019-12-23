from django.shortcuts import render
from contact.models import Contact
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact()
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return render(request, template_name='index.html')
    return render(request, template_name='index.html')

