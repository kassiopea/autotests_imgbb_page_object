from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):

    def should_be_upload_home_buttons(self):
        assert self.is_element_present(*MainPageLocators.UPLOAD_BUTTON), "Upload button is not presented"