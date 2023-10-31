import logging
from typing import List

from ultralytics import YOLO

from settings import ROBOFLOW_DIR


logger = logging.getLogger('YOLOv8')


class YoloV8Model:

    def __init__(
        self, 
        weights: str = 'yolov8n.pt'
    ):
        # Load a model
        self.model = YOLO(weights)

    
    def inference(
        self, 
        paths: List[str]
    ):
        """
        Run inference on a set of images as specified by paths

        Params
        ------
        paths : List[str]
            List of image paths
        """
        logger.info(f'Running inferences ...')
        res = self.model.predict(paths, save=True)
        logger.info(f'Predictions saved at \"runs/detect/predict\"')

        return res


    def train(
        self, 
        epochs: int = 100, 
        imgsz: int = 640
    ):
        """
        Download Roboflow dataset & train

        Params
        ------
        epochs : int
            Number of epochs
        imgsz : int
            Image width & height (assume square format)
        """
        from datagen import download_dataset

        download_dataset()
        self.model.train(data=f'{ROBOFLOW_DIR}/data.yaml', epochs=epochs, imgsz=imgsz)
        self.save()
    
    
    def save(self):
        """
        Export model to ONNX format
        """
        path = self.model.export(format="onnx")
        logger.info(f'Saved ONNX model to {path}')


if __name__ == '__main__':
    # train & save model using Roboflow dataset
    model = YoloV8Model('models/yolov8n_50_2410.pt')
    # model.train(epochs=1)
    model.save()
