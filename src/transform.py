from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List

from src.models import Transaction


def transform_transactions(transactions: List[Transaction]) -> List[Dict]:
    """
    Apply business transformations to retail transactions.
    """

    transformed_transactions: List[Dict] = []

    payment_mapping = {
        "card": "Card",
        "cash": "Cash",
        "upi": "UPI",
        "wallet": "Wallet",
    }

    for transaction in transactions:

        payment_method = payment_mapping.get(
            transaction.payment_method.strip().lower(),
            transaction.payment_method,
        )

        gross_amount = (
            Decimal(transaction.quantity) * transaction.unit_price
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
        )

        discount_amount = (
            (gross_amount * transaction.discount_pct) / Decimal("100")
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
        )

        net_amount = (
            gross_amount - discount_amount
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
        )

        transformed_transactions.append(
            {
                "transaction_id": transaction.transaction_id,
                "order_timestamp": transaction.order_timestamp,
                "store_id": transaction.store_id,
                "customer_id": transaction.customer_id,
                "product_sku": transaction.product_sku,
                "quantity": transaction.quantity,
                "unit_price": transaction.unit_price,
                "discount_pct": transaction.discount_pct,
                "payment_method": payment_method,
                "region": transaction.region,
                "gross_amount": gross_amount,
                "discount_amount": discount_amount,
                "net_amount": net_amount,
            }
        )

    return transformed_transactions