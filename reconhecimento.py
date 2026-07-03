import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import speech_recognition as sr
import pyttsx3
import os
import requests
import geocoder
import datetime
import random

#pip install speechrecognition pyttsx3 pyowm requests geocoder pyaudio easyocr opencv-python opencv-contrib-python
#pip install requirements (do reconhemcimento de Objetivo)


# Configurações de Voz
alexa = pyttsx3.init()
alexa.setProperty('rate', 180)
alexa.setProperty('volume', 1.0)
alexa.setProperty('voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
reconhecedor_voz = sr.Recognizer()  # Renomeado para reconhecimento de voz

# Configuração de Câmera
detectorFace = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
reconhecedor_face = cv2.face.EigenFaceRecognizer_create() # Renomeado para reconhecimento facial
reconhecedor_face.read('classificadoreigen.yml')
largura, altura = 220, 220

font = cv2.QT_FONT_NORMAL
camera = cv2.VideoCapture(0)
saida = False
#Falas:
    #ok sexta-feira
    #cadastrar evento na agenda
    #ler agenda
    #apagar agenda
    #ver clima
    #Que horas são
    #Me conte uma piada
    #calculadora
    #Me conte uma curiosidade


#OpenWeather
api_key = '5b72b4e4d53d4d1d5ff83453b1ef92b5'
lang = 'pt'

#Função Clima | Ele indica as localizações do Centro do Estado
def clima():
    try:
        # Obtém a localização atual
        g = geocoder.ip('me')
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        print(latitude)
        print(longitude)

        # URL da API do OpenWeatherMap
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&lang={lang}&units=metric'

        # Fazendo a requisição
        response = requests.get(url)
        data = response.json()

        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            # Obtendo os dados do clima
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']

        else:
            # Se houve um erro na requisição
            alexa.say("Desculpe, não consegui obter as informações do clima para a sua localização atual.")
            alexa.runAndWait()

        print(f"A temperatura atual é de {temperature} graus Celsius, e o clima é de {weather_description}.")
        alexa.say(f"A temperatura atual é de {temperature} graus Celsius, e o clima é de {weather_description}.")
        alexa.runAndWait()
    except:
        print("Ops, ocorreu algum erro na função clima!")

#Função referente a criação da Agenda
def adicionar_entrada(agenda):
    try:
        with open('agenda.txt', 'a') as arquivo:
            arquivo.write(f"{agenda} ;")
            alexa.say("O evento foi salvo na sua agenda.")
            alexa.runAndWait()
    except:
        print("Ops, ocorreu algum erro na função de entrada da agenda!")

#Função referente a Leitura da Agenda
def ler_agenda():
    if not os.path.exists('agenda.txt'):
        alexa.say("A agenda está vazia")
        alexa.runAndWait()
        return
    with open('agenda.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        if conteudo:
            alexa.say("Conteudo da Agenda")
            alexa.runAndWait()
            alexa.say(conteudo)
            alexa.runAndWait()
        else:
            alexa.say("A agenda está vazia.")
            alexa.runAndWait()

#Função que apaga a agenda
def apagar_agenda():
    # Verifica se o arquivo existe antes de tentar deletá-lo
    if os.path.exists('agenda.txt'):
        os.remove('agenda.txt')
        print('O arquivo foi deletado com sucesso.')
        alexa.say('O arquivo foi deletado com sucesso.')
        alexa.runAndWait()
    else:
        print('O arquivo não existe.')
        alexa.say('O arquivo não existe')
        alexa.runAndWait()

#Função para obter a hora atual
def dizer_horas():
    now = datetime.datetime.now()
    horas = now.strftime('%H:%M')
    print(f'Agora são {horas}.')
    alexa.say(f'Agora são {horas}.')
    alexa.runAndWait()

#Função para contar piadas
def contar_piada():
    piadas = [
        "Você conhece a piada do pônei? Pô nei eu",
        "O que o pagodeiro foi fazer na igreja? Cantar pá God",
        "O que o pato falou para a pata? Vem quá",
        "Você sabe qual é o rei dos queijos? O reiqueijão",
        "O que acontece quando chove na Inglaterra? Vira Inglalama",
        "O que o tomate foi fazer no banco? Tirar extrato",
        "Por que a velhinha não usa relógio? Porque ela é sem hora.",
        "Por que há uma cama elástica no polo Norte? Para o urso polar",
    ]
    piada_escolhida = random.choice(piadas)
    print(piada_escolhida)
    alexa.say(piada_escolhida)
    alexa.runAndWait()

#Calculadora
def Calculadora():
    reconhecedor_voz.adjust_for_ambient_noise(mic, duration=2)
    print("O que deseja calcular?")
    alexa.say("O que deseja calcular?")
    alexa.runAndWait()
    audio = reconhecedor_voz.listen(mic, timeout=10)
    print("Reconhecendo audio...")
    alexa.say("Reconhecendo audio...")
    alexa.runAndWait()
    texto = reconhecedor_voz.recognize_google(audio, language='pt')
    print(texto)
    resultado = None
    conta = texto.split(" ")
    print("Váriavel Conta ", conta)
    if conta[1] == '+':
        resultado = float(conta[0]) + float(conta[2])
        print("Resultado: ", resultado)
    elif conta[1] == '-':
        resultado = float(conta[0]) - float(conta[2])
        print("Resultado: ", resultado)
    elif conta[1] == 'x':
        resultado = float(conta[0]) * float(conta[2])
        print("Resultado: ", resultado)
    elif conta[1] == '/' and float(conta[2]) != 0:
        resultado = float(conta[0]) / float(conta[2])
        print("Resultado: ", resultado)
    else:
        print("Não entendi!")

    if resultado is not None:
        alexa.say("O resultado é " + str(resultado))
        alexa.runAndWait()

#Curiosidades
def contar_curiosidade():
    curiosidades = [
        "O Brasil é o maior país da América do Sul e o quinto maior do mundo.",
        "A palavra Brasil significa vermelho como brasa.",
        "O Brasil é o maior produtor de café do mundo.",
        "O Brasil tem a maior biodiversidade do mundo, graças à Floresta Amazônica.",
        "O Brasil tem quatro fusos horários.",
        "O Brasil tem um município situado em dois hemisférios.",
        "O Brasil tem o 15º litoral mais extenso do mundo.",
        "A primeira missa foi realizada no Brasil no dia 26 de abril de 1.500.",
        "A primeira capital do Brasil foi a cidade de Salvador.",
        "O Brasil é o único país da América cuja língua oficial é o português.",
        "O Brasil é considerado uma das maiores economias do mundo."
    ]
    curiosidade_escolhida = random.choice(curiosidades)
    print(curiosidade_escolhida)
    alexa.say(curiosidade_escolhida)
    alexa.runAndWait()

#Reconhecer Objetos
def Reconhecer_Objetos():
    try:
        # Capture vídeo da webcam
        cap = cv2.VideoCapture(0)  # Use 0 para a webcam padrão

        while not saida:
            # Leia um quadro da webcam
            ret, frame = cap.read()

            if not ret or frame is None:
                print("Não foi possível capturar vídeo ou o frame está vazio.")
                break

            # Aplique a detecção de objetos
            bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov3-tiny')

            if label:
                # Concatene os objetos detectados em uma frase
                objetos_detectados = ', '.join(label)
                frase = f"{objetos_detectados}"

                # Fale a frase (ou envie para Alexa)
                alexa.say(frase)
                alexa.runAndWait()

            # Desenhe a caixa delimitadora sobre os objetos detectados
            out = draw_bbox(frame, bbox, label, conf, write_conf=True)

            # Exiba a saída
            cv2.imshow("Detector de objetos em tempo real", out)

            # Pressione 'e' para sair da função
            if cv2.waitKey(1) & 0xFF == ord('e'):
                print("Saindo da função.")
                cap.release()
                cv2.destroyWindow("Detector de objetos em tempo real")
                break

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

fim = False
audio_esperando = False  # Variável de controle para o reconhecimento de voz

while not fim:
    if not audio_esperando:  # Somente continuar o loop da câmera se não estiver esperando pelo reconhecimento de voz
        font = cv2.QT_FONT_NORMAL
        camera = cv2.VideoCapture(0)
        status, imagem = camera.read()

        # Verifica se a captura foi bem-sucedida
        if not status or imagem is None:
            print("Não foi possível capturar a imagem da câmera. Tentando novamente...")
            continue  # Retorna ao início do loop se a imagem não estiver disponível

        # Se a imagem foi capturada corretamente, continue com o processamento
        try:
            status, imagem = camera.read()
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))
        except Exception as e:
            print(f"Erro ao processar a imagem: {e}")

        try:
            for x, y, l, a in facesDetectadas:
                imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (altura, largura))
                cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
                nome, confianca = reconhecedor_face.predict(imagemFace)  # Usando a variável correta agora
                print(f"Confiança: {confianca}, Nome previsto: {nome}")

                if nome == 1:
                    nome = 'Kaue'
                    print('Boas vindas')
                    alexa.say('Boas vindas ' + str(nome))
                    alexa.runAndWait()
                    alexa.say('O que posso fazer por você hoje?')
                    alexa.runAndWait()

                    # Iniciar reconhecimento de voz
                    audio_esperando = True  # Mudar o estado para parar o loop da câmera
                
                elif nome == 2:
                    nome = 'Karen'
                    print('Boas vindas')
                    alexa.say('Boas vindas ' + str(nome))
                    alexa.runAndWait()
                    alexa.say('O que posso fazer por você hoje?')
                    alexa.runAndWait()

                    # Iniciar reconhecimento de voz
                    audio_esperando = True  # Mudar o estado para parar o loop da câmera
                    
                else:
                    nome = 'Desconhecido'

                cv2.putText(imagem, str(nome), (x, y + altura - 20), font, 2, (0, 0, 255))

        except Exception as e:
            print(f"Erro no reconhecimento facial: {e}")

        cv2.imshow("Faces", imagem)

    if audio_esperando:
        with sr.Microphone() as mic:
            try:
                print('Fale Algo!')
                audio = reconhecedor_voz.listen(mic, phrase_time_limit=7)
                print("Reconhecendo áudio...")  # Debug
                texto = reconhecedor_voz.recognize_google(audio, language='pt')  #
                print(texto)
                print("Reconhecendo audio...")
                agenda = 'cadastrar evento na agenda'
                if texto == agenda:
                    alexa.say("Ok, qual evento devo cadastrar?")
                    alexa.runAndWait()
                    audio = reconhecedor_voz.listen(mic, phrase_time_limit=10
                                                    )
                    print("Reconhecendo audio...")
                    texto = reconhecedor_voz.recognize_google(audio, language='pt')
                    print(texto)
                    agenda = texto
                    adicionar_entrada(agenda)
                ler = 'ler agenda'
                if texto == ler:
                    ler_agenda()
                clima_texto = 'ver clima'
                if texto == clima_texto:
                    clima()
                agenda_apagar = 'apagar agenda'
                if texto == agenda_apagar:
                    apagar_agenda()
                horas = 'Que horas são'
                if texto == horas:
                    dizer_horas()
                piada = 'Me conte uma piada'
                if texto == piada:
                    contar_piada()
                calcular = 'calculadora'
                if texto == calcular:
                    Calculadora()
                curiosidade = 'Me conte uma curiosidade'
                if texto == curiosidade:
                    contar_curiosidade()
                rec_objeto = 'reconhecer objeto'
                if texto == rec_objeto:
                    Reconhecer_Objetos()
                    status, imagem = camera.read()
                    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
                    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))

            except sr.UnknownValueError:
                print("Não foi possível entender o que foi dito.")
                alexa.say("Desculpe, não entendi o que você falou.")
                alexa.runAndWait()

            except sr.RequestError as e:
                print("Erro ao se conectar ao serviço de reconhecimento de voz; {0}".format(e))

            audio_esperando = False  # Voltar para o loop da câmera

    if cv2.waitKey(1) == ord('q'):
        fim = True

camera.release()
cv2.destroyAllWindows()
