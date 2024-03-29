import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


from PIL import Image # Importando o módulo Pillow para abrir a imagem no script

import pytesseract # Módulo para a utilização da tecnologia OCR


teste = Image.open('tt.png').convert("L")
Image._show(teste)

#print(teste)
#teste.save("tes123te.png")

#frase_t = pytesseract.image_to_string( teste )# Extraindo o texto da imagem
print( pytesseract.image_to_string( teste,  config="-psm 100 -c tessedit_char_whitelist=.0123456789") ) # Extraindo o texto da imagem

#print(frase_t)
#Funcao responsavel por falar
def cria_audio(audio):

    tts = gTTS(audio,lang='pt-br')

    #Salva o arquivo de audio
    tts.save('hello.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('hello.mp3')


#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)

        #Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")

        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)

    try:

        #Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio,language='pt-BR')

        #Após alguns segundos, retorna a frase falada
        print("Você disse: " + frase)#Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem

    except sr.UnkownValueError:
        print("Não entendi")

    return frase

#frase = pytesseract.image_to_string( Image.open('original_1.jpeg').convert("1")) # Extraindo o texto da imagem #ouvir_microfone()
#print(frase)
#cria_audio(frase)
