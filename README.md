# Распознавание лиц на Python

## Инструкция

```bash
# Установить Python библиотеки:

# 1. Для распознавания
pip install mediapipe opencv-contrib-python "numpy<2"

# 2. Для узнавания

pip install cmake deepface face_recognition opencv-contrib-python opencv-python

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
pip install "numpy<2"

# 2. Иногда помогает откатить версию protobuf:
pip install "protobuf==3.20.3"

# 3. В новой версии mediapipe другой API:
pip install "mediapipe==0.10.8"
```

**Альтернативное решение:**

```bash
# Шаг 1
pip uninstall mediapipe opencv-python protobuf tensorflow -y
pip install protobuf==3.20.3
pip install mediapipe==0.10.8 --no-deps
pip install opencv-python
pip install numpy

# Шаг 2
pip uninstall numpy -y
pip install numpy==1.24.3
pip uninstall mediapipe -y
pip install mediapipe==0.10.8
pip uninstall matplotlib -y
pip install matplotlib==3.7.1
```
