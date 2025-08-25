import pytest
from app.Peoples.domain.contracts.peoples import People

# python -m pytest -v


def test_person_exists_is_true():
    person = People("Alice", 30, "Wonderland", "padaraia@gmail.com", "123456789")
    assert person.exists() is True