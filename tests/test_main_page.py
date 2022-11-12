from pages.main_page import MainPages

from Browsers.Undetected_Chrome_browser import *

from confest import set_up

# Class
Main_Pages_class = MainPages(driver)


# Tests
def test_open_page(set_up):
    Main_Pages_class.open_main_page()


def test_registration_user(set_up):
    Main_Pages_class.registration_user()


def test_enter_user(set_up):
    Main_Pages_class.enter_user()


def test_select_city(set_up):
    Main_Pages_class.select_city()


def test_select_category_phone(set_up):
    Main_Pages_class.select_category_phones()


def test_reload_click_logo(set_up):
    Main_Pages_class.reload_page_logo()


def test_field_search_input(set_up):
    Main_Pages_class.input_position_search()


def test_enter_user_and_buy_iphone13pro(set_up):
    Main_Pages_class.enter_user_and_buy_iphone13pro()


def test_fail_user(set_up):
    Main_Pages_class.fail_access_user()


def test_fail_select_city(set_up):
    Main_Pages_class.fail_select_city()


def test_double_number_user(set_up):
    Main_Pages_class.double_user()
