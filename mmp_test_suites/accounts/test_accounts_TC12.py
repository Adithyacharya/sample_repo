from utils.commons import read_data_from_config
from utils.commons import login_user_to_mmp
from utils.commons import get_move_report_content_from_csv
from utils.commons import rename_downloaded_report
from pytest_check import check
from pages.accounts.account_page import AccountPage
from pages.accounts.add_account_page import AddAccountPage
from pages.nav_menu_page import NavMenuPage
from pages.accounts.move_account_pop_up import MoveAccountPopUp
from pages.accounts.edit_account_page import EditAccountPage
from utils.commons import custom_assert
import time
import os


def test_move_user_to_sub_org_from_edit_account_screen(
    chrome_driver, logger, screen_shots_list
):
    try:
        file = os.path.basename(os.path.abspath(__file__))
        config = read_data_from_config(file)
        login_user_to_mmp(chrome_driver)
        logger.info(
            "********* TC12 : Move Account to a Sub Org from Edit Page ********"
        )
        account_page = AccountPage(chrome_driver)
        nav_menu = NavMenuPage(chrome_driver)
        move_pop_up = MoveAccountPopUp(chrome_driver)
        edit_account_page = EditAccountPage(chrome_driver)

        nav_menu.go_to_accounts_tab()
        # start of TC12
        account_page.enter_value_to_perform_search(config["TC12"]["move_org_email"])
        account_page.click_on_search_button()
        account_page.click_on_edit_account()

        edit_account_page.click_on_move_button_from_edit_accounts_page()

        sub_org_name = config["TC12"]["move_org_sub_org_name"]
        move_pop_up.select_sub_org_to_be_moved(sub_org_name)
        move_pop_up.click_on_move_button()
        move_pop_up.click_confirm_move_edit_accounts_page()
        move_pop_up.click_download_button_for_move_and_complete_with_done()

        # Again Search to Validate on UI
        account_page.click_on_clear_search_button()
        account_page.enter_value_to_perform_search(config["TC12"]["move_org_email"])
        account_page.click_on_search_button()

        results = account_page.get_all_columns_on_search()

        test_case_data = config["TC12"]["move_org_name"]
        custom_assert(
            test_case_data == results["name"],
            f"Validation Failed expected {test_case_data} but got {results['name']}",
            file,
            screen_shots_list,
            chrome_driver,
        )

        test_case_data = config["TC12"]["move_org_email"]
        custom_assert(
            test_case_data == results["email"],
            f"Validation Failed expected {test_case_data} but got {results['email']}",
            file,
            screen_shots_list,
            chrome_driver,
        )

        test_case_data = config["TC12"]["move_org_sub_org_name"]
        custom_assert(
            test_case_data == results["org"],
            f"Validation Failed expected {test_case_data} but got {results['org']}",
            file,
            screen_shots_list,
            chrome_driver,
        )

        report_file_name = config["TC12"]["report_file_name"]
        rename_downloaded_report("Account_move_status", report_file_name)
        report_dict_list = get_move_report_content_from_csv(logger, report_file_name)
        if len(report_dict_list) == 0:
            with check:
                assert False, "Validation failed as no content from report downloaded"
        else:
            report_dict = report_dict_list[0]
            # Validate the Account Move Satus Report
            with check:
                test_case_data = config["TC12"]["move_org_name"]
                assert (
                    test_case_data == report_dict["Name"]
                ), f"Validation Failed for Name expected {test_case_data} but got {report_dict['Name']}"
                test_case_data = config["TC12"]["move_org_organization"]
                assert (
                    test_case_data == report_dict["Current organization"]
                ), f"Validation Failed for Current organization expected {test_case_data} but got {report_dict['Current organization']}"
                test_case_data = config["TC12"]["move_org_sub_org_name"]
                assert (
                    test_case_data == report_dict["Destination organization"]
                ), f"Validation Failed for Destination organization expected {test_case_data} but got {report_dict['Destination organization']}"
                test_case_data = "Success"
                assert (
                    test_case_data == report_dict["Status"]
                ), f"Validation Failed for Status expected {test_case_data} but got {report_dict['Status']}"

    except Exception as e:
        logger.info("Exception occures " + str(e))
        with check:
            assert False, "Exception occured, hence test case is failed"
