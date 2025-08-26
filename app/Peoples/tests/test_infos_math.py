import pytest
from app.Peoples.domain.contracts.infosmath import DeltaInfo

def test_delta_calculation_social_returns_fail_negative_one():
    Infos = DeltaInfo(5)
    assert Infos.delta_social() == -1.0