from selene import have, be
from selene.support.shared import browser


def test_submit_form():
    browser.open('/text-box')
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(have.exact_text('Text Box'))
    browser.element('#userName').type('qqqq')
    browser.element('#userEmail').type('test@test.com')
    browser.element('#currentAddress').type('Earth')
    browser.element('#permanentAddress').type('Universe')
    browser.element('#submit').click()

    # TODO: finish implementation