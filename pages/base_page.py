from playwright.async_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def type_text(self, locator, text):
        locator.click()
        locator.clear()
        self.page.keyboard.type(text)

    def get_text(self, locator, expected_text):
        expect(locator).to.equal(expected_text)

    def select_dropdown_option(self, dropdown_locator, dropdown_option):
        dropdown_locator.select_option(dropdown_option)

    def get_element_count(self, locator):
        count = locator.count()
        return count
