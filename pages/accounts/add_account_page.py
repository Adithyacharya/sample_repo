from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction
import time


class AddAccountPage(CommonAction):

    add_account_first_name = (By.XPATH, '//*[@id="first_name"]')
    add_account_last_name = (By.XPATH, '//*[@id="last_name"]')
    add_account_email_id = (By.XPATH, '//*[@id="user_name"]')
    # email_id = (By.XPATH, '//*[@id="user_name"]')
    applications = (By.XPATH, '//*[@id="applications_myids"]')
    drop_down_app_select = (By.XPATH, '//*[text()=" MultiLine "]')
    assign_number = (By.XPATH, '//*[@id="assign_number_btn"]')
    sls_number = (By.XPATH, '//*[@id="sls_number_value"]')
    forward_number = (By.XPATH, '//*[@id="forwarding_number"]')
    compliance_group = (By.XPATH, '//*[@id="compliance_tag_options"]')
    drop_down_compliance_select = (
        By.XPATH, '//*[@x-placement="bottom-start"]//*[text()=" Unrestricted"]')
    save_invite_btn = (
        By.XPATH, '//*[@id = "myid_authentications_add_submit"]')
    save_btn = (By.XPATH, '//*[@id= "myid_authentications_add_submit"]')
    # cancel_btn = (By.XPATH, '//*[@id = "single_add_account_cancel"]')
    pagination = (By.XPATH, '//*[@id="mmp_pagination"]')
    pagination1 = (By.XPATH, '//*[@id="mmp_pagination"]//p')
    loading = (By.XPATH, '//*[text()="Loading"]')
    no_account_found = (By.XPATH, '//*[text()="No  account(s). are found"]')
    invitation_failed = (By.XPATH, '//*[text()="Invitation failed"]')
    invitated = (By.XPATH, '//*[text()="Invited"]')
    not_invited = (By.XPATH, '//*[text()="Not invited"]')
    call_recording_selector = (By.XPATH, '//*[@id="call_recording_selector"]')
    go_to_next = (By.XPATH, '//*[text()="Next "]')
    go_to_prev = (By.XPATH, '//*[text()=" Prev"]')
    go_to_page_number = (By.XPATH, '//*[@id="jumpto_page_number"]')

    # Ravi
    # add_account_first_name = (By.XPATH, '//*[@id="first_name"]')
    # add_account_last_name = (By.XPATH, '//*[@id="last_name"]')
    # add_account_email_id = (By.XPATH, '//*[@id="user_name"]')
    # applications = (By.XPATH, '//*[@id="applications_myids"]')
    # drop_down_app_select = (By.XPATH, '//*[text()=" MultiLine "]')
    # assign_number = (By.XPATH, '//*[@id="assign_number_btn"]')
    # sls_number = (By.XPATH, '//*[@id="sls_number_value"]')
    # forward_number = (By.XPATH, '//*[@id="forwarding_number"]')
    # compliance_group = (By.XPATH, '//*[@id="compliance_tag_options"]')
    # drop_down_compliance_select = (
    #     By.XPATH, '//*[@x-placement="bottom-start"]//*[text()=" Unrestricted"]')
    # save_invite_btn = (
    #     By.XPATH, '//*[@id = "myid_authentications_add_submit"]')
    edit_account_save_invite = (
        By.XPATH, "//*[@id = 'myid_authentications_edit_submit']")
    add_account_save_btn = (
        By.XPATH, '//*[@id = "myid_authentications_save_submit"]')
    add_account_cancel_btn = (
        By.XPATH, '//*[@id = "single_add_account_cancel"]')
    account_first_place = (By.XPATH, "(//*[@id='accounts'][1]//p)[1]")
    no_account_first_place = (
        By.XPATH, "//*[@id='accounts'][1]//*[contains(text(),'MMP-Automation')]")
    accounts_edit_btn = (By.XPATH, '//*[@id="accounts_edit_btn"]')
    account_invited_status = (
        By.XPATH, "//*[@id='accounts'][1]//*[@title ='Invited']")
    account_notinvited_status = (
        By.XPATH, "//*[@id='accounts'][1]//*[@title ='Not invited']")
    reports_nav_menu_option = (By.XPATH, '//*[@id="tab18"]')
    add_account_btn = (By.XPATH, '//*[@id="add_enterprise_user_inv"]')
    multiple_accounts = (By.XPATH, "//*[@id='multiple_account_tab']")
    social_messaging_btn = (
        By.XPATH, "//*[@id = 'custom_whatsapp_enable_checkbox']")
    no_accounts_found = (By.XPATH, "//*[@id = 'ent_invitation_user']")

    def add_account_enter_first_name(self, first_name):
        self.wait_till_located(
            self.add_account_first_name).send_keys(first_name)

    def add_account_enter_last_name(self, last_name):
        self.wait_till_located(self.add_account_last_name).send_keys(last_name)

    def add_account_enter_email_id(self, email):
        self.wait_till_located(self.add_account_email_id).send_keys(email)

    def add_account_click_application(self):
        self.wait_till_located(self.applications).click()

    def add_account_select_app_from_drop_down(self):
        self.wait_till_located(self.drop_down_app_select).click()

    def add_account_click_assign_number(self):
        self.wait_till_located(self.assign_number).click()

    def add_account_assign_sls_number(self, mml_number):
        self.wait_till_located(self.sls_number).send_keys(mml_number)
        time.sleep(3)
        self.click_enter_key()

    def add_account_assign_forward_number(self, fwd_number):
        self.wait_till_located(self.forward_number).send_keys(fwd_number)

    def add_account_click_compliance_group(self):
        time.sleep(1)
        self.wait_till_located(self.compliance_group).click()

    def add_account_assign_compliance_group(self):
        time.sleep(1)
        self.wait_till_located(self.drop_down_compliance_select).click()

    def add_account_click_save_invite_button(self):
        self.wait_till_clickable(self.save_invite_btn).click()

    def getall_text_from_pagination(self):
        ele = self.find_element_on_web(self.pagination1)
        return ele.text

    def wait_for_loading(self):
        self.wait_till_located(self.loading)

    def wait_for_no_account_found(self):
        self.wait_till_located(self.no_account_found)

    def click_on_invitated(self):
        self.wait_till_located(self.invitated).click()

    def click_on_not_invitated(self):
        self.wait_till_located(self.not_invited).click()

    def click_on_invitation_failed(self):
        self.wait_till_located(self.invitation_failed).click()

    def click_on_call_recording_selector(self):
        self.wait_till_located(self.call_recording_selector).click()

    def click_on_next_page(self):
        self.wait_till_located(self.go_to_next).click()

    def click_on_prev_page(self):
        self.wait_till_located(self.go_to_prev).click()

    def enter_go_to_page(self, page_number):
        self.wait_till_located(self.go_to_page_number).send_keys(page_number)

    # ravi
    def add_account_enter_first_name(self, first_name):
        self.wait_till_located(
            self.add_account_first_name).send_keys(first_name)

    def add_account_enter_last_name(self, last_name):
        self.wait_till_located(self.add_account_last_name).send_keys(last_name)

    def add_account_enter_email_id(self, email):
        self.wait_till_located(self.add_account_email_id).send_keys(email)

    def add_account_click_application(self):
        self.wait_till_located(self.applications).click()

    def add_account_select_app_from_drop_down(self):
        self.wait_till_located(self.drop_down_app_select).click()

    def add_account_click_assign_number(self):
        self.wait_till_located(self.assign_number).click()

    def add_account_assign_sls_number(self, mml_number):
        self.wait_till_located(self.sls_number).send_keys(mml_number)
        time.sleep(3)
        self.click_enter_key()

    def add_account_assign_forward_number(self, fwd_number):
        self.wait_till_located(self.forward_number).send_keys(fwd_number)

    # def add_account_click_compliance_group(self):
    #     time.sleep(1)
    #     self.wait_till_located(self.compliance_group).click()

    # def add_account_assign_compliance_group(self):
    #     time.sleep(1)
    #     self.wait_till_located(self.drop_down_compliance_select).click()

    # def add_account_click_save_invite_button(self):
    #     self.wait_till_clickable(self.save_invite_btn).click()

    def add_account_edit_account_save_invite_button(self):
        self.wait_till_clickable(self.edit_account_save_invite).click()

    def check_account_presence_first_place(self):
        time.sleep(2)
        ele = self.wait_till_located(self.account_first_place)
        return (ele.text)

    def check_no_account_presence_first_place(self):
        return self.is_element_displayed(self.no_account_first_place)

    def click_account_edit_button(self):
        self.wait_till_clickable(self.accounts_edit_btn).click()
        time.sleep(2)

    def validate_first_name(self):
        return self.get_value_attribute_from_element(self.add_account_first_name)

    def validate_last_name(self):
        return self.get_value_attribute_from_element(self.add_account_last_name)

    def validate_edited_last_name(self):
        return self.get_value_attribute_from_element(self.add_account_last_name)

    def validate_email_id(self):
        return self.get_value_attribute_from_element(self.add_account_email_id)

    def validate_account_invited_status(self):
        time.sleep(2)
        return self.is_element_displayed(self.account_invited_status)

    def validate_account_notinvited_status(self):
        time.sleep(2)
        return self.is_element_displayed(self.account_notinvited_status)

    def click_reports_options_from_nav_menu(self):
        self.wait_till_clickable(self.reports_nav_menu_option).click()
        time.sleep(3)

    def add_account_click_save_button(self):
        self.wait_till_clickable(self.add_account_save_btn).click()
        time.sleep(3)

    def add_account_click_cancel_button(self):
        self.wait_till_clickable(self.add_account_cancel_btn).click()
        time.sleep(2)

    def check_element_displayed(self):
        time.sleep(2)
        return self.is_element_displayed(self.add_account_btn)

    def click_social_msg_button(self):
        self.wait_till_clickable(self.social_messaging_btn).click()

    def click_multiple_accounts_tab(self):
        self.wait_till_clickable(self.multiple_accounts).click()
        time.sleep(2)

    def check_for_no_account_found(self):
        time.sleep(2)
        ele = self.wait_till_located(self.no_accounts_found)
        return ele.text
