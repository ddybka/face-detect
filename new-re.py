import cv2

cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("model.yml")

# загружаем имена
names = {}
with open("labels.txt", encoding="utf-8") as f:
    for line in f:
        i, name = line.strip().split(",", 1)
        names[int(i)] = name

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in detected:
        face = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
        label, confidence = recognizer.predict(face)
        # у LBPH меньше = лучше. >70 считаем "не уверены"
        if confidence < 70:
            text = f"{names.get(label, '?')} ({int(confidence)})"
        else:
            text = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, text, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Recognition", frame)
    if cv2.waitKey(1) & 0xFF == 27:   # Esc
        break

cap.release()
cv2.destroyAllWindows()
