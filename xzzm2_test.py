import pytest
import System

#takes a name and password and sets the user for the program
#verify that correct user is created by checking json files
#PASS
def test_login(grading_system):
   username = 'hdjsr7'
   password = 'pass1234'
   grading_system.login(username,password)
   assert username in grading_system.users
   grading_system.reload_data()

#checks password is correct
#FAIL
def test_check_password(grading_system):
    username = 'hdjsr7'
    password = 'PASS1234'
    password2 = 'PaSs1234'
    checkPass = grading_system.check_password(username, password)
    checkPass2 = grading_system.check_password(username, password)
    assert checkPass == True and checkPass2 == True
    grading_system.reload_data()

#change the grade of student and updates json files
#verify correct grade is changed
#FAIL
def test_change_grade(grading_system):
    studentUser = 'yted91'
    course = 'software_engineering'
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.change_grade(studentUser, course, 'assignment1', 10)
    assert grading_system.users[studentUser]['courses'][course]['assignment1']['grade'] == 10
    grading_system.reload_data()

#allows staff to create new assignment
#verify assignment created with correct due date in correct course in database
#PASS
def test_create_assignment(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.create_assignment('assignment4', '04/01/20', 'software_engineering')
    assert 'assignment4' in grading_system.courses['software_engineering']['assignments']
    grading_system.reload_data()

#allows professor to add student to course
#verify student will be added to correct course in database
#PASS
def test_add_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.add_student('akend3', 'software_engineering')
    assert 'software_engineering' in grading_system.users['akend3']['courses']
    grading_system.reload_data()

#allows professor to drop student in course
#verify student is dropped from correct course in database
#FAIL
def test_drop_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.drop_student('akend3', 'software_engineering')
    assert 'software_engineering' not in grading_system.users['akend3']['courses']
    grading_system.reload_data()

#allows student to submit assignment
#verify database updated with correct assignment, submission, data, and course
#FAIL
def test_submit_assignment(grading_system):
    course = 'comp_sci'
    assignment = 'assignment1'
    comment = 'blahblah'
    date = '03/01/20'
    grading_system.login('akend3', '123454321')
    grading_system.usr.submit_assignment(course, assignment, comment, date)
    assert assignment and comment and date in grading_system.users['akend3'][course]
    grading_system.reload_data()

#checks if assignment submitted on time
#verify true if assignment on time, and false if assignment late
#PASS
def test_check_ontime(grading_system):
    grading_system.login('akend3', '123454321')
    assert grading_system.usr.check_ontime('2/1/20', '2/2/20') == True
    grading_system.reload_data()

#returns users grades for specific course
#verify correct grades returned for correct user
#PASS
def test_check_grades(grading_system):
    grading_system.login('akend3', '123454321')
    grades = grading_system.usr.check_grades('comp_sci')
    print(grades)
    assert True

#returns assignments and due dates for a specific course
#verify correct assignments displayed
#PASS
def test_view_assignments(grading_system):
    grading_system.login('akend3', '123454321')
    assignments = grading_system.usr.view_assignments('comp_sci')
    print(assignments)
    assert True


### my tests ###

#check username is in database
def test_check_username(grading_system):
    assert grading_system.login('akend2', 'fake') in grading_system.users

#check professor isn't able to change grade in course that they're not assigned to
def test_check_grade_access(grading_system):
     grading_system.login('saab', 'boomr345')
     grading_system.usr.add_student('akend3', 'databases')
     assert 'cloud_computing' not in grading_system.users['akend3']['courses']
     grading_system.reload_data()

#check professor creating assignment is professor of course
#verify assignment isn't changed if professor is not assigned to course
def test_check_assignment_access(grading_system):
    grading_system.login('saab', 'boomr345')
    grading_system.usr.create_assignment('assignment5', '04/01/20', 'software_engineering')
    assert 'assignment5' not in grading_system.courses['software_engineering']['assignments']
    grading_system.reload_data()

#check professor can't submit assignment
#verify assignment isn't submitted
def test_check_professor_submit(grading_system):
    course = 'comp_sci'
    assignment = 'assignment1'
    comment = 'blahblah'
    date = '03/01/20'
    grading_system.login('saab', 'boomr345')
    grading_system.usr.submit_assignment(course, assignment, comment, date)
    assert assignment and comment and date not in grading_system.users['saab']['courses']
    grading_system.reload_data()

#check professor dropping student is professor of course
#verify student is not dropped if professor not assigned to course
def test_check_student_drop(grading_system):
    grading_system.login('saab', 'boomr345')
    grading_system.usr.drop_student('akend3', 'databases')
    assert 'databases' in grading_system.users['akend3']['courses']
    grading_system.reload_data()

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

