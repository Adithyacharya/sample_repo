from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction


class DeleteAccountPopUp(CommonAction):
    proceed_button = (By.XPATH, '//*[text()="Proceed"]')
    tag_name_text_field = (By.XPATH, '//*[contains(@placeholder,"Enter tag name")]')

    def click_proceed_button(self):
        self.wait_till_clickable(self.proceed_button).click()

    def enter_tag_name(self, tag):
        self.wait_till_located(self.tag_name_text_field).send_keys(tag)

    def remove_tag_name(self):
        self.wait_till_located(self.tag_name_text_field).clear()
