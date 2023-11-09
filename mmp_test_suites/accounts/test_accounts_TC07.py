from utils.commons import login_user_to_mmp
from utils.commons import read_data_from_config
from pages.accounts.account_page import AccountPage
from pages.accounts.add_account_page import AddAccountPage
from pages.accounts.add_multiple_account_page import AddMulitpleAccounts
from pytest_check import check
import os
import time
from utils.commons import custom_assert


def test_add_new_account(chrome_driver, logger, screen_shots_list):
    file = os.path.basename(os.path.abspath(__file__))
    config = read_data_from_config(file)
    login_user_to_mmp(chrome_driver)

    # Launch the Accounts Page
    account_page = AccountPage(chrome_driver)
    add_account_page = AddAccountPage(chrome_driver)
    multi_accounts = AddMulitpleAccounts(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    account_page.click_add_accounts_button()
    logger.info("****** TC7:Clicked on Add accounts page ********")

    # Launch Add Accounts Page
    add_account_page.click_multiple_accounts_tab()
    logger.info("****** TC7:Clicked on Multiple accounts tab ********")
    multi_accounts.click_choose_org_dropdown()
    multi_accounts.choose_org_dropdown_select()
    multi_accounts.click_multi_accts_app_dropdown()
    multi_accounts.multi_accts_app_dropdown_select()
    multi_accounts.click_user_permission_dropdown()
    multi_accounts.user_permission_select()
    file_path = os.path.join(
        os.getcwd(), "templates", config["meta_info"]["file_path3"]
    )
    multi_accounts.upload_file_button(file_path)
    time.sleep(1)
    logger.info("******* TC7: Uploaded accounts CSV file ********")
    multi_accounts.click_multi_accts_cancel()
    account_page.click_accounts_options_from_nav_menu(logger)

    account_page.add_account_enter_email_id_default_search_field(
        config["TC7"]["email_id"]
    )
    account_page.add_account_click_default_search_button()
    no_account_msg = add_account_page.check_for_no_account_found()
    print(no_account_msg)
    with check:
        custom_assert(
            no_account_msg == config["TC7"]["error_msg"],
            "Error!, account's found",
            file,
            screen_shots_list,
            chrome_driver,
        )
