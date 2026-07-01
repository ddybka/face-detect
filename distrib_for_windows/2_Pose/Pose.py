import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)  # создаём объект для захвата видео с вебкамеры
with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()  # получаем кадр с вебкамеры
        if not success:
            print("Ignoring empty camera frame.")
            continue
        # переворачиваем картинку и переводим кодировку цвета из BGR в RGB
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # Этот флаг можно установить в False для улучшения производительности перед обработкой изображения
        image.flags.writeable = False
        # Обрабатываем изображение (находим ключевые точки)
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # выводим координаты всех точек
        if results.pose_landmarks:
            print(results.pose_landmarks)
            #print(results.pose_landmarks.landmark[30]) - пример вывод точки с номером 30(правая пятка)
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imshow('MediaPipe Pose', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
