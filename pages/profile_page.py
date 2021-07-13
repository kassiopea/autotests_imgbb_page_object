from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from constants import Auth
from pages.locators import ProfilePageLocators


def locator_uploaded_img(id_img):
    locator = (By.CSS_SELECTOR, f'[data-id="{id_img}"]')
    return locator


def button_delete_in_uploaded_img(id_img):
    button_locator = (By.CSS_SELECTOR, f'[data-id="{id_img}"] .tool-delete')
    return button_locator


class ProfilePage(BasePage):

    def is_element_in_list(self, list_elem, name, attribute):
        list_files = self.browser.find_elements(*list_elem)
        for i in list_files:
            if i.get_attribute(attribute) == name:
                return True

        return False

    def delete_all_files(self):
        img_files = ProfilePageLocators.LIST_ITEMS
        list_files = self.browser.find_elements(*img_files)
        for i in list_files:
            img_id = i.get_attribute('data-id')
            locator = locator_uploaded_img(img_id)
            button_locator = button_delete_in_uploaded_img(img_id)

            self.hover_on_elem_end_click_for_other(locator, button_locator)

            confirm_locator = ProfilePageLocators.CONFIRM_DELETIONS
            confirm = self.browser.find_element(*confirm_locator)
            confirm.click()
            self.is_disappeared(*locator, timeout=1)

    def profile_is_empty(self):
        assert self.is_element_present(*ProfilePageLocators.PROFILE_CONTENT_EMPTY), "Profile is not empty"

    def should_be_file_in_profile(self, filename):
        list_files = ProfilePageLocators.LIST_IMG
        assert self.is_element_in_list(list_files, filename, "alt")

    def should_be_profile_url(self):
        assert Auth.USERNAME in self.browser.current_url, "It is not profile url"

