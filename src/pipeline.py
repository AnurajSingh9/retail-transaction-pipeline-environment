from src.exporter import export_transactions
from src.loader import load_transactions
from src.transform import transform_transactions
from src.validator import validate_transactions


def run_pipeline() -> None:
    """
    Execute the complete retail transaction pipeline.
    """

    print("Loading transactions...")
    transactions = load_transactions()

    print("Transforming transactions...")
    transformed_transactions = transform_transactions(transactions)

    print("Validating transactions...")
    validation_errors = validate_transactions(transformed_transactions)

    if validation_errors:
        print("\nValidation failed.\n")

        for error in validation_errors:
            print(f"- {error}")

        return

    print("Exporting transactions...")
    export_transactions(transformed_transactions)

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()