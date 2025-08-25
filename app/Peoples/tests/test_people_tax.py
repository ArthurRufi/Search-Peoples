import pytest
from app.Peoples.domain.contracts.peoples import People

# python -m pytest -v


def test_person_exists_is_true():
    person = People("Alice", 30, "Wonderland", "padaraia@gmail.com", "123456789")
    assert person.exists() is True

def test_person_exists_is_false():
    person = People("", 30, "Wonderland", "", "123456789")
    assert person.exists() is False

def test_sucess_rate_all_params_account_is_valid():
    person = People("Alice", 30, "Wonderland", "padaraia@gmail.com", "123456789")
    if person.success_rate(1, 1, 1, 2) == 1.25:
        assert True
    else:
        assert False
    