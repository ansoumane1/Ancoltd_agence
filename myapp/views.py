from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import datetime
from .models import  Service, Tarif
from pages.models import Page
from .forms import ContactForm
# Create your views here.

def index(request):

    services = Service.objects.all()
    tarifs = Tarif.objects.all()
    current_date = datetime.datetime.now()
    context = {
                'services':services,
                'tarifs':tarifs,
                'format_date':current_date,
                'page_links':Page.objects.all()
                }
    return render(request, 'myapp/home.html', context)



def contact(request):
    submitted = False
    if request.method == 'POST':
        message_name = request.POST['nom']
        message_email = request.POST['email']
        message_telephone = request.POST['telephone']
        message_subject = request.POST['sujet']
        message_contenu = request.POST['message']

        subject = f"{message_subject}" 
                   
        message =f"Nom: {message_name}\n\n{message_email}\n\ntelephone: {message_telephone}\n\n {message_contenu}"
            
        sender = message_email

        send_mail(subject, message,sender ,
                 ['ansoucompany@gmail.com'])
        submitted = True
        return render(request, 'myapp/contact.html',{'submitted': submitted, 'customer_name':message_name})
    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'myapp/contact.html',{'submitted': submitted})
