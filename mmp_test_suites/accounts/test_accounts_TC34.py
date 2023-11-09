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


def has_ordered_subset(order_arr, input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)

    subset_length = len(result)
    for i in range(len(order_arr) - subset_length + 1):
        if all(result[j] == order_arr[i + j] for j in range(subset_length)):
            return True
    return False


def test_accounts_sort_by_status(chrome_driver, logger, screen_shots_list):
    file = os.path.basename(os.path.abspath(__file__))
    logger.info("********* TC34 : Accounts_sort_Status ********")
    login_user_to_mmp(chrome_driver)
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    account_filter = AccountFilter(chrome_driver)

    if (account_page.check_first_account_in_accounts() == True):
        account_filter.click_on_status_sort()
        time.sleep(10)
        logger.info("Sort the status")
        all_account_fn_ui = account_filter.get_all_status_from_account_list()
        flag_res = has_ordered_subset(dsc_order_status, all_account_fn_ui)
        with check:
            custom_assert(
                flag_res == True,
                "Error Order",
                file,
                screen_shots_list,
                chrome_driver,
            )
        account_filter.click_on_status_sort()
        time.sleep(10)
        logger.info("Sort the status")
        all_account_fn_ui1 = account_filter.get_all_status_from_account_list()
        has_ordered_subset(asc_order_status, all_account_fn_ui1)
        with check:
            custom_assert(
                flag_res == True,
                "Error Order",
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
