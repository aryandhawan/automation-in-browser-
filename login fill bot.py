from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://secure-retreat-92358.herokuapp.com/')

# input and stuff

first_name=driver.find_element(By.NAME,'fName')
first_name.send_keys('Aryan')
first_name.send_keys(Keys.TAB)

last_name=driver.find_element(By.NAME,'lName')
last_name.send_keys('Dhawan')
last_name.send_keys(Keys.TAB)

email_address=driver.find_element(By.NAME,'email')
email_address.send_keys('abcedeg@ghi.com')

submit=driver.find_element(By.CLASS_NAME,'btn.btn-lg.btn-primary.btn-block')
submit.click()

