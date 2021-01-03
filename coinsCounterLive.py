from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(1)
width = 440
heigth = 280

cap.set(3, width)
cap.set(4, heigth)
cap.set(10, 150)

def detectCircles(imgAux, img):
    circles = cv2.HoughCircles(imgAux, cv2.HOUGH_GRADIENT, 1, 50, param1=255, param2=35, minRadius=30, maxRadius=300)
    
    radius = []
    coins = []
    five, ten, fifty = 0, 0, 0
    if circles is not None:
        circles = np.round(circles[0, :]).astype('int')

        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 255, 0), 1)
            radius.append([r, x, y])


        radius.sort()
        minim = radius[0][0]
        for i in radius:
            coins.append([i[0] / minim, i[1], i[2]])
            
        for coin in coins:
            if coin[0] <= 1.08: 
                five += 1
                cv2.putText(img, '5', (coin[1], coin[2]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
            elif coin[0] <= 1.25: 
                ten += 1
                cv2.putText(img, '10', (coin[1], coin[2]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
            else: 
                fifty += 1
                cv2.putText(img, '50', (coin[1], coin[2]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    
            

while True:
    
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.medianBlur(imgGray, 1)
    detectCircles(imgBlur, img)
    cv2.imshow('Camera', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break