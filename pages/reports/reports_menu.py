from utils.selenium_helpers import CommonAction
from selenium.webdriver.common.by import By


class ReportsMenu(CommonAction):
    activities_report_menu_item = (By.XPATH, '//*[@id="tab33"]')
    voice_option_in_activities = (By.XPATH, '//*[@id="tab34"]')
    voice_text_for_wait = (By.XPATH, '//*[text()="VOICE"]')

    message_option_in_activities = (By.XPATH, '//*[@id="tab35"]')
    user_metrics_report_menu_item = (By.XPATH, '//*[@id="tab32"]')
    search_text_for_wait = (By.XPATH, '//*[text()="SEARCH BY"]')

    def click_on_activities_menu_item(self):
        self.wait_till_located(self.voice_text_for_wait)
        self.wait_till_located(self.activities_report_menu_item).click()

    def click_on_voice_option_in_activities(self):
        self.wait_till_located(self.voice_option_in_activities).click()
        self.wait_till_located(self.search_text_for_wait)

    def click_on_user_metrics_menu_item(self):
        self.wait_till_located(self.voice_text_for_wait)
        self.wait_till_located(self.user_metrics_report_menu_item).click()

    def click_on_message_option_in_activities(self):
        self.wait_till_located(self.message_option_in_activities).click()
        self.wait_till_located(self.search_text_for_wait)
