from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def start(request):
    counter = 0
    request.session["counter"] = counter
    return redirect("/random") 

def random(request):
    
    word = get_random_string(length=14)

    request.session["counter"] +=1
    request.session["word"] = word

    return render(request,"random.html")

def reset(request):
    request.session["counter"] = 0

    return redirect("/random")
