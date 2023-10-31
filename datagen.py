import logging
import os

from roboflow import Roboflow

from settings import (
    ROBOFLOW_API_KEY,
    ROBOFLOW_WORKSPACE,
    ROBOFLOW_PROJECT,
    ROBOFLOW_VERSION,
    ROBOFLOW_DIR
)


logger = logging.getLogger('Roboflow')


def download_dataset():
    """
    Download Roboflow dataset
    """
    rf = Roboflow(api_key=ROBOFLOW_API_KEY)
    project = rf.workspace(ROBOFLOW_WORKSPACE).project(ROBOFLOW_PROJECT)
    project.version(ROBOFLOW_VERSION).download('yolov8')
    logger.info(f'Downloaded Roboflow dataset to \"{ROBOFLOW_DIR}\"')
    
    update_yaml()


def update_yaml():
    """
    Update train, val, test paths to absolute paths in yaml file
    """
    yaml_path = os.path.join(ROBOFLOW_DIR, 'data.yaml')

    with open(yaml_path, 'r') as f:
        lines = f.readlines()

    lines[-1] = f'val: {os.path.join(ROBOFLOW_DIR, "valid", "images")}\n'
    lines[-2] = f'train: {os.path.join(ROBOFLOW_DIR, "train", "images")}\n'
    lines[-3] = f'test: {os.path.join(ROBOFLOW_DIR, "test", "images")}\n'

    with open(yaml_path, 'w') as f:
        f.write('\n'.join(lines))


if __name__ == '__main__':
    download_dataset()