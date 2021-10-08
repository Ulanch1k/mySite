from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'index.html')

def create_film(request):
    return render(request, 'Film_create.html')


def edit_main(request):
    return render(request, 'edit_main.html')

def daykino(request):
    return render(request, 'daykino.html')

def MyAccount(request):
    return render(request, 'MyAccount.html')

def accept_post(request):
    print(request.POST)
    return render(request, 'index.html')

def create_films(request):
    print(request.POST)
    return redirect('/product/')
