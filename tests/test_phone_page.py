from pages.phone_page import PhonePage

from confest import set_up

from Browsers.Undetected_Chrome_browser import *


# Class
Phone_page_class = PhonePage(driver)


# Tests
def test_open_phone_page(set_up):
    Phone_page_class.open_phone_page()


def test_select_samsung(set_up):
    Phone_page_class.select_samsung_phone()
