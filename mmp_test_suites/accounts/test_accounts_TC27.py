from utils.commons import login_user_to_mmp
from pages.accounts.account_page import AccountPage
from pages.accounts.add_account_page import AddAccountPage
from pages.accounts.account_filter import AccountFilter
from pytest_check import check
import os
from utils.commons import custom_assert


def test_status_filter(chrome_driver, logger, screen_shots_list):
    file = os.path.basename(os.path.abspath(__file__))
    logger.info("********* TC27 : Status_Filter ********")
    login_user_to_mmp(chrome_driver)
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    add_account_page = AddAccountPage(chrome_driver)
    account_filter = AccountFilter(chrome_driver)

    logger.info("Check for status Active")
    account_filter.click_filter()
    account_filter.click_active_filter()
    if (account_page.check_first_account_in_accounts() == True):
        no_of_account = account_page.get_text_from_pagination()
        status_activated_account = account_filter.get_list_of_status_activated()
        with check:
            custom_assert(
                str(no_of_account) == str(
                    len(status_activated_account)), "Error in the filter",
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

    logger.info("Check for status Invitation Failed")
    account_filter.click_on_clear_filter()
    account_filter.click_filter()
    add_account_page.click_on_invitation_failed()
    if (account_page.check_first_account_in_accounts() == True):
        no_of_account = account_page.get_text_from_pagination()
        status_invitation_failed_account = account_filter.get_list_of_status_invitation_failed()
        with check:
            custom_assert(
                str(no_of_account) == str(
                    len(status_invitation_failed_account)),
                "Error in the Invitation filter",
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

    logger.info("Check for status Invited")
    account_filter.click_on_clear_filter()
    account_filter.click_filter()
    add_account_page.click_on_invitated()
    if (account_page.check_first_account_in_accounts() == True):
        no_of_account = account_page.get_text_from_pagination()
        res = account_filter.get_list_of_status_invited()
        with check:
            custom_assert(
                str(no_of_account) == str(len(res)),
                "Error in the Invited filter",
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

    logger.info("Check for status Not Invited")
    account_filter.click_on_clear_filter()
    account_filter.click_filter()
    add_account_page.click_on_not_invitated()
    if (account_page.check_first_account_in_accounts() == True):
        no_of_account = account_page.get_text_from_pagination()
        res = account_filter.get_list_of_status_not_invited()
        with check:
            custom_assert(
                str(no_of_account) == str(
                    len(res)),
                "Error in the Not Invited filter",
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
