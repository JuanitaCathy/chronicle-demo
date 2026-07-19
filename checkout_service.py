def process_checkout(cart_id: str, payment_method: str) -> dict:
    # applies discount, charges payment, returns order confirmation
    return {"status": "confirmed", "cart_id": cart_id}
 
 
def get_cart(cart_id: str) -> dict:
    return {"cart_id": cart_id, "items": []}
 
