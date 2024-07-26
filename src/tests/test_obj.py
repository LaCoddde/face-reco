#Unit tests for object detection.
import os
import tempfile
import pytest
from app import app

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config['UPLOAD_FOLDER'] = tempfile.mkdtemp()
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_detect_objects_success(client):
    data = {
        'image': (open('path/to/your/test/image.jpg', 'rb'), 'test_image.jpg')
    }
    response = client.post('/api/v1/object-detection/', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'success'
    assert 'data' in json_data
    assert 'objects' in json_data['data']

def test_detect_objects_no_image(client):
    response = client.post('/api/v1/object-detection/', content_type='multipart/form-data')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['status'] == 'error'
    assert json_data['message'] == 'Image file is required.'
