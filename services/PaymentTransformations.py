import xml.etree.ElementTree as ET
import json

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

