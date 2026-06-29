from src.loader import load_transactions
from src.transform import transform_transactions
from src.validator import validate_transactions


def test_pipeline_runs_successfully():
    transactions = load_transactions()

    transformed_transactions = transform_transactions(transactions)

    validation_errors = validate_transactions(transformed_transactions)

    assert len(transactions) > 0
    assert len(transformed_transactions) == len(transactions)
    assert validation_errors == []