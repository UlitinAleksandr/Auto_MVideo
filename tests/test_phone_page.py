from pages.phone_page import PhonePage

from confest import set_up

import allure

from Browsers.Undetected_Chrome_browser import *

# Class
Phone_page_class = PhonePage(driver)


# Tests
@allure.description("test open phone page")
def test_open_phone_page(set_up):
    Phone_page_class.open_phone_page()


@allure.description("test select samsung")
def test_select_samsung(set_up):
    Phone_page_class.select_samsung_phone()
