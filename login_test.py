import pytest
import System

def test_login(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    grading_system.login(username,password)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
