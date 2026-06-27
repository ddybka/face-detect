import os
import cv2
from deepface import DeepFace

DB = "known_faces"
MODEL = "Facenet"
PROCESS_EVERY = 15          # узнаём раз в 15 кадров — иначе тормозит

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
frame_no = 0
last_name = "..."

while True:
    ok, frame = cap.read()
    if not ok:
        break

    frame_no += 1
    if frame_no % PROCESS_EVERY == 0:
        try:
            results = DeepFace.find(
                img_path=frame,
                db_path=DB,
                model_name=MODEL,
                enforce_detection=False,
                silent=True,
            )
            if len(results) > 0 and not results[0].empty:
                best = results[0].iloc[0]["identity"]      # путь к ближайшему фото
                last_name = os.path.basename(os.path.dirname(best))  # имя = папка
            else:
                last_name = "Unknown"
        except Exception:
            last_name = "Unknown"

    cv2.putText(frame, last_name, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    cv2.imshow("DeepFace", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
