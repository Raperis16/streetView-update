from django.shortcuts import render



# Create your views here.




def index(request):
    return render (request, 'test.html')

def timet(request):
    return render (request, 'start.html')

def mainmenu(request):
    return render (request, 'mainmenu.html')

def search(request):
    return render (request, 'search.html')

def meme(request):
    return render (request, 'meme.html')
    
def about(request):
    return render (request, 'about.html')

def contact(request):
    return render (request, 'contact.html')

def weather(request):
    return render (request, 'weather.html')