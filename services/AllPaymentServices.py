import json
import xml.etree.ElementTree as ET

class PaymentTransformations:
    def __init__(self):
        self.object_mapper = json

    def transform_json_into_payment(self, payload):
        return self.object_mapper.loads(payload)

    def transform_xml_from_payment(self, payment):
        root = ET.Element("Payment")
        for key, value in payment.items():
            ET.SubElement(root, key).text = str(value)
        return ET.tostring(root, encoding="utf-8").decode()

class CardPaymentService:
    def process_payment(self, payment):
        # Implementation for card payments
        pass

class CashPaymentService:
    def process_payment(self, payment):
        # Implementation for cash payments
        pass

class PaymentProcessingHandler:
    def __init__(self):
        self.payment_processing_handler = {
            'CASH': CashPaymentService(),
            'CARD': CardPaymentService()
        }
        self.payment_transformations = PaymentTransformations()

    def process_payment(self, payload):
        payment = self.payment_transformations.transform_json_into_payment(payload)
        self.payment_processing_handler[payment['payment_type']].process_payment(payment)
