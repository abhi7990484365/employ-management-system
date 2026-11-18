# Implementation Plan - EMP-101

1. Create SQLite employee table.
2. Implement FastAPI CRUD/search endpoints.
3. Build browser UI.
4. Add pytest API tests and Playwright UI tests.
5. Run locally and document evidence.

## Delete confirmation story

`app/static/app.js` already calls `confirm("Delete this employee?")` before the
DELETE request, so no application code changed. Work done was test and tooling only:

- `tests/test_ui.py`: added `test_delete_cancelled_keeps_employee` and
  `test_delete_confirmed_removes_employee`.
- `pytest.ini`: rewritten (it contained literal `\n` text).
- `tests/conftest.py`: `gc.collect()` before `os.unlink` to avoid a Windows SQLite file lock.
