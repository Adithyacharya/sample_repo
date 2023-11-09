from utils.commons import read_data_from_config
from utils.commons import login_user_to_mmp
from pytest_check import check
from pages.nav_menu_page import NavMenuPage
from pages.reports.reports_menu import ReportsMenu
from pages.reports.activities_voice import VoiceActivity
from utils.commons import rename_downloaded_report
from utils.commons import get_data_from_voice_activity_report
import os
from utils.commons import custom_assert
from datetime import datetime


def test_voice_activity_all_call_type_all_call_mode(
    chrome_driver, logger, screen_shots_list
):
    try:
        file = os.path.basename(os.path.abspath(__file__))
        config = read_data_from_config(file)
        login_user_to_mmp(chrome_driver)
        logger.info("********* TC43 : Voice Activity filter using Date Range ********")

        nav_menu = NavMenuPage(chrome_driver)
        nav_menu.go_to_reports_tab()
        reports_menu = ReportsMenu(chrome_driver)
        reports_menu.click_on_activities_menu_item()
        reports_menu.click_on_voice_option_in_activities()

        voice_activity_page = VoiceActivity(chrome_driver)
        voice_activity_page.update_wait_time(30)
        # About to remove this entry of dates
        date_range = config["TC43"]["date_range"]
        voice_activity_page.enter_date_range(date_range)

        voice_activity_page.click_on_search_button()
        result = voice_activity_page.get_search_result()

        headers_on_ui = voice_activity_page.get_header_list_on_search()
        headers = config["report_activities_voice"]["header_list_on_ui"]
        test_case_data = [str(header.strip()) for header in headers.split(",")]

        logger.info("Header displayed on UI : " + str(headers_on_ui))
        logger.info("Header expected : " + str(test_case_data))
        custom_assert(
            headers_on_ui == test_case_data,
            f"Validation Failed as the headers obtained {headers_on_ui} and headers expected in test data {test_case_data}",
            file,
            screen_shots_list,
            chrome_driver,
        )

        assert result != "No records are found", "Failed as there are no search results"

        voice_activity_page.download_voice_report_activity()

        report_file_name = config["TC43"]["report_file_name"]
        rename_downloaded_report("Voice-activity-Report", report_file_name)
        (
            param_dict,
            fetched_header_list_csv,
            data_dict_list,
        ) = get_data_from_voice_activity_report(logger, report_file_name)

        filter_type = param_dict["Type"]
        report_name_from_csv = param_dict["Report name"]

        # Validate header list from CSV downloaded
        headers = config["TC43"]["header_list"]
        test_case_data = [str(header.strip()) for header in headers.split(",")]

        logger.info("Header list in CSV Expected " + str(test_case_data))
        logger.info(
            "Header list fetched from CSV downloaded " + str(fetched_header_list_csv)
        )
        with check:
            assert (
                test_case_data == fetched_header_list_csv
            ), f"Validation Failed as Expected Header List {str(test_case_data)} but got {str(fetched_header_list_csv)}"

        # Validate Report Name from CSV downloaded
        test_case_data = config["report_activities_voice"]["report_name"]
        logger.info("Report Name as per test data " + str(test_case_data))
        logger.info("Report Name in CSV downloaded " + str(report_name_from_csv))
        with check:
            assert (
                test_case_data.lower() == report_name_from_csv.lower()
            ), f"Validation Failed as Expected report type {str(test_case_data)} but got {str(report_name_from_csv)}"

        # Validate Type from CSV downloaded
        test_case_data = config["TC43"]["report_type"]
        logger.info("Type of report as per test data " + str(test_case_data))
        logger.info("Type of report in CSV downloaded " + str(filter_type))
        with check:
            assert (
                test_case_data == filter_type
            ), f"Validation Failed as Expected report type {str(test_case_data)} but got {str(filter_type)}"

        # Validate Presence of data from CSV downloaded
        logger.info("Voice Activity Report Data : " + str(data_dict_list))
        with check:
            assert (
                len(data_dict_list) != 0
            ), f"Validation Failed as Downloaded report doesn't have data"

        # Validate the obtained csv has only records with in the date range
        arr = date_range.split(" ")
        start_date = datetime.strptime(arr[0], "%d-%b-%Y")
        end_date = datetime.strptime(arr[2], "%d-%b-%Y")
        print(str(start_date) + " " + str(end_date))

        for voice_data in data_dict_list:
            timestamp = datetime.strptime(voice_data["Timestamp"], "%d-%b-%Y %H:%M:%S")
            timestamp_str = timestamp.strftime("%d-%b-%Y")
            fetched_timestamp = datetime.strptime(timestamp_str, "%d-%b-%Y")

            assert start_date <= fetched_timestamp <= end_date

    except Exception as e:
        logger.info("Exception occures " + str(e))
        with check:
            assert False, "Exception occured, hence test case is failed"
