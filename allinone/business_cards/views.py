from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'business_cards/index.html')

def core1(request):
    return render(request, 'business_cards/core1.html')

def core2(request):
    return render(request, 'business_cards/core2.html')

def core3(request):
    return render(request, 'business_cards/core3.html')

def core4(request):
    return render(request, 'business_cards/core4.html')