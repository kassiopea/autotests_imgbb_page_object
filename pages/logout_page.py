from pages.base_page import BasePage
from constants import Urls


class LogoutPage(BasePage):
    def should_be_logout_link(self):
        assert Urls.LOGOUT_PAGE == self.browser.current_url, "The page is not logout page"

