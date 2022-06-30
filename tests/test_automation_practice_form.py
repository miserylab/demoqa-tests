__author__ = 'miserylab'

import os

from selene import have, command
from selene.support.shared import browser



def test_student_registration_form():
    browser.open('/automation-practice-form')

    browser.element('.main-header').should(have.exact_text('Practice Form'))
    browser.element('#firstName').type('firstName')
    browser.element('#lastName').type('lastName')
    browser.element('#userEmail').type('test@test.com')
    browser.element("[for='gender-radio-2']").click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element("[value='8']").click()
    browser.element('.react-datepicker__year-select').click().element("[value='1973']").click()
    browser.element('.react-datepicker__day--013').click()
    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element('#subjectsInput').send_keys('S').hover()
    browser.element('#react-select-2-option-2').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../data/e85.jpg'))
    browser.element('#currentAddress').type('currentAddress')
    browser.element('#state').click()
    browser.element("#react-select-3-option-2").click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').perform(command.js.click)

    # asserts
    browser.elements('table tr').element(1).should(have.text('firstName lastName'))
    browser.elements('table tr').element(2).should(have.text('test@test.com'))
    browser.elements('table tr').element(3).should(have.text('Female'))
    browser.elements('table tr').element(4).should(have.text('1234567890'))
    browser.elements('table tr').element(5).should(have.text('13 September,1973'))
    browser.elements('table tr').element(6).should(have.text('Physics'))
    browser.elements('table tr').element(7).should(have.text('Reading, Music'))
    browser.elements('table tr').element(8).should(have.text('e85.jpg'))
    browser.elements('table tr').element(9).should(have.text('currentAddress'))
    browser.elements('table tr').element(10).should(have.text('Haryana Panipat'))

