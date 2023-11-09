from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction
import time


class ConsumptionMetrics(CommonAction):
    consumption_metrics_menu = (By.XPATH, '//a[text()="Consumption metrics"]')
    report_duration_dropdown = (By.XPATH, '//*[@id="report_duration"]')
    custom_data_option = (By.XPATH, '(//*[text()="Custom Date"])[1]')
    today_option = (By.XPATH, '//*[text()="Today"]')
    last_7_days_option = (By.XPATH, '//*[text()="Last 7 Days"]')
    current_cycle_option = (By.XPATH, '//*[text()="Current Cycle"]')
    last_cycle_option = (By.XPATH, '//*[text()="Last Cycle"]')
    report_duration = (By.XPATH, '//*[@id="report_duration1"]')
    apply_in_calendar = (By.XPATH, '//*[@type="button"][text()="Apply"]')
    voice_date_range = (By.XPATH, '//*[@id="backtoparentvoice"]')
    voice_incoming_data = (By.XPATH, '(//*[@id="voice_in"])[1]')
    voice_outcoming_data = (By.XPATH, '(//*[@id="voice_out"])[1]')
    messages_received_data = (By.XPATH, '(//*[@id="sms_in"])[1]')
    messages_sent_data = (By.XPATH, '(//*[@id="sms_out"])[1]')
    download_voice_report = (
        By.XPATH, '//*[@id="consumption_metrics_voice_down_icon"]')
    download_message_report = (
        By.XPATH, '//*[@id="consumption_metrics_msg_down_icon"]')
    download_data_report = (
        By.XPATH, '//*[@id="consumption_metrics_data_down_icon"]')
    message_date_range = (By.XPATH, '//*[@id="backtoparentmessage"]')
    data_date_range = (By.XPATH, '//*[@id="backtoparentdata"]')
    total_data_usage = (By.XPATH, '//*[@id="data_usage"]')

    def click_on_consumption_metrics_menu(self):
        self.wait_till_clickable(self.consumption_metrics_menu).click()

    def click_on_report_duration_dropdown(self):
        self.wait_till_clickable(self.report_duration_dropdown).click()

    def click_on_custom_data_option(self):
        self.wait_till_clickable(self.custom_data_option).click()

    def click_on_today_option(self):
        self.wait_till_clickable(self.today_option).click()

    def click_on_last_7_days_option(self):
        self.wait_till_clickable(self.last_7_days_option).click()

    def click_on_current_cycle_option(self):
        self.wait_till_clickable(self.current_cycle_option).click()

    def click_on_last_cycle_option(self):
        self.wait_till_clickable(self.last_cycle_option).click()

    def enter_report_duration(self, dt):
        self.wait_till_clickable(self.report_duration).clear()
        time.sleep(5)
        self.wait_till_clickable(self.report_duration).send_keys(dt)

    def click_on_calendar_apply(self):
        time.sleep(5)
        self.wait_till_clickable(self.apply_in_calendar).click()

    def get_voice_date_range(self):
        self.wait_till_clickable(self.voice_date_range)
        return self.get_text(self.voice_date_range)

    def get_voice_incoming_data(self):
        self.wait_till_clickable(self.voice_incoming_data)
        return self.get_text(self.voice_incoming_data)

    def get_voice_outcoming_data(self):
        self.wait_till_clickable(self.voice_outcoming_data)
        return self.get_text(self.voice_outcoming_data)

    def download_voice_report_in_consumption_metrics(self):
        self.wait_till_clickable(self.download_voice_report).click()
        time.sleep(10)

    def download_message_report_in_consumption_metrics(self):
        self.wait_till_clickable(self.download_message_report).click()
        time.sleep(10)

    def download_data_report_in_consumption_metrics(self):
        self.wait_till_clickable(self.download_data_report).click()
        time.sleep(10)

    def get_messages_date_range(self):
        self.wait_till_clickable(self.message_date_range)
        return self.get_text(self.message_date_range)

    def get_messages_incoming_data(self):
        self.wait_till_clickable(self.messages_received_data)
        return self.get_text(self.messages_received_data)

    def get_messages_outcoming_data(self):
        self.wait_till_clickable(self.messages_sent_data)
        return self.get_text(self.messages_sent_data)

    def get_data_date_range(self):
        self.wait_till_clickable(self.data_date_range)
        return self.get_text(self.data_date_range)

    def get_total_data_usage(self):
        self.wait_till_clickable(self.total_data_usage)
        return self.get_text(self.total_data_usage)
