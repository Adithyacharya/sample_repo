from utils.selenium_helpers import CommonAction
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


class MessageActivity(CommonAction):
    message_type_drop_down = (By.XPATH, '//*[@id="eventname_id"]')
    message_type_drop_down_all_messages_option = (
        By.XPATH,
        '//*[text()="All Messages"]',
    )
    message_type_drop_down_all_sms_messages_option = (
        By.XPATH,
        '//*[text()="All SMS Messages"]',
    )

    search_result = (
        By.XPATH,
        '//*[@id="comm"]/p | (//*[@id="comm"])[2]//div/p[@class]',
    )
    search_button = (By.XPATH, '//*[@id="communication_filter"]')
    date_text_for_wait = (By.XPATH, '//*[text()="Date"]')

    headers_list_on_search = (By.XPATH, '(//*[@id="comm"])[1]//div/p')
    message_activity_download = (By.XPATH, '//*[@id="communication_filter_download"]')

    date_range_field = (By.XPATH, '//*[@id="logdata_fdate"]')

    def select_message_type(self, value):
        self.wait_till_located(self.message_type_drop_down)
        dropdown = Select(self.find_element_on_web(self.message_type_drop_down))
        dropdown.select_by_visible_text(value)

    def click_on_search_button(self):
        self.wait_till_clickable(self.search_button).click()
        self.wait_till_located(self.date_text_for_wait)

    def get_search_result(self):
        element = self.wait_till_located(self.search_result)
        self.scroll_till_visible(element)
        return element.text

    def get_header_list_on_search(self):
        elements = self.find_elements_on_web(self.headers_list_on_search)
        headers = [str(element.text) for element in elements]
        return headers

    def download_message_report_activity(self):
        self.wait_till_clickable(self.message_activity_download).click()
        time.sleep(10)

    def enter_date_range(self, date_range):
        self.wait_till_located(self.date_range_field).clear()
        self.wait_till_located(self.date_range_field).send_keys(date_range)
