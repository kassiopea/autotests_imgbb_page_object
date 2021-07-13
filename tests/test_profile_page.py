import pytest
import os
from constants import Auth
from constants import Upload
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


def replace_name(file):
    name = str(file)
    name = name.replace("_", "-")
    if name[-3:] == "bmp":
        return name.replace(".bmp", ".png")
    elif name[-3:] == "tif":
        return name.replace(".tif", ".png")
    return name


@pytest.mark.guest_in_profile_user
class TestGuestRedirectToLogin(object):
    def test_redirection_guest_to_login_page(self, browser):
        link = "https://{}.imgbb.com/".format(Auth.USERNAME)
        page = ProfilePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.autorizated_user
class TestUserUploadFile(object):
    def test_upload_file_from_profile_page(self, browser, setup):
        link = "https://{}.imgbb.com/".format(Auth.USERNAME)
        page = ProfilePage(browser, link)
        page.open()
        files_name = "test.jpg"
        path = os.path.join(Upload.PATH_TO_FILES_FOLDER, files_name)
        page.add_file_from_pc(path)
        page.should_be_upload_button()
        page.upload_file_from_pc()
        page.should_be_embed_codes()
        page.should_be_profile_url()

    def test_upload_file_with_valid_formats(self, browser, data_files, setup):
        link = "https://{}.imgbb.com/".format(Auth.USERNAME)
        page = ProfilePage(browser, link)
        page.open()
        files_name = data_files
        path = os.path.join(Upload.PATH_TO_FILES_FOLDER, files_name)
        page.add_file_from_pc(path)
        page.should_be_upload_button()
        page.upload_file_from_pc()
        page.should_be_embed_codes()
        page.should_be_profile_url()
        browser.refresh()
        name = replace_name(files_name)
        page.should_be_file_in_profile(name)

    def test_upload_invalid_file_formats(self, browser, data_invalid_files, setup):
        link = "https://{}.imgbb.com/".format(Auth.USERNAME)
        page = ProfilePage(browser, link)
        page.open()
        files_name = data_invalid_files
        path = os.path.join(Upload.PATH_TO_FILES_FOLDER, files_name)
        page.add_file_from_pc(path)
        page.should_be_popup_with_error_message()
        page.should_be_text_error_upload_message()
        page.close_popup_message()
        page.should_be_disappear_popup_with_error_upload_message()
        page.should_be_popup_open()
