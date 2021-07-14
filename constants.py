import os


class Auth:
    EMAIL = "randomnanastya@gmail.com"
    USERNAME = "randomnanastya"
    PASSWORD = "123456"
    PROFILE_NAME = "Anastasia Salikova"


class Urls:
    MAIN_PAGE = "https://imgbb.com/"
    LOGIN_PAGE = "https://imgbb.com/login/"
    LOGOUT_PAGE = "https://imgbb.com/logout"


class Upload:
    PATH_TO_FILES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./files/")
