import os
from MRCNNDetector import MRCNNDetector
from YoloV8Detector import YoloV8Detector
import argparse


mrcnn_config_path = os.path.abspath('models/mrcnn/config_3.py')
mrcnn_model_path = os.path.abspath('models/mrcnn/3_epoch_9.pth')
yolov8_model_path = os.path.abspath('models/yolov8/train20.pt')


def createParser ():
    parser_ = argparse.ArgumentParser()
    parser_.add_argument('-d', '--detector', choices=['mrcnn', 'yolov8'], required=True)
    parser_.add_argument('-m', '--mode', choices=['image', 'video'], required=True)
    parser_.add_argument('-f', '--file', required=True, type=str)
    return parser_


if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    mode = args.mode
    path = os.path.abspath(args.file)
    if args.detector == 'mrcnn':
        detector = MRCNNDetector(mrcnn_config_path, mrcnn_model_path)
    elif args.detector == 'yolov8':
        detector = YoloV8Detector(yolov8_model_path)
    else:
        print('Детектор не опознан')
        exit()
    detector.detect(path, mode)
