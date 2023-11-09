import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-javascript")
# chrome_options.add_argument("--disable-images")  # Disable images
# chrome_options.add_argument("--headless")  # Run in headless mode
 chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking

# Disable JavaScript

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(10)
iframe = driver.find_element(By.ID, "webklipper-publisher-widget-container-notification-frame")
driver.switch_to.frame(iframe)
close_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'webklipper-publisher-widget-container-notification-close-div'))
)
close_btn.click()

close_btn1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//span[@class="commonModal__close"]'))
)
close_btn1.click()

round_trip = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@data-cy="roundTrip"]'))
)
round_trip.click()

From_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//label[@for="fromCity"]'))
)
From_btn.click()

From = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@aria-autocomplete="list"]'))
)
From.send_keys("Mumbai")

time.sleep(15)
driver.quit()




