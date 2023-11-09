from utils.commons import login_user_to_mmp
from pages.accounts.account_page import AccountPage
from pages.accounts.account_filter import AccountFilter
import time
from pytest_check import check
import os
from utils.commons import custom_assert


def test_accounts_sort_by_name(chrome_driver, logger, screen_shots_list):
    file = os.path.basename(os.path.abspath(__file__))
    logger.info("********* TC32 : Accounts_sort_Name ********")
    login_user_to_mmp(chrome_driver)
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    account_filter = AccountFilter(chrome_driver)
    account_filter.click_on_name_sort()

    logger.info("sort the names in ascending(A-Z)")
    if (account_page.check_first_account_in_accounts() == True):
        # Get the number of accounts from the pagination
        num_accounts = account_page.get_text_from_pagination()
        # Get account names and convert them to lowercase
        filtered_account_names = account_filter.get_account_names(num_accounts)
        lowercase_account_names = [name.lower()
                                   for name in filtered_account_names]
        # Sort the lowercase account names
        sorted_lowercase_account_names = sorted(lowercase_account_names)
        with check:
            custom_assert(
                sorted_lowercase_account_names == lowercase_account_names,
                "Error in Sorting name",
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

    account_filter.click_on_name_sort()
    logger.info("sort the names in descending(Z-A)")
    if (account_page.check_first_account_in_accounts() == True):
        num_accounts = account_page.get_text_from_pagination()
        # Convert to lower case, Sort it and Compare it
        reversed_account_names = account_filter.get_account_names(num_accounts)
        time.sleep(10)
        lower_case_reversed_account_names = [
            element.lower() for element in reversed_account_names]
        sorted_all_account_fn_reversed_in_lowercase = sorted(
            lower_case_reversed_account_names)
        lowercase_sorted_reversed_account_names = sorted_all_account_fn_reversed_in_lowercase[
            ::-1]
        with check:
            custom_assert(
                lowercase_sorted_reversed_account_names == lower_case_reversed_account_names,
                "Error in Sorting name",
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
