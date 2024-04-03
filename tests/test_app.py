import json
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app
#from controllers.payment_controller import payment_processing

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello world'
'''
def test_card_payment():
    with open(os.path.join("tests", "inputdata", "card_valid_payment.json"), "r") as file:
        payload = json.load(file)
        payment_processing(json.dumps(payload))
'''
'''
def test_payment_processing_with_valid_payload(client):
    with open(os.path.join("tests", "inputdata", "card_valid_payment.json"), "r") as file:
        payload = json.load(file)
        response = client.post('/pay', json={'payload': payload})
        data = response.get_json()  # Parse JSON response
        assert response.status_code == 200
        assert data['message'] == 'Payment accepted'

def test_payment_processing_with_invalid_payload(client):
    payload = json.dumps({'invalid_key': 'invalid_value'})
    response = client.post('/pay', json={'payload': payload})
    data = response.get_json()  # Parse JSON response
    assert response.status_code == 400
    assert data['message'] == 'Payment rejected'
'''