#Fixtures
import pytest


@pytest.fixture(scope="module") #@scope = module
def preWork():
    print("I setup browser instance")
    return "pass"


def test_initialCheck(preWork):
    print("This is first test")
    assert preWork == "pass"


def test_initialCheck(preWork):
    print("This is second test")
    
