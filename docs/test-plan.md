# Test Plan - EMP-101

API: create, list, update, delete, duplicate email, missing ID, search.

UI: create employee, search employee, delete cancelled (employee kept),
delete confirmed (employee removed).

Run API tests: `pytest tests/test_api.py -v`.
Run UI tests with the app running on port 8000: `pytest tests/test_ui.py -v`.

## Latest results

- `tests/test_api.py`: 5 passed.
- `tests/test_ui.py`: 3 passed, in two runs against uvicorn on port 8000.
- Only deprecation warnings (httpx/starlette, pytest-playwright session fixtures).
- No screenshots were produced.

## Known limitations

- UI tests run against the real `employees.db` through the live server, using fixed
  emails. Re-runs are partly vacuous: duplicate emails return 409 and old rows are
  already visible.
- The cancel test never cleans up. Test rows (Jamie Taylor, Cancel Case) were left in
  the gitignored `employees.db`.
- In the cancel test, the check that the employee still exists runs immediately after
  the dialog is dismissed.
- CI (`.github/workflows`) runs only `tests/test_api.py`; UI tests are not in CI.
- Delete was not clicked manually in a browser during deployment checks.
