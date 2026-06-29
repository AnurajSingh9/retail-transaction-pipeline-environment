from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime


@dataclass
class Transaction:
    """
    Represents a single retail transaction processed by the Retail Data Platform.
    """

    transaction_id: str
    order_timestamp: datetime
    store_id: str
    customer_id: str
    product_sku: str
    quantity: int
    unit_price: Decimal
    discount_pct: Decimal
    payment_method: str
    region: str