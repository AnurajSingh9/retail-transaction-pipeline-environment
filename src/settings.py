from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXPECTED_DATA_DIR = DATA_DIR / "expected"
LOG_DIR = DATA_DIR / "logs"

INPUT_FILE = RAW_DATA_DIR / "transactions.csv"
OUTPUT_FILE = PROCESSED_DATA_DIR / "transactions_clean.csv"
EXPECTED_FILE = EXPECTED_DATA_DIR / "transactions_clean.csv"
LOG_FILE = LOG_DIR / "pipeline.log"