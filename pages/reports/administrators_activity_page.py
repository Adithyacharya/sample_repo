from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction
from selenium.webdriver.support.ui import Select
from pages.accounts.add_account_page import AddAccountPage
from pages.accounts.account_page import AccountPage
import time


class AdminActivityReportsPage(CommonAction):
    administrators_activity_btn = (By.XPATH, '//*[@id="tab39"]')
    reports_activity = (By.XPATH, "//*[text()='All Selected (4)']")
    reports_activity_dropdown_option_all = (
        By.XPATH, "//*[text()='Activity']//parent::div//*[text()=' All']")
    reports_activity_dropdown_option_write = (
        By.XPATH,
        "//*[text()='Activity']//parent::div//*[text() =' Write']",
    )
    reports_event_type = (
        By.XPATH,
        "//*[text()='Event type']//parent::div//*[text()='All Selected (32)']",
    )
    reports_event_type_search_field = (
        By.XPATH,
        "//*[@placeholder = 'Search for something...']",
    )
    reports_event_type_dropdown_option_all = (
        By.XPATH,
        "//*[text()='Event type']//parent::div//*[text()=' All']",
    )
    reports_event_type_dropdown_option_add_account = (
        By.XPATH,
        "//*[text()='Event type']//parent::div//*[text()=' Add Account']",
    )
    reports_activity_details = (
        By.XPATH, '//*[@id="reports_admin_activity_details"]')
    reports_search_btn = (By.XPATH, '//*[@id="login_filter"]')
    reports_administrator_activity_title = (
        By.XPATH,
        "//*[@id = 'reports-right-block']//*[text()='Administrators activity']",
    )
    accounts_nav_menu_option = (By.XPATH, '//*[@id="tab63"]')
    default_search_field = (By.XPATH, '//*[@id="usr_srch_blk"]')
    default_search_btn = (By.XPATH, "//*[@id='search_on_filter']")
    accounts_edit_btn = (By.XPATH, '//*[@id="accounts_edit_btn"]')
    accounts_delete_btn = (By.XPATH, '//*[@id="user_deactivate_delete"]')
    delete_window_input_filed = (
        By.XPATH, '//*[@placeholder="Enter tag name "]')
    delete_window_proceed_btn = (By.XPATH, '//*[@id= "user_activate"]')
    No_account_found = (
        By.XPATH,
        '//*[@id = "comm"]//*[text() = "No records are found"]',
    )
    reports_first_name = (
        By.XPATH,
        "//*[text() = 'First Name']/following-sibling::label//span",
    )
    reports_last_name = (
        By.XPATH,
        "//*[text() = 'Last Name']/following-sibling::label//span",
    )
    reports_user_name = (
        By.XPATH,
        '//*[text() = "User Name"]/following-sibling::label//span',
    )
    reports_invitation_status = (
        By.XPATH,
        "//*[text() = 'Invitation Status']/following-sibling::label//span",
    )
    reports_Name_email = (By.XPATH, "//*[text() = '[External Administrator]']")
    reports_organisation = (
        By.XPATH,
        "//*[text() ='Organization']/following-sibling::label//span",
    )
    reports_user_permission = (
        By.XPATH,
        "//*[text() = 'User Permission']/following-sibling::label//span",
    )
    reports_assigned_number = (
        By.XPATH,
        "//*[text() = 'Assigned Number']/following-sibling::label//span",
    )
    reports_applications = (
        By.XPATH,
        "//*[text() = 'Application(S)']/following-sibling::label/span",
    )
    # number_of_allowed_ids = (By.XPATH,"//*[text() = "Number of Allowed ID"
    #                          's"]/following-sibling::label/span")

    # Dhanush
    event_type_drop_down = (
        By.XPATH,
        '//*[text()="Event type"]//parent::div//*[@data-toggle="dropdown"]',
    )
    activity_drop_down = (
        By.XPATH,
        '//*[text()="Activity"]//parent::div//*[@data-toggle="dropdown"]',
    )

    event_type_drop_down_option_all = (
        By.XPATH,
        "//*[text()='Event type']//parent::div//*[text()=' All']",
    )
    event_type_drop_down_option_move_account = (
        By.XPATH,
        "//*[text()='Event type']//parent::div//*[text()=' All']",
    )
    event_type_drop_down_xpath_template = "//*[text()='Event type']//parent::div//"

    search_result_text_indicator = (
        By.XPATH,
        '//*[@id="comm"]/div[1]//div/p[text()="Date"]',
    )
    fixed_text = (By.XPATH, '//*[text()="SEARCH BY"]')
    moved_from_org = (
        By.XPATH,
        '//*[text()="Moved From Organization"]/following-sibling::label/span',
    )
    moved_to_org = (
        By.XPATH,
        '//*[text()="Moved to Organization"]/following-sibling::label/span',
    )
    # End Dhanush

    # Action Dhanush
    def click_event_drop_down(self):
        self.wait_till_clickable(self.event_type_drop_down).click()

    def select_event_type_option(self, option_value):
        self.event_type_drop_down_xpath_template = (
            "//*[text()='Event type']//parent::div//"
        )
        adder = "*[text()=' " + option_value + "']"
        self.event_type_drop_down_xpath_template += adder
        drop_down_options = (
            By.XPATH, self.event_type_drop_down_xpath_template)
        self.wait_till_clickable(drop_down_options).click()

    def get_search_results_for_move_account(self):
        src_org = self.wait_till_located(self.moved_from_org).text
        dest_org = self.wait_till_located(self.moved_to_org).text
        return src_org, dest_org

    def click_fixed_text(self):
        self.wait_till_located(self.fixed_text).click()

    # End Action Dhanush

    def click_administrators_activity_reports(self):
        self.wait_till_clickable(self.administrators_activity_btn).click()
        time.sleep(2)

    def click_reports_activtiy_dropdown(self):
        self.wait_till_clickable(self.reports_activity).click()
        time.sleep(2)

    def click_activity_dropdown_option_all(self):
        print("in loop")
        self.wait_till_clickable(
            self.reports_activity_dropdown_option_all).click()
        time.sleep(4)

    def click_activity_dropdown_option_write(self):
        self.wait_till_clickable(
            self.reports_activity_dropdown_option_write).click()
        time.sleep(3)

    def click_reports_event_type_dropdown(self):
        self.wait_till_clickable(self.reports_event_type).click()
        time.sleep(2)

    def click_event_type_dropdown_option_all(self):
        self.wait_till_clickable(
            self.reports_event_type_dropdown_option_all).click()
        time.sleep(2)

    def reports_event_type_searchfield_enter_value(self, value):
        time.sleep(1)
        self.wait_till_located(
            self.reports_event_type_search_field).send_keys(value)
        time.sleep(2)

    def click_event_type_dropdown_option_add_account(self):
        time.sleep(5)
        self.wait_till_clickable(
            self.reports_event_type_dropdown_option_add_account
        ).click()
        time.sleep(2)

    def click_reports_title_administrator_activity(self):
        self.wait_till_located(
            self.reports_administrator_activity_title).click()
        time.sleep(2)

    # Modified by Dhanush
    def enter_activity_details_email_id(self, email):
        self.wait_till_located(self.reports_activity_details).send_keys(email)

    # Modified by Dhanush
    def click_administrator_activity_search_button(self):
        self.wait_till_clickable(self.reports_search_btn).click()
        self.wait_till_located(self.search_result_text_indicator)

    def check_account_found(self):
        element = self.is_element_displayed(self.No_account_found)
        print(element)
        return element

    def validate_report_first_name(self, name):
        element = self.is_element_displayed(self.reports_first_name)
        print(element.text)
        return element.text

    # Deleting an account#

    def click_accounts_options_from_nav_menu(self):
        self.wait_till_clickable(self.accounts_nav_menu_option).click()
        time.sleep(3)

    def add_account_enter_email_id_default_search_field(self, email):
        self.wait_till_located(self.default_search_field).send_keys(email)
        time.sleep()

    def add_account_click_default_search_button(self):
        self.wait_till_clickable(self.default_search_btn).click()
        time.sleep(5)

    def click_account_edit_button(self):
        self.wait_till_clickable(self.accounts_edit_btn).click()
        time.sleep(2)

    def click_delete_btn(self):
        self.wait_till_clickable(self.accounts_delete_btn).click()
        time.sleep(2)

    def enter_tag_name_delete_window(self, tag_name):
        self.wait_till_located(
            self.delete_window_input_filed).send_keys(tag_name)
        time.sleep(2)

    def click_delete_proceed(self):
        self.wait_till_clickable(self.delete_window_proceed_btn).click()
        time.sleep(1)
