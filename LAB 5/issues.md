# Lab 5: Static Code Analysis — Issue Log

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| SQL injection risk (B608) | Security | 8 | Applicant values were interpolated directly into SQL. | Replaced interpolation with parameterized SQL. |
| Unsafe eval (B307) | Security | 14 | eval() could execute arbitrary Python expressions. | Replaced expression evaluation with a numeric salary limit. |
| Silent exception (B110) | Reliability | 28–29 | Exceptions were swallowed without reporting failures. | Removed the broad exception handler and pass statement. |
| Unused variable (F841) | Code quality | 15 | total_seen was assigned but never used. | Removed the unnecessary variable. |
| Long lines (C0301/E501) | Style | 4, 8, 13, 26, 39 | Several lines exceeded the configured length limits. | Reformatted SQL and expressions across multiple lines. |
| Missing docstrings (C0114/C0116) | Maintainability | Multiple | The module and functions lacked documentation. | Added module and function docstrings. |
| Invalid function names (C0103) | Style | 7, 24, 31, 38 | Function names used camelCase. | Renamed functions to snake_case and updated calls. |
| Broad exception (W0718) | Reliability | 28 | Exception handling caught unrelated errors. | Removed the unnecessary catch-all handler. |
| Resource handling (R1732) | Maintainability | 32–35 | The exported report file was opened and closed manually. | Used a with statement and UTF-8 encoding. |
| Inconsistent returns (R1710) | Code quality | 12–21 | shortlist() could return None when no applicants matched. | Made shortlist() always return a list. |
