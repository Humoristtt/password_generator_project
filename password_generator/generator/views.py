import secrets
import string

from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')


def generator_password(length, uppercase, numbers, special):
    letters = string.ascii_lowercase
    if uppercase == 'on':
        letters = string.ascii_letters
    if numbers == 'on':
        letters += string.digits
    if special == 'on':
        letters += '`~!@#$%^&*()_-+={}[]:;"<>,.?'
    rand_string = ''.join(secrets.choice(letters) for i in range(length))
    return rand_string


def password(request):
    length = int(request.GET.get('length', 12))
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    special = request.GET.get('special')
    password_def = generator_password(length, uppercase, numbers, special)
    return render(request, 'generator/password.html', {'password': password_def})
