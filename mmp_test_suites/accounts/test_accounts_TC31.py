from utils.commons import login_user_to_mmp
from pages.accounts.account_page import AccountPage
from pages.accounts.add_account_page import AddAccountPage
from pages.accounts.account_filter import AccountFilter
import time
from pytest_check import check
import os
from utils.commons import custom_assert


def test_salesforce_filter(chrome_driver, logger, screen_shots_list):
    file = os.path.basename(os.path.abspath(__file__))
    logger.info("********* TC31 : Salesforce_Filter ********")
    login_user_to_mmp(chrome_driver)
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    account_filter = AccountFilter(chrome_driver)
    account_filter.click_filter()
    account_filter.click_active_filter()
    account_filter.click_on_sales_force_filter()
    account_filter.click_on_sales_force_filter_on()

    logger.info("Check for Salesforce filter on")
    if (account_page.check_first_account_in_accounts() == True):
        account_page.click_on_first_account_in_accounts()
        account_page.click_on_edit_account_line()
        account_filter.click_on_account_activity()
        salesforce_flag = account_filter.verify_salesforce()
        with check:
            custom_assert(
                salesforce_flag == True,
                "Salesforce flag is not present",
                file,
                screen_shots_list,
                chrome_driver,
            )
    else:
        response = account_page.get_no_records_found_text()
        with check:
            custom_assert(
                response == 'No account(s). are found',
                "Error in page",
                file,
                screen_shots_list,
                chrome_driver,
            )
    time.sleep(5)
    account_page.click_accounts_options_from_nav_menu(logger)
    account_filter.click_filter()
    account_filter.click_active_filter()

    logger.info("Check for Salesforce filter off")
    account_filter.click_on_sales_force_filter()
    account_filter.click_on_sales_force_filter_off()
    if (account_page.check_first_account_in_accounts() == True):
        account_page.click_on_first_account_in_accounts()
        account_page.click_on_edit_account_line()
        account_filter.click_on_account_activity()
        salesforce_flag = account_filter.verify_salesforce()
        with check:
            custom_assert(
                salesforce_flag == False,
                "Salesforce flag is present",
                file,
                screen_shots_list,
                chrome_driver,
            )
    else:
        response = account_page.get_no_records_found_text()
        with check:
            custom_assert(
                response == 'No account(s). are found',
                "Error in page",
                file,
                screen_shots_list,
                chrome_driver,
            )
