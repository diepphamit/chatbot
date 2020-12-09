from nltk.chat.util import Chat, reflections
from .chatbotdata import  chat_pair, reflection
import wikipedia
import requests, json 
import datetime
from bs4 import BeautifulSoup



english_words = {'mango' : 'quả xoài', 'banana': 'quả chuối', 'cherry': 'quả cherry', 'null': 'null'}

def xReturn(s_String):
    for key in english_words.keys():
        if s_String.find(key) != -1:
            return key, english_words[key]

    return 'null', 'null'

def pheptoan(s_string):
    number1, number2, bt = 0, 0, ''
    pheptoan1 = ''
    for i in range(len(s_string)):
        if(s_string[i] >= '0' and s_string[i] <= '9'):
            for j in range(len(s_string) - 1, i, -1):
                if(s_string[j] >= '0' and s_string[j] <= '9' ):
                    pheptoan1 += s_string[i:j+1]
                    break

            break

    for i in range(len(pheptoan1)):
        if(pheptoan1[i] == '+'):
            return float(pheptoan1[:i]) + float(pheptoan1[i+1:])
        
        if(pheptoan1[i] == '-'):
            return float(pheptoan1[:i]) - float(pheptoan1[i+1:])
        
        if(pheptoan1[i] == '*'):
            return float(pheptoan1[:i]) * float(pheptoan1[i+1:])
        
        if(pheptoan1[i] == '/'):
            return float(pheptoan1[:i]) / float(pheptoan1[i+1:])
            

    return 'null'


#define a function vbot
def vbot(s_string):
    s_string = s_string.strip()
    if s_string.lower().find('how many degree') != -1:
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Danang' 
        response = requests.get(api_address) 
        return  str(int(response.json()['main']['temp'] - 273.15)) + 'oC'

    if s_string.lower().find('how is the weather') != -1:
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Danang' 
        response = requests.get(api_address) 
        return  'Temperature: '+ str(int(response.json()['main']['temp'] - 273.15)) + 'oC. The weather is: ' +  response.json()['weather'][0]['main']
    
    if s_string.lower().find('image') != -1 or s_string.lower().find('picture') != -1 or s_string.lower().find('photo') != -1:
        url = 'https://www.google.com/search?q={0}&tbm=isch'.format(s_string.lower())
        content = requests.get(url).content
        soup = BeautifulSoup(content,'lxml')
        return soup.findAll('img')[1].get('src')

    if s_string.lower().find('what time is this') != -1:   
        H = str((int(datetime.datetime.now().strftime("%H")) + 7) % 24)
        M = str(datetime.datetime.now().strftime("%M"))
        S = str(datetime.datetime.now().strftime("%S"))
        return  'This time is: ' + H  + ":"+M+ ":"+S


    if s_string.find('wiki') != -1:
        s_string = s_string.replace('wiki', '')
        return wikipedia.summary(s_string, sentences = 4)
        #default message at the start
    key, val = xReturn(s_string)
    if key != 'null':
        return 'The meaning of the word ' + key + ' is: "'+ val + '"'
    elif pheptoan(s_string) != 'null':
        return 'This result: ' + str(pheptoan(s_string))
    else: 
        chat = Chat(chat_pair.chat_pairs, reflection.reflections)
        return chat.respond(s_string)





