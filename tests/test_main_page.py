import pytest
import os
import os.path
from pages.main_page import MainPage
from constants import Urls
from constants import Upload


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = Urls.MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_page(self, browser):
        link = Urls.MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.signup_guest
class TestSignupFromMainPage:
    def test_guest_can_go_to_signup_page(self, browser):
        link = Urls.MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.go_to_signup_page()

    def test_guest_should_see_signup_page(self, browser):
        link = Urls.MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.should_be_signup_link()


@pytest.mark.upload_guest
class TestUploadFromMainPage:
    def test_guest_can_go_to_upload_popup(self, browser):
        link = Urls.MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.go_to_upload_popup()

    def test_guest_should_see_upload_links(self, browser):
        link = Urls.MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.should_be_upload_link()
        page.should_be_upload_home_buttons()

    def test_guest_can_add_file(self, browser):
        link = Urls.MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.go_to_upload_popup()
        files_name = "test.jpg"
        path = os.path.join(Upload.PATH_TO_FILES_FOLDER, files_name)
        page.add_file_from_pc(path)
        page.should_be_added_file()

    def test_guest_can_upload_file(self, browser):
        link = Urls.MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.go_to_upload_popup()
        files_name = "test.jpg"
        path = os.path.join(Upload.PATH_TO_FILES_FOLDER, files_name)
        page.add_file_from_pc(path)
        page.should_be_upload_button()
        page.upload_file_from_pc()
        page.should_be_disappear_upload_button()
        page.should_be_embed_codes()



