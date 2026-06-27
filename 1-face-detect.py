import cv2
import mediapipe as mp

mp_face = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.6) as detector:
    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = detector.process(rgb)
        if results.detections:
            for det in results.detections:
                mp_draw.draw_detection(frame, det)
        cv2.imshow("MediaPipe Face Detection", frame)
        if cv2.waitKey(1) & 0xFF == 27:   # Esc — выход
            break

cap.release()
cv2.destroyAllWindows()
