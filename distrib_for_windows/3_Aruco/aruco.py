import cv2
import cv2.aruco
 
camera = cv2.VideoCapture(0)  # создаем объект VideoCapture  с 'первой' камерой (Вашей вебкой)
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_1000) #распознает только маркеры 6х6. Для распознавания других маркеров необходимо заменить
while (True):                                                           #поле DICT_6X6_1000
    ret, frame = camera.read()  # фиксируем кадр с помощью frame
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
 
    (corners,ids,rejected)=cv2.aruco.detectMarkers(gray, dictionary)
 
    if len(corners) > 0:
        for i in [0,len(corners)-1]:
            print(ids[i],corners[i])
        cv2.aruco.drawDetectedMarkers(gray, corners, ids)
 
    cv2.imshow('Press Spacebar to Exit', gray)  # отображаем  frame
 
    if cv2.waitKey(1) & 0xFF == ord(' '):  # Останавливаем, если нажат пробел
        break
 
camera.release()  # Очистка после обнаружения нажатого пробела.
cv2.destroyAllWindows()
