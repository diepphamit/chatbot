
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
import json

from .model import classifiaction, chatbot
from bs4 import BeautifulSoup

@api_view(['GET'])
def getALl(request):
    if request.method == 'GET':
        # tutorial_data = JSONParser().parse(request)
        app_id = '494cf8d1'
        app_key = '25cf11d675c814665281e22f45e3cd34'
        language = 'en-gb'
        word_id = 'ruler'
        url = '	https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
        
        r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

        # phoneticAudio = r.json()['results'][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["audioFile"]
        # phonetic = r.json()['results'][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["phoneticSpelling"]
        # wordType = r.json()['results'][0]["lexicalEntries"][0]["lexicalCategory"]["text"]
        example = r.json()['results'][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
        print(example)
        data = {
        # "response":  r.json()['results'][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["audioFile"]
        "response":  r.json()
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
        # print(classifiaction.read_image(image))

        # r = requests.get('https://localhost:5001/api/Flashcard/1')
        # user = r.json()


        return JsonResponse({"data":classifiaction.read_image(image)})

@api_view(['POST'])
def get_flashcard_api(request):
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request) 

        if(tutorial_data['data'].lower().find('teacher') == -1 and  tutorial_data['data'].lower().find('lecturer') == -1):
            url = 'https://www.google.com/search?q={0}&tbm=isch'.format(tutorial_data['data'].lower() + " cartoon image")
            content = requests.get(url).content
            soup = BeautifulSoup(content,'lxml')
            imageUrl = soup.findAll('img')[1].get('src')
        else:
            imageUrl = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrUm0ifTfzS357AMmOB08c3AjDzijC5_Tnc2IUhwyqDjPg2kBqISEd3NljUA&s'

        app_id = '494cf8d1'
        app_key = '25cf11d675c814665281e22f45e3cd34'
        language = 'en-gb'
        word_id = tutorial_data['data']
        url = '	https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
        r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

        phoneticAudio = r.json()['results'][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["audioFile"]
        phonetic = r.json()['results'][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["phoneticSpelling"]
        wordType = r.json()['results'][0]["lexicalEntries"][0]["lexicalCategory"]["text"]
        example = r.json()['results'][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
        data = {
        "response":  [word_id, word_id, wordType, example, phonetic, phoneticAudio, imageUrl]
        }
    
        return JsonResponse(data)

@api_view(['POST'])
def get_image_url(request):
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        url = 'https://www.google.com/search?q={0}&tbm=isch'.format(tutorial_data['data'].lower() + " image")
        content = requests.get(url).content
        soup = BeautifulSoup(content,'lxml')

        data = {
        "response": soup.findAll('img')[1].get('src')
        }
        
        return JsonResponse(data)

@api_view(['POST'])
def chatbot_response(request):
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        data = {
        "response": chatbot.vbot(tutorial_data['data'])
        }
        
        return JsonResponse(data)
