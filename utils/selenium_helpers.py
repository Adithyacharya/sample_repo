from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class CommonAction:
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 15)

    def update_wait_time(self, time):
        self._wait = WebDriverWait(self.driver, time)

    def wait_till_located(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def wait_till_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def click_enter_key(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()

    def find_element_on_web(self, locator):
        return self.driver.find_element(*locator)

    def find_elements_on_web(self, locator):
        return self.driver.find_elements(*locator)

    def is_element_displayed(self, locator):
        time.sleep(10)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return element.is_displayed()
        except Exception as e:
            # print("error is", e)
            return False

    def get_checked_attribute_from_element(self, locator):
        element = self.driver.find_element(*locator)
        attribute_value = element.get_attribute("checked")
        print("attribute_value is", attribute_value)
        return attribute_value

    def get_title(self, locator):
        elements = self.driver.find_elements(*locator)
        title_attributes = []
        for element in elements:
            title_attribute = element.get_attribute("title")
            title_attributes.append(title_attribute)
        return title_attributes

    def get_all_names(self, locator, no_of_account):
        elements = self.driver.find_elements(*locator)
        number_of_acc = int(no_of_account)
        print("no_of_account", number_of_acc)
        names = [element.text.split()[0] for element in elements[:number_of_acc]]
        print("List is", names)
        return names

    def scroll_till_visible(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    # ravi
    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        print(element.text)
        return element.text

    def get_value_attribute_from_element(self, locator):
        element = self.driver.find_element(*locator)
        attribute_value = element.get_attribute("value")
        # print("attribute_value is", attribute_value)
        return attribute_value
