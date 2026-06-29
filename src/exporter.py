import csv
from typing import Dict, List

from src.settings import OUTPUT_FILE


def export_transactions(transactions: List[Dict]) -> None:
    """
    Export validated transactions to the processed dataset.
    """

    if not transactions:
        return

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=transactions[0].keys(),
        )

        writer.writeheader()
        writer.writerows(transactions)