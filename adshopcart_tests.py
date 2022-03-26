import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods


class AdshopcartPositiveTests(unittest.TestCase):

    @staticmethod
    def test_AOS():
        methods.setUp()
        methods.sign_up()
        methods.tearDown()