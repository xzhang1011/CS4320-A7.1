import pytest
import System

# checks if password correct
def check_password(grading_system):
    username = 'hdjsr7'
    password = 'PASS1234'
    grading_system.check_password(username, password)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
