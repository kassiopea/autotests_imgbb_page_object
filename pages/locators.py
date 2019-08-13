from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#top-bar-signin a")
    SIGNUP_LINK = (By.CSS_SELECTOR, "#top-bar-signup a")
    UPLOAD_LINK = (By.CSS_SELECTOR, "li[data-action='top-bar-upload']")
    LANGUAGE_MENU = (By.CSS_SELECTOR, "li[data-nav='language']")
    ABOUT_MENU = (By.CSS_SELECTOR, "li[data-nav='about']")
    UPLOAD_INPUT = (By.CSS_SELECTOR, "input#anywhere-upload-input")
    UPLOAD_INPUT_HIDDEN = (By.CSS_SELECTOR, "#anywhere-upload-input.hidden-visibility")
    PROFILE_NAME = (By.CSS_SELECTOR, "#top-bar-user span.text")

    USER_MENU = (By.CSS_SELECTOR, "#top-bar-user")
    USER_MENU_SIGN_OUT = (By.CSS_SELECTOR, ".pop-box-inner a[href='https://imgbb.com/logout']")

    POPUP_MESSAGE = (By.CSS_SELECTOR, "#fullscreen-modal-box")
    POPUP_MESSAGE_CLOSE = (By.CSS_SELECTOR, "#fullscreen-modal-box .close-modal")

    MODAL_WINDOW = (By.CSS_SELECTOR, "#fullscreen-modal")


class MainPageLocators(object):
    UPLOAD_BUTTON = (By.CSS_SELECTOR, ".home-buttons a[data-trigger='anywhere-upload-input']")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, ".form-content form")
    LOGIN_SUBJECT = (By.ID, "login-subject")
    LOGIN_PASSWORD = (By.ID, "login-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")


class UploadFilesLocators(object):
    ADDED_FILE = (By.CSS_SELECTOR, "#anywhere-upload-queue .queue-item")
    UPLOAD_BUTTON = (By.CSS_SELECTOR, "#anywhere-upload-submit button[data-action='upload']")
    EMBED_CODES_BLOCK = (By.CSS_SELECTOR, "#uploaded-embed-toggle-combo")
    POPUP_OPEN = (By.CSS_SELECTOR, ".upload-box--show")
    CLOSE_POPUP = (By.CSS_SELECTOR, "#anywhere-upload a[data-action='close-upload']")


class ProfilePageLocators(object):
    LIST_IMG = (By.CSS_SELECTOR, "#list-most-recent img")


class LogoutPageLocators(object):
    pass