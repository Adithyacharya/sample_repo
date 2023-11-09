from selenium.webdriver.common.by import By

from utils.selenium_helpers import CommonAction


class NavMenuPage(CommonAction):
    accounts_nav_menu_option = (By.XPATH, '//*[@id="tab63"]')
    reports_nav_menu_option = (By.XPATH, '//*[@id="tab18"]')
    setup_nav_menu_option = (By.XPATH, '//*[@id="tab40"]')

    def go_to_accounts_tab(self):
        self.wait_till_clickable(self.accounts_nav_menu_option).click()

    def go_to_reports_tab(self):
        self.wait_till_clickable(self.reports_nav_menu_option).click()

    def go_to_setup_tab(self):
        self.wait_till_clickable(self.setup_nav_menu_option).click()
