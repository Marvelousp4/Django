from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    line1 = '<h1 style="text-align: center">Marvelousp4</h1>'
    line2 = '<a href="/play/">Enter into the game page</a>'
    line3 = '<hr>'
    return HttpResponse(line1 + line2 + line3)

def play(request):
    line1 = '<h1 style="text-align: center">Game</h1>'
    line2 = '<a href="/">Back the main page</a>'
    return HttpResponse(line1 + line2)
