#!/usr/bin/python3
import io
import socket
from PIL import Image
import cv2
import numpy as np

sock = socket.socket()  # создаем сокет
sock.connect(('127.0.0.1', 9092))  # подключаемся к серверу (в данном случае к localhost-у)
cap = cv2.VideoCapture(0)  # Включаем первую камеру
while True:
    ret, frame = cap.read()  # читаем кадр с вебкамеры
    if not ret:  # если не получилось - выводим ошибку
        print("failed to grab frame")
        break
    cv2.imshow("Press space to take a photo", frame)  # выводим изображение с камеры на экран
    k = cv2.waitKey(1)
    if k % 256 == 32:  # если нажат пробел -- сохраняем текущий кадр и передаем его на сервер
        buf = io.BytesIO()  # создаем объект BytesIO
        im = Image.fromarray(np.uint8(frame)).convert('RGB')  # преобразуем объект np.array в объект Image
        im.save(buf, "JPEG") # сохраняем его в виде байт в buf
        sock.sendall(buf.getvalue())  # отправляем все содержимое buf на сервер через сокет
        break
cap.release()  # отключаем камеру
cv2.destroyAllWindows()  # уничтожаем окно
sock.close()  # закрываем сокет
