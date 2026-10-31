
import pytest

from library_fines import late_fine, can_borrow, renewal_status


# late_fine() - Member validation

def test_unknown_member():
    with pytest.raises(ValueError):
        late_fine("visitor", 10, False)


def test_valid_member():
    assert late_fine("student", 10, False) == 0


# late_fine() - Days validation

def test_negative_days():
    with pytest.raises(ValueError):
        late_fine("student", -1, False)


def test_valid_days():
    assert late_fine("student", 10, False) == 0


# late_fine() - Faculty and non-faculty

def test_faculty_member():
    assert late_fine("faculty", 35, False) == 5


def test_non_faculty_member():
    assert late_fine("student", 20, False) == 12


# late_fine() - Overdue and not overdue

def test_overdue_book():
    assert late_fine("student", 20, False) == 12


def test_not_overdue_book():
    assert late_fine("student", 10, False) == 0


# late_fine() - Fine cap

def test_fine_exceeds_limit():
    assert late_fine("student", 200, False) == 200


def test_fine_below_limit():
    assert late_fine("student", 20, False) == 12


# late_fine() - Damaged and undamaged books

def test_damaged_book():
    assert late_fine("student", 10, True) == 150


def test_undamaged_book():
    assert late_fine("student", 10, False) == 0


# can_borrow() - Pending fine

def test_pending_fine_exceeds_limit():
    assert can_borrow(1, 101, "student") is False


def test_pending_fine_within_limit():
    assert can_borrow(1, 50, "student") is True


# can_borrow() - Faculty conditions

def test_faculty_within_book_limit():
    assert can_borrow(5, 0, "faculty") is True


def test_faculty_at_book_limit():
    assert can_borrow(10, 0, "faculty") is False


# can_borrow() - Student conditions

def test_student_within_book_limit():
    assert can_borrow(2, 0, "student") is True


def test_student_at_book_limit():
    assert can_borrow(3, 0, "student") is False


# renewal_status() - Reservation condition

def test_has_reservation():
    assert renewal_status(0, True, 5) == "denied"


def test_no_reservation():
    assert renewal_status(0, False, 5) == "renewed"


# renewal_status() - Renewal limit

def test_renewal_limit_reached():
    assert renewal_status(2, False, 5) == "limit reached"


def test_renewal_limit_not_reached():
    assert renewal_status(1, False, 5) == "renewed"


# renewal_status() - Overdue condition

def test_book_is_overdue():
    assert renewal_status(1, False, -1) == "overdue"


def test_book_is_not_overdue():
    assert renewal_status(1, False, 5) == "renewed"
