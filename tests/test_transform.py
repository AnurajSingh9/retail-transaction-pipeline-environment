from decimal import Decimal

from src.loader import load_transactions
from src.transform import transform_transactions


def test_transform_calculations():
    transactions = load_transactions()
    transformed = transform_transactions(transactions)

    first = transformed[0]

    assert first["gross_amount"] == Decimal("1599.98")
    assert first["discount_amount"] == Decimal("160.00")
    assert first["net_amount"] == Decimal("1439.98")