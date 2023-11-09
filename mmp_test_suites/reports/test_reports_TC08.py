from utils.commons import login_user_to_mmp
from pages.accounts.account_page import AccountPage
from pages.nav_menu_page import NavMenuPage
from pages.reports.consumption_metrics import ConsumptionMetrics
from pages.reports.administrators_activity_page import AdminActivityReportsPage
from pytest_check import check
import time
import os
from utils.commons import (read_data_from_config,
                           getFormattedDate, rename_downloaded_report, read_content_from_csv, custom_assert, getTodayDate)


def test_consumption_metrics_data_message_for_7_days(chrome_driver, logger, screen_shots_list):
    logger.info(
        "********* Reports-TC08 : Consumption Metrics_Message for Last 7 days ********")
    file = os.path.basename(os.path.abspath(__file__))
    config = read_data_from_config(file)
    consumption_metrics = ConsumptionMetrics(chrome_driver)
    report_file_name = config["TC08"]["report_name"]
    downloaded_file_name = config["meta_info"]["consumption_SMS"]
    custom_date_duration = config["meta_info"]["last_7_days"]
    organization_name = config["meta_info"]["organization_name"]
    consumption_report_name = config["meta_info"]["consumption_SMS_report_name"]
    todatDate = getTodayDate()
    formattedDate = getFormattedDate(custom_date_duration)

    login_user_to_mmp(chrome_driver)
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    consumption_metrics = ConsumptionMetrics(chrome_driver)
    nav_menu_page = NavMenuPage(chrome_driver)
    nav_menu_page.go_to_reports_tab()
    consumption_metrics.click_on_consumption_metrics_menu()
    consumption_metrics.click_on_report_duration_dropdown()
    consumption_metrics.click_on_last_7_days_option()
    formattedDate = getFormattedDate(custom_date_duration)

    time.sleep(8)
    voice_date_range = consumption_metrics.get_messages_date_range()
    print("voice_date_range", voice_date_range)
    voice_incoming_data = consumption_metrics.get_messages_incoming_data()
    print("voice_incoming_data", voice_incoming_data)
    voice_outcoming_data = consumption_metrics.get_messages_outcoming_data()
    print("voice_outcoming_data", voice_outcoming_data)
    logger.info("Get all report details")
    consumption_metrics.download_message_report_in_consumption_metrics()
    rename_downloaded_report(downloaded_file_name, report_file_name)
    report_dict = read_content_from_csv(logger, report_file_name)
    formattedDateArray = formattedDate.split("to")

    custom_assert(
        report_dict['Report name'] == consumption_report_name,
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
        report_dict['Duration'] == 'Last 7 days',
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
        report_dict['Total messages Received'] == voice_incoming_data[1:-1],
        "Validation Failed for UI Total Calls Received in CSV ",
        file,
        screen_shots_list,
        chrome_driver,
    )
    custom_assert(
        report_dict['Total messages Sent'] == voice_outcoming_data[1:-1],
        "Validation Failed for UI Total Calls in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
    custom_assert(
        voice_date_range == formattedDate,
        "Validation Failed for UI Date range in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
