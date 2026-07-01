#!/usr/bin/python3
import io
import socket
from PIL import Image

sock = socket.socket()  # создаем сокет
# устанавливаем параметр SO_REUSEADDR в значение истины (позволяет нескольким приложениям «слушать» сокет)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', 9092))  # выбираем хост и порт (в данном случае хост - любой, порт - 9092)

# запускаем для данного сокета режим прослушивания
sock.listen(1)  # Метод принимает один аргумент — максимальное количество подключений в очереди

while True:
    conn, addr = sock.accept()  # принимаем подключение, conn - новый сокет, addr - аддрес клиента
    print("connected: " + addr[0])
    data = bytearray()
    while True:  # читаем данные порциями по 1024 байта пока они не закончились и сохраняем их в data
        packet = conn.recv(1024)
        if not packet:
            break
        data.extend(packet)
    conn.close()  # закрываем соединение
    im = Image.open(io.BytesIO(data))  # преобразуем полученные данные сначала в объект BytesIO, затем в картинку
    im.save("out.jpg", "JPEG")  # сохраняем картинку в файл "out.jpg"
    print("saved")
