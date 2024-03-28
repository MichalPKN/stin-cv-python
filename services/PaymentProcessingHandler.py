import services.CashPaymentService as CashPaymentService
import services.CardPaymentService as CardPaymentService
import services.PaymentTransformations as PaymentTransformations


class PaymentProcessingHandler:
    def __init__(self):
        self.payment_processing_handler = {
            'CASH': CashPaymentService.CashPaymentService(),
            'CARD': CardPaymentService.CardPaymentService()
        }
        self.payment_transformations = PaymentTransformations.PaymentTransformations()

    def process_payment(self, payload):
        payment = self.payment_transformations.transform_json_into_payment(payload)
        self.payment_processing_handler[payment['payment_type']].process_payment(payment)
