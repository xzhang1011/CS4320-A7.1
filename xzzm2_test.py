import pytest
import System

#takes a name and password and sets the user for the program
#verify that correct user is created by checking json files
def test_login(grading_system):
   username = 'hdjsr7'
   password = 'pass1234'
   grading_system.login(username,password)

#checks password is correct
def test_check_password(grading_system):
    username = 'hdjsr7'
    password = 'PASS1234'
    checkPass = grading_system.check_password(username, password)
    assert checkPass == False

#change the grade of student and updates json files
#verify correct grade is changed
def test_change_grade(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.change_grade('yted91', 'software_engineering', 'assignment1', 10)

#allows staff to create new assignment
#verify assignment created with correct due date in correct course in database
def test_create_assignment(grading_system):
    grading_system.login('sgoggins', 'augurrox')
    grading_system.usr.create_assignment('asdf')

#allows professor to add student to course
#verify student will be added to correct course in database
def test_add_student(grading_system):
    grading_system.login('sgoggins', 'augurrox')
    grading_system.usr.create_assignment('asdf')

def test_drop_student(grading_system):
    assert True

def test_submit_assignment(grading_system):
    assert True

def test_check_ontime(grading_system):
    assert True

def test_check_grades(grading_system):
    assert True

def test_view_assignments(grading_system):
    assert True

def test_check_username(grading_system):
    assert True

def test_check_professor_access(grading_system):
    assert True

def test_change_assignment_name(grading_system):
    assert True

def test_change_comment(grading_system):
    assert True

def test_change_assignment_date(grading_system):
    assert True

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

