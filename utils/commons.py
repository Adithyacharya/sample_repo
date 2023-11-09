import configparser
from pages.login_page import LoginForm
import os
import chardet
import csv
from pytest_check import check
import time
from datetime import datetime, timedelta


def login_user_to_mmp(chrome_driver):
    form = LoginForm(chrome_driver)
    config = read_data_from_config("meta")
    form.enter_user_email(config["meta_info"]["mmp_user"])
    form.click_continue_button()
    form.enter_user_password(config["meta_info"]["mmp_password"])
    form.click_login_button()


def custom_assert(assertion_condition, message, file, screenshots, driver):
    new_file = file + str(int(time.time())) + ".png"
    try:
        assert assertion_condition, message
    except AssertionError:
        file_name = os.path.join(os.getcwd(), "test_execution_data", new_file)
        driver.get_screenshot_as_file(file_name)
        screenshots.append(file_name)
        with check:
            assert False


def open_new_tab(chrome_driver):
    chrome_driver.execute_script("window.open('', '_blank');")
    chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
    return chrome_driver


def switch_back_to_original_tab(chrome_driver):
    chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
    return chrome_driver


def read_data_from_config(file):
    "Returns the test configuration object to be used in the tests."
    config_file = "./mmp_config.ini"
    if "accounts" in file:
        config_file = "./test_data_accounts.ini"
    elif "reports" in file:
        config_file = "./test_data_reports.ini"
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


def rename_downloaded_report(existing_file, desired_file):
    path = os.path.join(os.getcwd(), "data")
    files = os.listdir(path)
    file = next((f for f in files if f.startswith(existing_file)), None)
    if file is not None:
        existing_file_path = os.path.join(path, file)
        desired_file_path = os.path.join(path, desired_file)
        os.rename(existing_file_path, desired_file_path)


def get_move_report_content_from_csv(logger, file_name):
    account_move_dict = {}
    result_account_move_list = []
    try:
        file_path = os.path.join(os.getcwd(), "data", file_name)
        with open(file_path, "rb") as file:
            result = chardet.detect(file.read())
            enc = result["encoding"]
        with open(file_path, "r", encoding=enc) as f:
            reader = csv.reader(f)
            rows = list(reader)
            for i in range(2, len(rows)):
                account_move_dict = {k: v for k, v in zip(rows[1], rows[i])}
                result_account_move_list.append(account_move_dict)
    except Exception as e:
        logger.info("[Exception] while fetching data from CSV " + file_name + str(e))
    finally:
        return result_account_move_list


def read_content_from_csv(logger, file_name):
    data_list = []
    result_dict = {}
    try:
        file_path = os.path.join(os.getcwd(), "data", file_name)
        print("here")
        with open(file_path, "rb") as file:
            result = chardet.detect(file.read())
            enc = result["encoding"]
        with open(file_path, "r", encoding=enc) as f:
            print("ok")
            csvreader = csv.DictReader(f)
            for row in csvreader:
                data_list.append(row)

        result_dict = {}

        # Iterate through each dictionary in the list
        for item in data_list:
            # Extract the "sep=" key and empty key ('') value
            key = item.get("sep=")
            value = item.get("")

            # Add the key-value pair to the result_dict
            if key:
                result_dict[key] = value

    except Exception as e:
        logger.info("[Exception] while fetching data from CSV " + file_name + str(e))
    finally:
        print("result_dict", result_dict)
        return result_dict


def get_header_list_from_account_report(logger, file_name):
    account_header_list = []
    try:
        file_path = os.path.join(os.getcwd(), "data", file_name)
        with open(file_path, "rb") as file:
            result = chardet.detect(file.read())
            enc = result["encoding"]
        with open(file_path, "r", encoding=enc) as f:
            reader = csv.reader(f)
            rows = list(reader)
            for row in rows:
                if len(row) > 1 and row[0] == "Name":
                    account_header_list = row
                    break
    except Exception as e:
        logger.info("[Exception] while fetching data from CSV " + file_name + str(e))
    finally:
        return account_header_list


def get_data_from_voice_activity_report(logger, file_name):
    parameter_dict = {}
    voice_activity_header_list = []
    header_row = None
    voice_activity_dict_list = []
    data_flag = False
    try:
        file_path = os.path.join(os.getcwd(), "data", file_name)
        with open(file_path, "rb") as file:
            result = chardet.detect(file.read())
            enc = result["encoding"]
        with open(file_path, "r", encoding=enc) as f:
            reader = csv.reader(f)
            rows = list(reader)
            for row in rows:
                if data_flag == True:
                    voice_activity_dict = {
                        k.strip(): v.strip() for k, v in zip(header_row, row)
                    }
                    voice_activity_dict_list.append(voice_activity_dict)
                    continue
                if len(row) > 1 and row[0] == "Timestamp":
                    voice_activity_header_list = row
                    header_row = row
                    data_flag = True
                if len(row) > 1:
                    parameter_dict[row[0].strip()] = row[1].strip()

    except Exception as e:
        logger.info("[Exception] while fetching data from CSV " + file_name + str(e))
    finally:
        return parameter_dict, voice_activity_header_list, voice_activity_dict_list


def getFormattedDate(days_to_subtract):
    today_date = datetime.now()
    date_format = "%d-%b-%Y"
    formatted_date = today_date.strftime(date_format)
    days_behind = today_date - timedelta(days=int(days_to_subtract))
    actualDate = days_behind.strftime(date_format)
    return f"{actualDate} to {formatted_date}"


def getTodayDate():
    today_date = datetime.now()
    date_format = "%d-%b-%Y"
    return today_date.strftime(date_format)
