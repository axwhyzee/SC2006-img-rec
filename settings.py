import logging
import os

from dotenv import find_dotenv, load_dotenv    


load_dotenv(find_dotenv())


# --------- download.py ---------
API_URL = 'https://api.data.gov.sg/v1/transport/traffic-images'
DOWNLOAD_FOLDER = 'assets'


# --------- datagen.py ---------
ROBOFLOW_API_KEY = os.environ.get('ROBOFLOW_PRIVATE_API_KEY')
ROBOFLOW_WORKSPACE = os.environ.get('ROBOFLOW_WORKSPACE')
ROBOFLOW_PROJECT = os.environ.get('ROBOFLOW_PROJECT')
ROBOFLOW_VERSION = int(os.environ.get('ROBOFLOW_VERSION'))
ROBOFLOW_DIR = os.path.join(os.getcwd(), f'{ROBOFLOW_PROJECT}-{ROBOFLOW_VERSION}')


# --------- yolov8.py ---------
SAVED_MODEL = 'models/yolov8n_50n_2410.pt' # pretrained weights to run inferences on


# --------- onnxyolov8 ---------
ONNX_MODEL = 'models/yolov8n_50_2410.onnx'
CONF_THRESHOLD = 0.3


# --------- app.py ---------
WHITELIST = ['127.0.0.1']


logging.basicConfig(level=logging.INFO)