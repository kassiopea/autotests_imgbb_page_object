import pytest
import os
from constants import Urls
from constants import Auth
from constants import Upload
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.logout_page import LogoutPage


def replace_name(file):
    name = str(file)
    name = name.replace("_", "-")
    if name[-4:] == "webp":
        return name.replace(".webp", ".png")
    elif name[-3:] == "bmp":
        return name.replace(".bmp", ".png")
    elif name[-3:] == "tif":
        return name.replace(".tif", ".png")
    return name


@pytest.mark.guest_in_profile_user
def test_redirection_guest_to_login_page(browser):
    link = "https://{}.imgbb.com/".format(Auth.USERNAME)
    page = ProfilePage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.autorizated_user
class TestUserUploadFile(object):

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        link = Urls.LOGIN_PAGE
        page = LoginPage(browser, link)
        page.open()
        page.login_with_password(Auth.USERNAME, Auth.PASSWORD)
        page.should_be_authorized_user()
        page = ProfilePage(browser, browser.current_url)
        page.should_be_profile_url()

    def test_upload_file_from_profile_page(self, browser):
        link = "https://{}.imgbb.com/".format(Auth.USERNAME)
        page = ProfilePage(browser, link)
        page.open()
        files_name = "test.jpg"
        path = os.path.join(Upload.PATH_TO_FILES_FOLDER, files_name)
        page.add_file_from_pc(path)
        page.upload_file_from_pc()
        page.should_be_embed_codes()
        page.should_be_profile_url()
        page.close_popup()

    def test_upload_file_with_avaliable_formats(self, browser, data_files):
        link = "https://{}.imgbb.com/".format(Auth.USERNAME)
        page = ProfilePage(browser, link)
        page.open()
        files_name = data_files
        path = os.path.join(Upload.PATH_TO_FILES_FOLDER, files_name)
        page.add_file_from_pc(path)
        page.upload_file_from_pc()
        page.should_be_embed_codes()
        page.should_be_profile_url()
        page.close_popup()
        browser.refresh()
        name = replace_name(files_name)
        page.should_be_file_in_profile(name)

    def test_upload_invalid_file_formats(self, browser, data_invalid_files):
        link = "https://{}.imgbb.com/".format(Auth.USERNAME)
        page = ProfilePage(browser, link)
        page.open()
        files_name = data_invalid_files
        path = os.path.join(Upload.PATH_TO_FILES_FOLDER, files_name)
        page.add_file_from_pc(path)
        page.should_be_error_upload_message()
        page.should_be_error_upload_message_text()
        page.close_popup_message()
        page.should_be_disappear_message_window()
        page.should_be_popup_open()
        page.close_popup()

    def logout(self, browser):
        link = browser.current_url
        page = BasePage(browser, link)
        page.logout()
        logout_page = LogoutPage(browser, browser.current_url)
        logout_page.should_be_logout_link()
