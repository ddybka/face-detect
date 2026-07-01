import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

# Если качество распознавания важнее производительности можно загрузить несколько фото одного человека
# Загружаем изображения и тренируем модель узнавать их
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

my_image = face_recognition.load_image_file("i.jpg")
my_face_encoding = face_recognition.face_encodings(my_image)[0]

# Массив закодированных изображений которые надо узнавать
known_face_encodings = [
    obama_face_encoding,
    my_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Me"
]

while True:
    # Получаем изображение с вебкамеры
    ret, frame = video_capture.read()

    # Переводим из BGR в RGB
    rgb_frame = frame[:, :, ::-1]

    # Находим все лица на изображении и кодируем их
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # цикл по всем лицам на изображении
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Смотрим похоже ли лицо на какое-то из известных
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # Если похоже то выбираем первого из кандидатов на которого оно похоже и присваиваем это имя
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Также можно использовать не первого попавшегося, а
        # наиболее похожего из всех кандидатов (их может быть несколько)
        # face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        # best_match_index = np.argmin(face_distances)
        # if matches[best_match_index]:
        #     name = known_face_names[best_match_index]

        # Рисуем рамку
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Рисуем метку с именем
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Выводим изоражение
    cv2.imshow('Video', frame)

    # Для выхода нажать 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
