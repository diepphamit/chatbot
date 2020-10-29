from nltk.chat.util import Chat, reflections
from .chatbotdata import  chat_pair, reflection
import wikipedia



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
    if s_string.find('wiki') != -1:
        s_string = s_string.replace('wiki', '')
        return wikipedia.summary(s_string, sentences = 5)
        #default message at the start
    key, val = xReturn(s_string)
    if key != 'null':
        return 'Nghia cua tu ' + key + ' la: '+ val
    elif pheptoan(s_string) != 'null':
        return 'This result: ' + str(pheptoan(s_string))
    else: 
        chat = Chat(chat_pair.chat_pairs, reflection.reflections)
        return chat.respond(s_string)