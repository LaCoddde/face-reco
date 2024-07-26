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

def test_extract_document_data_pdf(client):
    data = {
        'document': (open('path/to/your/test/document.pdf', 'rb'), 'test_document.pdf')
    }
    response = client.post('/api/v1/document-extraction/', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'success'
    assert 'data' in json_data
    assert 'document_data' in json_data['data']
    assert json_data['data']['document_data']

def test_extract_document_data_docx(client):
    data = {
        'document': (open('path/to/your/test/document.docx', 'rb'), 'test_document.docx')
    }
    response = client.post('/api/v1/document-extraction/', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'success'
    assert 'data' in json_data
    assert 'document_data' in json_data['data']
    assert json_data['data']['document_data']

def test_extract_document_data_image(client):
    data = {
        'document': (open('path/to/your/test/document.png', 'rb'), 'test_document.png')
    }
    response = client.post('/api/v1/document-extraction/', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'success'
    assert 'data' in json_data
    assert 'document_data' in json_data['data']
    assert json_data['data']['document_data']
