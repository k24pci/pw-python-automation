from pages.base_page import BasePage


class Homepage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        # Locator by classname
        self.__get_btn_card = self.page.get_by_test_id(
            "product-01M14E5MVW80B74TPX1CZW8BNV"
        )
        self.get_filters_container = self.page.locator("#filters")


# Combination Pliers
