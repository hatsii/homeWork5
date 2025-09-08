from selene import browser, be, have


def test_search_positive(size_browser):
    browser.open('https://duckduckgo.com/')
    browser.element('[id="searchbox_input"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('//span[contains(text(), "qa guru")]')

