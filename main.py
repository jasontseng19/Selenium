# _*_ coding: UTF-8 _*_
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from datetime import datetime
import os
import sys
import HTMLTestRunner
from pages import register_page
from pages import search_page
from pages import car_page


sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option("prefs", {
    "profile.password_manager_enabled": False,
    "credentials_enable_service": False,
    "profile.password_manager_leak_detection": False
})
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://rhinoshield.tw/")
# 同意cookie
_ele = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@class='switcher__confirm']")))
time.sleep(1)
_ele.click()


class AutomationTest(unittest.TestCase):
    """ 自動化測試 """

    r_page = register_page.RegisterPage(driver)
    s_page = search_page.SearchPage(driver)
    c_page = car_page.ShoppingCarPage(driver)

    def test_register1(self):
        result = self.r_page.test_to_register_page()
        self.assertEqual(True, result)

    def test_register2(self):
        result = self.r_page.test_first_name_input()
        self.assertEqual(True, result)

    def test_register3(self):
        result = self.r_page.test_last_name_input()
        self.assertEqual(True, result)

    def test_register4(self):
        result = self.r_page.test_email_input()
        self.assertEqual(True, result)

    def test_register5(self):
        result = self.r_page.test_password_input()
        self.assertEqual(True, result)

    def test_register6(self):
        result = self.r_page.test_finish()
        self.assertEqual(True, result)

    def test_search1(self):
        result = self.s_page.test_search()
        self.assertEqual(True, result)

    def test_search2(self):
        result = self.s_page.test_click_first_product()
        self.assertEqual(True, result)

    def test_search3(self):
        result = self.s_page.test_phone_type_color()
        self.assertEqual(True, result)

    def test_search4(self):
        result = self.s_page.test_phone_case_color()
        self.assertEqual(True, result)

    def test_shopping_car1(self):
        result = self.c_page.test_add_to_shopping_car()
        self.assertEqual(True, result)

    def test_shopping_car2(self):
        result = self.c_page.test_check_shopping_car_page()
        self.assertEqual(True, result)

if __name__ == '__main__':
    test_units = unittest.TestSuite()
    test_units.addTests([
        AutomationTest("test_register1"),
        # AutomationTest("test_register2"),
        # AutomationTest("test_register3"),
        # AutomationTest("test_register4"),
        # AutomationTest("test_register5"),
        # AutomationTest("test_register6"),
        # AutomationTest("test_search1"),
        # AutomationTest("test_search2"),
        # AutomationTest("test_search3"),
        # AutomationTest("test_search4"),
        # AutomationTest("test_shopping_car1"),
        # AutomationTest("test_shopping_car2")
    ])

    now = datetime.now().strftime('%m-%d %H_%M_%S')
    filename = now + '.html'
    with open(filename, 'wb+') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='網頁自動化測試',
        )
        runner.run(test_units)

    driver.quit()
