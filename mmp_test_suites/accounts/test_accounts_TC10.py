from utils.commons import read_data_from_config
from utils.commons import login_user_to_mmp
from pages.sub_org_page import SubOrgPage
from pytest_check import check
import pytest
from utils.commons import custom_assert
import os


def test_create_sub_org(chrome_driver, logger, screen_shots_list):
    try:
        file = os.path.basename(os.path.abspath(__file__))
        config = read_data_from_config(file)
        login_user_to_mmp(chrome_driver)
        logger.info("********* TC10 : Create/Edit/Delete Sub org ********")

        sub_org_page = SubOrgPage(chrome_driver)
        test_case_data = config["TC10"]["sub_org_name"]

        # Create Sub Org
        logger.info("Create a new sub org")
        sub_org_page.click_profile_icon()
        sub_org_page.select_sub_org_option()
        sub_org_page.click_create_sub_org_button()
        sub_org_page.enter_sub_org_name(test_case_data)
        sub_org_page.click_create_button()

        created_sub_org = sub_org_page.get_text_from_the_orgs_list_first_item()

        # Check the presence of the sub org created is on TOP
        logger.info("SUB Org from test data " + test_case_data)
        logger.info("SUB Org in Top position " + created_sub_org)
        custom_assert(
            created_sub_org == test_case_data,
            f"Validation Failed as the name obtained {created_sub_org} and name given in test data {test_case_data}",
            file,
            screen_shots_list,
            chrome_driver,
        )

        # Edit Sub Org
        logger.info("Updating the created sub org")
        sub_org_page.go_to_the_desired_sub_org(test_case_data)
        sub_org_page.click_edit_sub_org()
        test_case_data = test_case_data + "Test"
        sub_org_page.enter_sub_org_name(test_case_data)
        sub_org_page.click_save_button_edit_sub_org()
        edited_sub_org = sub_org_page.get_text_from_the_orgs_list_first_item()

        # Check the presence of the sub org edited is on TOP
        logger.info("SUB Org from test data " + test_case_data)
        logger.info("SUB Org Created " + edited_sub_org)
        custom_assert(
            edited_sub_org == test_case_data,
            f"Validation Failed as the name obtained {created_sub_org} and name given in test data {test_case_data}",
            file,
            screen_shots_list,
            chrome_driver,
        )

        # Delete the Sub Org
        sub_org_page.go_to_the_desired_sub_org(test_case_data)
        sub_org_name_list = sub_org_page.get_all_sub_org_names()
        logger.info("SUB Orgs list before deletion " + str(sub_org_name_list))
        sub_org_page.delete_the_sub_org()
        sub_org_name_list = sub_org_page.get_all_sub_org_names()

        logger.info("SUB Org deleted " + test_case_data)
        logger.info("SUB Orgs list after deletion " + str(sub_org_name_list))
        custom_assert(
            test_case_data not in sub_org_name_list,
            f"Validation Failed as the name obtained {created_sub_org} and name given in test data {test_case_data}",
            file,
            screen_shots_list,
            chrome_driver,
        )

    except Exception as e:
        logger.info("Exception occured " + str(e))
        with check:
            assert False, "Exception occured " + str(e)
