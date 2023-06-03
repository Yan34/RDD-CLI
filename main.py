import os
from MRCNNDetector import MRCNNDetector
from YoloV8Detector import YoloV8Detector
import argparse


if __name__ == '__main__':
    detector = MRCNNDetector(os.path.abspath('models/mrcnn/config_3.py'), os.path.abspath('models/mrcnn/3_epoch_9.pth'))
    # detector = YoloV8Detector(os.path.abspath('models/yolov8/train20.pt'))
    # detector.detect("D:\\University\\RoadDamageDetection\\DatasetCocoFormat1200\\test\\819785_ES_259_259ES000000_00410_RAW.jpg", 'image')
    detector.detect("D:\\University\\АД\\Кузьмичи\\18 ОП РЗ 18К-01-16 (прямое направление).avi", 'video')
