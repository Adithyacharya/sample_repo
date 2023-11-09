from utils.commons import login_user_to_mmp
from pages.accounts.account_page import AccountPage
from pages.nav_menu_page import NavMenuPage
from pages.reports.consumption_metrics import ConsumptionMetrics
import time
import os
from utils.commons import (read_data_from_config, getFormattedDate,
                           rename_downloaded_report, read_content_from_csv, custom_assert, getTodayDate)


def test_consumption_metrics_data_for_custom_date(chrome_driver, logger, screen_shots_list):
    logger.info(
        "********* Reports-TC11 : Consumption Metrics_Message data for Custom Date ********")
    file = os.path.basename(os.path.abspath(__file__))
    config = read_data_from_config(file)
    report_file_name = config["TC11"]["report_name"]
    downloaded_file_name = config["meta_info"]["consumption_data"]
    custom_date_duration = config["meta_info"]["custom_date_duration"]
    organization_name = config["meta_info"]["organization_name"]
    consumption_voice_report_name = config["meta_info"]["consumption_data_report_name"]

    login_user_to_mmp(chrome_driver)
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    consumption_metrics = ConsumptionMetrics(chrome_driver)
    nav_menu_page = NavMenuPage(chrome_driver)
    nav_menu_page.go_to_reports_tab()
    logger.info("Click on reports tab")
    consumption_metrics.click_on_consumption_metrics_menu()
    consumption_metrics.click_on_report_duration_dropdown()
    consumption_metrics.click_on_custom_data_option()
    formattedDate = getFormattedDate(custom_date_duration)
    todatDate = getTodayDate()
    consumption_metrics.enter_report_duration(formattedDate)
    consumption_metrics.click_on_calendar_apply()

    time.sleep(8)
    date_range = consumption_metrics.get_data_date_range()
    print("date_range", date_range)
    total_data_usage = consumption_metrics.get_total_data_usage()
    print("total_data_usage", total_data_usage)
    consumption_metrics.download_data_report_in_consumption_metrics()
    rename_downloaded_report(downloaded_file_name, report_file_name)
    report_dict = read_content_from_csv(logger, report_file_name)
    formattedDateArray = formattedDate.split("to")

    custom_assert(
        report_dict['Report name'] == consumption_voice_report_name,
        "Validation Failed for Report name in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
    custom_assert(
        todatDate in report_dict['Date/Time'],
        "Validation Failed for Date/Time in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
    custom_assert(
        report_dict['Duration'] == formattedDate,
        "Validation Failed for Duration in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
    custom_assert(
        report_dict['Organization Name'] == organization_name,
        "Validation Failed for Organization Name in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
    custom_assert(
        formattedDateArray[0].strip() == report_dict['From Timestamp'].strip(),
        "Validation Failed for From Timestamp in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
    custom_assert(
        todatDate == report_dict['To Timestamp'],
        "Validation Failed for To Timestamp in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
    custom_assert(
        report_dict['Total Data(MB)'] in total_data_usage,
        "Validation Failed for UI Total Data(MB) in CSV ",
        file,
        screen_shots_list,
        chrome_driver,
    )
    custom_assert(
        date_range == formattedDate,
        "Validation Failed for UI Date range in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
