from src.loader import load_transactions
from src.transform import transform_transactions
from src.validator import validate_transactions


def test_validate_transactions():
    transactions = load_transactions()
    transformed = transform_transactions(transactions)

    errors = validate_transactions(transformed)

    assert errors == []