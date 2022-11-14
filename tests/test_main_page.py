import allure
import pytest

from pages.main_page import MainPages

from Browsers.Undetected_Chrome_browser import *

from confest import set_up

# Class
Main_Pages_class = MainPages(driver)


# Tests
@pytest.mark.run(order=1)
@allure.description("test open page")
def test_open_page(set_up):
    Main_Pages_class.open_main_page()


@pytest.mark.run(order=11)
@allure.description("test registration user")
def test_registration_user(set_up):
    Main_Pages_class.registration_user()


@pytest.mark.run(order=9)
@allure.description("test enter user")
def test_enter_user(set_up):
    Main_Pages_class.enter_user()


@pytest.mark.run(order=2)
@allure.description("test select city")
def test_select_city(set_up):
    Main_Pages_class.select_city()


@pytest.mark.run(order=3)
@allure.description("test select category phone")
def test_select_category_phone(set_up):
    Main_Pages_class.select_category_phones()


@pytest.mark.run(order=4)
@allure.description("test reload click logo")
def test_reload_click_logo(set_up):
    Main_Pages_class.reload_page_logo()


@pytest.mark.run(order=5)
@allure.description("test field search input")
def test_field_search_input(set_up):
    Main_Pages_class.input_position_search()


@pytest.mark.run(order=10)
@allure.description("test enter user and buy iphone13pro")
def test_enter_user_and_buy_iphone13pro(set_up):
    Main_Pages_class.enter_user_and_buy_iphone13pro()


@pytest.mark.run(order=6)
@allure.description("test fail user")
def test_fail_user(set_up):
    Main_Pages_class.fail_access_user()


@pytest.mark.run(order=7)
@allure.description("test fail select city")
def test_fail_select_city(set_up):
    Main_Pages_class.fail_select_city()


@pytest.mark.run(order=8)
@allure.description("test double number user")
def test_double_number_user(set_up):
    Main_Pages_class.double_user()
