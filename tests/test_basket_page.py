import allure
import pytest

from pages.basket_page import BasketPage
from confest import set_up

from Browsers.Undetected_Chrome_browser import *

# Class
Basket_Pages_class = BasketPage(driver)


# Tests
@pytest.mark.run(order=2)
@allure.description("test open page basket")
def test_open_page_basket(set_up):
    Basket_Pages_class.open_page_basket()


@pytest.mark.run(order=1)
@allure.description("test click logo go main")
def test_click_logo_go_main(set_up):
    Basket_Pages_class.click_logo_go_main()


@pytest.mark.run(order=3)
@allure.description("test select city")
def test_select_city(set_up):
    Basket_Pages_class.select_city_basket()


@pytest.mark.run(order=6)
@allure.description("test authorization user basket")
def test_authorization_user_basket(set_up):
    Basket_Pages_class.authorization_basket()


@pytest.mark.run(order=4)
@allure.description("test add product basket")
def test_add_product_basket(set_up):
    Basket_Pages_class.add_product()


@pytest.mark.run(order=5)
@allure.description("test delete product from basket")
def test_delete_product_from_basket(set_up):
    Basket_Pages_class.delete_product_from_basket()
