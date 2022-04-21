from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

browser = webdriver.Chrome("driver/chromedriver.exe")
browser.maximize_window()


class AutomationTest(unittest.TestCase):
    """
    自動化測試
    """

    def test_register(self):
        """
        測試註冊資訊
        :return:
        """

        self.br = browser
        result_lsit = []
        page = True

        try:
            self.br.get("https://rhinoshield.tw/")
            WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='functional-item login']"))).click()
            WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                (By.XPATH, "//a[./input[@value='註冊']]"))).click()
            # 確認是否在註冊頁面
            WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='register']//div[@class='form' and not(contains(@style, 'display: none'))]")))
        except Exception as e:
            print(e)
            print("Fail: 無法進到註冊頁面")
            page = False

        # 確認有近到註冊頁面在進行
        if page:
            # 姓氏
            try:
                input = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='first-name']")))
                input.send_keys("123")
                try:
                    error_msg = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                        (By.XPATH, "//input[@id='first-name']/..//p[@class='form__error-message']")))
                    if "請輸入正確的字元" not in error_msg.text:
                        print(f"Fail: 姓氏 輸入錯誤字元，顯示訊息有誤:{error_msg.text}")
                        result_lsit.append("False")
                except:
                    print("Fail: 姓氏 輸入錯誤字元時無顯示錯誤提示")
                    result_lsit.append("False")
                # 輸入正確格式
                input.clear()
                input.send_keys("asd")
            except:
                print("Fail: 驗證 姓氏 錯誤時異常")
                result_lsit.append("False")

            # 姓名
            try:
                input = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='last-name']")))
                input.send_keys("123")
                try:
                    error_msg = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                        (By.XPATH, "//input[@id='last-name']/..//p[@class='form__error-message']")))
                    if "請輸入正確的字元" not in error_msg.text:
                        print(f"Fail: 姓名 輸入錯誤字元，顯示訊息有誤:{error_msg.text}")
                        result_lsit.append("False")
                except:
                    print("Fail: 姓名 輸入錯誤字元時無顯示錯誤提示")
                    result_lsit.append("False")
                # 輸入正確格式
                input.clear()
                input.send_keys("asd")
            except:
                print("Fail: 驗證 姓名 錯誤時異常")
                result_lsit.append("False")

            # 生日
            try:
                ele = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='birthday-input']")))
                ele.click()
                WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='btn-flat picker__today']"))).click()
                WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='btn-flat picker__close']"))).click()
            except:
                print("Fail: 設定 生日 時異常")
                result_lsit.append("False")

            # 性別
            try:
                WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//select/option[@value='male']"))).click()
            except:
                print("Fail: 設定 性別 時異常")
                result_lsit.append("False")
            time.sleep(3)
        else:
            return page

        results = False if "False" in result_lsit else True
        return results


if __name__ == '__main__':
    auto_test = AutomationTest()
    result = auto_test.test_register()
    print(result)
    browser.quit()
