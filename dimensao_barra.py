import cv2
import numpy as np

# Valores reais para efeito de cálculo (em cm)

#distancia_camera_objeto = 24
pixelsY = 330
pixelsX = 115
realY = 15
realX = 5

# Escolha da fonte da webcam
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('http://192.168.1.64:4747/mjpegfeed?640x480')

while True:
    _, frame = cap.read()

    # Cortar a imagem da camera caso necessário
    # frame = frame[0:350, 15:540]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.erode(threshold, kernel, iterations=1)

    contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for (i, c) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        # Dimensão em pixels
        # cv2.putText(frame, str(h), (x, y + h + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1)
        # cv2.putText(frame, str(w), (x, y + w - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1)

        # Conta de pixels para centimentros
        cmY = (h * realY) / pixelsY
        cmX = (w * realX) / pixelsX

        # A exibir o valor no ecra da dimensão em X e Y
        cv2.putText(frame, str(int(cmY)), (x, y + h + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 1)
        cv2.putText(frame, str(int(cmX)), (x + w + 15, y + h + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 1)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()