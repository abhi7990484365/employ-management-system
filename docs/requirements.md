# Requirements - EMP-101

- Create, list, update and delete employees.
- Search employees by name.
- Validate required fields and email format.
- Reject duplicate email addresses.
- Persist data in SQLite.
- Delete confirmation: the UI asks "Delete this employee?" before sending
  `DELETE /api/employees/{id}`. Cancelling keeps the employee; confirming removes it.
