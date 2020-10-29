
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
import io
import os
import requests
from PIL import Image

from .model import classifiaction, chatbot

@api_view(['GET'])
def getALl(request):
    if request.method == 'GET':
        # tutorial_data = JSONParser().parse(request)
        data = {
        "response": "adsadad"
        }
        
        return JsonResponse(data)

@api_view(['POST'])
def classification_api(request):
    print(request.FILES)
    # tutorial_data = JSONParser().parse(request)
    # print(tutorial_data)
    if request.method == 'POST' and request.FILES['File']:
        image_request = request.FILES["File"]
        image_bytes = image_request.read()
        # print(image_bytes)
        image = Image.open(io.BytesIO(image_bytes))
        # image.save(imgByteArr, format=image.format)
        # imgByteArr = imgByteArr.getvalue()
        # print(imgByteArr)
        print(classifiaction.read_image(image))

        # r = requests.get('https://localhost:5001/api/Flashcard/1')
        # user = r.json()


        return JsonResponse({"data":classifiaction.read_image(image)})

@api_view(['POST'])
def chatbot_response(request):
    print("asdasd")
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        data = {
        "response": chatbot.vbot(tutorial_data['data'])
        }
        
        return JsonResponse(data)