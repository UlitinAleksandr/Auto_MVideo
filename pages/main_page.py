import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.phone_page import PhonePage
from utilities.logger import Logger


class MainPages(PhonePage):

    # Url
    url_main_pages = "https://www.mvideo.ru/"
    url_enter_iphone13 = "https://www.mvideo.ru/product-list-page?q=iphone+13+pro&category=smartfony-205"

    # Assert word
    write_chat = "Написать в чат"

    # Locators
    link_enter = "//div[@class='nav-tab tab-profile']"
    input_field_number = "//input[@id='mvideo-form-field-input-0']"
    button_continue = "//div[@class='login-form__container login-form__button-container']"
    field_input_code = "//input[@id='mvideo-form-field-input-1']"
    field_email = "//input[@id='mvideo-form-field-input-2']"
    field_name = "//input[@id='mvideo-form-field-input-3']"
    field_last_name = "//input[@id='mvideo-form-field-input-4']"
    button_end = "//button[@class='registration-form__button mv-main-" \
                 "button--large mv-main-button--primary mv-button mv-main-button']"
    city_link = "//span[@class='location-text top-navbar-link ng-tns-c220-1']"
    placeholder_city = "//input[@placeholder='Ваш город']"
    city_spb = "//li[@class='location-select__location ng-star-inserted']"
    menu_catalog = "//mvid-button[@class='catalog-button ng-tns-c220-1']"
    menu_phone = "//a[@href='https://www.mvideo.ru/telefony']"
    button_write_chat = "//button[@class='chat__button_main mv-main-button--" \
                        "large visible mv-main-button--primary mv-button mv-main-button ng-star-inserted']"
    logo = "//a[@class='logo ng-tns-c220-1 ng-star-inserted']"
    field_search = "//input[@class='input__field']"

    # Getters
    def get_link_enter(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       self.link_enter)))

    def get_input_field_number(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.input_field_number)))

    def get_button_continue(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_continue)))

    def get_field_input_code(self):
        return WebDriverWait(self.driver, timeout=100).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.field_input_code)))

    def get_field_email(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.field_email)))

    def get_field_name(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.field_name)))

    def get_field_last_name(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.field_last_name)))

    def get_button_end(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_end)))

    def get_city_link(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.city_link)))

    def get_placeholder_city(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.placeholder_city)))

    def get_city_spb(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.city_spb)))

    def get_menu_catalog(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.menu_catalog)))

    def get_menu_phone(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.menu_phone)))

    def get_button_write_chat(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_write_chat)))

    def get_logo(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.logo)))

    def get_field_search(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.field_search)))

    # Actions
    def click_link_enter(self):
        self.get_link_enter().click()
        print("Click link enter ")

    def input_number(self):
        self.get_input_field_number().send_keys("9619256461")
        print("Phone number: OK")

    def fail_input_number(self):
        self.get_input_field_number().send_keys("9999999999")
        print("Input fail number: OK")

    def enter_button_continue(self):
        self.get_button_continue().click()
        print("Button continue: OK")

    def input_code(self):
        self.get_field_input_code().send_keys(input("Input code from sms: "))
        print("Input code: OK")

    def input_fail_code(self):
        self.get_field_input_code().send_keys("1234")
        print("Input fail code: OK")

    def input_email(self):
        self.get_field_email().send_keys(input("Input your email: "))
        print("Input email: OK")
        self.action_tab()

    def input_name(self):
        self.get_field_name().send_keys(input("Input your name: "))
        print("Input name: OK")
        self.action_tab()

    def input_last_name(self):
        self.get_field_last_name().click()
        self.get_field_last_name().send_keys(input("Input your last name: "))
        print("Input last name: OK")

    def end_button(self):
        self.get_button_end().click()
        print("Button end: OK")

    def menu_city(self):
        self.get_city_link().click()
        self.get_placeholder_city().send_keys("Санкт-Петербург")
        time.sleep(1)
        self.get_city_spb().click()
        print("City: OK")

    def fail_menu_city(self):
        self.get_city_link().click()
        self.get_placeholder_city().send_keys("Питирбург")
        print("Fail understand City: OK")

    def open_category_phone(self):
        self.get_menu_catalog().click()
        self.get_menu_phone().click()
        print("Category phone: OK")

    def reload_click_logo(self):
        self.get_logo().click()
        print("Click Logo: OK")

    def input_search(self):
        self.get_field_search().send_keys("Iphone 13 pro")
        print("Input position: OK")

    # Methods
    def open_main_page(self):
        with allure.step("open main page"):
            Logger.add_start_step(method="open_main_page")
            self.driver.get(self.url_main_pages)
            self.driver.maximize_window()
            self.assert_current_url(self.url_main_pages)
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="open_main_page")

    def registration_user(self):
        with allure.step("registration user"):
            Logger.add_start_step(method="registration_user")
            self.driver.get(self.url_main_pages)
            self.driver.maximize_window()
            self.assert_current_url(self.url_main_pages)
            self.click_link_enter()
            self.input_number()
            self.enter_button_continue()
            self.input_code()
            self.input_email()
            self.input_name()
            self.input_last_name()
            self.end_button()
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="registration_user")

    def enter_user(self):
        with allure.step("enter user"):
            Logger.add_start_step(method="enter_user")
            self.driver.get(self.url_main_pages)
            self.driver.maximize_window()
            self.assert_current_url(self.url_main_pages)
            self.click_link_enter()
            self.input_number()
            self.enter_button_continue()
            self.input_code()
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="enter_user")

    def select_city(self):
        with allure.step("select city"):
            Logger.add_start_step(method="select_city")
            self.driver.get(self.url_main_pages)
            self.driver.maximize_window()
            self.assert_current_url(self.url_main_pages)
            self.menu_city()
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="select_city")

    def select_category_phones(self):
        with allure.step("select category phones"):
            Logger.add_start_step(method="select_category_phones")
            self.driver.get(self.url_main_pages)
            self.driver.maximize_window()
            self.open_category_phone()
            self.assert_current_url(self.url_phone_page)
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="select_category_phones")

    def reload_page_logo(self):
        with allure.step("reload page logo"):
            Logger.add_start_step(method="reload_page_logo")
            self.driver.get(self.url_main_pages)
            self.driver.maximize_window()
            self.assert_current_url(self.url_main_pages)
            self.reload_click_logo()
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="reload_page_logo")

    def input_position_search(self):
        with allure.step("input position search"):
            Logger.add_start_step(method="input_position_search")
            self.driver.get(self.url_main_pages)
            self.driver.maximize_window()
            self.assert_current_url(self.url_main_pages)
            self.input_search()
            self.action_return()
            time.sleep(2)
            self.assert_current_url(self.url_enter_iphone13)
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="input_position_search")

    def enter_user_and_buy_iphone13pro(self):
        with allure.step("enter user and buy iphone13pro"):
            Logger.add_start_step(method="enter_user_and_buy_iphone13pro")
            self.driver.get(self.url_main_pages)
            self.driver.maximize_window()
            self.assert_current_url(self.url_main_pages)
            self.click_link_enter()
            self.input_number()
            self.enter_button_continue()
            self.input_code()
            self.input_search()
            self.action_return()
            self.action_esc()
            self.action_move_slider(self.get_slider(), 50, 0)
            self.action_move_element(self.get_checkbox_iphone13pro())
            self.click_check_15_min()
            self.action_move_element(self.get_link_op_memory())
            self.click_check_iphone13pro()
            self.action_move_element(self.get_link_first_popular())
            self.click_add_product()
            self.click_button_go_to_design()
            self.assert_current_url(self.url_purchase_step1)
            self.click_button_menu_city()
            self.click_button_list_menu()
            self.click_enter_second_shop()
            self.click_from_here_get()
            self.click_continue_button()
            self.assert_current_url(self.url_purchase_step2)
            self.click_pay_button()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="enter_user_and_buy_iphone13pro")

    def fail_access_user(self):
        with allure.step("fail access user"):
            Logger.add_start_step(method="fail_access_user")
            self.driver.get(self.url_main_pages)
            self.driver.maximize_window()
            self.assert_current_url(self.url_main_pages)
            self.click_link_enter()
            self.input_number()
            self.enter_button_continue()
            self.input_fail_code()
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="fail_access_user")

    def fail_select_city(self):
        with allure.step("fail select city"):
            Logger.add_start_step(method="fail_select_city")
            self.driver.get(self.url_main_pages)
            self.driver.maximize_window()
            self.assert_current_url(self.url_main_pages)
            self.fail_menu_city()
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="fail_select_city")

    def double_user(self):
        with allure.step("double user"):
            Logger.add_start_step(method="double_user")
            self.driver.get(self.url_main_pages)
            self.driver.maximize_window()
            self.assert_current_url(self.url_main_pages)
            self.click_link_enter()
            self.fail_input_number()
            self.enter_button_continue()
            self.assert_word(self.get_button_write_chat(), self.write_chat)
            self.get_screenshot()
            self.driver.delete_all_cookies()
            Logger.add_end_step(url=self.driver.current_url, method="double_user")
