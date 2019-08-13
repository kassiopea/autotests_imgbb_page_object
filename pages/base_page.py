from pages.locators import BasePageLocators
from pages.locators import UploadFilesLocators
from constants import Auth
from constants import Urls

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def add_file_from_pc(self, path):
        if self.is_element_present(*BasePageLocators.UPLOAD_INPUT_HIDDEN):
            self.browser.execute_script("document.getElementById('anywhere-upload-input')"
                                        ".classList.remove('hidden-visibility')")
        upload = self.browser.find_element(*BasePageLocators.UPLOAD_INPUT)
        upload.send_keys(path)

    def to_get_clickable_elem(self, how, what, timeout=4):
        return WebDriverWait(self.browser, timeout).until\
            (EC.element_to_be_clickable((how, what)))

    def close_popup(self):
        # self.should_be_disappear_message_window()
        close_popup = self.to_get_clickable_elem(*UploadFilesLocators.CLOSE_POPUP)
        close_popup.click()

    def close_popup_message(self):
        close_popup_message = self.browser.find_element(*BasePageLocators.POPUP_MESSAGE_CLOSE)
        close_popup_message.click()

    def is_disappeared(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_signup_page(self):
        link = self.browser.find_element(*BasePageLocators.SIGNUP_LINK)
        link.click()

    def go_to_upload_popup(self):
        link = self.browser.find_element(*BasePageLocators.UPLOAD_LINK)
        link.click()

    def logout(self):
        self.open_user_menu()
        sign_out = self.browser.find_element(*BasePageLocators.USER_MENU_SIGN_OUT)
        sign_out.click()

    def open(self):
        self.browser.get(self.url)

    def open_user_menu(self):
        user_menu = self.browser.find_element(*BasePageLocators.USER_MENU)
        user_menu.click()

    def should_be_added_file(self):
        assert self.is_element_present(*UploadFilesLocators.ADDED_FILE), "File is not added"

    def should_be_authorized_user(self):
        assert self.browser.find_element(*BasePageLocators.PROFILE_NAME).text == Auth.PROFILE_NAME, \
            "Profile name is not presented,probably unauthorised user"

    def should_be_disappear_upload_button(self):
        assert self.is_disappeared(*UploadFilesLocators.UPLOAD_BUTTON), "Upload button is not disappeared"

    def should_be_error_upload_message(self):
        assert self.is_element_present(*BasePageLocators.POPUP_MESSAGE), "The popup message error is not present"

    def should_be_error_upload_message_text(self):
        popup = self.browser.find_element(*BasePageLocators.POPUP_MESSAGE)
        assert popup.find_element_by_tag_name('h1').text == "Some files couldn't be added", "Is not error message"

    def should_be_language_menu(self):
        assert self.is_element_present(*BasePageLocators.LANGUAGE_MENU), "Language menu is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_main_page(self):
        assert Urls.MAIN_PAGE == self.browser.current_url, "It is not main url"

    def should_be_popup_open(self):
        assert self.is_element_present(*UploadFilesLocators.POPUP_OPEN), "Popup is not open"

    def should_be_signup_link(self):
        assert self.is_element_present(*BasePageLocators.SIGNUP_LINK), "Signup link is not presented"

    def should_be_upload_link(self):
        assert self.is_element_present(*BasePageLocators.UPLOAD_LINK), "Upload link is not presented"

    def should_be_upload_button(self):
        assert self.is_element_present(*UploadFilesLocators.UPLOAD_BUTTON), "Upload button is not present"

    def should_be_embed_codes(self):
        assert self.is_element_present(*UploadFilesLocators.EMBED_CODES_BLOCK), "Embed codes block is not present"

    def upload_file_from_pc(self):
        button = self.browser.find_element(*UploadFilesLocators.UPLOAD_BUTTON)
        button.click()

    def should_be_disappear_message_window(self):
        assert self.is_disappeared(*BasePageLocators.MODAL_WINDOW)


