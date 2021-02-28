import time
import cv2
import numpy as np


def find_marker(image):

    # Converter a imagem em escala de cinzento e adionar efeito blur oara detectar contornos

    blurred_frame = cv2.GaussianBlur(image, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    #Caso queria usar sem blur
    #hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    # Definir a escala de cor em HSV

    #Azul
    #lower = np.array([110, 50, 50])
    #upper = np.array([130, 255, 255])
    lower = np.array([100, 150, 0], np.uint8)
    upper = np.array([140, 255, 255], np.uint8)
    #lower = np.array([0, 50, 50])
    #upper = np.array([10, 255, 255])

    #laranja
    #upper = np.array([10, 100, 20])
    #lower = np.array([25, 255, 255])
    #mask = cv2.inRange(hsv, (10, 100, 20), (25, 255, 255))

    #Aplicar mascara
    mask = cv2.inRange(hsv, lower, upper)


    #Encontrar contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    con = max(contours, key=cv2.contourArea)
    cv2.imshow("mask", mask)
    cv2.imshow("hsv", hsv)
    return cv2.minAreaRect(con)


def distance_to_camera(knownWidth, focalLength, perWidth):

    # Calculo da distancia
    return (knownWidth * focalLength) / perWidth


# Distancia (em cm) da camera ao objeto conhecida, efeito de calibração
KNOWN_DISTANCE = 30.0

# Largura do objeto em cm
KNOWN_WIDTH = 5.0


print("<<<---- Calibração ---->>>")
time.sleep(2)

#cap = cv2.VideoCapture('http://192.168.1.64:4747/mjpegfeed?640x480')
cap = cv2.VideoCapture(0)
_, img = cap.read()

marker = find_marker(img)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

time.sleep(2)

print("<<<---- Programa Principal a iniciar ---->>>")

while True:

    _, image = cap.read()

    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    marker = find_marker(image)
    CM = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])

    # Imprimir a saida
    cv2.putText(image, "%.2fcm" % CM,
                (image.shape[1] - 350, image.shape[0] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                2.0, (255, 0, 0), 3)
    cv2.imshow("Distancia", image)
    key = cv2.waitKey(1)

    # Esc para sair
    if key == 27:
        break

cv2.destroyAllWindows()
