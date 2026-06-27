# Распознавание лиц на Python

## Инструкция

```bash
# Установить Python библиотеки:

# 1. Для распознавания
pip install mediapipe opencv-python

# 2. Для узнавания

pip install cmake deepface face_recognition

# 3. Запустить скрипт для распознавания лица (остановить на Escape):
python 1-face-detect.py

# 4. Подготовить фотографии человека (пробел - фотография, Escape - выход):
python 2-face-camera.py

# 5. Запустить скрипт распознавания лиц:
python 3-face-recognition.py
```

## Возможные сбои

```bash
# 1. Может потребоваться Numpy<2:
python install "numpy<2"

# 2. Ошибка новой версии Tensorflow
pip install "tensorflow==2.15.0"

pip install "numpy<2" "opencv-python==4.10.0.84" "tensorflow==2.15.0" deepface mediapipe
```
