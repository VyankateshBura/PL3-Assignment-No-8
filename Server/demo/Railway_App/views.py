from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
# Create your views here.
from .forms import MyForm
 
 
def index(request):
  return HttpResponse("Hello Geeks")

 
# Create your views here.
def home_view(request):
    context ={}
    context['form']= MyForm()
    return render(request, "home.html", context)

@csrf_exempt
def Fetch_Data(request):
    # dt = request.POST.get('search')
    # dt = json.load(request)['search']
    # print(dt)
    print("Fetching Data")
    url = "https://trains.p.rapidapi.com/"

    payload = {"search": "delhi"}
    headers = {
      "content-type": "application/json",
      "X-RapidAPI-Key": "238f5056d0mshe5ad349fc027ce8p1d8a96jsna9f574fb189a",
      "X-RapidAPI-Host": "trains.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    # print(response.text)
    return JsonResponse(response.text,safe=False)
    # return HttpResponse("Request arrived in the Fetch Data view!")