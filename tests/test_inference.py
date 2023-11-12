import json
from urllib import parse

from unittest.mock import patch

from mocks import mocked_imread_from_url


IMG_URL = 'https://play-lh.googleusercontent.com/mMRQ1AtZgQY3GxkxFGuC6uD74NEmkn7AuTyZVBVZhzL2khQggE3fq85i9V8-57t12w'


def test_inference_valid(client):
    r = client.get(f'/inference?url={parse.quote_plus(IMG_URL)}')
    data = json.loads(r.data)
    
    assert r._status_code == 200
    assert data['error'] == None
    assert len(data['boxes']) >= 0
    assert len(data['classes']) >= 0
    assert len(data['conf']) >= 0


def test_inference_no_url(client):
    r = client.get('/inference')
    data = json.loads(r.data)

    assert r._status_code == 400
    assert data['error'] == 'No URL received'
    assert data['boxes'] == []
    assert data['classes'] == []
    assert data['conf'] == []


@patch('app.imread_from_url', mocked_imread_from_url)
def test_inference_url_invalid_url(client):
    r = client.get(f'/inference?url={parse.quote_plus(IMG_URL)}')
    data = json.loads(r.data)
    
    assert r._status_code == 400
    assert data['error'] == 'Invalid image URL'
    assert data['boxes'] == []
    assert data['classes'] == []
    assert data['conf'] == []


def test_inference_url_non_img_url(client):
    r = client.get(f'/inference?url={parse.quote_plus("https://www.google.com/")}')
    data = json.loads(r.data)
    
    assert r._status_code == 400
    assert data['error'] == "'NoneType' object has no attribute 'shape'"
    assert data['boxes'] == []
    assert data['classes'] == []
    assert data['conf'] == []
