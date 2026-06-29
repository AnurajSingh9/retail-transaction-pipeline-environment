from src.loader import load_transactions
from src.transform import transform_transactions
from src.exporter import export_transactions
from src.settings import OUTPUT_FILE


def test_export_transactions():
    transactions = load_transactions()
    transformed = transform_transactions(transactions)

    export_transactions(transformed)

    assert OUTPUT_FILE.exists()
    assert OUTPUT_FILE.stat().st_size > 0