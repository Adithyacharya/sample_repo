from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction
import time


class AccountFilter(CommonAction):

    call_recording_filter = (By.XPATH, '//*[@id="call_recording_selector"]')
    status_filter = (By.XPATH, '//*[@id="status_filter"]')
    active_filter = (By.XPATH, '//*[text()="Active"]')
    clear_filter = (By.XPATH, '//*[@id="fa_status_filter_close"]')
    call_recording_filter_on = (
        By.XPATH, '//*[@id="call_recording_options"]//span[text()="on"]')
    call_recording_filter_off = (
        By.XPATH, '//*[@id="call_recording_options"]//span[text()="off"]')
    call_recording_clear_filter = (
        By.XPATH, '//*[@id="fa_monitor_calls_close"]')
    message_recording_selector = (
        By.XPATH, '//*[@id="message_recording_selector"]')
    message_recording_selector_clear_filter = (
        By.XPATH, '//*[@id="fa_monitor_sms_close"]')
    message_recording_filter_on = (
        By.XPATH, '//*[@id="message_recording_options"]//span[text()="on"]')
    message_recording_filter_off = (
        By.XPATH, '//*[@id="message_recording_options"]//span[text()="off"]')
    social_messaging = (
        By.XPATH, '//*[@id="whatsapp_selector"]')
    social_messaging_filter_on = (
        By.XPATH, '//*[@id="whatsapp_options"]//span[text()="on"]')
    social_messaging_clear_filter = (
        By.XPATH, '//*[@id="fa_whatsapp_enable_filter_close"]')
    social_messaging_filter_off = (
        By.XPATH, '//*[@id="whatsapp_options"]//span[text()="off"]')
    sales_force_filter = (
        By.XPATH, '//*[@id="salesforce_selector"]')
    sales_force_clear_filter = (
        By.XPATH, '//*[@id="fa_salesforce_close"]')
    sales_force_filter_on = (
        By.XPATH, '//*[@id="salesforce_options"]//span[text()="on"]')
    sales_force_filter_off = (
        By.XPATH, '//*[@id="salesforce_options"]//span[text()="off"]')
    account_activity = (
        By.XPATH, '//*[@id="user-activity"]')
    salesforce = (
        By.XPATH, '//*[contains(text(), "Salesforce")]')
    social_messaging_flag = (
        By.XPATH, '//*[@id="subscriber_whatsapp_enable"]')
    custom_monitor_calls_flag = (
        By.XPATH, '//*[@id="subscriber_monitor_calls"]')
    name_filter = (
        By.XPATH, '//*[@id="account_name_col"]//i')
    org_filter = (
        By.XPATH, '//*[@id="account_org_col"]//i')
    account_names_list = (
        By.XPATH, '//*[@id="accounts_names"]')
    org_names_list = (
        By.XPATH, '//*[@id="accounts_organization"]')
    status_sort = (
        By.XPATH, '//*[@id="account_status_col"]//i')
    status_activated = (
        By.XPATH, '//*[@title="Activated"]')
    status_invitation_failed = (
        By.XPATH, '//*[@title="Invitation failed"]')
    status_invited = (
        By.XPATH, '//*[@title="Invited"]')
    status_not_invited = (
        By.XPATH, '//*[@title="Not invited"]')
    all_status_from_account_list = (
        By.XPATH, '//*[@title="Activated"] | //*[@title="Invited"]  | //*[@title="Invitation failed"] | //*[@title="Not invited"]')
    click_on_jump_to_page_number = (
        By.XPATH, '//*[@id="jumpto_page_number_submit"]')

    def click_on_clear_filter(self):
        time.sleep(5)
        self.wait_till_located(self.clear_filter).click()

    def click_filter(self):
        self.wait_till_located(self.status_filter).click()

    def click_active_filter(self):
        self.wait_till_located(self.active_filter).click()
        time.sleep(5)

    def click_on_call_recording_filter(self):
        self.wait_till_located(
            self.call_recording_filter).click()

    def click_on_call_recording_filter_on(self):
        self.wait_till_located(
            self.call_recording_filter_on).click()

    def click_on_call_recording_filter_off(self):
        self.wait_till_located(
            self.call_recording_filter_off).click()

    def click_on_call_recording_clear_filter(self):
        self.wait_till_located(
            self.call_recording_clear_filter).click()

    def click_on_message_recording_selector_filter(self):
        self.wait_till_located(
            self.message_recording_selector).click()

    def click_on_message_recording_selector_on(self):
        self.wait_till_located(
            self.message_recording_filter_on).click()

    def click_on_message_recording_selector_off(self):
        self.wait_till_located(
            self.message_recording_filter_off).click()

    def click_on_message_recording_selector_clear_filter(self):
        self.wait_till_located(
            self.message_recording_selector_clear_filter).click()

    def click_on_social_messaging_filter(self):
        self.wait_till_located(
            self.social_messaging).click()

    def click_on_social_messaging_filter_on(self):
        self.wait_till_located(
            self.social_messaging_filter_on).click()

    def click_on_social_messaging_filter_off(self):
        self.wait_till_located(
            self.social_messaging_filter_off).click()

    def click_on_social_messaging_clear_filter(self):
        self.wait_till_located(
            self.social_messaging_clear_filter).click()

    def click_on_sales_force_filter(self):
        self.wait_till_located(
            self.sales_force_filter).click()

    def click_on_sales_force_filter_on(self):
        self.wait_till_located(
            self.sales_force_filter_on).click()

    def click_on_sales_force_filter_off(self):
        self.wait_till_located(
            self.sales_force_filter_off).click()

    def click_on_sales_force_clear_filter(self):
        self.wait_till_located(
            self.sales_force_clear_filter).click()

    def click_on_account_activity(self):
        self.wait_till_located(
            self.account_activity).click()

    def verify_salesforce(self):
        return self.is_element_displayed(
            self.salesforce)

    def get_checked_attribute_from_social_messaging(self):
        return self.get_checked_attribute_from_element(
            self.social_messaging_flag)

    def get_checked_attribute_from_monitor_calls(self):
        return self.get_checked_attribute_from_element(
            self.custom_monitor_calls_flag)

    def click_on_name_sort(self):
        return self.wait_till_located(
            self.name_filter).click()

    def click_on_org_sort(self):
        return self.wait_till_located(
            self.org_filter).click()

    def click_on_status_sort(self):
        return self.wait_till_located(
            self.status_sort).click()

    def get_account_names(self, no_of_account):
        return self.get_all_names(
            self.account_names_list, no_of_account)

    def get_org_names(self, no_of_account):
        return self.get_all_names(
            self.org_names_list, no_of_account)

    def get_status_list(self, no_of_account):
        return self.get_all_names(
            self.account_names, no_of_account)

    def get_list_of_status_activated(self):
        return self.find_elements_on_web(
            self.status_activated)

    def get_list_of_status_invitation_failed(self):
        return self.find_elements_on_web(
            self.status_invitation_failed)

    def get_list_of_status_invited(self):
        return self.find_elements_on_web(
            self.status_invited)

    def get_list_of_status_not_invited(self):
        return self.find_elements_on_web(
            self.status_not_invited)

    def get_all_status_from_account_list(self):
        return self.get_title(
            self.all_status_from_account_list)

    def click_on_jump_to_page(self):
        return self.find_element_on_web(
            self.click_on_jump_to_page_number).click()
