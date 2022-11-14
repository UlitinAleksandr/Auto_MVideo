import time
from datetime import datetime

from selenium.webdriver import ActionChains, Keys


class Base:

    def __init__(self, driver):
        self.driver = driver

    # Method get_current_url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    # Method assert word
    @staticmethod
    def assert_word(word, result):
        value_word = word.text
        assert value_word == result
        print("Value word: OK")

    # Method screenshot
    def get_screenshot(self):
        time.sleep(3)
        now = datetime.utcnow().strftime("%Y.%m.%d.  %H.%M.%S")
        self.driver.save_screenshot("C:\\Users\\satanavsarae\\PycharmProjects\\"
                                    "Auto_MVideo_single_test\\screens\\" + "screenshot " + now + ".png")

    # Method assert_current_url
    def assert_current_url(self, url):
        time.sleep(3)
        assert self.driver.current_url == url
        print(f"{url} assert")

    # Method action move element
    def action_move_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        print(f"Action element: {element}")

    # Method action tab
    def action_tab(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB).perform()
        print(f"Action TAB: OK")

    # Method action return
    def action_return(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.RETURN).perform()
        print(f"Action return: OK")

    # Method action click_and_hold
    def action_click_and_hold(self, element):
        action = ActionChains(self.driver)
        action.click_and_hold(element).perform()
        print(f"Action click_and_hold: {element}")

    # Method action esc
    def action_esc(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()
        print(f"Action esc: OK")

    # Method action click and offset
    def action_move_slider(self, element, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x, y).perform()
        time.sleep(2)
        print("Move element offset: OK")