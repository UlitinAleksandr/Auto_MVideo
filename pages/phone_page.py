from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.purchase_page import PurchasePage
from utilities.logger import Logger

import allure


class PhonePage(PurchasePage):

    # Url
    url_phone_page = "https://www.mvideo.ru/telefony"
    url_smartphone_page = "https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205?reff=menu_main"

    # Locators
    city_moscow_assess = "//a[@class='c-btn geolocation__action-approve-city']"
    link_text_smartphone = "Смартфоны"
    checkbox_samsung = "Samsung"
    slider_13 = "//button[@class='slider__knob ng-star-inserted']"
    checkbox_15_min = "//span[contains(text(),'Забрать через 15 минут')]"
    checkbox_iphone13pro = "//div[@class='filter-checkbox-list__container']/div[2]"
    link_op_memory = "//span[contains(text(),'Оперативная память')]"
    link_first_popular = "//span[contains(text(),'Сначала популярные')]"
    add_product_basket = "//mvid-plp-product-checkout[3]//button[@class='button ng-star-inserted']"

    # Getters
    def get_city_moscow_assess(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.city_moscow_assess)))

    def get_link_smartphone(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.LINK_TEXT,
                                                                                       self.link_text_smartphone)))

    def get_checkbox_samsung(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.LINK_TEXT,
                                                                                       self.checkbox_samsung)))

    def get_slider(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.slider_13)))

    def get_checkbox_15_min(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.checkbox_15_min)))

    def get_checkbox_iphone13pro(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.checkbox_iphone13pro)))

    def get_link_op_memory(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.link_op_memory)))

    def get_link_first_popular(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.link_first_popular)))

    def get_add_product_basket(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.add_product_basket)))

    # Actions
    def click_smartphone_link(self):
        self.get_link_smartphone().click()
        print("Link smartphone: OK")

    def click_checkbox_samsung(self):
        self.get_checkbox_samsung().click()
        print("Checkbox samsung: OK")

    def click_check_15_min(self):
        self.get_checkbox_15_min().click()
        print("Checkbox 15 min: OK")

    def click_check_iphone13pro(self):
        self.get_checkbox_iphone13pro().click()
        print("Checkbox iphone13pro: OK")

    def click_add_product(self):
        self.get_add_product_basket().click()
        print("Click add product: OK")

    # Methods
    def open_phone_page(self):
        with allure.step("open phone page"):
            Logger.add_start_step(method="open_phone_page")
            self.driver.get(self.url_phone_page)
            self.driver.maximize_window()
            self.assert_current_url(self.url_phone_page)
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="open_phone_page")

    def select_samsung_phone(self):
        with allure.step("select samsung phone"):
            Logger.add_start_step(method="select_samsung_phone")
            self.driver.get(self.url_phone_page)
            self.driver.maximize_window()
            self.assert_current_url(self.url_phone_page)
            self.click_smartphone_link()
            self.click_checkbox_samsung()
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="select_samsung_phone")
