# Распознавание лиц на Python

## Инструкция

```bash
# Установить Python библиотеки:

# 1. Для распознавания
pip install mediapipe opencv-python

# 2. Для узнавания

pip install cmake deepface face_recognition opencv-contrib-python

# 3. Запустить скрипт для распознавания лица (остановить на Escape):
python 1-face-detect.py

# 4. Подготовить фотографии человека (пробел - фотография, Escape - выход):
python 2-face-camera.py

# 5. Обучить модель на фотографиях
python 3-train.py

# 6. Запустить скрипт распознавания лиц:
python 4-face-recognition.py
```

## Возможные сбои

```bash
# 1. Может потребоваться Numpy<2:
python install "numpy<2"

python install "protobuf==3.20.3"
```
