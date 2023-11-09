from utils.commons import read_data_from_config
from utils.commons import login_user_to_mmp
from pytest_check import check
from pages.accounts.account_page import AccountPage
from pages.nav_menu_page import NavMenuPage
from pages.accounts.delete_account_pop_up import DeleteAccountPopUp
from utils.database_utils import get_data_from_table
import time
from utils.commons import custom_assert
import os


def test_delete_account_from_line_details_bin_icon(
    chrome_driver, logger, screen_shots_list
):
    try:
        file = os.path.basename(os.path.abspath(__file__))
        config = read_data_from_config(file)
        login_user_to_mmp(chrome_driver)
        logger.info(
            "********* TC17 : Delete Account from bin icon in line details ********"
        )

        account_page = AccountPage(chrome_driver)
        nav_menu = NavMenuPage(chrome_driver)
        delete_pop_up = DeleteAccountPopUp(chrome_driver)

        nav_menu.go_to_accounts_tab()
        account_page.enter_value_to_perform_search(config["TC17"]["email_to_delete"])
        account_page.click_on_search_button()
        account_page.click_on_delete_bin_from_line_details()
        delete_pop_up.enter_tag_name(config["TC17"]["tag"])
        delete_pop_up.click_proceed_button()
        logger.info("Deleted User using delete bin icon in line details")
        time.sleep(3)

        # Search Again for verification
        account_page.click_on_clear_search_button()
        account_page.enter_value_to_perform_search(config["TC17"]["email_to_delete"])
        account_page.click_on_search_button()
        search_result_text = account_page.get_no_records_found_text()
        test_case_data = config["TC9"]["search_no_result"]

        custom_assert(
            search_result_text.lower() == test_case_data.lower(),
            f"Validation Failed expected {test_case_data} but got {str(search_result_text)}",
            file,
            screen_shots_list,
            chrome_driver,
        )

        # Check in Database users DB for various tables
        user_db = config["meta_info"]["host_user_db"]
        common_db = config["meta_info"]["host_common_db"]
        email_param = config["TC17"]["email_to_delete"]
        mml_param = config["TC17"]["mml_number"]
        device_number_param = config["TC17"]["device_number"]

        # users Table
        sql = f"select count(*) as ctr from users where mobile_phone = '{device_number_param}'"
        check_table_result(logger, sql, user_db, "users")

        # device_owners table
        sql = f"select count(*) as ctr from device_owners where device_number = '{device_number_param}'"
        check_table_result(logger, sql, user_db, "device_owners")

        # phones table
        sql = f"select count(*) as ctr from phones where device_number = '{device_number_param}'"
        check_table_result(logger, sql, common_db, "phones")

        # myid_authentications table based on device_number
        sql = f"select count(*) as ctr from myid_authentications where phone_number = '{device_number_param}'"
        check_table_result(logger, sql, common_db, "myid_authentications")

        # myid_authentications table based on email
        sql = f"select count(*) as ctr from myid_authentications where email_address = '{email_param}'"
        check_table_result(logger, sql, common_db, "myid_authentications")

        # myidauth_users table based on email
        sql = f"select count(*) as ctr from myidauth_users where primary_number = '{mml_param}'"
        check_table_result(logger, sql, common_db, "myidauth_users")

        # device_owners table based on email
        sql = f"select count(*) as ctr from device_owners where virtual_number = '{mml_param}'"
        check_table_result(logger, sql, common_db, "device_owners")

        # users table based on email
        sql = f"select count(*) as ctr from users where primary_number = '{mml_param}'"
        check_table_result(logger, sql, common_db, "users")

        # user_indices table based on email
        sql = f"select count(*) as ctr from user_indices where skey = '{mml_param}'"
        check_table_result(logger, sql, common_db, "user_indices")
    except Exception as e:
        logger.info("Exception occures " + str(e))
        with check:
            assert False, "Exception occured, hence test case is failed"


def check_table_result(logger, sql, db_host, table_name):
    try:
        result_set = get_data_from_table(db_host, sql)
        logger.info("Executed Query in DB : " + sql)
        logger.info("Query Result : " + str(result_set))
        with check:
            assert result_set != None, "The query resulted in a None reference"
        db_value = result_set[0]["ctr"]
        with check:
            assert (
                str(db_value) == "0"
            ), f"MMP Validation failed as there is record in DB" + str(result_set[0])
    except Exception as e:
        logger.info(
            "Exception while fetching data from DB - "
            + db_host
            + " table name - "
            + table_name
        )
        with check:
            assert (
                False
            ), f"Exception while fetching data from DB - {db_host} in table - {table_name}"
