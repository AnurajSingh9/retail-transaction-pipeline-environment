from typing import Dict, List


VALID_PAYMENT_METHODS = {
    "Card",
    "Cash",
    "UPI",
    "Wallet",
}

VALID_REGIONS = {
    "North",
    "South",
    "East",
    "West",
}


def validate_transactions(transactions: List[Dict]) -> List[str]:
    """
    Validate transformed transaction records.

    Returns:
        List[str]: A list of validation errors.
        An empty list indicates all records are valid.
    """

    errors: List[str] = []
    seen_transaction_ids = set()

    for transaction in transactions:

        transaction_id = transaction["transaction_id"]

        if transaction_id in seen_transaction_ids:
            errors.append(
                f"Duplicate transaction_id: {transaction_id}"
            )
        else:
            seen_transaction_ids.add(transaction_id)

        if transaction["quantity"] <= 0:
            errors.append(
                f"Invalid quantity for {transaction_id}"
            )

        if transaction["unit_price"] < 0:
            errors.append(
                f"Negative unit price for {transaction_id}"
            )

        if not (0 <= transaction["discount_pct"] <= 100):
            errors.append(
                f"Invalid discount percentage for {transaction_id}"
            )

        if transaction["payment_method"] not in VALID_PAYMENT_METHODS:
            errors.append(
                f"Invalid payment method for {transaction_id}"
            )

        if transaction["region"] not in VALID_REGIONS:
            errors.append(
                f"Invalid region for {transaction_id}"
            )

    return errors