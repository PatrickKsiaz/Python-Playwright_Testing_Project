#Fixtures
import pytest


@pytest.fixture(scope="function") #@scope = module

def test_thirdCheck(preSetupWork):
    print("This is Third Test")







