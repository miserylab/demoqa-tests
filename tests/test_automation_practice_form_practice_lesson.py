__author__ = 'miserylab'

from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser

from demoqa_tests.controls import dropdown, TagsInput, table
from demoqa_tests.path.path import data
from demoqa_tests.controls import tags_input



def test_student_registration_form():
    browser.open('/automation-practice-form')

    browser.element('.main-header').should(have.exact_text('Practice Form'))
    browser.element('#firstName').type('firstName')
    browser.element('#lastName').type('lastName')
    browser.element('#userEmail').type('test@test.com')
    browser.element("[for='gender-radio-2']").click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()

    # def select(element: Element, /, *, month: int, year: int, day: int):
    #     element.click()
    #     browser.element('.react-datepicker__month-select').click().element(month).click()
    #     browser.element('.react-datepicker__year-select').click().element(year).click()
    #     browser.element(f'.react-datepicker__day--{day}').click()
    #
    #
    # def set_value(element: Element, /, *, date: str):
    #     element.element('#dateOfBirthInput').perform(command.js.set_value(date))
    #
    # select(browser.element('#dateOfBirthInput'), 8, 1973, 13)
    # set_value(browser.element('#dateOfBirthInput'), '13 Sep 1973')


    browser.element('.react-datepicker__month-select').click().element("[value='8']").click()
    browser.element('.react-datepicker__year-select').click().element("[value='1973']").click()
    browser.element('.react-datepicker__day--013').click()

    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element("[for='hobbies-checkbox-3']").click()

    # browser.element('#subjectsInput').type(Subjects.computer_science)
    # browser.all('.subjects-auto-complete__option').element_by(have.text(Subjects.computer_science))
    # browser.element('#subjectsInput').type(Subjects.english)
    # browser.all('.subjects-auto-complete__option').element_by(have.text(Subjects.english))

    def autocomplete(selector: str, /, *, from_: str, to: str = None):
        browser.element(selector).type(from_).press_tab()
        browser.all('.subjects-auto-complete__option').element_by(have.exact_text(
            to if to is not None else from_))

    '''
       # OR:
        browser.all('.subjects-auto-complete__option').element_by(have.exact_text(
            to or from_
        ))
       # OR:
        browser.all('.subjects-auto-complete__option').element_by(have.exact_text(
            to if to else from_
        ))
       # OR:
        if to is not None:
            browser.all('.subjects-auto-complete__option').element_by(have.exact_text(to))
        else:
            browser.all('.subjects-auto-complete__option').element_by(have.exact_text(from_))
        '''

    subjects = TagsInput(browser.element('#subjectsInput'))

    subjects.add('Com', autocomplete='Computer Science')
    subjects.add('English')
    '''
    # OR:
    subjects = browser.element('#subjectsInput')
    tags_input.add(subjects, from_='Com', to=Subjects.computer_science)
    tags_input.add(subjects, from_=Subjects.english)
    '''

    # browser.element('#subjectsInput').send_keys('S').hover()

    # browser.element('#react-select-2-option-2').click()

    browser.element('#uploadPicture').send_keys(data('e85.jpg'))

    browser.element('#currentAddress').type('currentAddress')

    dropdown.select(browser.element('#state'), option='Haryana')
    dropdown.autocomplete(browser.element('#city'), option='Panipat')

    # browser.element('#state').perform(command.js.scroll_into_view).click()
    # browser.element("#react-select-3-option-2").click()
    # browser.element('#city').perform(command.js.scroll_into_view).click()
    # browser.element('#react-select-4-option-1').perform(command.js.click)

    browser.element('#submit').perform(command.js.click)

    # asserts
    table.cells_of_row(0).should(have.exact_texts('Student Name', 'firstName lastName'))
    table.cells_of_row(1).should(have.exact_texts('Student Email', 'test@test.com'))
    table.cells_of_row(2).should(have.exact_texts('Gender', 'Female'))
    table.cells_of_row(3).should(have.exact_texts('Mobile', '1234567890'))
    table.cells_of_row(4).should(have.exact_texts('Date of Birth', '13 September,1973'))
    table.cells_of_row(5).should(have.exact_texts('Subjects', 'Computer Science, English'))
    table.cells_of_row(6).should(have.exact_texts('Hobbies', 'Reading, Music'))
    table.cells_of_row(7).should(have.exact_texts('Picture', 'e85.jpg'))
    table.cells_of_row(8).should(have.exact_texts('Address', 'currentAddress'))
    table.cells_of_row(9).should(have.exact_texts('State and City', 'Haryana Panipat'))


# def select_by(selector: str, /, *, option: str):  # todo: consider option_text
#     select(browser.element(selector), option=option)
# browser.element(selector).perform(command.js.scroll_into_view).click()
# browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).perform(command.js.click)

def select_dropdown(selector: str, /, *, option: str):
    browser.element(selector).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).perform(command.js.click)


'''Основное задание

1. Применение инструментов Модульной Парадигмы

1.1. Вынести в отдельный модуль функцию-хелпер для трансформации пути к файлу с относительного в абсолютный, реализовав эту функцию, если это еще не сделано.



2. Применение инструментов Объектно-Ориентированной Парадигмы

2.1. Повторить показанное в уроке, создав PageObject для контрола типа «Tags Input». Добавить в "шаблон фабрики" оба способа работы с контролом – через автодополнение по Tab и выбор из списка предложенных вариантов.

2.2. Реализовать PageObject для контрола «Dropdown с автодополнением», с возможностью устанавливать значение для поля как через автодополнение по Tab, так и выбор из списка. 

2.3. Реализовать PageObject для контрола DatePicker с возможностью как установить значение в поле ввода явно, так и выбрать нужную дату из диалога дейтпикера.

2.4. Реализовать PageObject для контрола «Table», использующийся в тесте для проверки результата подтверждения формы.





Бонусное задание (сдавать в отдельной бренче)

1.2* Вместо PageObject реализовать в отдельном модуле функцию для работы с контролом «Tags Input», которая в зависимости от переданных именованых аргументов будет либо автодополнять введенный текст по Tab, либо выбирать по клику из предложенных в списке.'''
