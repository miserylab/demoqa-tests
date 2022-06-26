__author__ = 'miserylab'

from selene import have
from selene.support.shared import browser

first_name = 'firstName'
last_name = 'lastName'
email = 'test@test.com'
age = 50
salary = 500
department = 'Test department'


def test_add_forth_entry():
    browser.open('/webtables')

    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type('firstName')
    browser.element('#lastName').type('lastName')
    browser.element('#userEmail').type('test@test.com')
    browser.element('#age').type('50')
    browser.element('#salary').type('500')
    browser.element('#department').type('Test department')
    browser.element('#submit').click()

    # browser.elements('.ReactTable .rt-table .rt-tbody .rt-tr').element(2).should(have.texts('firstName', 'lastName', 'test@test.com', 50, 500, 'Test department'))

    pass


def update_second_entry():

    pass


def delete_third_entry():

    pass
