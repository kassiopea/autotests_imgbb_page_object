from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def login_with_password(self, login, password):
        login_subject = self.browser.find_element(*LoginPageLocators.LOGIN_SUBJECT)
        login_subject.send_keys(login)
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(password)
        sign_in_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        sign_in_button.click()

    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It is not login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "no login form"


