"""Module to support parsing of top menu """
from .parseutil import *

class TopMenuParser():
    """Class to interact with the top menu """
    def __init__(self, driver):
        self.driver = driver

    def get_input_search(self):
        """Get the search bar input field on this page """
        return get_element(self.driver, '//input[@name="q"]')

    def logout(self):
        """Logout of github """
        print_pretty("Going to logout from github")

        menu_settings = self.get_menu_settings_dropdown()
        menu_settings.click()
        menu_logout = self.get_menu_logout()
        menu_logout.click()

        wait_page_loaded(self.driver, "https://github.com/")
        self.wait_logged_out()

        if self.logged_out():
            print_pretty("Logged out from github: SUCCESS")
            return True
        else:
            print_pretty("Logged out from github: FAILED")
            return False

    def wait_logged_out(self):
        """Wait for your account to be logged out """
        return wait_element(self.driver, '//a[text()="Sign up for GitHub"]')

    def logged_out(self):
        """Verify if you are logged out """
        return has_element(self.driver, '//a[text()="Sign up for GitHub"]')

    def get_menu_settings_dropdown(self):
        """Get the settings menu on this page """
        return get_element(self.driver, '//summary[@aria-label="View profile and more"]')

    def get_menu_logout(self):
        """Get the logout menu on this page """
        return get_element(self.driver, '//button[contains(text(),"Sign out")]')

    def get_menu_pullrequests(self):
        """Get the pull request menu on this page """
        return get_element(self.driver, '//a[@href="/pulls"]')

    def get_menu_issues(self):
        """Get the issues menu on this page """
        return get_element(self.driver, '//a[@href="/issues"]')

    def get_menu_marketplace(self):
        """Get the marketplace menu on this page """
        return get_element(self.driver, '//a[@href="/marketplace"]')

    def get_menu_explore(self):
        """Get the explore menu on this page """
        return get_element(self.driver, '//a[@href="/explore"]')
