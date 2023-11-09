from utils.commons import read_data_from_config
from utils.commons import login_user_to_mmp
from pytest_check import check
from pages.accounts.account_page import AccountPage
from pages.nav_menu_page import NavMenuPage
from utils.commons import rename_downloaded_report
from utils.commons import get_header_list_from_account_report
import os


# This test is for Account where MML Number is not assigned
def test_download_account_csv(chrome_driver, logger, screen_shots_list):
    try:
        file = os.path.basename(os.path.abspath(__file__))
        config = read_data_from_config(file)
        headers = config["TC19"]["header_list"]
        test_case_data = [str(header.strip()) for header in headers.split(",")]
        login_user_to_mmp(chrome_driver)
        logger.info("********* TC19 : Download Account CSV ********")

        account_page = AccountPage(chrome_driver)
        nav_menu = NavMenuPage(chrome_driver)

        nav_menu.go_to_accounts_tab()
        account_page.click_download_csv()
        report_file_name = config["TC19"]["report_file_name"]
        rename_downloaded_report("Accounts", report_file_name)
        fetched_list_from_csv = get_header_list_from_account_report(
            logger, report_file_name
        )
        logger.info("Header list in test data " + str(test_case_data))
        logger.info(
            "Header list fetched from CSV downloaded " + str(fetched_list_from_csv)
        )
        assert (
            test_case_data == fetched_list_from_csv
        ), f"Validation Failed as Expected Header List {str(test_case_data)} but got {str(fetched_list_from_csv)}"

    except Exception as e:
        logger.info("Exception occures " + str(e))
        with check:
            assert False, "Exception occured, hence test case is failed"
