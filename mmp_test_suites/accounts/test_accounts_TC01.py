from utils.commons import login_user_to_mmp
from utils.commons import read_data_from_config
from pages.accounts.account_page import AccountPage
from pages.accounts.add_account_page import AddAccountPage
from utils.database_utils import get_data_from_table
from pytest_check import check
import time
import os
from utils.commons import custom_assert


def test_add_new_account(chrome_driver, logger, screen_shots_list):
    file = os.path.basename(os.path.abspath(__file__))
    config = read_data_from_config(file)
    login_user_to_mmp(chrome_driver)

    # Launch the Accounts Page
    account_page = AccountPage(chrome_driver)
    account_page.click_accounts_options_from_nav_menu(logger)
    account_page.click_add_accounts_button()
    logger.info("******TC1:Clicked on Add accounts page********")

    # Launch Add Accounts Page
    add_account_page = AddAccountPage(chrome_driver)
    logger.info(
        "*********TC1:Launching Add Accounts Page and adding accounts*************"
    )
    add_account_page.add_account_enter_first_name(config["TC1"]["fname"])
    logger.info("Enter First name")
    add_account_page.add_account_enter_last_name(config["TC1"]["lname"])
    add_account_page.add_account_enter_email_id(config["TC1"]["email_id"])
    add_account_page.add_account_click_application()
    add_account_page.add_account_select_app_from_drop_down()
    add_account_page.add_account_click_assign_number()
    time.sleep(2)
    add_account_page.add_account_assign_sls_number(config["TC1"]["mml_number1"])

    add_account_page.add_account_assign_forward_number(config["TC1"]["fwd_number"])
    add_account_page.add_account_click_compliance_group()
    add_account_page.add_account_assign_compliance_group()
    add_account_page.add_account_click_save_invite_button()
    time.sleep(5)
    account_page.click_accounts_options_from_nav_menu(logger)
    time.sleep(3)

    mmp_email_fplace = add_account_page.check_account_presence_first_place()
    with check:
        custom_assert(
            mmp_email_fplace == config["TC1"]["fname"] + " " + config["TC1"]["lname"],
            "Error: no Account present in first place",
            file,
            screen_shots_list,
            chrome_driver,
        )

    account_page.add_account_enter_email_id_default_search_field(
        config["TC1"]["email_id"]
    )
    account_page.add_account_click_default_search_button()

    mmp_invited = add_account_page.validate_account_invited_status()
    with check:
        custom_assert(
            mmp_invited == True,
            "Error! Invite status is wrong in accounts page",
            file,
            screen_shots_list,
            chrome_driver,
        )

    add_account_page.click_account_edit_button()
    time.sleep(3)

    mmp_fname = add_account_page.validate_first_name()
    with check:
        custom_assert(
            mmp_fname == config["TC1"]["fname"],
            "Error in 'first name' in the added account ",
            file,
            screen_shots_list,
            chrome_driver,
        )

    mmp_lname = add_account_page.validate_last_name()
    with check:
        custom_assert(
            mmp_lname == config["TC1"]["lname"],
            "Error in 'last name' in the added account ",
            file,
            screen_shots_list,
            chrome_driver,
        )

    mmp_email_id = add_account_page.validate_email_id()
    with check:
        custom_assert(
            mmp_email_id == config["TC1"]["email_id"],
            "Error in 'emai id' in the added account ",
            file,
            screen_shots_list,
            chrome_driver,
        )
    # # Admin Activity Report

    # reports_page.click_administrators_activity_reports()
    # logger.info("*********TC1:Clicked on administrators_activity ************")
    # reports_page.click_reports_activtiy_dropdown()
    # reports_page.click_activity_dropdown_option_all()
    # reports_page.click_activity_dropdown_option_write()
    # reports_page.click_reports_event_type_dropdown()
    # reports_page.click_event_type_dropdown_option_all()
    # reports_page.reports_event_type_searchfield_enter_value(config['test_data']['reports_event_type'])
    # reports_page.click_event_type_dropdown_option_add_account()
    # reports_page.click_reports_search_by_string()
    # reports_page.enter_activity_details_email_id(config['TC1']['email_id'])
    # reports_page.click_administrator_activity_search_button()

    # Check in Database users DB

    sql = "select * from myid_authentications where email_address='{}'".format(
        config["TC1"]["email_id"]
    )
    result_set = get_data_from_table(config["meta_info"]["host_common_db"], sql)
    logger.info("Executed Query in DB : " + sql)
    with check:
        custom_assert(
            result_set != None,
            "The query resulted in a None reference ",
            file,
            screen_shots_list,
            chrome_driver,
        )

    # Checking presence of the record in DB
    email_in_db = config["TC1"]["email_id"]
    with check:
        custom_assert(
            len(result_set) != 0,
            f"The query resulted with 0 records from DB, expecting record with email {email_in_db}",
            file,
            screen_shots_list,
            chrome_driver,
        )

    logger.info("Obtained Result : " + str(result_set))

    # Email Address Validation
    ref_email_value = result_set[0]["email_address"]
    with check:
        custom_assert(
            ref_email_value == email_in_db,
            f"MMP Validation failed expected email address {ref_email_value} email present in Data base {email_in_db}",
            file,
            screen_shots_list,
            chrome_driver,
        )

    # First Name Validation
    fname_in_db = result_set[0]["first_name"]
    ref_fname_value = config["TC1"]["fname"]
    with check:
        custom_assert(
            fname_in_db == ref_fname_value,
            f"MMP Validation failed expected first name {ref_fname_value} email present in Data base {fname_in_db}",
            file,
            screen_shots_list,
            chrome_driver,
        )

    # Last Name Validation
    lname_in_db = result_set[0]["last_name"]
    ref_lname_value = config["TC1"]["lname"]
    with check:
        custom_assert(
            lname_in_db == ref_lname_value,
            f"MMP Validation failed expected first name {ref_lname_value} email present in Data base {lname_in_db}",
            file,
            screen_shots_list,
            chrome_driver,
        )
