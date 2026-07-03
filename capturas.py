import cv2
import numpy as np
import os

classificador = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)

amostra = 1
numeroMaxAmostras = 50
nome = input("Digite seu nome: ")

altura, largura = 220, 220

pastaFotos = r'C:\Users\Admin\Documents\GIT\Alexa_v1\Alexa_CP5\fotos'
os.makedirs(pastaFotos, exist_ok=True) 

while True:
    status, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.05, minSize=(150,150))
    for x, y, a, l in facesDetectadas:
        cv2.rectangle(imagem, (x,y), (x+l, y+a), (0,0,255), 2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Média: ", np.average(imagemCinza))

            if np.average(imagemCinza) > 110:
                imagemFace = cv2.resize(imagemCinza[y: y+a, x:x+l], (largura, altura))

                localFoto = os.path.join(pastaFotos, f"{nome}_{amostra}.jpg")
                sucesso = cv2.imwrite(localFoto, imagemFace)
                print("Salvou?", sucesso, "->", localFoto)  # debug: confirma se salvou de verdade
                amostra+=1

    cv2.imshow("face detectada: ", imagem)
    if amostra > numeroMaxAmostras:
        break

print("Amostras capturadas com sucesso!")
camera.release()
cv2.destroyAllWindows()