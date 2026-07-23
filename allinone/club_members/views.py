from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def club_members(request):
    return HttpResponse("Club Members")