import cv2
import filetype
from pathlib import Path


class Detector:
    def __init__(self, name=None):
        print("Детектор: "+str(name))

    def _get_video(self, path: str | Path):
        try:
            cap = cv2.VideoCapture(path)
        except Exception as e:
            print("Не удалось извлечь видео. Ошибка: "+str(e))
            exit()
        return cap

    def _detect_image(self, path):
        pass

    def _detect_video(self, path):
        pass

    def detect(self, path, mode):
        if mode == 'video':
            print('Режим: Видео')
            if filetype.is_video(path):
                self._detect_video(path)
            else:
                print('Неверный тип файла')
        elif mode == 'image':
            print('Режим: Изображение')
            if filetype.is_image(path):
                self._detect_image(path)
            else:
                print('Неверный тип файла')
        else:
            print('Режим не определён')
