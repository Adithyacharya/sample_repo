import pytest
from selenium import webdriver
from utils.commons import read_data_from_config
import logging
import os
import time


@pytest.fixture(scope="module")
def chrome_driver():
    # Made as global to re-use current chrome driver instance to capture screenshot upon failures
    global driver
    # Create Options
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    # Changing the default download directory to data folder
    file_path = str(os.path.join(os.getcwd(), "data"))
    prefs = {"download.default_directory": file_path}
    options.add_experimental_option("prefs", prefs)
    # Create a WebDriver instance (Chrome, in this case)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    # Maximize the browser window for better visibility
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    config = read_data_from_config("meta")
    driver.get(config["meta_info"]["mmp_url"])
    driver.find_elements()

    # Provide the WebDriver instance to the test cases
    yield driver

    # Teardown: Close the WebDriver instance after all tests in the module have run
    driver.quit()


def pytest_html_report_title(report):
    report.title = "MMP Portal Automation Test Report"


# Establishes communication between test functions and pytest hooks in conftest
@pytest.fixture
def screen_shots_list():
    return []


# This hook is capture the screenshot upon failure and add the screenshot to the respective TC in report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    try:
        # Instantiate the pytest plugin manager for html
        pytest_html = item.config.pluginmanager.get_plugin("html")
        outcome = yield
        # get the current test case result
        report = outcome.get_result()
        extra = getattr(report, "extra", [])
        # At Setup phase or when framework calls it to update report we need to capture screenshot only on failure
        if report.when == "call" or report.when == "setup":
            xfail = hasattr(report, "wasxfail")
            if (report.skipped and xfail) or (report.failed and not xfail):
                # get all screenshots from current test case
                screen_shots = item.funcargs["screen_shots_list"]
                for i, file_name in enumerate(screen_shots):
                    # If file exist, then add the extra hyperlink that can show the screen shot captured
                    if file_name:
                        html = f'<a href="{file_name}">Failure Screenshot {i+1}</a>'
                        extra.append(pytest_html.extras.html(html))
                # Upon failure, capture the last screen where it is terminated
                file_name_with_out_path = report.nodeid.split("/")[-1]
                file = (
                    file_name_with_out_path.replace("::", "_")
                    + str(int(time.time()))
                    + ".png"
                )
                # Define the custom path where to store the screen shots
                file_name = os.path.join(
                    os.getcwd(), "test_execution_data", file)
                capture_screen_shot(file_name)
                if file_name:
                    html = f'<a href="{file_name}">Test case Termination Screenshot</a>'
                    extra.append(pytest_html.extras.html(html))
            report.extras = extra
    except Exception as e:
        print("Exception occured in Pytest makereport Hook")


# Method to capture screen shot


def capture_screen_shot(name):
    driver.get_screenshot_as_file(name)


@pytest.fixture(scope="session", autouse=True)
def make_log_file_ready():
    with open("./data/mmp_automation.log", "w") as file:
        pass


def clear_directory(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if (
            os.path.isfile(file_path)
            and filename != ".gitkeep"
            and filename != "mmp_automation.log"
        ):
            os.remove(file_path)


@pytest.fixture(scope="session", autouse=True)
def empty_data():
    clear_directory("./data")
    clear_directory("./test_execution_data")


@pytest.fixture(scope="session")
def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(f"./data/mmp_automation.log")
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
