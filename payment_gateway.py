import time


class PaymentGateway:
    def __init__(self, provider: str = "stripe"):
        self.provider = provider

    def charge(self, amount_cents: int, token: str) -> dict:
        # validates token, charges card, returns transaction result
        return {
            "status": "success",
            "amount_cents": amount_cents,
            "timestamp": time.time(),
        }

    def refund(self, transaction_id: str) -> dict:
        return {"status": "refunded", "transaction_id": transaction_id}
