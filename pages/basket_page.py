from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class BasketPage(Base):

    # Url
    url_basket = "https://www.mvideo.ru/cart"
    url_login_page = "https://www.mvideo.ru/login"
    url_buy_step1 = "https://www.mvideo.ru/purchase/step1"

    # Locators
    logo_basket = "//a[@data-sel='mvideo-logo']"
    menu_city = "//a[@class='c-link cart-header__delivery-city-link hidden-fl-mobile']"
    field_city = "//input[@id='region-selection-form-city-input']"
    city_click = "//a[@data-drop-item-id='CityCZ_6276']"
    authorization_button = "//a[@class='c-link c-link_pseudo'] [@href='/login']"
    field_number = "//input[@type='tel']"
    button_continue_basket = "//button[@class='login-form__button mv-main-button--large mv-main-button"\
                             "--primary mv-button mv-main-button']"
    field_code = "//input[@id='mvideo-form-field-input-2']"
    button_add_basket = "//button[@data-id='add-button-30052737']"
    text_add_basket_link = "//div[@data-init='affix'] [@class='c-popup__title affix-top']"
    button_go_to_basket = "//a[@data-sel='page_name-a-cart_redirect']"
    link_delete_product = "//a[@class='c-link c-link_pseudo c-link_gray60'] [@data-action='click']"
    delete_button_assess_link = "//div[@class='c-popup__content']//a[@data-action='click']"
    text_empty_basket_page = "//div[@class='c-cart__empty-title']"
    button_basket = "//mvid-header-icon[@tooltiptype='cart']"
    button_go_to_design = "//div[contains(text(),'Перейти к оформлению')]"

    # Assert text
    text_add_basket = "Товар добавлен в корзину"
    text_empty_basket = "Ваша корзина пока пуста"

    # Getters
    def get_logo_basket(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.logo_basket)))

    def get_menu_city(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.menu_city)))

    def get_field_city(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.field_city)))

    def get_city_click(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.city_click)))

    def get_aut_button(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.authorization_button)))

    def get_field_number(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.field_number)))

    def get_button_continue_basket(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_continue_basket)))

    def get_field_code(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.field_code)))

    def get_button_add_basket(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_add_basket)))

    def get_text_add_basket_link(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.text_add_basket_link)))

    def get_button_go_to_basket(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_go_to_basket)))

    def get_link_delete_product(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.link_delete_product)))

    def get_delete_button_assess(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.delete_button_assess_link)))

    def get_text_empty_basket_page(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.text_empty_basket_page)))

    def get_button_basket(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_basket)))

    def get_button_go_to_design(self):
        return WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        self.button_go_to_design)))

    # Actions
    def click_logo(self):
        self.get_logo_basket().click()
        print("Click Logo: OK")

    def click_menu_city(self):
        self.get_menu_city().click()
        print("Click menu_city: OK")

    def input_field_city(self):
        self.get_field_city().send_keys("Оренбург")
        print("Input city: OK")

    def click_need_city(self):
        self.get_city_click().click()
        print("Click need_city: OK")

    def auth_click_button(self):
        self.get_aut_button().click()
        print("Click authorization button: OK")

    def input_number_phone(self):
        self.get_field_number().send_keys(input("Input phone number(10 value): "))
        print("Phone number: OK")

    def enter_button_continue_basket(self):
        self.get_button_continue_basket().click()
        print("Button continue: OK")

    def input_code_basket(self):
        self.get_field_code().send_keys(input("Input code from sms: "))
        print("Input code: OK")

    def click_button_add_basket(self):
        self.get_button_add_basket().click()
        print("Button add product: OK")

    def click_button_go_to_basket(self):
        self.get_button_go_to_basket().click()
        print("Button go to basket: OK")

    def delete_product(self):
        self.get_link_delete_product().click()
        print("Delete product")

    def assess_delete_button(self):
        self.get_delete_button_assess().click()
        print("Product delete from basket")

    def click_button_basket(self):
        self.get_button_basket().click()
        print("Click basket: OK")

    def click_button_go_to_design(self):
        self.get_button_go_to_design().click()
        print("Click go to design: OK")

    # Methods
    def open_page_basket(self):
        self.driver.get(self.url_basket)
        self.driver.maximize_window()
        self.assert_current_url(self.url_basket)
        self.get_screenshot()
        self.driver.quit()

    def click_logo_go_main(self):
        self.driver.get(self.url_basket)
        self.driver.maximize_window()
        self.assert_current_url(self.url_basket)
        self.click_logo()
        self.assert_current_url("https://www.mvideo.ru/")
        self.get_screenshot()
        self.driver.quit()

    def select_city_basket(self):
        self.driver.get(self.url_basket)
        self.driver.maximize_window()
        self.assert_current_url(self.url_basket)
        self.click_menu_city()
        self.input_field_city()
        self.click_need_city()
        self.get_screenshot()
        self.driver.quit()

    def authorization_basket(self):
        self.driver.get(self.url_basket)
        self.driver.maximize_window()
        self.assert_current_url(self.url_basket)
        self.auth_click_button()
        self.assert_current_url("https://www.mvideo.ru/login")
        self.input_number_phone()
        self.enter_button_continue_basket()
        self.input_code_basket()
        self.get_screenshot()
        self.driver.quit()

    def add_product(self):
        self.driver.get(self.url_basket)
        self.driver.maximize_window()
        self.assert_current_url(self.url_basket)
        self.click_button_add_basket()
        self.assert_word(self.get_text_add_basket_link(), self.text_add_basket)
        self.click_button_go_to_basket()
        self.get_screenshot()
        self.driver.quit()

    def delete_product_from_basket(self):
        self.driver.get(self.url_basket)
        self.driver.maximize_window()
        self.assert_current_url(self.url_basket)
        self.click_button_add_basket()
        self.assert_word(self.get_text_add_basket_link(), self.text_add_basket)
        self.click_button_go_to_basket()
        self.delete_product()
        self.assess_delete_button()
        self.assert_word(self.get_text_empty_basket_page(), self.text_empty_basket)
        self.get_screenshot()
        self.driver.quit()
