from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction
import time


class SubOrgPage(CommonAction):
    profile_icon_button = (By.XPATH, '//*[@id="dashboard_profile_icon"]/img')
    sub_orgnization_menu_option = (By.XPATH, '//*[@id="tab52"]')
    create_sub_org_button = (
        By.XPATH, '//*[text()="Create new Sub-Organization"]')
    sub_org_name_field = (By.XPATH, '//*[@id="organization_description"]')
    create_page_create_button = (By.XPATH, '//input[@type="submit"]')
    sub_org_name_first_list_item = (
        By.XPATH, '//*[@id="org_menu"]/li/ul/li[1]/a')
    sub_orgs_list = (By.XPATH, '//*[@id="org_menu"]/li/ul/li/a')
    all_sub_orgs_text = (
        By.XPATH, '//*[@id="so_suborgs"]//div/h3[text()="All Sub-Organizations"]')
    edit_button = (
        By.XPATH, '(//*[contains(@id,"so_main")]//div/button[text()="Edit"])[2]')
    edit_page_save_button = (By.XPATH, '//*[@id="edit_suborg_btn"]')

    delete_button = (
        By.XPATH, '(//*[contains(@id,"so_main")]//div/button[text()="Delete"])[1]')

    yes_button_pop_up_for_delete = (
        By.XPATH, '//*[@id="delete_organization_confirmation"]//div/button[text()="Yes"]')

    def click_profile_icon(self):
        self.wait_till_clickable(self.profile_icon_button).click()

    def select_sub_org_option(self):
        self.wait_till_clickable(self.sub_orgnization_menu_option).click()

    def click_create_sub_org_button(self):
        self.wait_till_clickable(self.create_sub_org_button).click()

    # Same method can be used for both Create Sub Org & Edit Sub Org
    def enter_sub_org_name(self, sub_org_name_param):
        self.wait_till_located(self.sub_org_name_field).clear()
        self.wait_till_located(
            self.sub_org_name_field).send_keys(sub_org_name_param)

    # This is used to create sub org in create sub org page
    def click_create_button(self):
        self.wait_till_clickable(self.create_page_create_button).click()

    def get_text_from_the_orgs_list_first_item(self):
        sub_org_text = self.wait_till_located(
            self.sub_org_name_first_list_item).text
        return sub_org_text

    def go_to_the_desired_sub_org(self, sub_org_name):
        elements = self.get_all_sub_orgs_list()
        for sub_org in elements:
            if sub_org.text == sub_org_name:
                sub_org.click()
                break

    def get_all_sub_orgs_list(self):
        self.wait_till_located(self.all_sub_orgs_text)
        elements = self.find_elements_on_web(self.sub_orgs_list)
        # return list(element_item.text for element_item in elements)
        return elements

    def get_all_sub_org_names(self):
        self.wait_till_located(self.all_sub_orgs_text)
        time.sleep(3)
        elements = self.find_elements_on_web(self.sub_orgs_list)
        return list(element_item.text for element_item in elements)

    def click_the_sub_org(self):
        self.wait_till_located(self.sub_org_name_first_list_item)
        self.wait_till_clickable(self.sub_org_name_first_list_item).click()

    def click_edit_sub_org(self):
        self.wait_till_clickable(self.edit_button).click()

    def click_save_button_edit_sub_org(self):
        self.wait_till_clickable(self.edit_page_save_button).click()

    def delete_the_sub_org(self):
        self.wait_till_clickable(self.delete_button).click()
        self.wait_till_clickable(self.yes_button_pop_up_for_delete).click()
