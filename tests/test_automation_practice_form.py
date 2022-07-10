__author__ = 'miserylab'

from selene import have, command
from selene.support.shared import browser

from demoqa_tests.controls import dropdown, TagsInput
from demoqa_tests.controls.datepicker import DatePicker
from demoqa_tests.controls.table import Table
from demoqa_tests.path.path import data


def test_student_registration_form():
    browser.open('/automation-practice-form')

    browser.element('.main-header').should(have.exact_text('Practice Form'))
    browser.element('#firstName').type('firstName')
    browser.element('#lastName').type('lastName')
    browser.element('#userEmail').type('test@test.com')
    browser.element("[for='gender-radio-2']").click()
    browser.element('#userNumber').type('1234567890')

    date = DatePicker(browser.element('#dateOfBirthInput'))

    date.select(13, 9, 1973)
    '''
    # OR:
    date.set_value('13 Sep 1973')
    '''

    subjects = TagsInput(browser.element('#subjectsInput'))

    subjects.add('Com', autocomplete='Computer Science')
    subjects.add('English')

    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element("[for='hobbies-checkbox-3']").click()

    browser.element('#uploadPicture').send_keys(data('e85.jpg'))

    browser.element('#currentAddress').type('currentAddress')

    dropdown.select(browser.element('#state'), option='Haryana')
    dropdown.autocomplete(browser.element('#city'), option='Panipat')

    browser.element('#submit').perform(command.js.click)

    # asserts
    table = Table(browser.element('.table'))
    table.cell(0, 1).should(have.exact_text('firstName lastName'))
    table.cell(1, 1).should(have.exact_text('test@test.com'))
    table.cell(2, 1).should(have.exact_text('Female'))
    table.cell(3, 1).should(have.exact_text('1234567890'))
    table.cell(4, 1).should(have.exact_text('13 September,1973'))
    table.cell(5, 1).should(have.exact_text('Computer Science, English'))
    table.cell(6, 1).should(have.exact_text('Reading, Music'))
    table.cell(7, 1).should(have.exact_text('e85.jpg'))
    table.cell(8, 1).should(have.exact_text('currentAddress'))
    table.cell(9, 1).should(have.exact_text('Haryana Panipat'))
