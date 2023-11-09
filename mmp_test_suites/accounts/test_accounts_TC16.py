from utils.commons import read_data_from_config
from utils.commons import login_user_to_mmp
from pytest_check import check
from pages.accounts.account_page import AccountPage
from pages.nav_menu_page import NavMenuPage
from pages.accounts.edit_account_page import EditAccountPage
from utils.database_utils import get_data_from_table
import time
from utils.commons import custom_assert
import os


# This test is for Account where MML Number is not assigned
def test_delete_account_from_edit_account_page(
    chrome_driver, logger, screen_shots_list
):
    try:
        file = os.path.basename(os.path.abspath(__file__))
        config = read_data_from_config(file)
        login_user_to_mmp(chrome_driver)
        logger.info("********* TC16 : Delete Account from Edit Accout Page ********")

        account_page = AccountPage(chrome_driver)
        nav_menu = NavMenuPage(chrome_driver)
        edit_account_page = EditAccountPage(chrome_driver)

        nav_menu.go_to_accounts_tab()
        account_page.enter_value_to_perform_search(config["TC16"]["email_to_delete"])
        account_page.click_on_search_button()
        account_page.click_on_edit_account()

        edit_account_page.click_on_delete_button_from_edit_accounts_page()
        edit_account_page.click_confirm_delete()

        # Search Again for verification
        account_page.click_on_clear_search_button()
        account_page.enter_value_to_perform_search(config["TC16"]["email_to_delete"])
        account_page.click_on_search_button()
        search_result_text = account_page.get_no_records_found_text()
        test_case_data = config["TC9"]["search_no_result"]

        custom_assert(
            search_result_text.lower() == test_case_data.lower(),
            f"Validation Failed expected {test_case_data} but got {str(search_result_text)}",
            file,
            screen_shots_list,
            chrome_driver,
        )

        # Check in Database users DB
        sql = "select count(*) as ctr from myid_authentications where email_address='{}'".format(
            config["TC16"]["email_to_delete"]
        )
        result_set = get_data_from_table(config["meta_info"]["host_common_db"], sql)
        logger.info("Executed Query in DB : " + sql)
        logger.info("Query Result : " + str(result_set))
        with check:
            assert result_set != None, "The query resulted in a None reference"
        db_value = result_set[0]["ctr"]
        with check:
            assert (
                str(db_value) == "0"
            ), f"MMP Validation failed as there is record in DB " + str(result_set[0])

    except Exception as e:
        logger.info("Exception occures " + str(e))
        with check:
            assert False, "Exception occured, hence test case is failed"
