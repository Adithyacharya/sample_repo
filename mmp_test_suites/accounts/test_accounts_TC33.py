from utils.commons import login_user_to_mmp
from pages.accounts.account_page import AccountPage
from pages.accounts.add_account_page import AddAccountPage
from pages.accounts.account_filter import AccountFilter
import time
from pytest_check import check
import os
from utils.commons import custom_assert


def test_account_sort_by_organization(chrome_driver, logger, screen_shots_list):
    file = os.path.basename(os.path.abspath(__file__))
    logger.info("********* TC33 : Accounts_sort_Organization ********")
    login_user_to_mmp(chrome_driver)
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    account_filter = AccountFilter(chrome_driver)
    account_filter.click_on_org_sort()

    logger.info("sort the org in ascending(A-Z)")
    if (account_page.check_first_account_in_accounts() == True):
        # Get the number of accounts from the pagination
        num_accounts = account_page.get_text_from_pagination()
        filtered_org_names = account_filter.get_org_names(num_accounts)
        # Get account names and convert them to lowercase
        lowercase_org_names = [
            element.lower() for element in filtered_org_names]
        # Sort the lowercase account names
        sorted_lowercase_org_names = sorted(
            lowercase_org_names)
        with check:
            custom_assert(
                sorted_lowercase_org_names == lowercase_org_names,
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

    account_filter.click_on_org_sort()
    logger.info("sort the org in descending(Z-A)")
    if (account_page.check_first_account_in_accounts() == True):
        num_accounts = account_page.get_text_from_pagination()
        filtered_org_names = account_filter.get_org_names(num_accounts)
        lowercase_org_names = [element.lower()
                               for element in filtered_org_names]
        sorted_all_account_fn_reversed_in_lowercase = sorted(
            lowercase_org_names)
        sorted_lowercase_org_names = sorted_all_account_fn_reversed_in_lowercase[::-1]
        with check:
            custom_assert(
                sorted_lowercase_org_names == lowercase_org_names,
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
