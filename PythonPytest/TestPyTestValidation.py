#Fixtures
import pytest


@pytest.fixture(scope="module") #@scope = module
def preWork():
    print("I setup browser instance")
    return "pass"

@pytest.fixture(scope="module") #@scope = module
def secondWork():
    print("I setup module instance")
    yield
    print("tear down validation")


def test_initialCheck(preWork,secondWork):
    print("This is first test")
    assert preWork == "fail"


def test_initialCheck(preWork, secondWork):
    print("This is second test")

