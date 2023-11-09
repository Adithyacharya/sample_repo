from utils.selenium_helpers import CommonAction
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


class UserMetrics(CommonAction):
    activities_report_menu_item = (By.XPATH, '//*[@id="tab33"]')
    voice_option_in_activities = (By.XPATH, '//*[@id="tab34"]')
    voice_text_for_wait = (By.XPATH, '//*[text()="VOICE"]')

    search_text_for_wait = (By.XPATH, '//*[text()="SEARCH BY"]')
    user_metrics = (By.XPATH, '//a[text()="User metrics"]')
    search_keywords = (By.XPATH, '//*[@id="keywords"]')
    account_activity_filter = (By.XPATH, '//*[@id="account_activity_filter"]')
    data_range_in_user_metrics = (By.XPATH, '//*[@id="logdata_fdate"]')
    name_in_user_metrics_header = (By.XPATH, '//*[text()="Name"]')
    multiline_in_user_metrics_header = (By.XPATH, '//*[text()="MultiLine #"]')
    device_in_user_metrics_header = (By.XPATH, '//*[text()="Device #"]')
    email_in_user_metrics_header = (By.XPATH, '//*[text()="Email"]')
    call_min_in_user_metrics_header = (
        By.XPATH, '//p[contains(text(), "Call") and contains(text(), "min")]')
    messages_num_in_user_metrics_header = (
        By.XPATH, '//p[contains(text(), "Messages") and contains(text(), "num")]')
    data_mb_in_user_metrics_header = (
        By.XPATH, '//p[contains(text(), "Data") and contains(text(), "M")]')
    name_in_user_metrics_result = (By.XPATH, '((//*[@id="comm"])[2]//p)[1]')
    multiline_in_user_metrics_result = (
        By.XPATH, '((//*[@id="comm"])[2]//p)[2]')
    device_in_user_metrics_result = (By.XPATH, '((//*[@id="comm"])[2]//p)[3]')
    email_in_user_metrics_result = (By.XPATH, '((//*[@id="comm"])[2]//p)[4]')
    call_min_in_user_metrics_result = (
        By.XPATH, '((//*[@id="comm"])[2]//p)[5]')
    messages_num_in_user_metrics_result = (
        By.XPATH, '((//*[@id="comm"])[2]//p)[6]')
    data_mb_in_user_metrics_result = (
        By.XPATH, '((//*[@id="comm"])[2]//p)[7]')

    def verify_heading_in_user_metrics(self):
        self.wait_till_clickable(self.name_in_user_metrics_header)
        self.wait_till_clickable(self.multiline_in_user_metrics_header)
        self.wait_till_clickable(self.device_in_user_metrics_header)
        self.wait_till_clickable(self.email_in_user_metrics_header)
        self.wait_till_clickable(self.call_min_in_user_metrics_header)
        self.wait_till_clickable(self.messages_num_in_user_metrics_header)
        self.wait_till_clickable(self.data_mb_in_user_metrics_header)

    def get_result_from_user_metrics(self):
        result_dict = {}
        self.wait_till_clickable(self.name_in_user_metrics_result)
        result_dict['name'] = self.get_text(self.name_in_user_metrics_result)
        result_dict['multiline'] = self.get_text(
            self.multiline_in_user_metrics_result)
        result_dict['device'] = self.get_text(
            self.device_in_user_metrics_result)
        result_dict['email'] = self.get_text(
            self.email_in_user_metrics_result)
        result_dict['call_min'] = self.get_text(
            self.call_min_in_user_metrics_result)
        result_dict['messages_num'] = self.get_text(
            self.messages_num_in_user_metrics_result)
        result_dict['data_mb'] = self.get_text(
            self.data_mb_in_user_metrics_result)
        return result_dict

    def click_on_activities_menu_item(self):
        self.wait_till_located(self.voice_text_for_wait)
        self.wait_till_located(self.activities_report_menu_item).click()

    def click_on_voice_option_in_activities(self):
        self.wait_till_located(self.voice_option_in_activities).click()
        self.wait_till_located(self.search_text_for_wait)

    def click_on_user_metrics(self):
        self.wait_till_clickable(self.user_metrics)
        self.wait_till_clickable(self.user_metrics).click()

    def enter_name_in_user_metrics(self, name):
        self.wait_till_clickable(self.search_keywords)
        self.wait_till_clickable(self.search_keywords).send_keys(name)

    def click_on_search_in_user_metrics(self):
        self.wait_till_clickable(self.account_activity_filter)
        self.wait_till_clickable(self.account_activity_filter).click()

    def enter_data_range_in_user_metrics(self, daterange):
        self.wait_till_clickable(self.data_range_in_user_metrics).click()
        # for _ in range(26):
        #     self.wait_till_clickable(
        #         self.data_range_in_user_metrics).send_keys(Keys.ARROW_RIGHT)
        # for _ in range(26):
        #     self.wait_till_clickable(
        #         self.data_range_in_user_metrics).send_keys(Keys.BACK_SPACE)
        time.sleep(3)
        self.wait_till_located(
            self.data_range_in_user_metrics).send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        self.wait_till_clickable(
            self.data_range_in_user_metrics).send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        self.wait_till_clickable(
            self.data_range_in_user_metrics).send_keys(daterange)
        time.sleep(5)
