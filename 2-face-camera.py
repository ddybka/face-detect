import os
import cv2
import face_recognition

BASE_DIR = "known_faces"
os.makedirs(BASE_DIR, exist_ok=True)


def capture_for(name):
    person_dir = os.path.join(BASE_DIR, name)
    os.makedirs(person_dir, exist_ok=True)

    # сколько уже снято — чтобы не перезатирать
    count = len([f for f in os.listdir(person_dir) if f.lower().endswith(".jpg")])

    cap = cv2.VideoCapture(0)          # на Windows можно cv2.VideoCapture(0, cv2.CAP_DSHOW)
    print(f"\n[{name}] ПРОБЕЛ — снять кадр, ESC — следующий человек")

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        view = frame.copy()
        cv2.putText(view, f"{name}: {count} foto | SPACE=snimok  ESC=dalee",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Capture", view)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:                  # ESC — закончить этого человека
            break
        if key == 32:                  # ПРОБЕЛ — снять кадр
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = face_recognition.face_locations(rgb)
            if len(faces) == 1:
                count += 1
                path = os.path.join(person_dir, f"{count}.jpg")
                cv2.imwrite(path, frame)
                print(f"  сохранено: {path}")
            elif len(faces) == 0:
                print("  лицо не найдено — переснимите")
            else:
                print(f"  в кадре {len(faces)} лица — нужно одно")

    cap.release()
    cv2.destroyAllWindows()


while True:
    name = input("\nИмя латиницей (anna, ivan), Enter — выход: ").strip()
    if not name:
        break
    capture_for(name)

print("Готово.")
