# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing it. In this lab, Pylint checked code quality and maintainability, Bandit identified potentially insecure patterns, and Flake8 checked style and formatting.

## 2. What issues did the tools identify?

The initial reports identified unsafe SQL string construction, use of eval(), silent exception handling, missing documentation, inconsistent naming, long lines, trailing whitespace, and resource-handling issues. Bandit reported two medium-severity findings and one low-severity finding.

## 3. How were the issues addressed?

SQL statements were changed to use parameterized queries, eval() was removed in favor of a numeric salary limit, and silent exception handling was removed. The code was then improved with docstrings, snake_case function names, consistent return values, multiline SQL statements, and context-managed file handling.

## 4. How did static analysis improve the program?

The original Pylint score was 4.74/10. After the fixes, it reached 10.00/10. Bandit reported no remaining issues, and Flake8 produced no violations. The program also retained its expected demonstration output. These results showed how static analysis can help identify security risks, improve readability, and make code easier to maintain.
