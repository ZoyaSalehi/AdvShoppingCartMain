import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods


class AdshopcartPositiveTests(unittest.TestCase):

    @staticmethod
    def test_AOS():
        methods.setUp()
        methods.check_homepage()
        methods.sign_up()
        methods.log_out()
        methods.log_in_valid_user(locators.new_username, locators.new_password)
        methods.check_full_name()
        methods.check_orders()
        methods.delete_test_account()
        #methods.log_out()
        methods.log_in_valid_user(locators.new_username, locators.new_password)
        methods.tearDown()