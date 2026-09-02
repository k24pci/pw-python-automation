from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = self.page.get_by_placeholder("Your email")
        self.password_input = self.page.get_by_placeholder("Your password")
        self.login_btn = self.page.get_by_role("button", name="Login")

    def login_user(self, username, password):
        print("entering:" + username)
        self.type_text(self.email_input, username)
        self.type_text(self.password_input, password)
        self.login_btn.click()
