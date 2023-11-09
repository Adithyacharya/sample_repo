from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)

#try:
 #   element = WebDriverWait(driver, 10).until(
  #      EC.presence_of_element_located((By.ID, '"//*[@id="email”]'))
   # )
#finally:


element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="email"]'))
    )
# click the element
element.click()
element.send_keys("Adithya")
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="pass"]'))
    )
element.click()
element.send_keys("Adithya")

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME,'login'))
    )



element.click()
element = driver.find_element(By.XPATH,'//*[@id="loginform"]/div[2]/div[2]')


def assertEqual(text, param, param1):
    if text==param:
        print(param1)




assertEqual(element.text,"The password that you've entered is incorrect. Forgotten password?", "pass")
driver.quit()




