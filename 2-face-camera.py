import os
import cv2

BASE_DIR = "known_faces"
os.makedirs(BASE_DIR, exist_ok=True)

# встроенный в OpenCV детектор лиц — dlib больше не нужен
cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def capture_for(name):
    person_dir = os.path.join(BASE_DIR, name)
    os.makedirs(person_dir, exist_ok=True)
    count = len([f for f in os.listdir(person_dir) if f.lower().endswith(".jpg")])

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   # CAP_DSHOW — стабильнее на Windows
    print(f"\n[{name}] ПРОБЕЛ — снять кадр, ESC — следующий человек")

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        view = frame.copy()
        cv2.putText(view, f"{name}: {count} foto | SPACE=snimok  ESC=dalee",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        for (x, y, w, h) in faces:
            cv2.rectangle(view, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Capture", view)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:                  # ESC
            break
        if key == 32:                  # ПРОБЕЛ
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
