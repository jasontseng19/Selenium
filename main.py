from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
import time
from datetime import datetime
import os
import HTMLTestRunner


class AutomationTest(unittest.TestCase):
    """
    自動化測試
    """

    @classmethod
    def setUpClass(cls):
        cls.br = webdriver.Chrome("driver/chromedriver.exe")
        cls.br.maximize_window()
        cls.br.get("https://rhinoshield.tw/")

    @classmethod
    def tearDownClass(cls):
        cls.br.quit()

    def check_display_report(self):
        """ 確認是否有顯示訂閱電子報 """

        report = True
        while report:
            try:
                WebDriverWait(self.br, 5, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//form[@id='ins-question-group-form']/..//div[contains(@id, 'wrap-close')]"))).click()
            except:
                report = False

    def test_register(self):
        """ 測試註冊資訊 """

        # init
        result_list = []
        page = True

        try:
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
            result_list.append("False")

        # 確認有進到註冊頁面在進行
        if page:
            # 姓氏
            try:
                input_first_name = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='first-name']")))
                input_first_name.send_keys("123")
                try:
                    error_msg = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                        (By.XPATH, "//input[@id='first-name']/..//p[@class='form__error-message']")))
                    if "請輸入正確的字元" not in error_msg.text:
                        print(f"Fail: 姓氏 輸入錯誤字元，顯示訊息有誤:{error_msg.text}")
                        result_list.append("False")
                except:
                    print("Fail: 姓氏 輸入錯誤字元時無顯示錯誤提示")
                    result_list.append("False")
                # 輸入正確格式
                input_first_name.clear()
                input_first_name.send_keys("asd")
            except:
                print("Fail: 驗證 姓氏 錯誤時異常")
                result_list.append("False")

            # 姓名
            try:
                input_last_name = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='last-name']")))
                input_last_name.send_keys("123")
                try:
                    error_msg = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                        (By.XPATH, "//input[@id='last-name']/..//p[@class='form__error-message']")))
                    if "請輸入正確的字元" not in error_msg.text:
                        print(f"Fail: 姓名 輸入錯誤字元，顯示訊息有誤:{error_msg.text}")
                        result_list.append("False")
                except:
                    print("Fail: 姓名 輸入錯誤字元時無顯示錯誤提示")
                    result_list.append("False")
                # 輸入正確格式
                input_last_name.clear()
                input_last_name.send_keys("asd")
            except:
                print("Fail: 驗證 姓名 錯誤時異常")
                result_list.append("False")

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
                result_list.append("False")

            # 性別
            try:
                WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//select/option[@value='male']"))).click()
            except:
                print("Fail: 設定 性別 時異常")
                result_list.append("False")

            # 手機
            try:
                input_phone = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//label[@for='phone-number']/..//input")))
                input_phone.send_keys("123")
                try:
                    error_msg = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                        (By.XPATH, "//label[@for='phone-number']/..//p[@class='form__error-message']")))
                    if "手機號碼格式有誤，請確認輸入的內容" not in error_msg.text:
                        print(f"Fail: 手機 輸入錯誤字元，顯示訊息有誤:{error_msg.text}")
                        result_list.append("False")
                except:
                    print("Fail: 手機 輸入錯誤字元時無顯示錯誤提示")
                    result_list.append("False")
                # 輸入正確格式
                input_phone.clear()
                input_phone.send_keys("912345678")
            except:
                print("Fail: 設定 手機 時異常")
                result_list.append("False")

            # 信箱
            try:
                ele = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//label[@for='phone-number']/..//input")))
                # 移動至該元素避免密碼輸入造成異常
                self.br.execute_script("arguments[0].scrollIntoView();", ele)
                input_mail = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='customer-email']")))
                input_mail.send_keys("123")
                try:
                    error_msg = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                        (By.XPATH, "//input[@id='customer-email']/..//p[@class='form__error-message']")))
                    if "Email包含無效的網域名稱，請確認輸入的內容" not in error_msg.text:
                        print(f"Fail: 信箱 輸入錯誤字元，顯示訊息有誤:{error_msg.text}")
                        result_list.append("False")
                except:
                    print("Fail: 信箱 輸入錯誤字元時無顯示錯誤提示")
                    result_list.append("False")
                # 輸入正確格式
                input_mail.clear()
                input_mail.send_keys("asd@asd.asd")
            except:
                print("Fail: 設定 信箱 時異常")
                result_list.append("False")

            # 密碼
            try:
                input_pwd = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='password']")))
                input_pwd.send_keys("asd")
                try:
                    error_msg = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                        (By.XPATH, "//input[@id='password']/../..//p[@class='form__error-message']")))
                    if "密碼至少要 5 個字元" not in error_msg.text:
                        print(f"Fail: 密碼 輸入錯誤字元，顯示訊息有誤:{error_msg.text}")
                        result_list.append("False")
                except:
                    print("Fail: 密碼 輸入錯誤字元時無顯示錯誤提示")
                    result_list.append("False")
                # 輸入正確格式
                input_pwd.clear()
                input_pwd.send_keys("asdas")
            except:
                print("Fail: 設定 密碼 時異常")
                result_list.append("False")

            # 勾選同意並點擊下一步
            try:
                input_check = WebDriverWait(self.br, 10, 1).until(EC.presence_of_element_located(
                    (By.XPATH, "//label[@for='accepts-terms-checkbox']")))
                check_box = WebDriverWait(self.br, 10, 1).until(EC.presence_of_element_located(
                    (By.XPATH, "//input[@id='accepts-terms-checkbox']")))
                input_check.click()
                # 確認是否有勾選
                if not check_box.is_selected():
                    input_check.click()
                time.sleep(1)
                # 判斷是否可以點擊下一步
                try:
                    input_next = WebDriverWait(self.br, 10, 1).until(EC.presence_of_element_located(
                        (By.XPATH, "//button[normalize-space(text())='下一步']")))
                    if not input_next.is_enabled():
                        # 確認是否有錯誤訊息
                        try:
                            error_list = WebDriverWait(self.br, 10, 1).until(EC.presence_of_all_elements_located(
                                (By.XPATH, "//p[@class='form__error-message']")))
                            print("Fail: 頁面顯示錯誤訊息")
                            for error in error_list:
                                print(error.text)
                        except:
                            print("Fail: 無錯誤訊息，請確認是否有異常")
                            result_list.append("False")
                    else:
                        try:
                            input_next.click()
                            time.sleep(1)
                            # 等待loading
                            WebDriverWait(self.br, 10, 1).until_not(EC.presence_of_element_located(
                                (By.XPATH, "//button[@class='form__button form__button--primary']/i")))
                            # 應會有手機號碼的錯誤訊息
                            error_msg = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                                (By.XPATH, "//label[@for='phone-number']/..//p[@class='form__error-message']")))
                            if "手機號碼已被使用，請輸入其他號碼" not in error_msg.text:
                                print(f"Fail: 手機已被使用，顯示訊息有誤:{error_msg.text}")
                                result_list.append("False")
                            # 輸入無重複號碼
                            input_phone = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                                (By.XPATH, "//label[@for='phone-number']/..//input")))
                            input_phone.clear()
                            input_phone.send_keys("912345679")
                            input_next.click()
                            time.sleep(1)
                            # 等待loading
                            WebDriverWait(self.br, 10, 1).until_not(EC.presence_of_element_located(
                                (By.XPATH, "//button[@class='form__button form__button--primary']/i")))
                            # 判斷是否導轉到驗證頁面
                            try:
                                WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                                    (By.XPATH, "//div[@id='phone-verify']/div[1]")))
                            except:
                                print("Fail: 重新輸入後無導轉到手機驗證頁面")
                                result_list.append("False")
                        except:
                            # 判斷是否導轉到驗證頁面
                            try:
                                WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                                    (By.XPATH, "//div[@id='phone-verify']/div[1]")))
                            except:
                                print("Fail: 無導轉到手機驗證頁面")
                                result_list.append("False")
                except:
                    print("Fail: 點擊下一步 時異常")
                    result_list.append("False")
            except:
                print("Fail: 勾選同意 時異常")
                result_list.append("False")

            time.sleep(3)

        results = False if "False" in result_list else True
        self.assertEqual(True, results)

    def test_search(self):
        """ 測試搜尋功能 """

        # init
        result_list = []
        product_page = True
        display_product = True

        # 返回首頁
        try:
            WebDriverWait(self.br, 10, 1).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='nav-menu__logo']"))).click()
            try:
                alert = WebDriverWait(self.br, 10, 1).until(EC.alert_is_present())
                alert.accept()
                # 確認是否離開註冊頁面
                WebDriverWait(self.br, 10, 1).until_not(EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='register']//div[@class='form' and not(contains(@style, 'display: none'))]")))
            except:
                pass
        except:
            print("Fail: 返回首頁 時異常")
            result_list.append("False")

        # 搜尋
        try:
            WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                (By.XPATH, "//i[@class='icon-search']"))).click()
            input_search = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@id='search']")))
            input_search.send_keys("asd")
            input_search.send_keys(Keys.ENTER)
            time.sleep(1)
            search_result = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(@class, 'result__desc') or contains(@class, 'results__desc')]")))
            if '找不到' not in search_result.text:
                print(f"Fail: 搜尋商品時顯示錯誤:{search_result.text}")
                result_list.append("False")
        except:
            print("Fail: 搜尋 未銷售商品 時異常")
            result_list.append("False")

        # 點選商品
        try:
            WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                (By.XPATH, "//i[@class='icon-search']"))).click()
            input_search = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@id='search']")))
            input_search.clear()
            input_search.send_keys("Naruto")
            input_search.send_keys(Keys.ENTER)
            self.check_display_report()
            search_result = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(@class, 'result__desc') or contains(@class, 'results__desc')]")))
            if '搜尋結果' not in search_result.text:
                print(f"Fail: 搜尋商品時顯示錯誤:{search_result.text}")
                result_list.append("False")
            search_list = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_all_elements_located(
                (By.XPATH, "//div[@class='results__container']/div[@class='results__card']")))
            product_msg = search_list[0].text
            product_msg = product_msg.split("\n")
            search_list[0].click()
            # 判斷是否還在註冊頁面
            try:
                alert = WebDriverWait(self.br, 5, 1).until(EC.alert_is_present())
                alert.accept()
            except:
                pass

            self.check_display_report()

            # 判斷顯示商品資訊是否正確
            try:
                title = WebDriverWait(self.br, 20, 1).until(EC.visibility_of_element_located(
                    (By.XPATH, "//div[@id='caseProduct']//h2[@class='product-form__content__title']")))
                sub_title = WebDriverWait(self.br, 20, 1).until(EC.visibility_of_element_located(
                    (By.XPATH, "//div[@id='caseProduct']//p[@class='product-form__content__subtitle']")))
                if list(filter(lambda x: x not in title.text, product_msg[:-1])) or\
                        list(filter(lambda x: x not in sub_title.text, product_msg[-1:])):
                    print("Fail: 商品連結顯示異常")
                    print(f"搜尋商品名稱: {product_msg}")
                    print(f"商品大標題:{title.text}")
                    print(f"商品副標題:{sub_title.text}")
                    result_list.append("False")
                    product_page = False
            except:
                print("Fail: 判斷商品 時異常")
                result_list.append("False")
                product_page = False
        except:
            print("Fail: 搜尋 目前銷售商品 時異常")
            result_list.append("False")
            product_page = False

        # 確認商品頁面正確在進行
        if product_page:
            try:
                # 展開產品
                plus = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, "//span[text()='選擇產品']/../..//div[contains(@class, 'plus')]")))
                plus.click()
                time.sleep(1)
                # 判斷是否有展開
                if 'minus' not in plus.get_attribute('class'):
                    plus.click()
                WebDriverWait(self.br, 10, 1).until(EC.visibility_of_element_located(
                    (By.XPATH, "//p[text()='Clear']")))
            except:
                print("Fail: 展開產品 時異常")
                result_list.append("False")
                display_product = False

            if display_product:
                # Clear
                try:
                    WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                        (By.XPATH, "//p[text()='Clear']"))).click()
                    # 確認已切換至產品
                    WebDriverWait(self.br, 10, 1).until(EC.presence_of_element_located(
                        (By.XPATH, "//div[./p[text()='Clear'] and contains(@class, 'active')]")))
                    product_option = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_all_elements_located(
                        (By.XPATH, "//div[@class='product-form__content__options']//p[@class='title']")))
                    option_list = [option.text for option in product_option[1:]]
                    select_item = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_all_elements_located(
                        (By.XPATH, "//div[@class='selected-item']")))
                    item_list = [select_item[i].text for i in range(len(select_item)) if i != 1]
                    if ('手機殼顏色' or '掛繩組(加購)') not in option_list or \
                            list(filter(lambda x: '透明' not in x, item_list)):
                        print("Fail: Clear 產品資訊顯示有誤")
                        print(option_list)
                        print(item_list)
                        result_list.append("False")

                    # 手機殼顏色
                    try:
                        plus = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                            (By.XPATH, "//span[text()='手機殼顏色']/../..//div[contains(@class, 'plus')]")))
                        plus.click()
                        time.sleep(1)
                        # 判斷是否有展開
                        if 'minus' not in plus.get_attribute('class'):
                            plus.click()
                        color_list = WebDriverWait(self.br, 10, 1).until(EC.presence_of_all_elements_located(
                            (By.XPATH, "//div[@id='color-picker']/ul[@class='color-picker hr']/li")))
                        for i in range(len(color_list)):
                            color_list[i].click()
                            # 確認已切換至產品
                            WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                                (By.XPATH, "//button[@class='add-to-cart-btn' and not(contains(@disabled, 'disabled'))]")))
                            select_item = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_all_elements_located(
                                (By.XPATH, "//div[@class='selected-item']")))
                            item_list = [select_item[i].text for i in range(len(select_item)) if i != 1]

                            if i == 0:
                                old_items = item_list
                            else:
                                # 比對完再取代
                                if old_items == item_list:
                                    print("Fail: 點擊 手機殼顏色無反應")
                                    print(f"之前: {old_items}")
                                    print(f"當前: {item_list}")
                                    result_list.append("False")
                                else:
                                    old_items = item_list
                    except:
                        print("Fail: 確認 Clear產品 -> 手機殼顏色 時異常")
                        result_list.append("False")
                except:
                    print("Fail: 確認 Clear產品 時異常")
                    result_list.append("False")

                # Mod NX
                try:
                    WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                        (By.XPATH, "//p[text()='Mod NX']"))).click()
                    # 確認已切換至產品
                    WebDriverWait(self.br, 10, 1).until(EC.presence_of_element_located(
                        (By.XPATH, "//div[./p[text()='Mod NX'] and contains(@class, 'active')]")))
                    product_option = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_all_elements_located(
                        (By.XPATH, "//div[@class='product-form__content__options']"
                                   "//p[@class='title' or @class='bundle__docs']")))
                    option_list = [option.text for option in product_option[1:]]
                    select_item = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_all_elements_located(
                        (By.XPATH, "//div[@class='selected-item']")))
                    item_list = [select_item[i].text for i in range(len(select_item)) if i != 2]
                    if ('Mod NX 整組（手機殼+背板）' or '手機殼顏色') not in option_list or \
                            list(filter(lambda x: '黑' not in x, item_list)):
                        print("Fail: Mod NX 產品資訊顯示有誤")
                        print(option_list)
                        print(item_list)
                        result_list.append("False")

                    # 手機殼顏色
                    try:
                        plus = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                            (By.XPATH, "//span[text()='手機殼顏色']/../..//div[contains(@class, 'plus')]")))
                        plus.click()
                        time.sleep(1)
                        # 判斷是否有展開
                        if 'minus' not in plus.get_attribute('class'):
                            plus.click()
                        color_list = WebDriverWait(self.br, 10, 1).until(EC.presence_of_all_elements_located(
                            (By.XPATH, "//div[@id='color-picker']/ul[@class='color-picker hr']/li")))
                        for i in range(len(color_list)):
                            color_list[i].click()
                            # 確認已切換至產品
                            WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                                (By.XPATH, "//button[@class='add-to-cart-btn' and not(contains(@disabled, 'disabled'))]")))
                            select_item = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_all_elements_located(
                                (By.XPATH, "//div[@class='selected-item']")))
                            item_list = [select_item[i].text for i in range(len(select_item)) if i != 1]

                            if i == 0:
                                old_items = item_list
                            else:
                                # 比對完再取代
                                if old_items == item_list:
                                    print("Fail: 點擊 手機殼顏色無反應")
                                    print(f"之前: {old_items}")
                                    print(f"當前: {item_list}")
                                    result_list.append("False")
                                else:
                                    old_items = item_list
                    except:
                        print("Fail: 確認 Mod NX產品 -> 手機殼顏色 時異常")
                        result_list.append("False")
                except:
                    print("Fail: 確認 Mod NX產品 時異常")
                    result_list.append("False")

                # SolidSuit
                try:
                    WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                        (By.XPATH, "//p[text()='SolidSuit']"))).click()
                    # 確認已切換至產品
                    WebDriverWait(self.br, 10, 1).until(EC.presence_of_element_located(
                        (By.XPATH, "//div[./p[text()='SolidSuit'] and contains(@class, 'active')]")))
                    product_option = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_all_elements_located(
                        (By.XPATH, "//div[@class='product-form__content__options']//p[@class='title']")))
                    option_list = [option.text for option in product_option[1:]]
                    select_item = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_all_elements_located(
                        (By.XPATH, "//div[@class='selected-item']")))
                    item_list = [select_item[i].text for i in range(len(select_item)) if i != 1]
                    if '手機殼顏色' not in option_list or\
                            list(filter(lambda x: '黑' not in x, item_list)):
                        print("Fail: SolidSuit 產品資訊顯示有誤")
                        print(option_list)
                        print(item_list)
                        result_list.append("False")

                    # 手機殼顏色
                    try:
                        plus = WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                            (By.XPATH, "//span[text()='手機殼顏色']/../..//div[contains(@class, 'plus')]")))
                        plus.click()
                        time.sleep(1)
                        # 判斷是否有展開
                        if 'minus' not in plus.get_attribute('class'):
                            plus.click()

                        color_list = WebDriverWait(self.br, 10, 1).until(EC.presence_of_all_elements_located(
                            (By.XPATH, "//div[@id='color-picker']/ul[@class='color-picker hr']/li")))

                        for i in range(len(color_list)):

                            color_list[i].click()
                            # 確認已切換至產品
                            WebDriverWait(self.br, 10, 1).until(EC.element_to_be_clickable(
                                (By.XPATH, "//button[@class='add-to-cart-btn' and not(contains(@disabled, 'disabled'))]")))
                            select_item = WebDriverWait(self.br, 10, 1).until(EC.visibility_of_all_elements_located(
                                (By.XPATH, "//div[@class='selected-item']")))
                            item_list = [select_item[i].text for i in range(len(select_item)) if i != 1]

                            if i == 0:
                                old_items = item_list
                            else:
                                # 比對完再取代
                                if old_items == item_list:
                                    print("Fail: 點擊 手機殼顏色無反應")
                                    print(f"之前: {old_items}")
                                    print(f"當前: {item_list}")
                                    result_list.append("False")
                                else:
                                    old_items = item_list
                    except:
                        print("Fail: 確認 SolidSuit產品 -> 手機殼顏色 時異常")
                        result_list.append("False")
                except:
                    print("Fail: 確認 SolidSuit產品 時異常")
                    result_list.append("False")

        results = False if "False" in result_list else True
        self.assertEqual(True, results)


if __name__ == '__main__':
    test_units = unittest.TestSuite()
    test_units.addTest(AutomationTest("test_register"))
    test_units.addTest(AutomationTest("test_search"))

    now = datetime.now().strftime('%m-%d %H_%M_%S')
    root_path = os.getcwd()
    filename = now + '.html'
    fp = open(filename, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='網頁測試',
    )
    runner.run(test_units)
    fp.close()
