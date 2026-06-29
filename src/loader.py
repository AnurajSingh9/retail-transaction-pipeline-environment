import csv
from datetime import datetime
from decimal import Decimal
from typing import List

from src.models import Transaction
from src.settings import INPUT_FILE


DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def load_transactions() -> List[Transaction]:
    """
    Load retail transactions from the raw CSV file.
    """

    transactions: List[Transaction] = []

    with open(INPUT_FILE, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            transaction = Transaction(
                transaction_id=row["transaction_id"],
                order_timestamp=datetime.strptime(
                    row["order_timestamp"],
                    DATE_FORMAT,
                ),
                store_id=row["store_id"],
                customer_id=row["customer_id"],
                product_sku=row["product_sku"],
                quantity=int(row["quantity"]),
                unit_price=Decimal(row["unit_price"]),
                discount_pct=Decimal(row["discount_pct"]),
                payment_method=row["payment_method"],
                region=row["region"],
            )

            transactions.append(transaction)

    return transactions