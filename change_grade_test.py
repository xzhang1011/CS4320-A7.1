import pytest
import System
import Staff

def test_change_grade(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    course = 'cloud_computing'
    assignment = 'assignment1'
    grade = '20'

    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.change_grade('yted91', 'software_engineering', 'assignment1', 10)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
