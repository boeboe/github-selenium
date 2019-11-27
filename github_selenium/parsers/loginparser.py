"""Module to support parsing of the github login page """
import sys

from .parseutil import *
from .exception import ParseError

class LoginParser():
    """Class to interact with the login page """

    def __init__(self, driver):
        self.driver = driver

    def load_initial(self, url):
        """Load the login page """
        self.driver.get(url)

        xpath_page_loaded = '//form[@action="/session"]'

        wait_element(self.driver, xpath_page_loaded)

        if not get_element(self.driver, xpath_page_loaded):
            raise ParseError(xpath_page_loaded, "Unable to load login page")

    def login(self, username, password):
        """Login into github """
        print_pretty("Going to login into github with user '" + username + "'")

        in_email = self.get_in_mail()
        in_password = self.get_in_password()

        in_email.clear()
        in_email.send_keys(username)
        in_password.clear()
        in_password.send_keys(password)
        click_element(self.driver, '//input[@value="Sign in"]')

        self.wait_logged_in()

        if self.logged_in():
            print_pretty("Login into github: SUCCESS")
            return True
        else:
            print_pretty("Login into github: FAILED")
            return False

    def wait_logged_in(self):
        """Wait for your account to be logged in """
        wait_element(self.driver, '//input[@name="q"]')

    def logged_in(self):
        """Verify if you are logged in """
        return has_element(self.driver, '//input[@name="q"]')

    def get_in_mail(self):
        """Get the email input element on this page """
        return get_element(self.driver, '//input[@id="login_field"]')

    def get_in_password(self):
        """Get the password input element on this page """
        return get_element(self.driver, '//input[@id="password"]')


 