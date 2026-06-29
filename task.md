# Restore the Nightly Retail Transaction Pipeline

## Context

Following the **v2.3.0** deployment, downstream analytics jobs began reporting data quality failures during the nightly processing window.

The release introduced support for a new regional transaction feed along with several internal pipeline changes. Although the deployment completed successfully, multiple validation checks began failing during scheduled processing.

Initial investigation indicates that the regression was introduced as part of the **v2.3.0** release, but the underlying cause has not yet been identified.

You have been assigned to investigate the repository, identify the root cause of the regression, and restore the pipeline to a production-ready state.

---

## Objective

Restore the pipeline by implementing the smallest appropriate change that resolves the regression while preserving the existing architecture.

A successful solution should:

* Execute the pipeline successfully.
* Produce the expected processed dataset.
* Pass all automated tests.
* Pass all validation checks.
* Complete the repository verification successfully.

---

## Repository Structure

```text
src/
    Pipeline implementation

data/
    Input datasets
    Processed outputs

tests/
    Automated test suite

verifier/
    Repository verification utilities

docs/
    Engineering documentation
```

---

## Expectations

Before making changes, investigate the repository to understand how the pipeline is intended to operate.

Useful starting points include:

* Project documentation
* Pipeline implementation
* Automated tests
* Validation output
* Version history

Do not bypass validation, hardcode expected outputs, or introduce unnecessary architectural changes.

Implement a maintainable fix that addresses the underlying cause of the regression.

---

## Completion Criteria

The task is complete when:

* The pipeline executes successfully.
* All automated tests pass.
* Validation reports no errors.
* The processed dataset is generated correctly.
* The repository verification completes successfully.
* The implemented solution resolves the regression without introducing new validation or test failures.
