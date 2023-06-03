import cv2

from Detector import Detector
from pathlib import Path
import mmdet.apis as mmapi


class MRCNNDetector(Detector):
    def __init__(self, config_pth: str | Path, checkpoint_pth: str | Path):
        super().__init__('Mask R-CNN')
        self.model = self._get_model(config_pth, checkpoint_pth)

    def _get_model(self, config_pth: str | Path, checkpoint_pth: str | Path):
        try:
            model = mmapi.init_detector(config_pth, checkpoint_pth, cfg_options=dict(resume_from=checkpoint_pth))
            model.CLASSES = ('crack', 'pothole')
        except Exception as e:
            print('Модель Mask R-CNN не была создана. Ошибка: '+str(e))
            exit()
        return model

    def _detect_video(self, path):
        cap = super()._get_video(path)
        while True:
            ret, frame = cap.read()
            if ret:
                try:
                    results = mmapi.inference_detector(self.model, frame)
                    annotated_frame = self.model.show_result(frame, results, score_thr=0.3, thickness=1)
                except Exception as e:
                    print('Mask R-CNN: Не получилось произвести сегментацию. Ошибка: ' + str(e))
                    exit()
                cv2.imshow("RDD Mask R-CNN", annotated_frame)
                if cv2.waitKey(25) & 0xFF == ord('q') or ret == False:
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    def _detect_image(self, path):
        try:
            result = mmapi.inference_detector(self.model, path)
            annotated = self.model.show_result(path, result, score_thr=0.2, thickness=1, mask_color=(90,100,100))
        except Exception as e:
            print('Mask R-CNN: Не получилось произвести сегментацию. Ошибка: '+str(e))
            exit()
        while True:
            cv2.imshow('RDD Mask R-CNN', annotated)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    def detect(self, path, mode):
        if mode == 'video':
            self._detect_video(path)
        elif mode == 'image':
            self._detect_image(path)
        else:
            print('Режим не определён')
