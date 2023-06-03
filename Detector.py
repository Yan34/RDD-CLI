import os
import cv2
from pathlib import Path


class Detector:
    def __init__(self, name=None):
        print("Детектор: "+str(name))

    def _get_video(self, path: os.PathLike):
        try:
            cap = cv2.VideoCapture(path)
        except Exception as e:
            print("Не удалось извлечь видео. Ошибка: "+str(e))
            exit()
        return cap
