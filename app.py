import json
import logging

from flask import abort, Flask, request, Response
from imread_from_url import imread_from_url
from requests.exceptions import ConnectionError

from onnxyolov8.YOLOv8 import yolov8_detector
from settings import WHITELIST


logger = logging.getLogger('App')

app = Flask(__name__)


def _error(e: str) -> Response:
    """
    Helper function to return a standard error payload

    Params
    ------
    e : str
        Error message

    Returns
    -------
    JSON response
    """
    return Response(response=json.dumps({'error': e, 'boxes': [], 'classes': [], 'conf': []}), status=400)


@app.before_request
def whitelist():
    """
    Whitelisting middleware
    """
    logger.info(request.remote_addr)
    if request.remote_addr not in WHITELIST:
        abort(403) 
        

@app.route('/')
def root():
    return ''


@app.route('/inference')
def inference():
    """
    Accepts a url param, & returns a payload in the following format: 
    {
        error: str,                // error message if req failed, else None
        boxes: list[list[float]],  // coords of bounding boxes (top left as origin, (x1 y1 x2 y2)) if success, else []
        classes: list[int],        // class indexes if success, else []
        conf: list[float]          // confidence levels if success, else []
    }

    Returns
    -------
    JSON response
    """
    url = request.args.get('url', default='', type=str)

    if not url:
        logger.error('No URL received')
        return _error('No URL received')

    try:
        img = imread_from_url(url)
        boxes, scores, class_ids = yolov8_detector(img)
        return Response(response=json.dumps({
            'error': None, 
            'boxes': boxes.tolist(), 
            'classes': class_ids.tolist(), 
            'conf': scores.tolist()
        }), status=200)

    except ConnectionError:
        logger.error('Invalid image URL')
        return _error('Invalid image URL')
    
    except Exception as e:
        logger.error(str(e))
        return _error(str(e))


if __name__ == '__main__':
    app.run()