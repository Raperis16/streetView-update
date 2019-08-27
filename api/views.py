from .models import Random
from .models import Game
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response




# Create your views here.

def ran_game(request):
    a = []
    for e in Random.objects.all().order_by('?')[:4]:
        #print(e.nos, e.lat, e.lng, e.id)
        test1 = {
            "id": e.id,
            "lat": e.lat,
            "lng": e.lng,
            "nos": e.nos
        }
        #e.to_json()
        a.append(test1)
    
    my_json_string = json.dumps(a)
    return HttpResponse(my_json_string, content_type='application/json')


def save(request):
    print(request.GET)
    print("test")
    if request.method == "POST":
    # new_games = Game() 
    # idd = request.GET.get(pk = "1")
        idd = Random.objects.get(pk = request.POST['id_loc'])
        res = request.POST['result']
        f1 = Random.objects.get(pk = request.POST['Fake3'])
        f2 = Random.objects.get(pk = request.POST['Fake1'])
        f3 = Random.objects.get(pk = request.POST['Fake2'])
        print(idd)
        new_games = Game(id_loc=idd, Result=res, Fake1=f1, Fake2=f2, Fake3=f3)
    # new_games.id_loc = idd
    #   request.POST.get['id_loc']
    # new_games.Result = request.GET.get('result')
    # new_games.Fake1 = request.GET.get('Fake1')
    # new_games.Fake2 = request.GET.get('Fake2')
    # new_games.Fake3 = request.GET.get('Fake3')
    
        new_games.save()
        return HttpResponse({"Result": request.GET.get('result')})
    if request.method == "GET":
        return HttpResponse("KUR TU LIEN IEKSSAAAAA. GET OUT OF MA SWAMP")

