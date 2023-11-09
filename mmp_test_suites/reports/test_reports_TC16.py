from utils.commons import login_user_to_mmp
from pages.accounts.account_page import AccountPage
from pages.nav_menu_page import NavMenuPage
from pages.reports.user_metrics import UserMetrics
import time
import os
from utils.commons import (read_data_from_config,
                           getFormattedDate, custom_assert)


def test_consumption_metrics_data_voice_for_last_cycle(chrome_driver, logger, screen_shots_list):
    logger.info(
        "********* Reports-TC16 :  ********")
    file = os.path.basename(os.path.abspath(__file__))
    config = read_data_from_config(file)
    login_user_to_mmp(chrome_driver)
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    nav_menu_page = NavMenuPage(chrome_driver)
    user_metrics = UserMetrics(chrome_driver)
    nav_menu_page.go_to_reports_tab()
    user_metrics.click_on_user_metrics()
    # Just for test data remove it later
    user_metrics.enter_name_in_user_metrics("Shabnam MS")
    formattedDate = getFormattedDate(6)
    user_metrics.enter_data_range_in_user_metrics(formattedDate)
    user_metrics.click_on_search_in_user_metrics()
    time.sleep(5)
    try:
        user_metrics.verify_heading_in_user_metrics()
        res = user_metrics.get_result_from_user_metrics()
        custom_assert(
            res["name"],
            "Name error in result of user metrix",
            file,
            screen_shots_list,
            chrome_driver,
        )
        custom_assert(
            res["multiline"],
            "Multiline error in result of user metrix",
            file,
            screen_shots_list,
            chrome_driver,
        )
        custom_assert(
            res["device"],
            "Device error in result of user metrix",
            file,
            screen_shots_list,
            chrome_driver,
        )
        custom_assert(
            res["email"],
            "Email error in result of user metrix",
            file,
            screen_shots_list,
            chrome_driver,
        )
        custom_assert(
            res["call_min"],
            "Call (min) error in result of user metrix",
            file,
            screen_shots_list,
            chrome_driver,
        )
        custom_assert(
            res["messages_num"],
            "Messages (num) error in result of user metrix",
            file,
            screen_shots_list,
            chrome_driver,
        )
        custom_assert(
            res["data_mb"],
            "Data (MB) error in result of user metrix",
            file,
            screen_shots_list,
            chrome_driver,
        )
    except Exception as e:
        logger.info("Error in search of user metrics" + str(e))
        custom_assert(
            False,
            "Error in search of user metrics",
            file,
            screen_shots_list,
            chrome_driver,
        )
