from src.loader import load_transactions
from src.transform import transform_transactions


def main() -> None:
    transactions = load_transactions()

    processed_transactions = transform_transactions(transactions)

    print(f"Loaded {len(processed_transactions)} transactions.\n")

    for transaction in processed_transactions:
        print(transaction)


if __name__ == "__main__":
    main()