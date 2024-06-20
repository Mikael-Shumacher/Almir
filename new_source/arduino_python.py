import sqlite3
import speech_recognition as sr
import pyttsx3
import datetime
import random
import os
import google.generativeai as genai
import re 
import serial as srl 
from time import sleep 


#conn = sqlite3.connect('../Data/{nome_}.db')
#cursor = conn.cursor()
# cursor.execute(
#    "CREATE  TABLE vendas (produto text, {nome_}or integer, quantidade integer, total integer)")
nome_ = "VAL"
api_google = 'AIzaSyDXF7x8AO_2eLKAc-wg-MUZmT_pAJMpm1E'
genai.configure(api_key=api_google)

model = genai.GenerativeModel('gemini-pro')
maquina = pyttsx3.init()
#arduino = srl.Serial('COM4', 9600) 
#arduino.flush()



sou = [f'sou {nome_}', f'me chamo {nome_}.',
       f'meu nome é {nome_}', f'sou um assistente chamado {nome_} ']

iniciativas = ['como eu posso te ajudar?',
               'como eu posso te ajudar, hoje?', 'do que você precisa hoje?']
horarios = ['O horario de hoje é:', 'Agora sao:']

datas = ['A data de hoje é:', 'hoje é:']

def falar(texto):
    maquina.setProperty("voice", "brazil")
    maquina.setProperty('rate', 170)
    maquina.say(texto)
    maquina.runAndWait()

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
        f'Voce agora se chama {nome_} e é um assistente virtual, fale brevemente quem  é você, suas funções em 150 palavras, inclusive seu nome.')
    print(response.text)

def data():
    dia = str(datetime.datetime.now().day)
    mes = str(datetime.datetime.now().month)
    ano = str(datetime.datetime.now().year)
    falar(random.choice(datas) + dia + "do" + mes)
    falar("de " + ano)

def horario():
    hora = datetime.datetime.now().strftime("%H")
    minuto = datetime.datetime.now().strftime("%M")
    sec = datetime.datetime.now().strftime("%S")
    falar(random.choice(horarios) + hora + "horas" +
          minuto + "minutos e " + sec + "segundos")


def microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
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
        return "None"
    return comando


iniciar()
sair = 0
while sair == 0:
    print("----Escutando----")
    comando = microfone().lower()
    if 'data' in comando:
        data()
    elif ('led' in comando or 'luz' in comando or 'ligue' in comando or 'ligar' in comando)  and (not 'desligar' in comando and not 'desligue' in comando):
        falar("O led será ligado.")
        #arduino.write('on'.encode()) 

    elif 'desativar' in comando or "desligar" in comando or 'desliga' in comando or 'desativa' in comando or 'desligue' in comando  :
          falar("O led será desligado.")
          #arduino.write('off'.encode()) 
    else:
        response = model.generate_content(comando)
        response_ = str(response.text).replace("*","")
        falar(response_)
        print(response_)
   
