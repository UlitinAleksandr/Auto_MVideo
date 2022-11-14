import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.basket_page import BasketPage


class PurchasePage(BasketPage):

    # Url
    url_purchase_step1 = "https://www.mvideo.ru/purchase/step1"
    url_purchase_step2 = "https://www.mvideo.ru/purchase/step2"

    # Locators
    button_menu_city = "//span[contains(text(),'Выбрать магазин')]"
    button_list_menu = "//button[contains(text(),'Список')]"
    enter_second_shop = "//div[@class='maps-pickup-list__scroll']/tr[2]"
    from_here_get = "//span[contains(text(),'Заберу отсюда')]"
    continue_button = "//div[contains(text(),'Далее')]"
    pay_button = "//div[contains(text(),'Оплатить')]"

    # Getters
    def get_button_menu_city(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_menu_city)))

    def get_button_list_menu(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_list_menu)))

    def get_enter_second_shop(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.enter_second_shop)))

    def get_from_here_get(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.from_here_get)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.continue_button)))

    def get_pay_button(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.pay_button)))

    # Actions
    def click_button_menu_city(self):
        self.get_button_menu_city().click()
        print("Click button menu city: OK")

    def click_button_list_menu(self):
        self.get_button_list_menu().click()
        print("Click button list menu: OK")

    def click_enter_second_shop(self):
        self.get_enter_second_shop().click()
        print("Click enter second shop: OK")

    def click_from_here_get(self):
        time.sleep(2)
        self.get_from_here_get().click()
        print("Click from here get: OK")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button: OK")

    def click_pay_button(self):
        self.get_pay_button().click()
        print("Click pay button: OK")
