# Retail Transaction Pipeline

A Python-based retail transaction processing pipeline maintained by the **Data Platform Engineering** team at **Lattice Commerce**.

The pipeline processes nightly retail transaction data, applies business transformations, validates data quality, and produces a cleaned dataset for downstream analytics workloads.

---

## Overview

This repository contains the implementation of the Retail Transaction Pipeline together with supporting documentation, automated tests, and tooling used to validate the pipeline.

If you have been assigned a maintenance or investigation task, begin by reviewing **`task.md`** before making any code changes.

---

## Getting Started

### Quick Start

```bash
pip install -r requirements.txt
python3 -m scripts.run_pipeline
pytest
```

### Requirements

* Python 3.11 or later
* pip

---

## Running the Pipeline

Execute the complete processing pipeline:

```bash
python3 -m scripts.run_pipeline
```

---

## Running the Test Suite

Execute all automated tests:

```bash
pytest
```

---

## Repository Structure

```text
|-- data/
|   |-- raw/              # Source transaction data
|   |-- processed/        # Generated pipeline output
|   |-- expected/         # Expected reference output
|   |-- logs/             # Pipeline execution logs
|
|-- docs/                 # Engineering documentation
|-- scripts/              # Pipeline entry points
|-- src/                  # Pipeline implementation
|-- tests/                # Automated test suite
|-- verifier/             # Repository verification utilities
```

---

## Pipeline Architecture

# How it works

Raw transactions come in as CSV, get loaded, cleaned, validated, 
and written out to the processed folder. Four stages:

loader -> transformer -> validator -> exporter

---

## Project Layout

| Directory   | Description                                   |
| ----------- | --------------------------------------------- |
| `src/`      | Core pipeline implementation                  |
| `tests/`    | Automated test suite                          |
| `data/`     | Input, processed, expected datasets, and logs |
| `docs/`     | Engineering documentation                     |
| `scripts/`  | Pipeline execution scripts                    |
| `verifier/` | Repository verification utilities             |

---

## Documentation

Additional project documentation is available in the `docs/` directory.

* Architecture Overview
* Data Dictionary
* Incident Report
* Change Log

---

## Design Principles

The project follows a modular pipeline architecture with clear separation of responsibilities.

* **Loader** — Reads raw transaction data.
* **Transformer** — Applies business transformations.
* **Validator** — Performs data quality checks.
* **Exporter** — Writes processed output datasets.
* **Pipeline** — Coordinates end-to-end execution.

Each stage of the pipeline is independently testable, making the system easier to maintain, troubleshoot, and extend.

---

## License

This repository is intended for engineering evaluation and demonstration purposes.