import os
import cv2
import face_recognition

KNOWN_DIR = "known_faces"   # anna.jpg, ivan.jpg, ...

known_encodings, known_names = [], []
for filename in os.listdir(KNOWN_DIR):
    image = face_recognition.load_image_file(os.path.join(KNOWN_DIR, filename))
    encs = face_recognition.face_encodings(image)
    if encs:                                  # вдруг на фото лицо не нашлось
        known_encodings.append(encs[0])
        known_names.append(os.path.splitext(filename)[0])

print("Загружено:", known_names)

cap = cv2.VideoCapture(0)
while True:
    ok, frame = cap.read()
    if not ok:
        break

    small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)   # уменьшаем ради скорости
    rgb_small = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    locations = face_recognition.face_locations(rgb_small)
    encodings = face_recognition.face_encodings(rgb_small, locations)

    for (top, right, bottom, left), enc in zip(locations, encodings):
        name = "Unknown"
        distances = face_recognition.face_distance(known_encodings, enc)
        if len(distances) > 0:
            best = distances.argmin()
            if distances[best] < 0.5:          # порог: меньше — строже
                name = known_names[best]

        top, right, bottom, left = top*4, right*4, bottom*4, left*4   # обратно к полному кадру
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
