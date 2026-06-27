import os
import cv2
import numpy as np

BASE_DIR = "known_faces"
cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces, labels = [], []
names = {}          # id -> имя
next_id = 0

for person in sorted(os.listdir(BASE_DIR)):
    person_dir = os.path.join(BASE_DIR, person)
    if not os.path.isdir(person_dir):
        continue

    names[next_id] = person
    for filename in os.listdir(person_dir):
        path = os.path.join(person_dir, filename)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue
        detected = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in detected:
            faces.append(cv2.resize(img[y:y+h, x:x+w], (200, 200)))
            labels.append(next_id)
    print(f"{person}: добавлено лиц")
    next_id += 1

if not faces:
    print("Лиц не найдено. Проверь, что в known_faces есть папки с фото.")
    raise SystemExit

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))
recognizer.save("model.yml")

# сохраняем словарь имён
with open("labels.txt", "w", encoding="utf-8") as f:
    for i, name in names.items():
        f.write(f"{i},{name}\n")

print("Готово. Обучено людей:", len(names))
