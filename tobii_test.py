from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
profilename = info[1]

def tobii_navigate(driver, link):
    driver.get(link)
    
def tobii_login(driver, username, password):
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()
    try:
        driver.find_element_by_xpath("//*[@class = 'animated fadeInUp']")
        print("Wrong email or password.")
        return False
    except NoSuchElementException:
        # can't locate the element, so login success
        return True

def verify_login(driver, profilename):
    name = driver.find_element_by_class_name("gs-userbar__username").text
    #return name
    if (name == profilename):
        print("Login success! Welcome {}!".format(profilename))
        return 1
    else:
        print("Can't verify login! Fail")
        return 0

def log_out(driver):
    driver.find_element_by_class_name("gs-userbar__dropdown-icon").click()
    driver.find_element_by_xpath('//*[@class="gs-dropdown__item gs-dropdown__item--nolink gs-dropdown__item--red gs-dropdown__item-btn-logout"]').click()
    print("Logout success!") 


if __name__ == "__main__":
    # initiate driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    print(username)
    # run the test
    tobii_navigate(driver, link)
    if tobii_login(driver, username, password):
        if verify_login(driver, profilename):
            log_out(driver)
            #driver.close()

    else:
        print("Login failed")
        #driver.close()

    
