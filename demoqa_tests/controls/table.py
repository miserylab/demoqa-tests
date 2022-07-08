__author__ = 'miserylab'

from selene.support.shared import browser


def cells_of_row(index):
    return browser.element(
        '.modal-content .table'
    ).all('tbody tr')[index].all('td')