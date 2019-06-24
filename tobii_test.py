from selenium import webdriver

import getpass, argparse

parser = argparse.ArgumentParser()
parser.add_argument("username")
args = parser.parse_args()
username = args.username
password = getpass.getpass()

with open('info.txt') as f:
    content = f.readlines()
info = [x.strip() for x in content]

link = info[0]
user_name = info[1]
def tobii_navigate(driver, link):
    driver.get(link)
def tobii_login(driver, username, password):
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()

def verify_login(driver):
    name = driver.find_element_by_class_name("gs-userbar__username").text
    return name

def log_out(driver):
    driver.find_element_by_class_name("gs-userbar__dropdown-icon").click()
    driver.find_element_by_xpath('//*[@class="gs-dropdown__item gs-dropdown__item--nolink gs-dropdown__item--red gs-dropdown__item-btn-logout"]').click()


if __name__ == "__main__":
    # initiate driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    print(username)
    # run the test
    tobii_navigate(driver, link)
    tobii_login(driver, username, password)
    name = verify_login(driver)
    if (name == user_name):
        print("Login sucess")
        log_out(driver)
    else:
        print("Login failed")

    
