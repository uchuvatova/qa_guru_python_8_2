from selene.support.shared import browser
from selene import be, have

def test_notsuccess_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yuyughfr').press_enter()
    (browser.element('[id="search"]')
    .should(be.visible)
    .should(have.text('Похоже, по вашему запросу нет полезных результатов')))

def test_success_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    (browser.element('[id="search"]')
    .should(be.visible)
    .should(have.text('yashaka/selene: User-oriented Web UI browser')))
