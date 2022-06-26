__author__ = 'miserylab'

from selene import have
from selene.support.shared import browser

first_name = 'firstName'
last_name = 'lastName'
email = 'test@test.com'
# gender = 'Female'
mobile = '1234567890'
# date_of_birth = '13 September,1973'
# subjects = 'Physics'
# hobbies = 'Reading, Music'
address = 'currentAddress'
# state = "Haryana"
# city = "Panipat"

file_path = r"C:\Users\miser\PycharmProjects\demoqa-tests\data\e85.jpg"


def test_student_registration_form():
    browser.open('/automation-practice-form')

    browser.element('.main-header').should(have.exact_text('Practice Form'))
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)
    browser.element("[for='gender-radio-2']").click()
    browser.element('#userNumber').type(mobile)

    # Date of Birth picker
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element("[value='8']").click()
    browser.element('.react-datepicker__year-select').click().element("[value='1973']").click()
    browser.element('.react-datepicker__day--013').click()

    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element("[for='hobbies-checkbox-3']").click()

    browser.element('#subjectsInput').send_keys('S').hover()
    browser.element('#react-select-2-option-2').click()

    # Picture selector
    browser.element("#uploadPicture").send_keys(file_path)

    browser.element('#currentAddress').type(address)

    # State and City picker
    browser.element('#state').click()
    browser.element("#react-select-3-option-2").click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()

    browser.element('#submit').click()

    # assertions

    browser.all('table tbody tr td:nth-child(2)').should(have.exact_texts(
        'firstName lastName',
        'test@test.com',
        'Female',
        '1234567890',
        '13 September,1973',
        'Physics',
        'Reading, Music',
        'e85.jpg',
        'currentAddress',
        'Haryana Panipat'
    ))
