from flask import Blueprint, request, jsonify
from services.AllPaymentServices import PaymentProcessingHandler
import json

payment_controller = Blueprint('payment_controller', __name__)

payment_processing_handler = PaymentProcessingHandler()

@payment_controller.route('/')
def hello():
    return 'Hello world'

@payment_controller.route('/pay', methods=['POST'])
def payment_processing():
    payload = request.json.get('payload')
    try:
        payment_processing_handler.process_payment(json.dumps(payload))
        return jsonify(message="Payment accepted"), 200
    except json.JSONDecodeError:
        return jsonify(message="Payment rejected"), 400

'''
from flask import Blueprint
import json

payment_controller = Blueprint('payment_controller', __name__)

class PaymentProcessingHandler:
    def payment_processing():
        try:
            payment = json.loads(payload)
            # Your payment processing logic here
            
            return "Payment accepted"
        except json.JSONDecodeError:
            return "Payment rejected"

@payment_controller.route('/')
def hello():
    return 'Hello world'

@payment_controller.route('/payment', methods=['GET', 'POST'])
def payment():
    handler = PaymentProcessingHandler()
    return handler.process_payment()
'''