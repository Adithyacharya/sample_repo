from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction
import time


class EditLinePage(CommonAction):
    delete_button = (By.XPATH, '//*[@id="myid_admin_trash_submit"]')

    def click_on_delete_button_from_edit_line_page(self):
        self.wait_till_clickable(self.delete_button).click()
