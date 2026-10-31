
import pytest

from library_fines import late_fine, can_borrow, renewal_status


# Tests for late_fine()

def test_unknown_member():
    with pytest.raises(ValueError, match="unknown member"):
        late_fine("visitor", 20, False)


def test_negative_days():
    with pytest.raises(ValueError, match="invalid days"):
        late_fine("student", -1, False)


def test_student_no_overdue():
    assert late_fine("student", 10, False) == 0


def test_student_overdue():
    assert late_fine("student", 20, False) == 12


def test_faculty_overdue():
    assert late_fine("faculty", 35, False) == 5


def test_guest_overdue():
    assert late_fine("guest", 16, False) == 10


def test_fine_cap():
    assert late_fine("student", 200, False) == 200


def test_damaged_book():
    assert late_fine("student", 10, True) == 150


def test_overdue_and_damaged():
    assert late_fine("student", 20, True) == 162


# Tests for can_borrow()

def test_pending_fine_above_limit():
    assert can_borrow(1, 101, "student") is False


def test_faculty_can_borrow():
    assert can_borrow(5, 0, "faculty") is True


def test_faculty_at_limit():
    assert can_borrow(10, 0, "faculty") is False


def test_student_at_limit():
    assert can_borrow(3, 0, "student") is False


# Tests for renewal_status()

def test_renewal_with_reservation():
    assert renewal_status(0, True, 5) == "denied"


def test_renewal_limit_reached():
    assert renewal_status(2, False, 5) == "limit reached"


def test_overdue_renewal():
    assert renewal_status(1, False, -1) == "overdue"


def test_successful_renewal():
    assert renewal_status(1, False, 5) == "renewed"
