from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction
import time


class MoveAccountPopUp(CommonAction):
    select_sub_org_to_move_drop_down = (
        By.XPATH, '//*[@id="all_suborgs"]/div/button')
    search_org_for_move_inside_drop_down = (
        By.XPATH, '//*[@id="bootstrap_select_input"]')
    move_button = (By.XPATH, '//*[@id="move_user_click"]')
    confirm_move_button_accounts_page = (By.XPATH, '//*[@id="confirm_move"]')
    confirm_move_button_edit_account_page = (
        By.XPATH, '//*[@id="confirm_move_edit"]')
    download_move_report = (By.XPATH, '//*[@id="move_user_download"]')
    done_move_transaction = (By.XPATH, '//*[@id="move_user_done"]')

    def select_sub_org_to_be_moved(self, org_name):
        self.wait_till_clickable(self.select_sub_org_to_move_drop_down).click()
        self.wait_till_located(self.search_org_for_move_inside_drop_down).send_keys(
            org_name
        )
        time.sleep(2)
        self.click_enter_key()
        time.sleep(2)

    def click_on_move_button(self):
        self.wait_till_clickable(self.move_button).click()

    def click_confirm_move_accounts_page(self):
        self.wait_till_clickable(
            self.confirm_move_button_accounts_page).click()

    def click_confirm_move_edit_accounts_page(self):
        self.wait_till_clickable(
            self.confirm_move_button_edit_account_page).click()

    def click_download_button_for_move_and_complete_with_done(self):
        self.wait_till_clickable(self.download_move_report).click()
        time.sleep(15)
        self.wait_till_clickable(self.done_move_transaction).click()
