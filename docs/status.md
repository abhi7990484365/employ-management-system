# Status - Delete confirmation (EMP-101)

Branch: Initial-employee-management-system. Review: APPROVE with follow-ups.

## Deployment (local only)
No Dockerfile or build step. Install with `pip install -r requirements.txt`, then
`python -m uvicorn app.main:app --host 127.0.0.1 --port 8000`. Smoke check: `/` 200,
`/docs` 200, `/api/employees` returned data, `/static/app.js` served the delete
confirm handler. The server was stopped afterwards.

## Follow-ups
- Medium: isolate UI tests from the real `employees.db` (temp DB, unique emails, cleanup);
  run UI tests in CI.
- Low: wait/poll in the cancel test instead of asserting immediately.
- Low: `app/database.py` does not close SQLite connections; `gc.collect()` in
  `tests/conftest.py` is a workaround.
- Info: `.claude/` and `.codemie/` are untracked. API authentication was not reviewed.
- The Confluence design page was not verified against these changes.
