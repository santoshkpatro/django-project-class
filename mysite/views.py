from django.shortcuts import HttpResponse, render


# def index(request):
#     return HttpResponse('Hello, World')

def index(request):
    name = 'Random'

    context = {
        'name': name,
        'age': 10
    }
    return render(request, 'index.html', context)

def about_us(request):
    return HttpResponse('<h1>About Us </h1>')