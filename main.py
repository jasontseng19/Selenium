# _*_ coding: UTF-8 _*_
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
from datetime import datetime
import os
import sys
import cv2
import base64
import numpy as np
import HTMLTestRunner
color_name = None


class AutomationTest(unittest.TestCase):
    """ 自動化測試 """

    @classmethod
    def setUpClass(cls):
        sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option("prefs", {
            "profile.password_manager_enabled": False,
            "credentials_enable_service": False,
            "profile.password_manager_leak_detection": False
        })
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()
        cls.driver.get("https://rhinoshield.tw/")
        # 同意cookie
        _ele = WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@class='switcher__confirm']")))
        time.sleep(1)
        _ele.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def close_popup(self):
        """ 關閉加入會員popup """

        try:
            # 關閉popup
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "//*[name()='svg']/*[name()='title']/.."))).click()
        except:
            # 若無出現則為pass
            pass

    def test_register(self):
        """ 測試註冊資訊 """

        # init
        result_list = []
        page = True

        try:
            self.close_popup()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/account']"))).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//a[./input[@value='註冊']]"))).click()
            # 確認是否在註冊頁面
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='register']//div[@class='form' and not(contains(@style, 'display: none'))]")))
        except:
            print("Fail: 無法進到註冊頁面")
            page = False
            result_list.append("False")

        # 確認有進到註冊頁面在進行
        if page:
            print("\n======= 測試「姓氏」=======")
            # 姓氏
            try:
                input_first_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='first-name']")))
                input_first_name.send_keys("123")
                try:
                    error_msg = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//input[@id='first-name']/..//p[@class='form__error-message']")))
                    if "請輸入正確的字元" not in error_msg.text:
                        print(f"Fail:「姓氏」輸入錯誤字元，顯示訊息有誤:{error_msg.text}")
                        result_list.append("False")
                except:
                    print("Fail:「姓氏」輸入錯誤字元時無顯示錯誤提示")
                    result_list.append("False")

                # 輸入正確格式
                input_first_name.clear()
                input_first_name.send_keys("asd")
            except:
                print("Fail: 測試「姓氏」欄位失敗")
                result_list.append("False")
            print("*** 測試結束 ***\n")

            print("======= 測試「姓名」=======")
            # 姓名
            try:
                input_last_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='last-name']")))
                input_last_name.send_keys("123")
                try:
                    error_msg = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//input[@id='last-name']/..//p[@class='form__error-message']")))
                    if "請輸入正確的字元" not in error_msg.text:
                        print(f"Fail:「姓名」輸入錯誤字元，顯示訊息有誤:{error_msg.text}")
                        result_list.append("False")
                except:
                    print("Fail:「姓名」輸入錯誤字元時無顯示錯誤提示")
                    result_list.append("False")

                # 輸入正確格式
                input_last_name.clear()
                input_last_name.send_keys("asd")
            except:
                print("Fail: 測試「姓名」欄位失敗")
                result_list.append("False")
            print("*** 測試結束 ***\n")

            print("======= 測試「信箱」=======")
            # 信箱
            try:
                input_mail = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='customer-email']")))
                input_mail.send_keys("123")
                try:
                    error_msg = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//input[@id='customer-email']/..//p[@class='form__error-message']")))
                    if "Email包含無效的網域名稱，請確認輸入的內容" not in error_msg.text:
                        print(f"Fail:「信箱」輸入錯誤字元，顯示訊息有誤:{error_msg.text}")
                        result_list.append("False")
                except:
                    print("Fail:「信箱」輸入錯誤字元時無顯示錯誤提示")
                    result_list.append("False")

                # 輸入正確格式
                input_mail.clear()
                input_mail.send_keys("asd@asd.asd")
            except:
                print("Fail: 測試「信箱」欄位失敗")
                result_list.append("False")
            print("*** 測試結束 ***\n")

            print("======= 測試「密碼」=======")
            # 密碼
            try:
                input_pwd = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='password']")))
                input_pwd.send_keys("asd")
                try:
                    error_msg = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//input[@id='password']/../..//p[@class='form__error-message']")))
                    if "密碼至少要 5 個字元" not in error_msg.text:
                        print(f"Fail:「密碼」輸入錯誤字元，顯示訊息有誤:{error_msg.text}")
                        result_list.append("False")
                except:
                    print("Fail:「密碼」輸入錯誤字元時無顯示錯誤提示")
                    result_list.append("False")

                # 輸入正確格式
                input_pwd.clear()
                input_pwd.send_keys("asdas")
            except:
                print("Fail: 測試「密碼」欄位失敗")
                result_list.append("False")
            print("*** 測試結束 ***\n")

            print("======= 測試「點擊完成」=======")
            # 點擊完成
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(), '完成')]"))).click()

                # 關閉認證popup
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//button[text()='我知道了']"))).click()
            except:
                print("Fail: 測試「完成」按鈕失敗")
                result_list.append("False")
            print("*** 測試結束 ***\n")

        results = False if "False" in result_list else True
        self.assertEqual(True, results)

    def test_search(self):
        """ 測試搜尋功能 """

        # init
        result_list = []
        search_page_data = []
        product_page = True
        search_result = True

        print("\n======= 測試「搜尋」=======")
        # 搜尋
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='https://shop.rhinoshield.tw/search/designs']"))).click()
            self.close_popup()
            input_search = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@type='search']")))
            input_search.send_keys("qwe")
            search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//button[./span[text()='搜尋']]")))
            search_button.click()
            time.sleep(1)
            search_msg_ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//h1[text()='犀牛盾設計展間']/following-sibling::p")))
            if '無搜尋結果' not in search_msg_ele.text:
                print(f"Fail: 「搜尋-未銷售商品」時顯示錯誤:{search_msg_ele.text}")
                result_list.append("False")

            input_search.clear()
            input_search.clear()
            time.sleep(1)
            input_search.send_keys("Naruto")
            search_button.click()
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(
                (By.XPATH, "//p[text()='抱歉，無搜尋結果 ']")))

            if 'Naruto' not in search_msg_ele.text and '項' not in search_msg_ele.text:
                print(f"Fail: 「搜尋-銷售商品」時顯示錯誤:{search_msg_ele.text}")
                result_list.append("False")
                search_result = False
        except:
            print("Fail: 測試「搜尋商品」失敗")
            result_list.append("False")
            search_result = False
        print("*** 測試結束 ***\n")

        if search_result:
            # 點選商品
            try:
                # 取第一筆資訊
                search_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@data-tour-id='search-results']/a[1]//div[@class='search-result--card__content']"))).text
                search_page_data = search_text.split("\n")

                # 點擊第一筆
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@data-tour-id='search-results']/a[1]"))).click()
                time.sleep(1)
                handles = self.driver.window_handles
                self.driver.switch_to.window(handles[-1])

                self.close_popup()

                # 關閉上方廣告bar
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='flex w-full bg-black']//*[name()='svg' and @viewBox='0 0 24 24']"))).click()

                # 判斷跳轉後的商品資訊是否正確
                print("======= 測試「驗證 - 系列/金額 資訊」=======")
                try:
                    # 系列
                    product_series = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//h1"))).text
                    if product_series not in search_page_data:
                        print(f"Fail:「系列」顯示有誤:{product_series}")
                        print(f"搜尋頁面資訊:{search_page_data}")
                        result_list.append("False")
                        product_page = False

                    # 系列/金額
                    footer_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//div[contains(@class, 'items-center') and contains(@class, 'py-3')]"))).text
                    product_series_and_cost = footer_text.split("\n")
                    product_series_and_cost.pop(2)
                    diff = list(set(search_page_data).symmetric_difference(set(product_series_and_cost)))
                    if diff:
                        print(f"Fail:「系列/金額」顯示有誤:{product_series_and_cost}")
                        print(f"搜尋頁面資訊:{search_page_data}")
                        result_list.append("False")
                except:
                    print("Fail:「確認商品」時失敗")
                    result_list.append("False")
                    product_page = False
                print("*** 測試結束 ***\n")
            except:
                print("Fail:「點選商品」時失敗")
                result_list.append("False")
                product_page = False

        # 確認商品頁面正確在進行
        if product_page:
            old_img_src = None
            old_image = None

            print("======= 測試「裝置顏色」=======")
            # 裝置顏色(手機顏色)
            try:
                # 當前手機型號
                phone_type_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='relative h-full']//p"))).text
                print(f"---- 當前手機型號「{phone_type_text}」-----")

                phone_color_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='w-18']")))
                phone_color_button.click()
                time.sleep(1)
                phone_color_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(
                    (By.XPATH, "//div[@class='w-18']//li/span")))
                for index, i in enumerate(phone_color_list):
                    color_num = index + 1
                    if ' before:opacity-100 ' in i.get_attribute('class') and color_num == 1:
                        # 關閉下拉選單
                        phone_color_button.click()
                        time.sleep(1)

                        old_color_num = color_num

                        # 點開圖片
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, "//div[@class='relative w-full h-full']"))).click()
                        time.sleep(1)
                        # wait loading
                        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(
                            (By.XPATH, "//div[@class='PhotoView__PhotoWrap']"
                                       "//img[@class='PhotoView__Photo' and contains(@src, 'data:image/svg')]")))

                        # 擷取當下畫面
                        old_canvas_base64 = self.driver.get_screenshot_as_base64()
                        old_canvas_png = base64.b64decode(old_canvas_base64)
                        old_image = cv2.imdecode(np.frombuffer(old_canvas_png, np.uint8), 1)

                        old_img_src = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                            (By.XPATH, "//img[@class='PhotoView__Photo' "
                                       "and contains(@src, 'blob:http')]"))).get_attribute('src')

                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, "//*[name()='svg' and @viewBox='0 0 768 768']"))).click()

                        continue
                    else:
                        phone_color_button.click()
                        time.sleep(1)
                        i.click()
                        time.sleep(1)

                        if ' before:opacity-100 ' not in i.get_attribute('class'):
                            print(f"Fail:「第{color_num}個」切換顏色失敗")
                            result_list.append("False")
                            continue
                        else:
                            # 點開圖片
                            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                                (By.XPATH, "//div[@class='relative w-full h-full']"))).click()
                            time.sleep(1)
                            # wait loading
                            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(
                                (By.XPATH, "//div[@class='PhotoView__PhotoWrap']"
                                           "//img[@class='PhotoView__Photo' and contains(@src, 'data:image/svg')]")))
                            img_src = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                                (By.XPATH, "//img[@class='PhotoView__Photo' "
                                           "and contains(@src, 'blob:http')]"))).get_attribute('src')

                            if img_src == old_img_src:
                                print(f"Fail:「第{color_num}個」切換網址無變化")
                                print(f"「第{old_color_num}個」網址:{old_img_src}")
                                print(f"「第{color_num}個」網址:{img_src}")
                                result_list.append("False")
                                continue

                            # 比對圖片
                            # 擷取當下畫面
                            canvas_base64 = self.driver.get_screenshot_as_base64()
                            canvas_png = base64.b64decode(canvas_base64)
                            target = cv2.imdecode(np.frombuffer(canvas_png, np.uint8), 1)

                            res = cv2.matchTemplate(old_image, target, cv2.TM_CCOEFF_NORMED)
                            _, max_v, _, _ = cv2.minMaxLoc(res)

                            if max_v == 1:
                                print(f"Fail:「第{color_num}個」圖片無變化")
                                print(f"「第{old_color_num}個」圖片網址:{old_img_src}")
                                print(f"「第{color_num}個」圖片網址:{img_src}")
                                result_list.append("False")
                            else:
                                old_color_num = color_num
                                old_img_src = img_src
                                old_image = target

                            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                                (By.XPATH, "//*[name()='svg' and @viewBox='0 0 768 768']"))).click()
            except:
                print("Fail: 測試「裝置顏色」失敗")
                result_list.append("False")
            print("*** 測試結束 ***\n")

            print("======= 測試「手機殼顏色」=======")
            # 手機殼顏色
            try:
                old_color_name = None
                old_img_src = None
                old_image = None
                new_color_name = None

                # 手機殼產品
                phone_case_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//p[text()='選擇產品']/following-sibling::p"))).text
                print(f"---- 當前手機殼產品「{phone_case_text}」-----")

                color_ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//p[text()='顏色']/following-sibling::p")))

                # 取得所有顏色
                color_list = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[./p[text()='顏色']]/../following-sibling::ul//span")))
                for index, color in enumerate(color_list):
                    color_num = index + 1
                    color.click()

                    if color_num == 1:
                        old_color_num = color_num
                        old_color_name = color_ele.text

                        # 點開圖片
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, "//div[@class='relative w-full h-full']"))).click()
                        time.sleep(1)
                        # wait loading
                        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(
                            (By.XPATH, "//div[@class='PhotoView__PhotoWrap']"
                                       "//img[@class='PhotoView__Photo' and contains(@src, 'data:image/svg')]")))

                        # 擷取當下畫面
                        old_canvas_base64 = self.driver.get_screenshot_as_base64()
                        old_canvas_png = base64.b64decode(old_canvas_base64)
                        old_image = cv2.imdecode(np.frombuffer(old_canvas_png, np.uint8), 1)

                        old_img_src = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                            (By.XPATH, "//img[@class='PhotoView__Photo' "
                                       "and contains(@src, 'blob:http')]"))).get_attribute('src')

                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, "//*[name()='svg' and @viewBox='0 0 768 768']"))).click()

                        continue
                    else:
                        new_color_name = color_ele.text
                        global color_name
                        color_name = new_color_name

                        if ' before:opacity-100 ' not in color.get_attribute('class'):
                            print(f"Fail:「第{color_num}個」切換顏色失敗")
                            result_list.append("False")
                            continue
                        elif new_color_name == old_color_name:
                            print(f"Fail:「第{color_num}個」切換後顏色名稱無變化")
                            print(f"「第{old_color_num}個」舊名稱:{old_color_name}")
                            print(f"「第{color_num}個」新名稱:{new_color_name}")
                            result_list.append("False")
                            continue
                        else:
                            # 點開圖片
                            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                                (By.XPATH, "//div[@class='relative w-full h-full']"))).click()
                            time.sleep(1)
                            # wait loading
                            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(
                                (By.XPATH, "//div[@class='PhotoView__PhotoWrap']"
                                           "//img[@class='PhotoView__Photo' and contains(@src, 'data:image/svg')]")))
                            img_src = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                                (By.XPATH, "//img[@class='PhotoView__Photo' "
                                           "and contains(@src, 'blob:http')]"))).get_attribute('src')

                            if img_src == old_img_src:
                                print(f"Fail:「第{color_num}個」切換網址無變化")
                                print(f"「第{old_color_num}個」網址:{old_img_src}")
                                print(f"「第{color_num}個」網址:{img_src}")
                                result_list.append("False")
                                continue

                            # 比對圖片
                            # 擷取當下畫面
                            canvas_base64 = self.driver.get_screenshot_as_base64()
                            canvas_png = base64.b64decode(canvas_base64)
                            target = cv2.imdecode(np.frombuffer(canvas_png, np.uint8), 1)

                            res = cv2.matchTemplate(old_image, target, cv2.TM_CCOEFF_NORMED)
                            _, max_v, _, _ = cv2.minMaxLoc(res)

                            if max_v == 1:
                                print(f"Fail:「第{color_num}個」圖片無變化")
                                print(f"「第{old_color_num}個」圖片網址:{old_img_src}")
                                print(f"「第{color_num}個」圖片網址:{img_src}")
                                result_list.append("False")
                            else:
                                old_color_num = color_num
                                old_img_src = img_src
                                old_image = target

                            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                                (By.XPATH, "//*[name()='svg' and @viewBox='0 0 768 768']"))).click()

            except:
                print("Fail: 測試「手機殼顏色」失敗 ")
                result_list.append("False")
            print("*** 測試結束 ***\n")

        results = False if "False" in result_list else True
        self.assertEqual(True, results)

    def test_shopping_car(self):
        """ 測試購物車 """

        # init
        result_list = []
        add_car = True
        sub_title = None
        product_style = None
        product_type = None
        # price = None
        phone_price_list = None

        print("\n======= 測試「加入購物車」=======")
        # 加入購物車
        try:
            # 取商品資訊
            sub_title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[./h1]/following-sibling::a"))).text
            # 產品樣式
            product_style = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "//p[text()='樣式']/following-sibling::p"))).text
            # 產品類型
            product_type = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//p[text()='產品類型']/following-sibling::p"))).text
            # 價錢
            phone_price_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'items-center') and contains(@class, 'py-3')]//div[./p]"))).text
            phone_price_list = phone_price_text.split("\n")
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//button/span[text()='加入購物車']"))).click()

            # 判斷是否加入成功
            alert_msg = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//p[text()='成功加入購物車！']")))
            if not alert_msg:
                print("Fail: 「加入購物車」無顯示提示訊息")
                result_list.append("False")

            # 加購頁面
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@data-title='手機保護貼']")))
            time.sleep(1)

            # 驗證數量
            car = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//li[@title='購物車']")))
            car_num = car.find_element(By.XPATH, "./a//span").text
            if "1" not in car_num:
                print(f"Fail: 「購物車-數量」顯示錯誤: {car_num}")
                result_list.append("False")
        except:
            print("Fail: 測試「加入購物車」失敗")
            result_list.append("False")
            add_car = False
        print("*** 測試結束 ***\n")

        # 有正常加入購物車在進行判斷
        if add_car:
            # 進入購物車頁面
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//button/span[text()='查看購物車']"))).click()
                time.sleep(1)
                # wait loading
                WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='loading__mask loading__mask__show']")))
                time.sleep(1)
                # 判斷購物車是否有商品
                try:
                    ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//div[@id='cart']//div[@class='expanded-message']"))).text
                    if "空的" in ele:
                        print(f"Fail: {ele}")
                        result_list.append("False")
                    else:
                        print(f"Fail: 「購物車頁面」顯示錯誤訊息: {ele}")
                        result_list.append("False")
                except:
                    print("======= 測試「檢查購物車資訊」=======")
                    try:
                        product_td = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
                            (By.XPATH, "//div[@id='CartProducts']//div[contains(@class, 'td')]")))
                        car_product = []
                        for product in product_td[1:-2]:
                            if product.get_attribute("class") == 'td qty':
                                car_num = product.find_element(By.XPATH, "//input")
                                car_product.append(car_num.get_attribute("value"))
                            else:
                                if '\n' in product.text:
                                    _text = product.text.split('\n')
                                    for _ in _text:
                                        if '/' in _:
                                            new_text = _.split(' / ')
                                            for _new in new_text:
                                                car_product.append(_new)
                                        else:
                                            car_product.append(_)
                                else:
                                    car_product.append(product.text)

                        check1 = len([i for i in [sub_title, color_name, '1'] if i not in car_product])
                        check2 = len([i for i in [product_style, product_type] if i not in car_product[1]])
                        check3 = len([i for i in phone_price_list if i not in car_product])
                        if (check1 or check2 or check3) != 0:
                            print(f"Fail:「購物車頁面-商品」顯示錯誤")
                            print(f"「購物車頁面-商品」: {car_product}")
                            print(f"「商品頁-樣式」:{product_style}")
                            print(f"「商品頁-類型」:{product_type}")
                            print(f"「商品頁-副標題」:{sub_title}")
                            print(f"「商品頁-價錢」:{phone_price_list}")
                            print(f"「商品頁-顏色」:{color_name}")
                            result_list.append("False")
                    except:
                        print("Fail: 檢查「購物車頁面-商品」時失敗")
                        result_list.append("False")
                    print("*** 測試結束 ***\n")

                    print("======= 測試「金額」=======")
                    # 測試金額
                    try:
                        # 商品數+1
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH, "//span[text()='+']"))).click()
                        time.sleep(1)
                        # wait loading
                        WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(
                            (By.XPATH, "//div[@class='loading__mask loading__mask__show']")))
                        price_dict = {
                            "合計": "",
                            "商品金額": "",
                            "運費小計": "",
                            "總共省下": "",
                            "應付金額": "",
                        }

                        for i in price_dict:
                            if i == '合計':
                                ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                                    (By.XPATH, "//div[@class='td sumprice not-mobile']")))
                                price_dict['合計'] = "".join(filter(lambda x: x in '0123456789', ele.text))
                            else:
                                ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                                    (By.XPATH, f"//p[text()='{i}']/following-sibling::p")))
                                price_dict[i] = "".join(filter(lambda x: x in '0123456789', ele.text))

                        # 數量
                        qty = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                            (By.XPATH, "//div[@class='td qty']//input"))).get_attribute("value")

                        # 金額
                        price = "".join(filter(lambda x: x in '0123456789', phone_price_list[0]))

                        # 驗證金額
                        if int(price) * int(qty) != int(price_dict['合計']):
                            print("Fail:「金額 x 數量」與「合計金額」不同")
                            print(f"「金額」: {price}")
                            print(f"「數量」: {qty}")
                            print(f"「合計金額」: {price_dict['合計']}")
                            result_list.append("False")
                        elif int(price_dict['合計']) != (int(price_dict['商品金額']) - int(price_dict['總共省下'])):
                            print("Fail: 「合計金額」與「商品金額 - 總共省下」不同")
                            print(f"「合計金額」: {price_dict['合計']}")
                            print(f"「商品金額」: {price_dict['商品金額']}")
                            print(f"「總共省下」: {price_dict['總共省下']}")
                            result_list.append("False")
                        elif (int(price_dict['商品金額']) - int(price_dict['總共省下'])) + int(price_dict['運費小計']) != int(price_dict['應付金額']):
                            print("Fail:「商品金額 - 總共省下 + 運費小計」與「應付金額」不同顯示異常")
                            print(f"「商品金額」: {price_dict['商品金額']}")
                            print(f"「總共省下」: {price_dict['總共省下']}")
                            print(f"「運費小計」: {price_dict['運費小計']}")
                            print(f"「應付金額」: {price_dict['應付金額']}")
                            result_list.append("False")
                    except:
                        print(traceback.format_exc())
                        print("Fail: 測試「金額」時失敗")
                        result_list.append("False")
                    print("*** 測試結束 ***\n")

                    print("======= 測試「清空購物車」=======")
                    # 清空購物車
                    try:
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH, "//div[@class='td remove']"))).click()
                        time.sleep(1)
                        # wait loading
                        WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(
                            (By.XPATH, "//div[@class='loading__mask loading__mask__show']")))
                        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                            (By.XPATH, "//div[@id='cart']//div[@class='expanded-message']")))
                        if "按這裡開始購物吧" not in ele.text:
                            print(f"Fail:「清空後購物車」顯示訊息異常: {ele.text}")
                            result_list.append("False")
                    except:
                        print("Fail: 測試「清空購物車」時失敗")
                        result_list.append("False")
                    print("*** 測試結束 ***\n")
            except:
                print("Fail: 測試「判斷購物車頁面資訊」失敗")
                result_list.append("False")

        results = False if "False" in result_list else True
        self.assertEqual(True, results)


if __name__ == '__main__':
    test_units = unittest.TestSuite()
    test_units.addTest(AutomationTest("test_register"))
    test_units.addTest(AutomationTest("test_search"))
    test_units.addTest(AutomationTest("test_shopping_car"))

    now = datetime.now().strftime('%m-%d %H_%M_%S')
    filename = now + '.html'
    with open(filename, 'wb+') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='網頁自動化測試',
        )
        runner.run(test_units)
