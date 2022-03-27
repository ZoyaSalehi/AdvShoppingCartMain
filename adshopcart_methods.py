import datetime

import selenium
from selenium.webdriver.support.ui import Select  # <--- add this import for drop down lists
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators


s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Test started at: {datetime.datetime.now()}')
    print(f'-------------------------~*~--------------------------')
    # make browswer full screen
    driver.maximize_window()
    driver.implicitly_wait(30)
    # navigate to AOS App website
    driver.get(locators.aos_URL)
    # check that AOS URL and the home page title are as expected
    if driver.current_url == locators.aos_URL and driver.title == locators.aos_homepage_title:
        print(f'Yey! {locators.app} App website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        #tearDown()


def sign_up():
    print(f'-------------------------~*~--------------------------')
    print("Start to Sign Up a new user")
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    print("The sign-in window pops up")
    assert driver.find_element(By.XPATH, '//div[contains(@class, "login ng-scope")]').is_displayed()
    #driver.find_element(By.XPATH, '//div[contains(@class, "login ng-scope")]').click()
    sleep(1)
    assert driver.find_element(By.XPATH, '//a[contains(., "CREATE NEW ACCOUNT")]').is_displayed()
    driver.find_element(By.XPATH, '//a[contains(., "CREATE NEW ACCOUNT")]').click()
    print("navigating to Create New Account page")
    print("Starting with new user registration")

    driver.find_element(By.XPATH, "//input[@name='usernameRegisterPage']").send_keys(locators.new_username)
    driver.find_element(By.XPATH, "//input[@name='emailRegisterPage']").send_keys(locators.email)
    driver.find_element(By.XPATH, "//input[@name='passwordRegisterPage']").send_keys(locators.new_password)
    driver.find_element(By.XPATH, "//input[@name='confirm_passwordRegisterPage']").send_keys(locators.new_password)
    driver.find_element(By.XPATH, "//input[@name='first_nameRegisterPage']").send_keys(locators.first_name)
    driver.find_element(By.XPATH, "//input[@name='last_nameRegisterPage']").send_keys(locators.last_name)
    driver.find_element(By.XPATH, "//input[@name='phone_numberRegisterPage']").send_keys(locators.phonenum)
    Select(driver.find_element(By.TAG_NAME, "select")).select_by_visible_text("Canada")
    sleep(1)
    driver.find_element(By.XPATH, "//input[@name='cityRegisterPage']").send_keys(locators.city)
    sleep(1)
    driver.find_element(By.XPATH, "//input[@name='addressRegisterPage']").send_keys(locators.address)
    driver.find_element(By.XPATH, "//input[@name='state_/_province_/_regionRegisterPage']").send_keys(locators.state)
    driver.find_element(By.XPATH, "//input[@name='postal_codeRegisterPage']").send_keys(locators.zip_code)
    driver.find_element(By.XPATH, "//input[@name='i_agree']").click()
    driver.find_element(By.ID, "register_btnundefined").click()
    sleep(0.5)
    assert driver.find_element(By.LINK_TEXT, f"{locators.new_username}")
    print("New User is successfully registered")

def check_full_name():
    print(f'-------------------------~*~--------------------------')
    print("Confirm if the user's Full Name is correctly captured in the Accounts Details")
    driver.find_element(By.ID, "menuUserLink").click()
    assert driver.find_element(By.ID, "loginMiniTitle").is_displayed()
    #Select(driver.find_element(By.ID, "loginMiniTitle")).select_by_value('My account')
    driver.find_element(By.XPATH, "(//label[text()='My account'])[2]").click()
    #assert driver.find_element(By.LINK_TEXT, "Account details").is_displayed()
    #fullname = (selenium.getText('//label[@class="ng-binding"][1]')).trim()


    assert driver.find_element(By.XPATH, "//div[@class='borderBox']//label")
    fullname = driver.find_element(By.XPATH, "//div[@class='borderBox']//label").get_attribute('innerText')
    if locators.full_name == fullname:
        print("Yes, User's Full Name is correctly captured in the Accounts Details")
    #if driver.find_element(By.XPATH, f"//label[normalize - space(text()) = '{locators.full_name}']"):
    # if driver.find_element(By.XPATH, "//label[text()[normalize-space()='Zoya Salehi']]"):
    #     print("Full name is found in My Account")
    #driver.find_element(By.LINK_TEXT, f"{fullname}" )


def check_orders():
    print(f'-------------------------~*~--------------------------')
    print("Check Orders")
    driver.find_element(By.ID, "menuUserLink").click()
    assert driver.find_element(By.ID, "loginMiniTitle").is_displayed()
    driver.find_element(By.XPATH, "(// label[text() = 'My orders'])[2]").click()

    assert driver.find_element(By.XPATH, "//label[text()=' - No orders - ']")

    print("User has no orders yet")


def log_out():
    print(f'-------------------------~*~--------------------------')
    print("Trying to log out")

    driver.find_element(By.ID, "menuUserLink").click()
    assert driver.find_element(By.ID, "loginMiniTitle").is_displayed()
    driver.find_element(By.XPATH, "(// label[@ translate='Sign_out'])[2]").click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, "//span[@class='hi-user containMiniTitle ng-binding ng-hide']").get_attribute('innerText') == ''
    print("User successfully log out")
    print("user successfully logged out")

def delete_test_account():
    print(f'-------------------------~*~--------------------------')
    print("Trying to delete the user's account")
    driver.find_element(By.ID, "menuUserLink").click()
    sleep(0.5)
    assert driver.find_element(By.ID, "loginMiniTitle").is_displayed()
    driver.find_element(By.XPATH, "(//label[text()='My account'])[2]").click()
    driver.find_element(By.XPATH, "//div[contains(., 'Delete Account')]").click()
    print("User's Account is successfully deleted")


def log_in_valid_user(username, password):
    print(f'-------------------------~*~--------------------------')
    print("Trying gto login with valid username and password")
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    print("The sign-in window pops up")
    if driver.find_element(By.XPATH, '//div[contains(@class, "login ng-scope")]').is_displayed():
        print("we r on pop window")
        sleep(1)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='SIGN IN']").click()
    assert driver.find_element(By.LINK_TEXT, f"{username}")
    print("Valid username and password is successfully logged in")


def log_in_invalid_user(username, password):
    print(f'-------------------------~*~--------------------------')
    print("Trying gto login with invalid username or password")
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    print("The sign-in window pops up")
    if driver.find_element(By.XPATH, '//div[contains(@class, "login ng-scope")]').is_displayed():
        print("we r on pop window")
        sleep(1)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='SIGN IN']").click()
    sleep(1)
    assert driver.find_element(By.ID, "signInResultMessage")
    print("Invalid username or password is successfully detected, not allowed to sign in")

def tearDown():
    if driver is not None:
        print(f'-------------------------~*~--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()

setUp()
sign_up()
log_out()
log_in_valid_user(locators.new_username, locators.new_password)
check_full_name()
check_orders()
delete_test_account()
log_out()
log_in_invalid_user(locators.new_username, locators.new_password)
tearDown()