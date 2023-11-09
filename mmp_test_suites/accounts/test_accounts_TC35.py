from utils.commons import login_user_to_mmp
from pages.accounts.account_page import AccountPage
from pages.accounts.add_account_page import AddAccountPage
from pages.accounts.account_filter import AccountFilter
import time
from pytest_check import check
import os
from utils.commons import custom_assert

dsc_order_status = ['Not invited', 'Invitation failed', 'Invited', 'Activated']
asc_order_status = ['Activated', 'Invited', 'Invitation failed', 'Not invited']


def assert_pagination(data, pagination_info):
    if data in pagination_info:
        with check:
            assert True, "Page displayed"
    else:
        with check:
            assert False, "Error in number of page displayed"


def test_account_sort_by_status(chrome_driver, logger, screen_shots_list):
    file = os.path.basename(os.path.abspath(__file__))
    logger.info("********* TC35 : Accounts_sort_Status ********")
    login_user_to_mmp(chrome_driver)
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    add_account_page = AddAccountPage(chrome_driver)
    account_filter = AccountFilter(chrome_driver)

    if (account_page.check_first_account_in_accounts() == True):
        pagination_info = add_account_page.getall_text_from_pagination()
        totalNumberOfUsers = int(pagination_info.split(" ")[3])
        if (totalNumberOfUsers > 200):
            logger.info("Check next page in account")
            add_account_page.click_on_next_page()
            time.sleep(10)
            pagination_info = add_account_page.getall_text_from_pagination()
            flag_res = assert_pagination("101-200", pagination_info)
            with check:
                custom_assert(
                    flag_res == True,
                    "Error Order",
                    file,
                    screen_shots_list,
                    chrome_driver,
                )
            add_account_page.click_on_prev_page()
            time.sleep(10)
            logger.info("Check prev page in account")
            pagination_info = add_account_page.getall_text_from_pagination()
            flag_res = assert_pagination("1-100", pagination_info)
            with check:
                custom_assert(
                    flag_res == True,
                    "Error Order",
                    file,
                    screen_shots_list,
                    chrome_driver,
                )
            add_account_page.enter_go_to_page("2")
            account_filter.click_on_jump_to_page()
            time.sleep(10)
            logger.info("Check jump to page in account")
            pagination_info = add_account_page.getall_text_from_pagination()
            flag_res = assert_pagination("101-200", pagination_info)
            with check:
                custom_assert(
                    flag_res == True,
                    "Error Order",
                    file,
                    screen_shots_list,
                    chrome_driver,
                )
        else:
            print("Accounts are less then 200")
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
