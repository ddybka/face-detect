#!/usr/bin/python3
import io
import socket
from PIL import Image

sock = socket.socket()  # создаем сокет
sock.connect(('127.0.0.1', 9092))  # подключаемся к серверу (в данном случае к localhost-у)
buf = io.BytesIO()  # создаем объект BytesIO
im = Image.open(r"./in.jpg")  # открываем картинку
im.save(buf, "JPEG")  # сохраняем её в виде байт в buf
sock.sendall(buf.getvalue())  # отправляем все содержимое buf на сервер через сокет
sock.close()  # закрываем сокет
