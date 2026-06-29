import subprocess
import sys
from pathlib import Path
import filecmp


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_command(command: list[str], description: str) -> bool:
    print(f"\n=== {description} ===")

    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        print(f"{description} FAILED")
        return False

    print(f"{description} PASSED")
    return True


def verify_processed_output() -> bool:
    print("\n=== Checking processed output ===")

    processed_file = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "transactions_clean.csv"
    )

    expected_file = (
        PROJECT_ROOT
        / "data"
        / "expected"
        / "transactions_clean.csv"
    )

    if not processed_file.exists():
        print("Processed dataset not found.")
        return False

    if not expected_file.exists():
        print("Expected dataset not found.")
        return False

    if processed_file.stat().st_size == 0:
        print("Processed dataset is empty.")
        return False

    if not filecmp.cmp(
        processed_file,
        expected_file,
        shallow=False,
    ):
        print("Processed dataset does not match expected output.")
        return False

    print("Processed dataset matches expected output.")
    return True


def main() -> int:
    checks = [
        run_command(
            [sys.executable, "-m", "scripts.run_pipeline"],
            "Pipeline Execution",
        ),
        run_command(
            [sys.executable, "-m", "pytest"],
            "Automated Tests",
        ),
        verify_processed_output(),
    ]

    print("\n==============================")

    if all(checks):
        print("Repository verification PASSED")
        return 0

    print("Repository verification FAILED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())