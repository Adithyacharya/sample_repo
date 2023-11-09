from utils.commons import login_user_to_mmp
from utils.commons import read_data_from_config
from pages.accounts.account_page import AccountPage
from pages.accounts.add_account_page import AddAccountPage
from utils.database_utils import get_data_from_table
import time
from pytest_check import check
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
    logger.info("******TC4:Clicked on Add accounts page********")

    # Launch Add Accounts Page
    add_account_page = AddAccountPage(chrome_driver)
    logger.info(
        "*********TC4:Launching Add Accounts Page and adding accounts*************"
    )
    add_account_page.add_account_enter_first_name(config["TC4"]["fname"])
    add_account_page.add_account_enter_last_name(config["TC4"]["lname"])
    add_account_page.add_account_enter_email_id(config["TC4"]["email_id"])
    add_account_page.add_account_click_application()
    add_account_page.add_account_select_app_from_drop_down()
    add_account_page.add_account_click_assign_number()
    add_account_page.add_account_assign_sls_number(config["TC4"]["mml_number4"])
    add_account_page.add_account_assign_forward_number(config["TC4"]["fwd_number"])
    # add_account_page.add_account_click_compliance_group()
    # add_account_page.add_account_assign_compliance_group()
    add_account_page.add_account_click_save_button()
    add_account_page.check_element_displayed()
    account_page.add_account_enter_email_id_default_search_field(
        config["TC4"]["email_id"]
    )
    account_page.add_account_click_default_search_button()

    mmp_invited = add_account_page.validate_account_notinvited_status()
    with check:
        custom_assert(
            mmp_invited == True,
            "Error! Invite status is wrong in accounts page",
            file,
            screen_shots_list,
            chrome_driver,
        )
    add_account_page.click_account_edit_button()
    time.sleep(2)
    # error
    add_account_page.click_social_msg_button()
    # add_account_page.click_social_msg_button()
    time.sleep(1)
    # error
    add_account_page.add_account_edit_account_save_invite_button()

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
    time.sleep(1)

    mmp_fname = add_account_page.validate_first_name()
    with check:
        custom_assert(
            mmp_fname == config["TC4"]["fname"],
            "Error in 'first name' in the added account ",
            file,
            screen_shots_list,
            chrome_driver,
        )
    mmp_lname = add_account_page.validate_last_name()
    with check:
        custom_assert(
            mmp_lname == config["TC4"]["lname"],
            "Error in 'last name' in the added account ",
            file,
            screen_shots_list,
            chrome_driver,
        )
    mmp_email_id = add_account_page.validate_email_id()
    with check:
        custom_assert(
            mmp_email_id == config["TC4"]["email_id"],
            "Error in 'emai id' in the added account ",
            file,
            screen_shots_list,
            chrome_driver,
        )
    add_account_page.click_reports_options_from_nav_menu()

    # Check in Database users DB

    sql = "select * from myid_authentications where email_address='{}'".format(
        config["TC4"]["email_id"]
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
    email_in_db = config["TC4"]["email_id"]
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
    ref_fname_value = config["TC4"]["fname"]
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
    ref_lname_value = config["TC4"]["lname"]
    with check:
        custom_assert(
            lname_in_db == ref_lname_value,
            f"MMP Validation failed expected first name {ref_lname_value} email present in Data base {lname_in_db}",
            file,
            screen_shots_list,
            chrome_driver,
        )
