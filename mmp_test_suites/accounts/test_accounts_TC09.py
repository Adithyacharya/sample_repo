from utils.commons import read_data_from_config
from utils.commons import login_user_to_mmp
from pages.accounts.account_page import AccountPage
from pages.nav_menu_page import NavMenuPage
from pytest_check import check
import os
from utils.commons import custom_assert


def test_search_accounts(chrome_driver, logger, screen_shots_list):
    try:
        file = os.path.basename(os.path.abspath(__file__))
        config = read_data_from_config(file)
        logger.info("Login for MMP Portal")
        login_user_to_mmp(chrome_driver)
        account_page = AccountPage(chrome_driver)
        nav_menu = NavMenuPage(chrome_driver)
        nav_menu.go_to_accounts_tab()
        logger.info("Clicked Accounts option from side Nav Menu")
        logger.info("Launching Accounts Page")

        try:
            # Perform Search based on Names
            logger.info("*** Perform Search based on Names ***")

            test_case_data = config["TC9"]["search_based_on_name"]
            enter_search_text_and_click_search_button(
                test_case_data, account_page, logger
            )
            search_results = account_page.get_results_based_on_user_name_search()
            get_multiple_web_elements_checked(
                search_results, logger, test_case_data, "Name"
            )
            account_page.click_on_clear_search_button()
        except Exception as e:
            logger.info("[Exception] " + str(e))
            with check:
                custom_assert(
                    False,
                    "Failed Due to Exception while searching with Names",
                    file,
                    screen_shots_list,
                    chrome_driver,
                )
        try:
            # Negative Test, to check No records found
            logger.info("*** Perform Negative Search for No Records ***")

            test_case_data = config["TC9"]["search_for_no_record_text"]
            enter_search_text_and_click_search_button(
                test_case_data, account_page, logger
            )
            search_result_text = account_page.get_no_records_found_text()
            test_case_data = config["TC9"]["search_no_result"]
            get_singular_validations_done(search_result_text, test_case_data, logger)
            account_page.click_on_clear_search_button()
        except Exception as e:
            logger.info("[Exception] " + str(e))
            with check:
                custom_assert(
                    False,
                    "Failed Due to Exception while searching for No Records",
                    file,
                    screen_shots_list,
                    chrome_driver,
                )
        try:
            # Perform Search based on Email ID
            logger.info("*** Perform Search based on Email ***")
            test_case_data = config["TC9"]["search_based_on_email"]
            enter_search_text_and_click_search_button(
                test_case_data, account_page, logger
            )
            search_results = account_page.get_results_based_on_user_email_search()
            get_multiple_web_elements_checked(
                search_results, logger, test_case_data, "Email"
            )
            account_page.click_on_clear_search_button()
        except Exception as e:
            logger.info("[Exception] " + str(e))
            with check:
                custom_assert(
                    False,
                    "Failed Due to Exception while searching with Email ID",
                    file,
                    screen_shots_list,
                    chrome_driver,
                )
        try:
            # Perform Search based on MML Number
            logger.info("*** Perform Search based on MML Number ***")
            test_case_data = config["TC9"]["search_based_on_mml_number"]
            enter_search_text_and_click_search_button(
                test_case_data, account_page, logger
            )
            search_result_text = account_page.get_results_based_on_user_mml_search()
            get_singular_validations_done(search_result_text, test_case_data, logger)
            account_page.click_on_clear_search_button()
        except Exception as e:
            logger.info("[Exception] " + str(e))
            with check:
                custom_assert(
                    False,
                    "Failed Due to Exception while searching with MML Number",
                    file,
                    screen_shots_list,
                    chrome_driver,
                )
        try:
            # Perform Search based on Device Number
            logger.info("*** Perform Search based on Device Number ***")
            test_case_data = config["TC9"]["search_based_on_device_number"]
            enter_search_text_and_click_search_button(
                test_case_data, account_page, logger
            )

            test_case_data = config["TC9"]["search_based_on_mml_number"]
            search_result_text = account_page.get_results_based_on_user_mml_search()
            logger.info("Verifying the MML Number tagged to Device Number")
            get_singular_validations_done(search_result_text, test_case_data, logger)
            account_page.click_on_clear_search_button()
        except Exception as e:
            logger.info("[Exception] " + str(e))
            with check:
                custom_assert(
                    False,
                    "Failed Due to Exception while searching with Device Number",
                    file,
                    screen_shots_list,
                    chrome_driver,
                )
    except Exception as e:
        logger.info("[Exception] " + str(e))
        with check:
            custom_assert(
                False,
                "Failed Due to Exception while searching with Device Number",
                file,
                screen_shots_list,
                chrome_driver,
            )


def enter_search_text_and_click_search_button(test_case_data, account_page, logger):
    # test_case_data = config["TC9"]["search_based_on_device_number"]
    account_page.enter_value_to_perform_search(test_case_data)
    logger.info("Entered Value for search box")
    account_page.click_on_search_button()
    logger.info("Clicked Search Button")


def get_multiple_web_elements_checked(search_results, logger, test_case_data, msg):
    logger.info("Checking the searched " + msg + "s")
    # Out of many search results, we are validating the first 5 accounts
    for index, tuple in enumerate(search_results):
        if index == 2:
            break
        logger.info("Search Result : " + tuple.text + "| Test Data : " + test_case_data)
        with check:
            assert test_case_data.lower() in tuple.text.lower(), (
                f"Validation Failed "
                + msg
                + " given to search {test_case_data}, search results {tuple.text}"
            )


def get_singular_validations_done(search_result_text, test_case_data, logger):
    with check:
        logger.info(
            "Search Result : " + search_result_text + "| Test Data : " + test_case_data
        )
        assert (
            search_result_text.lower() == test_case_data.lower()
        ), f"Validation Failed name expecting {test_case_data}, but got {search_result_text}"
