from pages.basket_page import BasketPage
from confest import set_up

from Browsers.Undetected_Chrome_browser import *

# Class
Basket_Pages_class = BasketPage(driver)


# Tests
def test_open_page_basket(set_up):
    Basket_Pages_class.open_page_basket()


def test_click_logo_go_main(set_up):
    Basket_Pages_class.click_logo_go_main()


def test_select_city(set_up):
    Basket_Pages_class.select_city_basket()


def test_authorization_user_basket(set_up):
    Basket_Pages_class.authorization_basket()


def test_add_product_basket(set_up):
    Basket_Pages_class.add_product()


def test_delete_product_from_basket(set_up):
    Basket_Pages_class.delete_product_from_basket()
