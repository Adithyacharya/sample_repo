from utils.commons import login_user_to_mmp
from pages.accounts.account_page import AccountPage
from pages.nav_menu_page import NavMenuPage
from pages.reports.consumption_metrics import ConsumptionMetrics
from datetime import datetime, timedelta
import time
import os
from utils.commons import (
    read_data_from_config, rename_downloaded_report, read_content_from_csv, custom_assert,
    getTodayDate)


def test_consumption_metrics_data_message_for_current_cycle(chrome_driver, logger, screen_shots_list):
    today_date = datetime.now()
    first_day_of_month = today_date.replace(day=1)
    next_month = today_date.replace(day=28) + timedelta(days=4)
    last_day_of_month = next_month - timedelta(days=next_month.day)
    first_day_formatted = first_day_of_month.strftime('%d-%b-%Y')
    last_day_formatted = last_day_of_month.strftime('%d-%b-%Y')
    print("First day of the month:", first_day_formatted)
    print("Last day of the month:", last_day_formatted)

    logger.info(
        "********* Reports-TC09 : Consumption Metrics_Voice for Currrent Cycle ********")
    file = os.path.basename(os.path.abspath(__file__))
    config = read_data_from_config(file)
    consumption_metrics = ConsumptionMetrics(chrome_driver)
    report_file_name = config["TC09"]["report_name"]
    downloaded_file_name = config["meta_info"]["consumption_SMS"]
    organization_name = config["meta_info"]["organization_name"]
    consumption_report_name = config["meta_info"]["consumption_SMS_report_name"]
    todatDate = getTodayDate()

    login_user_to_mmp(chrome_driver)
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    consumption_metrics = ConsumptionMetrics(chrome_driver)
    nav_menu_page = NavMenuPage(chrome_driver)
    nav_menu_page.go_to_reports_tab()
    consumption_metrics.click_on_consumption_metrics_menu()
    consumption_metrics.click_on_report_duration_dropdown()
    consumption_metrics.click_on_current_cycle_option()

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
        report_dict['Duration'] == "Current Cycle",
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
        first_day_formatted.strip() == report_dict['From Timestamp'].strip(),
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
        voice_date_range == f"{first_day_formatted} to {last_day_formatted}",
        "Validation Failed for UI Date range in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
