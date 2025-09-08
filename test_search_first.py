from selene import browser, be, have

fakeRequest = "####!!@#!"

def test_search_negative(size_browser):
    browser.open("https://duckduckgo.com/")
    browser.element('[id="searchbox_input"]').should(be.blank).type(fakeRequest).press_enter()
    browser.element('//span[contains(text(), "ничего не найдено")]')



