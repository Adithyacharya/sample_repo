from utils.commons import login_user_to_mmp
from utils.commons import read_data_from_config
from pages.accounts.account_page import AccountPage
from pages.accounts.add_account_page import AddAccountPage
import time
from pytest_check import check
import os
from utils.commons import custom_assert


def test_add_new_account(chrome_driver, logger, screen_shots_list):
    file = os.path.basename(os.path.abspath(__file__))
    config = read_data_from_config(file)
    login_user_to_mmp(chrome_driver)

    # Launch the Accounts Page
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    account_page.click_add_accounts_button()
    logger.info("****** TC3:Clicked on Add accounts page ********")

    # Launch Add Accounts Page
    add_account_page = AddAccountPage(chrome_driver)
    logger.info(
        "********* TC3:Launching Add Accounts Page and adding accounts *************"
    )
    add_account_page.add_account_enter_first_name(config["TC3"]["fname"])
    add_account_page.add_account_enter_last_name(config["TC3"]["lname"])
    add_account_page.add_account_enter_email_id(config["TC3"]["email_id"])
    add_account_page.add_account_click_application()
    add_account_page.add_account_select_app_from_drop_down()
    add_account_page.add_account_click_assign_number()
    add_account_page.add_account_assign_sls_number(config["TC3"]["mml_number3"])
    add_account_page.add_account_assign_forward_number(config["TC3"]["fwd_number"])
    add_account_page.add_account_click_compliance_group()
    add_account_page.add_account_assign_compliance_group()
    add_account_page.add_account_click_cancel_button()
    ele_displayed = add_account_page.check_element_displayed()
    print(ele_displayed)
    account_page.add_account_enter_email_id_default_search_field(
        config["TC3"]["email_id"]
    )
    account_page.add_account_click_default_search_button()
    time.sleep(2)
    no_account_msg = add_account_page.check_for_no_account_found()
    print(no_account_msg)
    with check:
        custom_assert(
            no_account_msg == config["TC3"]["error_msg"],
            "Error!, account's found",
            file,
            screen_shots_list,
            chrome_driver,
        )
