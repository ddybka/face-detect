import os
import face_recognition

KNOWN_DIR = "known_faces"

known_encodings, known_names = [], []
for person in os.listdir(KNOWN_DIR):
    person_dir = os.path.join(KNOWN_DIR, person)
    if not os.path.isdir(person_dir):
        continue
    for filename in os.listdir(person_dir):
        image = face_recognition.load_image_file(os.path.join(person_dir, filename))
        encs = face_recognition.face_encodings(image)
        if encs:
            known_encodings.append(encs[0])
            known_names.append(person)        # имя = название папки

print("Загружено:", known_names)
