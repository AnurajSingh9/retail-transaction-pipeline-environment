from src.loader import load_transactions


def test_load_transactions():
    transactions = load_transactions()

    assert len(transactions) == 5
    assert transactions[0].transaction_id == "TXN-100001"
    assert transactions[0].store_id == "STR-101"