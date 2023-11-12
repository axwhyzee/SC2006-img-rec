def mocked_imread_from_url(*_):
    raise ConnectionError('Invalid image URL')