from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction
import time


class AccountPage(CommonAction):
    accounts_nav_menu_option = (By.XPATH, '//*[@id="tab63"]')
    add_account_btn = (By.XPATH, '//*[@id="add_enterprise_user_inv"]')
    no_accounts_search_result = (By.XPATH, '//*[@id="user_emptytable_text"]')
    pagination = (By.XPATH, '//*[@id="mmp_pagination"]')
    custom_monitor_sms_flag = (
        By.XPATH, '//*[@id="subscriber_monitor_sms"]')
    edit_account_line = (
        By.XPATH, '//*[@title="Edit Line"]')
    first_account_in_accounts = (
        By.XPATH, '(//*[@id="ent_invitation_user"]//*[@id="accounts_names"])[1]')
    # ravi
    # accounts_nav_menu_option = (By.XPATH, '//*[@id="tab63"]')
    # add_account_btn = (By.XPATH, '//*[@id="add_enterprise_user_inv"]')
    # search_account_clear_btn = (By.XPATH, '//*[@id="close_user"]')
    # search_account_filtered_result_indicator = (
    #     By.XPATH, '//*[@id="mmp_pagination"]//p/span')
    # account_names_pane = (By.XPATH, '//*[@id="accounts_names"]')
    # account_user_names_pane = (By.XPATH, '//*[@id="accounts_username"]')
    # account_user_multiline_pane = (
    #     By.XPATH, '//span[contains(text(),"MultiLine")]/following-sibling::span',)
    dashboard_profile_arrow = (
        By.XPATH, "//*[@id = 'dashboard_profile_arrow']")
    sub_organisation = (By.XPATH, "//*[@id ='tab52']")
    org_id = (
        By.XPATH, "//*[@id = 'so_main']//*[text() = 'Organization ID']/following-sibling::h4")
    org_name = (By.XPATH, "//*[@id = 'so_main_description']")
    profile = (By.XPATH, "//*[@id = 'profile']")
    profile_first_name = (By.XPATH, "//*[@id = 'first_name']")
    profile_last_name = (By.XPATH, "//*[@id = 'last_name']")
    profile_email_id = (
        By.XPATH, "//*[@id = 'email_address']//parent::div//span")
    # default_search_field = (By.XPATH, '//*[@id="usr_srch_blk"]')
    default_search_btn = (By.XPATH, "//*[@id='search_on_filter']")

    # dhanush
    # add_account_btn = (By.XPATH, '//*[@id="add_enterprise_user_inv"]')
    search_account_text_filed = (By.XPATH, '//*[@id="usr_srch_blk"]')
    search_account_btn = (By.XPATH, '//*[@id="search_on_filter"]')
    search_account_clear_btn = (By.XPATH, '//*[@id="close_user"]')
    search_account_filtered_result_indicator = (
        By.XPATH, '//*[@id="mmp_pagination"]//p/span')
    account_names_pane = (By.XPATH, '//*[@id="accounts_names"]')
    account_user_names_pane = (By.XPATH, '//*[@id="accounts_username"]')
    account_user_multiline_pane = (
        By.XPATH, '//span[contains(text(),"MultiLine")]/following-sibling::span')
    account_status_pane = (
        By.XPATH, '//*[@title="Activated"] | //*[@title="Invited"]  | //*[@title="Invitation failed"] | //*[@title="Not invited"]')
    # no_accounts_search_result = (By.XPATH, '//*[@id="user_emptytable_text"]')
    account_organization_pane = (By.XPATH, '//*[@id="accounts_organization"]')
    # Move Accounts
    select_the_account = (By.XPATH, '//*[@id="accounts_individual_checkbox"]')
    move_button_accounts_page = (By.XPATH, '//*[@id="select_account_move"]')
    # Edit Account
    edit_icon_for_account = (By.XPATH, '//*[@id="accounts_edit_btn"]')
    resend_invite_button = (By.XPATH, '//*[@id="invite_button"]')
    line_details_delete_bin = (By.XPATH, '//*[@id="action_delete"]')
    # edit_line_icon = (By.XPATH, '//*[@title="Edit Line"]')
    download_csv_icon = (By.XPATH, '//*[@id="accounts_down"]')

    def click_on_edit_account_line(self):
        self.wait_till_located(
            self.edit_account_line).click()

    def click_on_first_account_in_accounts(self):
        self.wait_till_located(
            self.first_account_in_accounts).click()

    def click_accounts_options_from_nav_menu(self, logger):
        self.wait_till_clickable(self.accounts_nav_menu_option).click()
        logger.info("Account logged in and clicked on account menu")

    def click_add_accounts_button(self):
        self.wait_till_clickable(self.add_account_btn).click()
        time.sleep(2)

    def get_checked_attribute_from_monitor_sms(self):
        return self.get_checked_attribute_from_element(
            self.custom_monitor_sms_flag)

    def get_no_records_found_text(self):
        no_records_text = self.wait_till_located(
            self.no_accounts_search_result).text
        return no_records_text

    def check_first_account_in_accounts(self):
        return self.is_element_displayed(
            self.first_account_in_accounts)

    def get_text_from_pagination(self):
        ele = self.find_element_on_web(self.pagination)
        number_of_page = ele.text
        actual_no_of_pages = number_of_page.split("-")[1].split()[0]
        return actual_no_of_pages

    # ravi
    # def click_accounts_options_from_nav_menu(self):
    #     self.wait_till_clickable(self.accounts_nav_menu_option).click()

    # def click_add_accounts_button(self):
    #     self.wait_till_clickable(self.add_account_btn).click()
    #     time.sleep(2)

    def enter_value_to_perform_search(self, search_text):
        self.wait_till_located(
            self.search_account_text_filed).send_keys(search_text)

    def click_on_search_button(self):
        self.wait_till_clickable(self.search_account_btn).click()

    def click_on_clear_search_button(self):
        self.wait_till_clickable(self.search_account_clear_btn).click()
        self.wait_till_clickable(self.search_account_btn)

    def get_the_search_account_count_result(self):
        self.wait_till_clickable(self.search_account_btn)
        display_text = self.wait_till_located(
            self.search_account_filtered_result_indicator
        ).text
        return display_text

    def get_org_id(self):
        ele = self.wait_till_located(self.org_id)
        return ele.text

    def get_org_name(self):
        ele = self.wait_till_located(self.org_name)
        return ele.text

    def click_dashboard_profile_arrow(self):
        self.wait_till_clickable(self.dashboard_profile_arrow).click()

    def click_sub_organisation_button(self):
        self.wait_till_clickable(self.sub_organisation).click()

    def click_profile(self):
        self.wait_till_clickable(self.profile).click()

    def get_profile_first_name(self):
        return self.get_value_attribute_from_element(self.profile_first_name)

    def get_profile_last_name(self):
        return self.get_value_attribute_from_element(self.profile_last_name)

    def get_profile_email_id(self):
        element = self.wait_till_located(self.profile_email_id)
        return element.text

    def add_account_enter_email_id_default_search_field(self, email):
        self.wait_till_located(self.search_account_text_filed).send_keys(email)

    def add_account_click_default_search_button(self):
        self.wait_till_clickable(self.default_search_btn).click()
        time.sleep(5)

    # dhanush
    def click_add_accounts_button(self):
        self.wait_till_clickable(self.add_account_btn).click()

    def enter_value_to_perform_search(self, search_text):
        self.wait_till_located(
            self.search_account_text_filed).send_keys(search_text)

    def click_on_search_button(self):
        self.wait_till_clickable(self.search_account_btn).click()
        self.wait_till_clickable(self.search_account_btn)

    def click_on_clear_search_button(self):
        self.wait_till_clickable(self.search_account_clear_btn).click()
        self.wait_till_clickable(self.search_account_btn)

    def click_on_delete_bin_from_line_details(self):
        self.wait_till_clickable(self.account_names_pane).click()
        self.wait_till_clickable(self.line_details_delete_bin).click()

    def click_on_edit_line(self):
        self.wait_till_clickable(self.account_names_pane).click()
        self.wait_till_clickable(self.edit_account_line).click()

    def get_status_of_account(self):
        status = self.wait_till_located(
            self.account_status_pane).get_attribute("title")
        return status

    def get_the_search_account_count_result(self):
        display_text = self.wait_till_located(
            self.search_account_filtered_result_indicator
        ).text
        return display_text

    def get_all_columns_on_search(self):
        result_dict = {
            "name": self.wait_till_located(self.account_names_pane).text,
            "email": self.wait_till_located(self.account_user_names_pane).text,
            "org": self.wait_till_located(self.account_organization_pane).text,
        }
        return result_dict

    def get_results_based_on_user_name_search(self):
        self.wait_till_located(self.account_names_pane)
        results = self.find_elements_on_web(self.account_names_pane)
        return results

    def get_results_based_on_user_email_search(self):
        results = self.find_elements_on_web(self.account_user_names_pane)
        return results

    def get_results_based_on_user_mml_search(self):
        self.wait_till_clickable(self.account_names_pane).click()
        return self.wait_till_located(self.account_user_multiline_pane).text

    def get_no_records_found_text(self):
        no_records_text = self.wait_till_located(
            self.no_accounts_search_result).text
        return no_records_text

    # Actions for Moving Account to different ORG
    def check_the_checkbox_to_select_the_account(self):
        self.wait_till_located(self.select_the_account).click()

    def click_on_move_button_from_accounts_page(self):
        self.wait_till_clickable(self.move_button_accounts_page).click()

    def click_on_edit_account(self):
        self.wait_till_clickable(self.edit_icon_for_account).click()

    def click_resend_invite_button(self):
        self.wait_till_clickable(self.resend_invite_button).click()

    def click_download_csv(self):
        self.wait_till_clickable(self.download_csv_icon).click()
        time.sleep(15)
