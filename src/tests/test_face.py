# src/tests/test_face.py
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

def test_recognize_face(client):
    data = {
        'image': (open('path/to/your/test/image.jpg', 'rb'), 'test_image.jpg')
    }
    response = client.post('/api/v1/face-recognition/', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'success'
    assert 'data' in json_data
