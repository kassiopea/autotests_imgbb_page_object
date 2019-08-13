from pages.base_page import BasePage
from constants import Auth
from pages.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def should_be_profile_url(self):
        assert Auth.USERNAME in self.browser.current_url, "It is not profile url"

    def should_be_file_in_profile(self, filename):
        list_files = ProfilePageLocators.LIST_IMG
        assert self.is_element_in_list(list_files, filename, "alt")

    def is_element_in_list(self, list_elem, name, attribute):
        list_files = self.browser.find_elements(*list_elem)
        for i in list_files:
            if i.get_attribute(attribute) == name:
                return True

        return False



