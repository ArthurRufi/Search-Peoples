import pytest
from app.Peoples.domain.contracts.infosmath import DeltaInfo

def test_delta_calculation_social_returns_fail_negative_one():
    Infos = DeltaInfo(5)
    assert Infos.delta_social() == -1.0

def test_delta_calc_social_returns_number_correctly():
    Infos = DeltaInfo(2)
    assert Infos.delta_social() == 0.5

def test_delta_calc_social_returns_number_correctly_lower_bound():
    Infos = DeltaInfo(1)
    assert Infos.delta_social() == 0.25