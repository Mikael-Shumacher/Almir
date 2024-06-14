# pp install -U google-generativeai
import sqlite3
import speech_recognition as sr
import pyttsx3
import datetime
import random
import os
import google.generativeai as genai

conn = sqlite3.connect('Almir.db')
cursor = conn.cursor()
cursor.execute(
    "CREATE  TABLE vendas (produto text, valor integer, quantidade integer, total integer)")
api_google = 'AIzaSyDXF7x8AO_2eLKAc-wg-MUZmT_pAJMpm1E'
genai.configure(api_key=api_google)
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
model = genai.GenerativeModel('gemini-pro')
audio = sr.Recognizer()
maquina = pyttsx3.init()
sou = ['sou o Almir', 'me chamo Almir.','meu nome é Almir', 'sou o assistente Almir']
 
iniciativas = ['como eu posso te ajudar?',
               'como eu posso te ajudar, hoje?', 'do que você precisa hoje?']
horarios = ['O horario de hoje é:', 'Agora sao:']

datas = ['A data de hoje é:', 'hoje é:']


def falar(texto):
    voices = maquina.getProperty('rate')
    maquina.setProperty('rate', 140)
    voices = maquina.getProperty('voices')
    #voices = engine.getProperty("voices")
    #for voice in voices:
        #print(voice.id)
    #maquina.setProperty('voice', voices[1].id)
    maquina.setProperty("voice", "brazil")
    maquina.say(texto)
    maquina.runAndWait()
        
    #falar(random.choice(horarios) + hora + "horas" +
          #minuto + "minutos e " + sec + "segundos")
def iniciar():
    hr = datetime.datetime.now().strftime('%H')
    hora = int(hr)
    if hora >= 5 and hora <= 12:
        falar('Bom dia,' + random.choice(sou))
    elif hora >= 12 and hora <= 18:
        falar('Boa tarde,' + random.choice(sou))
    elif hora >= 18 and hora <= 23:
        falar('Boa noite,' + random.choice(sou))
    else:
        falar('Olá,' + random.choice(sou))
    falar(random.choice(iniciativas))
    response = model.generate_content(
        'Voce agora se chama almir e é um assistente virtual')
    print(response.text)

def microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        print(source)
        print(sr.Recognizer())
        audio = r.listen(source)
    try:
        print("...")
        comando = r.recognize_google(audio, language='PT-BR')
        print('"' + comando + '"')
    except Exception as e:
        print(e)
        falar("Por favor, repita!")
        comando = r.recognize_google(audio, language='PT-BR')
        print('"' + comando + '"')
        #print('"' + comando + '"')

        return "None"
    return comando

#iniciar()
microfone()
