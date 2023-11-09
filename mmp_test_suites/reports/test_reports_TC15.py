from utils.commons import login_user_to_mmp
from pages.accounts.account_page import AccountPage
from pages.nav_menu_page import NavMenuPage
from pages.reports.consumption_metrics import ConsumptionMetrics
import time
from datetime import datetime, timedelta
import os
from utils.commons import (read_data_from_config,
                           rename_downloaded_report, read_content_from_csv, custom_assert, getTodayDate)


def test_consumption_metrics_data_voice_for_last_cycle(chrome_driver, logger, screen_shots_list):
    today_date = datetime.now()
    first_day_of_month = today_date.replace(day=1)
    last_day_of_last_month = first_day_of_month - timedelta(days=1)
    first_day_of_last_month = last_day_of_last_month.replace(day=1)
    last_month_start_date = first_day_of_last_month.strftime('%d-%b-%Y')
    last_month_end_date = last_day_of_last_month.strftime('%d-%b-%Y')
    print("Last month start date:", last_month_start_date)
    print("Last month end date:", last_month_end_date)

    logger.info(
        "********* Reports-TC15 : Consumption Metrics_Voice data for Last Cycle ********")
    file = os.path.basename(os.path.abspath(__file__))
    config = read_data_from_config(file)
    report_file_name = config["TC15"]["report_name"]
    downloaded_file_name = config["meta_info"]["consumption_data"]
    organization_name = config["meta_info"]["organization_name"]
    consumption_voice_report_name = config["meta_info"]["consumption_data_report_name"]

    login_user_to_mmp(chrome_driver)
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    consumption_metrics = ConsumptionMetrics(chrome_driver)
    nav_menu_page = NavMenuPage(chrome_driver)
    nav_menu_page.go_to_reports_tab()
    consumption_metrics.click_on_consumption_metrics_menu()
    consumption_metrics.click_on_report_duration_dropdown()
    consumption_metrics.click_on_last_cycle_option()
    todatDate = getTodayDate()

    time.sleep(8)
    date_range = consumption_metrics.get_data_date_range()
    print("date_range", date_range)
    total_data_usage = consumption_metrics.get_total_data_usage()
    print("total_data_usage", total_data_usage)
    consumption_metrics.download_data_report_in_consumption_metrics()
    rename_downloaded_report(downloaded_file_name, report_file_name)
    report_dict = read_content_from_csv(logger, report_file_name)

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
        report_dict['Duration'] == "Last Cycle",
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
        last_month_start_date.strip() == report_dict['From Timestamp'].strip(),
        "Validation Failed for From Timestamp in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
    custom_assert(
        last_month_end_date == report_dict['To Timestamp'],
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
        date_range == f"{last_month_start_date} to {last_month_end_date}",
        "Validation Failed for UI Date range in CSV",
        file,
        screen_shots_list,
        chrome_driver,
    )
