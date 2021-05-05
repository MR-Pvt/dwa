from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse

def home(request):

    return render(request, 'dwapp/script.html')

def transcript(request):

    return render(request, 'dwapp/transcript.html')