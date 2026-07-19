from dataclasses import dataclass, field
from typing import List


@dataclass
class CartItem:
    sku: str
    quantity: int
    price_cents: int


@dataclass
class Cart:
    cart_id: str
    items: List[CartItem] = field(default_factory=list)

    @property
    def total_cents(self) -> int:
        return sum(item.price_cents * item.quantity for item in self.items)


@dataclass
class Order:
    order_id: str
    cart_id: str
    status: str = "pending"
