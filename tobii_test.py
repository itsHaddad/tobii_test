from selenium import webdriver
import sys


driver = webdriver.Chrome()
driver.implicitly_wait(10)

username=sys.argv[1]
password=sys.argv[2]
    
print(username, password)

link = 'https://sprint.tobiipro.com'



def tobii_login(driver, link, username, password):
    driver.get(link)
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()



def verify_login(driver):
    name = driver.find_element_by_class_name("gs-userbar__username").text
    print(name)
    print('something')
    return name

def log_out(driver):
    driver.find_element_by_class_name("gs-userbar__dropdown-icon").click()
    driver.find_element_by_xpath('//*[@class="gs-dropdown__item gs-dropdown__item--nolink gs-dropdown__item--red gs-dropdown__item-btn-logout"]').click()



tobii_login(driver, link, username, password)


name = verify_login(driver)
if (name == "Sprint Test"):
    print("Log in sucess")
else:
    print("Log in failed")

log_out(driver)