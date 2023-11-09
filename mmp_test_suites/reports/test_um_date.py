from utils.commons import read_data_from_config
from utils.commons import login_user_to_mmp
from pytest_check import check
from pages.nav_menu_page import NavMenuPage
from pages.reports.reports_menu import ReportsMenu
from pages.reports.activities_message import MessageActivity
from utils.commons import rename_downloaded_report, get_data_from_voice_activity_report
import os
from utils.commons import custom_assert
import time


def test_message_activity_all_messages_type(chrome_driver, logger, screen_shots_list):
    try:
        file = os.path.basename(os.path.abspath(__file__))
        config = read_data_from_config(file)
        login_user_to_mmp(chrome_driver)
        logger.info(
            "********* TC45 : Message Activity filter using Type as All Messages ********"
        )

        nav_menu = NavMenuPage(chrome_driver)
        nav_menu.go_to_reports_tab()

        reports_menu = ReportsMenu(chrome_driver)
        reports_menu.click_on_user_metrics()
        reports_menu.clear_and_enter_date_user_metric("22-Sep-2023 to 25-Sep-2023")
        time.sleep(10)

    except Exception as e:
        logger.info("Exception occures " + str(e))
        with check:
            assert False, "Exception occured, hence test case is failed"
