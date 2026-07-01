import cv2
import socket
import pickle
import struct

cap = cv2.VideoCapture(0)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 9092))

while True:
    ret, frame = cap.read()
    # Серизализируем кадр
    data = pickle.dumps(frame)

    # Посылаем длину сообщения
    message_size = struct.pack("L", len(data))

    # Посылаем данные
    clientsocket.sendall(message_size + data)
