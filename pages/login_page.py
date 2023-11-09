from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction


class LoginForm(CommonAction):
    email_field = (By.XPATH, '//*[@id="acct"]')
    continue_btn = (By.XPATH, '//*[@id="idContinue"]')
    password_field = (By.XPATH, '//*[@id="password"]')
    login_btn = (By.XPATH, '//*[@id="idLogin"]')
    accounts_nav_menu_option = (By.XPATH, '//*[@id="tab63"]')

    def enter_user_email(self, email):
        self.wait_till_located(self.email_field).send_keys(email)

    def click_continue_button(self):
        self.wait_till_clickable(self.continue_btn).click()

    def enter_user_password(self, password):
        self.wait_till_located(self.password_field).send_keys(password)

    def click_login_button(self):
        self.wait_till_clickable(self.login_btn).click()
        self.wait_till_located(self.accounts_nav_menu_option)
