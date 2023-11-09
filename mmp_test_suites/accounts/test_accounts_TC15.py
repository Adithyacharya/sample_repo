from utils.commons import read_data_from_config
from utils.commons import login_user_to_mmp
from utils.commons import get_move_report_content_from_csv
from utils.commons import rename_downloaded_report
from pytest_check import check
from pages.accounts.account_page import AccountPage
from pages.nav_menu_page import NavMenuPage
import time
from utils.commons import custom_assert
import os


def test_resend_invite_to_invitation_failed_account(
    chrome_driver, logger, screen_shots_list
):
    try:
        file = os.path.basename(os.path.abspath(__file__))
        config = read_data_from_config(file)
        login_user_to_mmp(chrome_driver)
        logger.info(
            "********* TC15 : Resend Invite to Invitation Failed account ********"
        )
        account_page = AccountPage(chrome_driver)
        nav_menu = NavMenuPage(chrome_driver)
        nav_menu.go_to_accounts_tab()

        account_page.enter_value_to_perform_search(
            config["TC15"]["resend_invite_email"]
        )
        account_page.click_on_search_button()
        account_page.check_the_checkbox_to_select_the_account()
        status = account_page.get_status_of_account()
        logger.info("Status of the Account before sending Invite " + str(status))

        account_page.click_resend_invite_button()
        time.sleep(3)
        account_page.click_on_clear_search_button()
        account_page.enter_value_to_perform_search(
            config["TC15"]["resend_invite_email"]
        )
        account_page.click_on_search_button()
        status = account_page.get_status_of_account()
        logger.info("Status of the Account After sending Invite " + str(status))

        test_case_data = config["TC15"]["post_account_status"]
        custom_assert(
            str(status.lower()) == test_case_data.lower(),
            f"Validation Failed expected {test_case_data} but got {str(status)}",
            file,
            screen_shots_list,
            chrome_driver,
        )

    except Exception as e:
        logger.info("Exception occures " + str(e))
        with check:
            assert False, "Exception occured, hence test case is failed"
