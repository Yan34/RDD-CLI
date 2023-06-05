from Detector import *
from ultralytics import YOLO


class YoloV8Detector(Detector):

    def __init__(self, checkpoint_pth: str | Path):
        super().__init__('YOLOv8')
        self.model = self._get_model(checkpoint_pth)

    def _get_model(self, checkpoint_pth: str | Path):
        try:
            model = YOLO(checkpoint_pth)
        except Exception as e:
            print('Модель YOLOv8 не была создана. Ошибка: '+str(e))
            exit()
        return model

    def _detect_video(self, path):
        cap = super()._get_video(path)
        while True:
            ret, frame = cap.read()
            if ret:
                try:
                    results = self.model(frame, iou=0.3)
                    annotated_frame = results[0].plot(labels=True, boxes=True, masks=True, probs=True)
                except Exception as e:
                    print('YOLOv8: Не получилось произвести сегментацию. Ошибка: ' + str(e))
                    exit()
                cv2.imshow("RDD YOLOv8", annotated_frame)
                if cv2.waitKey(25) & 0xFF == ord('q') or ret==False:
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    def _detect_image(self, path):
        try:
            result = self.model(path, iou=0.2)
            annotated = result[0].plot(labels=True, boxes=True, masks=True, probs=True)
        except Exception as e:
            print('YOLOv8: Не получилось произвести сегментацию. Ошибка: '+str(e))
            exit()
        while True:
            cv2.imshow("RDD YOLOv8", annotated)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
