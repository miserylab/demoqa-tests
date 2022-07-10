__author__ = 'miserylab'

from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

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

    # date.select(13, 9, 1973)
    date.set_value('13 Sep 1973')

    subjects = TagsInput(browser.element('#subjectsInput'))

    subjects.add('Com', autocomplete='Computer Science')
    subjects.add('English')
    '''
    # OR:
    subjects = browser.element('#subjectsInput')
    tags_input.add(subjects, from_='Com', to=Subjects.computer_science)
    tags_input.add(subjects, from_=Subjects.english)
    '''


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
    table = Table(browser.element('.table'))
    table.cell(0, 1).should(have.exact_text('firstName lastName'))
    # table.cells_of_row(1, 2).should(have.exact_texts('Student Name', 'firstName lastName'))
    # table.cells_of_row(1, 2).should(have.exact_texts('Student Name', 'firstName lastName'))
    # browser.element('table tbody tr:nth-child(1) td:nth-child(2)').should(have.exact_text('firstName lastName'))
    table.cell(1, 1).should(have.exact_text('test@test.com'))
    table.cell(2, 1).should(have.exact_text('Female'))
    table.cell(3, 1).should(have.exact_text('1234567890'))
    table.cell(4, 1).should(have.exact_text('13 September,1973'))
    table.cell(5, 1).should(have.exact_text('Computer Science, English'))
    table.cell(6, 1).should(have.exact_text('Reading, Music'))
    table.cell(7, 1).should(have.exact_text('e85.jpg'))
    table.cell(8, 1).should(have.exact_text('currentAddress'))
    table.cell(9, 1).should(have.exact_text('Haryana Panipat'))
    # table.cells_of_row(2, 2).should(have.exact_texts('Student Email', 'test@test.com'))
    # table.cells_of_row(2).should(have.exact_texts('Gender', 'Female'))
    # table.cells_of_row(3).should(have.exact_texts('Mobile', '1234567890'))
    # table.cells_of_row(4).should(have.exact_texts('date of Birth', '13 September,1973'))
    # table.cells_of_row(5).should(have.exact_texts('Subjects', 'Computer Science, English'))
    # table.cells_of_row(6).should(have.exact_texts('Hobbies', 'Reading, Music'))
    # table.cells_of_row(7).should(have.exact_texts('Picture', 'e85.jpg'))
    # table.cells_of_row(8).should(have.exact_texts('Address', 'currentAddress'))
    # table.cells_of_row(9).should(have.exact_texts('State and City', 'Haryana Panipat'))


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
