# _*_ coding: UTF-8 _*_
from base_page import BasePage


class RegisterPage(BasePage):
    """ 註冊頁面 """

    # locate
    account_icon = "//a[@href='/account']"
    register_button = "//a[./input[@value='註冊']]"
    register_page = "//div[@id='register']//div[@class='form' and not(contains(@style, 'display: none'))]"
    first_name_input = "//input[@id='first-name']"
    first_name_error = f"{first_name_input}/..//p[@class='form__error-message']"
    last_name_input = "//input[@id='last-name']"
    last_name_error = f"{last_name_input}/..//p[@class='form__error-message']"
    email_input = "//input[@id='customer-email']"
    email_error = f"{email_input}/..//p[@class='form__error-message']"
    pwd_input = "//input[@id='password']"
    pwd_error = f"{pwd_input}/../..//p[@class='form__error-message']"
    finish_button = "//button[contains(text(), '完成')]"
    i_know_button = "//button[text()='我知道了']"

    def test_to_register_page(self):
        try:
            self.wait_until_element_is_clickable(self.account_icon).click()
        except Exception as e:
            self.driver.save_screenshot('page.png')  # 出錯時截圖
            raise e
        
        self.wait_until_element_is_clickable(self.register_button).click()
        page = self.wait_until_element_is_visibility(self.register_page)
        return True if page else False

    def test_first_name_input(self):
        print("\n======= 測試「姓氏」=======")
        first_name = self.wait_until_element_is_clickable(self.first_name_input)
        first_name.send_keys("123")
        error_msg = self.wait_until_element_is_visibility(self.first_name_error).text
        if "請輸入正確的字元" not in error_msg:
            print(f"Fail:「姓氏」輸入錯誤字元，顯示訊息有誤:{error_msg}")
            return False

        # 輸入正確格式
        first_name.clear()
        first_name.send_keys("asd")
        self.wait_until_element_is_invisibility(self.first_name_error)
        print("*** 測試結束 ***\n")
        return True

    def test_last_name_input(self):
        print("======= 測試「姓名」=======")
        last_name = self.wait_until_element_is_clickable(self.last_name_input)
        last_name.send_keys("123")
        error_msg = self.wait_until_element_is_visibility(self.last_name_error).text
        if "請輸入正確的字元" not in error_msg:
            print(f"Fail:「姓名」輸入錯誤字元，顯示訊息有誤:{error_msg}")
            return False

        # 輸入正確格式
        last_name.clear()
        last_name.send_keys("asd")
        self.wait_until_element_is_invisibility(self.last_name_error)
        print("*** 測試結束 ***\n")
        return True

    def test_email_input(self):
        print("======= 測試「信箱」=======")
        email = self.wait_until_element_is_clickable(self.email_input)
        email.send_keys("123")
        error_msg = self.wait_until_element_is_visibility(self.email_error).text
        if "Email包含無效的網域名稱，請確認輸入的內容" not in error_msg:
            print(f"Fail:「信箱」輸入錯誤字元，顯示訊息有誤:{error_msg}")
            return False

        # 輸入正確格式
        email.clear()
        email.send_keys("asd@asd.asd")
        self.wait_until_element_is_invisibility(self.email_error)
        print("*** 測試結束 ***\n")
        return True

    def test_password_input(self):
        print("======= 測試「密碼」=======")
        pwd = self.wait_until_element_is_clickable(self.pwd_input)
        pwd.send_keys("asd")
        error_msg = self.wait_until_element_is_visibility(self.pwd_error).text
        if "密碼至少要 5 個字元" not in error_msg:
            print(f"Fail:「密碼」輸入錯誤字元，顯示訊息有誤:{error_msg}")
            return False

        # 輸入正確格式
        pwd.clear()
        pwd.send_keys("asdas")
        self.wait_until_element_is_invisibility(self.pwd_error)
        print("*** 測試結束 ***\n")
        return True

    def test_finish(self):
        print("======= 測試「點擊完成」=======")
        self.wait_until_element_is_clickable(self.finish_button).click()
        # 關閉認證popup
        button = self.wait_until_element_is_clickable(self.i_know_button)
        if button:
            button.click()
            return True
        else:
            print("Fail: 測試「完成」按鈕失敗")
            return False

