import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
    if driver.current_url == locators.aos_URL and driver.title == locators.aos_homepage_titel:
        print(f'Yey! {locators.app} App website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'-------------------------~*~--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()

# setUp()
# tearDown()