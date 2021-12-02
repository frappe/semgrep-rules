# Frappe Semgrep rules

Semgrep rules specific to [Frappe Framework](https://github.com/frappe/frappe)

These rules guard against typical mistakes or bad practices while working on Frappe Framework apps. Frappe's own apps also use this to simplify repetitive checks in code review process.

## How to Use in my app

- You can reuse the GitHub Action that Frappe Framework itself uses for running Semgrep: [Workflow file](https://github.com/frappe/frappe/blob/develop/.github/workflows/semgrep.yml)

## How to contribute new rules

- Read how Semgrep works: [Getting started with semgrep rules](https://semgrep.dev/docs/writing-rules/overview/)
- Write a rule. Make sure it doesn't have too many false positives.
- Write positive and negative test cases for rule you are adding: [Testing rules](https://semgrep.dev/docs/writing-rules/testing-rules/)
