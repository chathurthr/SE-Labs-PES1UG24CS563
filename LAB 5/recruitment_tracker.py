
"""A simple SQLite-based recruitment tracking application."""

import sqlite3

conn = sqlite3.connect(":memory:")

conn.execute(
    """
    CREATE TABLE applicants (
        id INTEGER PRIMARY KEY,
        name TEXT,
        role TEXT,
        expected_salary INTEGER,
        status TEXT
    )
    """
)


def add_applicant(name, role, expected_salary, status="applied"):
    """Add a new applicant to the database."""
    conn.execute(
        """
        INSERT INTO applicants (name, role, expected_salary, status)
        VALUES (?, ?, ?, ?)
        """,
        (name, role, expected_salary, status),
    )
    conn.commit()


def shortlist(role, salary_limit):
    """Return applicants matching a role and salary limit."""
    rows = conn.execute(
        """
        SELECT name, expected_salary
        FROM applicants
        WHERE role = ?
        """,
        (role,),
    ).fetchall()

    return [
        name
        for name, salary in rows
        if salary <= salary_limit
    ]


def update_status(applicant_id, status):
    """Update an applicant's recruitment status."""
    conn.execute(
        "UPDATE applicants SET status = ? WHERE id = ?",
        (status, applicant_id),
    )
    conn.commit()


def export_report(path):
    """Export applicant names, roles, and statuses to a file."""
    with open(path, "w", encoding="utf-8") as report_file:
        rows = conn.execute(
            "SELECT name, role, status FROM applicants"
        )
        for row in rows:
            report_file.write(",".join(row) + "\n")


def count_by_status(status):
    """Count applicants with a specified recruitment status."""
    result = conn.execute(
        "SELECT COUNT(*) FROM applicants WHERE status = ?",
        (status,),
    )
    return result.fetchone()[0]


def main():
    """Run the recruitment tracker demonstration."""
    add_applicant("Nina", "analyst", 600000)
    add_applicant("Omar", "analyst", 750000, "interview")
    add_applicant("Priya", "developer", 900000)
    update_status(1, "interview")
    print(shortlist("analyst", 650000))
    export_report("applicants_report.csv")
    print(count_by_status("interview"), "in interview")


if __name__ == "__main__":
    main()
