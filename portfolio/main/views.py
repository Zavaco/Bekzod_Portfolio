from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .forms import ClientForm
from .models import *

# Create your views here.


def main(request):
    menu = Menu.objects.all()
    info_first = HeadFoot.objects.first()
    info = HeadFoot.objects.all()
    gallery = Gallery.objects.all()
    context = {
        'menu': menu,
        'info_first': info_first,
        'info': info,
        'gallery': gallery,
    }
    return render(request, 'main/index.html', context)


def contact(request):
    form = ClientForm()
    menu = Menu.objects.all()
    info_first = HeadFoot.objects.first()
    contact_info = Client.objects.first()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'menu': menu,
        'info_first': info_first,
        'form': form,
        'contact_info': contact_info,
    }
    return render(request, 'main/contact.html', context)


