from django.shortcuts import render
import random

# Create your views here.


def main(request):
    return render(request, 'index.html')


def generate(request):
    if request.method == 'POST':
        chars = list('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        alpha = list('qwertyuiopasdfghjklzxcvbnm')
        num = list('123456789')
        simb = list('!@#$%^&*}{][')
        number = num
        length = int(request.POST.get('numb'))
        password = ''
        if request.POST.get('letter'):
            number += alpha
        if request.POST.get('numbers'):
            number += num
        if request.POST.get('simvols'):
            number += simb
        for i in range(length):
            password += random.choice(chars)
        return render(request, 'generate.html', {'password': password})
