from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction
import time
import os


class AddMulitpleAccounts(CommonAction):
    csv_template_download = (
        By.XPATH, "//*[@id = 'myid_csv_form']//*[text() = 'CSV template']")
    multi_accts_app_dropdown = (
        By.XPATH, "//*[@id = 'multi_acc_update_div']//*[@data-toggle = 'dropdown']")
    multi_accts_app_dropdown_options = (
        By.XPATH, "//*[@id = 'multi_acc_update_div']//*[text() = 'MultiLine']")
    upload_csv_file = (By.XPATH, "//input[@type='file']")
    choose_org = (By.XPATH, "//*[@id = 'organization_id_mulOrg']")
    choose_org_dropdown_options = (
        By.XPATH, "//*[@x-placement = 'bottom-start']//*[text() = 'CDR Automation']")
    user_permission = (By.XPATH, "//*[@id = 'feature_pack_cosid_3']")
    user_permission_dropdown_select = (
        By.XPATH, "//*[@x-placement= 'top-start']//*[text() = 'default cos for org 2000 (Default)']")
    import_invite = (
        By.XPATH, "//*[@id = 'add_multiple_accounts_import_invite_btn']")
    import_only = (By.XPATH, "//*[@id = 'add_multiple_accounts_import_btn']")
    multi_accounts_cancel = (
        By.XPATH, "//*[@id = 'multiple_add_account_cancel']")
    uploaded_file_status = (By.XPATH, "//*[@id = 'users_common_res']")

    def click_choose_org_dropdown(self):
        self.wait_till_clickable(self.choose_org).click()
        time.sleep(2)

    def choose_org_dropdown_select(self):
        self.wait_till_clickable(self.choose_org_dropdown_options).click()

    def click_multi_accts_app_dropdown(self):
        self.wait_till_clickable(self.multi_accts_app_dropdown).click()
        time.sleep(2)

    def multi_accts_app_dropdown_select(self):
        self.wait_till_clickable(self.multi_accts_app_dropdown_options).click()
        time.sleep(1)

    def click_user_permission_dropdown(self):
        self.wait_till_clickable(self.user_permission).click()
        time.sleep(2)

    def user_permission_select(self):
        self.wait_till_clickable(self.user_permission_dropdown_select).click()
        time.sleep(1)

    def upload_file_button(self, file):
        self.wait_till_located(self.upload_csv_file).send_keys(file)

    def click_import_invite_button(self):
        self.wait_till_clickable(self.import_invite).click()
        time.sleep(11)

    def click_import_button(self):
        self.wait_till_clickable(self.import_only).click()
        time.sleep(5)

    def click_multi_accts_cancel(self):
        time.sleep(2)
        self.wait_till_clickable(self.multi_accounts_cancel).click()

    def check_uploaded_file_status(self):
        ele = self.wait_till_located(self.uploaded_file_status)
        return ele.text

    def download_CSV_template(self):
        self.wait_till_clickable(self.csv_template_download).click()
        time.sleep(2)
