from django.shortcuts import render
import random


# Create your views here.

def home(requests):
    return render(requests, 'core/home.html', {})


def password(requests):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if requests.GET.get('length', 12):
        length = int(requests.GET.get('length', 12))
    if requests.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if requests.GET.get('numbers'):
        characters.extend('0123456789')
    if requests.GET.get('special'):
        characters.extend('!@#$%^&*()')

    the_password = ''

    for x in range(length):
        the_password += random.choice(characters)
    return render(requests, 'core/password.html', {'password': the_password})


def about(requests):
    return render(requests, 'core/about.html', {})
