#Fixtures
import pytest


@pytest.fixture(scope="function") #@scope = module

def test_thirdCheck(preSetupWork):
    print("This is Third Test")

@pytest.fixture(scope="module") #@scope = module
def preWork():
    print("I setup browser instance")
    return "pass"


@pytest.mark.smoke
def test_thirdCheck(preSetupWork):
    print("This is Thire test")






