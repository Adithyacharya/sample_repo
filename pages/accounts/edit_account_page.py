from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction
import time


class EditAccountPage(CommonAction):
    move_button = (By.XPATH, '//*[@id="select_account_move_edit"]')
    delete_button = (By.XPATH, '//*[@id="action_delete"]')
    confirm_yes_deletion = (
        By.XPATH, '//*[@id="delete_account_confirmation"]//div/button[text()="Yes"]')

    def click_on_move_button_from_edit_accounts_page(self):
        self.wait_till_clickable(self.move_button).click()

    def click_on_delete_button_from_edit_accounts_page(self):
        self.wait_till_clickable(self.delete_button).click()

    def click_confirm_delete(self):
        self.wait_till_clickable(self.confirm_yes_deletion).click()
