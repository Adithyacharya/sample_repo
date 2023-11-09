from utils.selenium_helpers import CommonAction
from selenium.webdriver.common.by import By
import time


class VoiceActivity(CommonAction):
    call_type_drop_down = (By.XPATH, '//*[@id="voice_activities_call_type_drpdown"]')
    call_type_drop_down_call_received_option = (
        By.XPATH,
        '//*[text()="Calls received"]',
    )
    call_type_drop_down_call_made_option = (
        By.XPATH,
        '//*[text()="Calls made"]',
    )

    call_type_drop_down_calls_to_vm_option = (
        By.XPATH,
        '//*[text()="Calls to voicemail"]',
    )

    call_type_drop_down_dropped_call_option = (
        By.XPATH,
        '//*[text()="Dropped call"]',
    )

    search_button = (By.XPATH, '//*[@id="voice_filter"]')

    date_text_for_wait = (By.XPATH, '//*[text()="Date"]')

    search_result = (
        By.XPATH,
        '//*[@id="comm"]/p | (//*[@id="comm"])[2]//div/p[@class]',
    )
    voice_activity_download = (By.XPATH, '//*[@id="voice_filter_download"]')
    no_records_found_text = (By.XPATH, '//*[text()="No records are found"]')

    date_range_field = (By.XPATH, '//*[@id="logdata_fdate"]')
    headers_list_on_search = (By.XPATH, '(//*[@id="comm"])[1]//div/p')

    call_mode_drop_down = (By.XPATH, '//*[@id="incomingmode_callmode"]')
    call_mode_drop_down_tdm = (By.XPATH, '//li[text()="TDM"]')
    call_mode_drop_down_data = (By.XPATH, '//li[text()="Data"]')
    call_mode_drop_down_all = (By.XPATH, '//li[text()="All"]')

    keywords_input_field = (By.XPATH, '//*[@id="keywords_query"]')

    from_to_radio_button = (
        By.XPATH,
        '//*[@id="from_to"]/following-sibling::span[text()="From"]',
    )
    from_ml_number_input_field = (By.XPATH, '//*[@id="from_number"]')
    to_ml_number_input_field = (By.XPATH, '//*[@id="to_number"]')

    min_duration_input_field = (By.XPATH, '//*[@id="cd_low"]')
    max_duration_input_field = (By.XPATH, '//*[@id="cd_high"]')

    def select_call_type_drop_down(self, indicator):
        self.wait_till_clickable(self.call_type_drop_down).click()
        option = self.call_type_drop_down_call_received_option
        if indicator == "cm":
            option = self.call_type_drop_down_call_made_option
        elif indicator == "ctv":
            option = self.call_type_drop_down_calls_to_vm_option
        elif indicator == "dc":
            option = self.call_type_drop_down_dropped_call_option

        self.wait_till_clickable(option).click()

    def select_call_mode_drop_down(self, indicator):
        self.wait_till_clickable(self.call_mode_drop_down).click()
        option = self.call_mode_drop_down_all
        if indicator == "tdm":
            option = self.call_mode_drop_down_tdm
        elif indicator == "data":
            option = self.call_mode_drop_down_data
        self.wait_till_clickable(option).click()

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

    def download_voice_report_activity(self):
        self.wait_till_clickable(self.voice_activity_download).click()
        time.sleep(10)

    def enter_date_range(self, date_range):
        self.wait_till_located(self.date_range_field).clear()
        self.wait_till_located(self.date_range_field).send_keys(date_range)

    def enter_keyword(self, value):
        self.wait_till_located(self.keywords_input_field).send_keys(value)

    def enter_from_to_ml_numbers(self, from_ml, to_ml):
        self.wait_till_clickable(self.from_to_radio_button).click()
        self.wait_till_located(self.from_ml_number_input_field).send_keys(from_ml)
        self.wait_till_located(self.to_ml_number_input_field).send_keys(to_ml)

    def enter_min_and_max_call_duration(self, min, max):
        self.wait_till_located(self.min_duration_input_field).send_keys(min)
        self.wait_till_located(self.max_duration_input_field).send_keys(max)
