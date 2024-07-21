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
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
color_name = None


class AutomationTest(unittest.TestCase):
    """ 自動化測試 """

    @classmethod
    def setUpClass(cls):
        sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
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
                (By.XPATH, "//div[@data-testid='POPUP']//button[@aria-label='Close dialog 1']"))).click()
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
            input_search.send_keys(Keys.ENTER)
            time.sleep(1)
            search_msg_ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//p[@class='text-title-sm-lighter text-center']")))
            if '無搜尋結果' not in search_msg_ele.text:
                print(f"Fail: 「搜尋-未銷售商品」時顯示錯誤:{search_msg_ele.text}")
                result_list.append("False")

            input_search.clear()
            time.sleep(1)
            input_search.send_keys("Naruto")
            input_search.send_keys(Keys.ENTER)
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
                search_ele = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[@data-tour-id='search-results']/div[1]//p[not(span)]")))
                for i in search_ele:
                    if '/' in i.text:
                        search_page_data.append(i.text.split(' /')[0])
                    else:
                        search_page_data.append(i.text)

                # 點擊第一筆
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@data-tour-id='search-results']/div[1]"))).click()
                time.sleep(1)
                handles = self.driver.window_handles
                self.driver.switch_to.window(handles[-1])

                self.close_popup()

                # 關閉試試看
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='close']"))).click()

                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                    (By.XPATH, "//div[@id='caseProduct']")))
                time.sleep(1)

                # 判斷跳轉後的商品資訊是否正確
                print("======= 測試「驗證上方 select 資訊」=======")
                try:
                    # 上方 select 資訊
                    # 產品
                    product = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//div[@class='product-selector']/p"))).text
                    if product not in search_page_data:
                        print(f"Fail:「產品」顯示有誤:{product}")
                        print(f"搜尋頁面資訊:{search_page_data}")
                        result_list.append("False")

                    # 型號
                    device = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//div[@class='selected']"))).text
                    if device not in search_page_data:
                        print(f"Fail:「型號」顯示有霧:{device}")
                        print(f"搜尋頁面資訊:{search_page_data}")
                        result_list.append("False")

                    # 系列
                    product_content = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//div[@class='product-form']"))).text
                    for i in search_page_data:
                        if i not in product_content:
                            print(f"Fail:「{i}」 不在此商品頁面")
                            result_list.append("False")
                            product_page = False
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
            # 當前window_id
            current_id = self.driver.current_window_handle
            all_handles = self.driver.window_handles
            old_color_id = None
            old_img_src = None
            old_image = None

            print("======= 測試「裝置顏色」=======")
            # 裝置顏色(手機顏色)
            try:
                phone_color_list = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(
                    (By.XPATH, "//ul[@class='color-picker']/li")))
                for i in phone_color_list:
                    if i.get_attribute('class') == 'active':
                        old_color_id = i.get_attribute('id')
                        old_img_src = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, "//div[@class='product-images-wrap']"
                                       "//img[@class='fluid-img__img']"))).get_attribute('src')
                        continue

                    i.find_element(By.XPATH, './/input').click()
                    time.sleep(1)
                    # wait loading
                    WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(
                        (By.XPATH, "//div[@class='loading__mask loading__mask__show']"
                                   "/div[@class='loading__indicator']")))

                    new_color_id = i.get_attribute('id')

                    if i.get_attribute('class') != 'active':
                        print(f"Fail:「{new_color_id}」切換顏色失敗")
                        result_list.append("False")
                        continue
                    else:
                        img_src = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, "//div[@class='product-images-wrap']"
                                       "//img[@class='fluid-img__img']"))).get_attribute('src')

                        if img_src == old_img_src:
                            print(f"Fail:「{new_color_id}」切換網址無變化")
                            print(f"「{old_color_id}」網址:{old_img_src}")
                            print(f"「{new_color_id}」網址:{img_src}")
                            result_list.append("False")
                            continue
                        else:
                            # 比對圖片

                            if not isinstance(old_image, np.ndarray):
                                # 新分頁，開舊圖片
                                new_window = f"window.open('{old_img_src}');"
                                self.driver.execute_script(new_window)
                                time.sleep(2)

                                handles = self.driver.window_handles
                                for w in handles:
                                    if w not in all_handles:
                                        self.driver.switch_to.window(w)

                                # 擷取當下畫面
                                old_canvas_base64 = self.driver.get_screenshot_as_base64()
                                old_canvas_png = base64.b64decode(old_canvas_base64)
                                old_image = cv2.imdecode(np.frombuffer(old_canvas_png, np.uint8), 1)

                                self.driver.close()
                                self.driver.switch_to.window(current_id)

                            # 新分頁，開新圖片
                            new_window = f"window.open('{img_src}');"
                            self.driver.execute_script(new_window)
                            time.sleep(2)

                            handles = self.driver.window_handles
                            for w in handles:
                                if w not in all_handles:
                                    self.driver.switch_to.window(w)

                            # 擷取當下畫面
                            canvas_base64 = self.driver.get_screenshot_as_base64()
                            canvas_png = base64.b64decode(canvas_base64)
                            target = cv2.imdecode(np.frombuffer(canvas_png, np.uint8), 1)

                            res = cv2.matchTemplate(old_image, target, cv2.TM_CCOEFF_NORMED)
                            _, max_v, _, _ = cv2.minMaxLoc(res)

                            if max_v == 1:
                                print(f"Fail:「{new_color_id}」圖片無變化")
                                print(f"「{old_color_id}」圖片網址:{old_img_src}")
                                print(f"「{new_color_id}」圖片網址:{img_src}")
                                result_list.append("False")
                            else:
                                old_color_id = new_color_id
                                old_img_src = img_src
                                old_image = target

                            self.driver.close()
                            self.driver.switch_to.window(current_id)
            except:
                print("Fail: 測試「裝置顏色」失敗")
                result_list.append("False")
            print("*** 測試結束 ***\n")

            print("======= 測試「手機殼顏色」=======")
            # 手機殼顏色
            try:
                old_color_name = None
                old_color_id = None
                old_img_src = None
                old_image = None

                # 確認是否單一版本
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, "//span[text()='版本']")))
                    only_one_type = False
                except:
                    only_one_type = True

                if not only_one_type:
                    # 確認版本有無展開
                    _ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, "//div[@class='product-form__content__options selectors types-selectors']/div")))
                    if 'active' not in _ele.get_attribute('class'):
                        _ele.click()
                        time.sleep(1)

                    type_list = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(
                        (By.XPATH, "//div[@class='drop-folder__slot-wrapper']//div[./p]")))
                    for i in type_list:
                        if 'active' not in i.get_attribute('class'):
                            i.click()
                            time.sleep(1)

                        # 確認手機殼顏色有無展開
                        _ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, "//div[@class='product-form__content__options"
                                       " selectors case-color-selectors']/div")))
                        if 'active' not in _ele.get_attribute('class'):
                            _ele.click()
                            time.sleep(1)

                        # 取得所有顏色
                        color_list = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(
                            (By.XPATH, "//div[@class='drop-folder__slot-wrapper']//div[@id='color-picker']/ul/li")))
                        for color in color_list:
                            if i.get_attribute('class') == 'active':
                                old_color_name = _ele.text.split(' ')[-1]
                                old_color_id = color.get_attribute('id')
                                old_img_src = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                                    (By.XPATH, "//div[@class='product-images-wrap']"
                                               "//img[@class='fluid-img__img']"))).get_attribute('src')
                                continue

                            color.click()
                            # wait loading
                            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(
                                (By.XPATH, "//div[@class='loading__mask loading__mask__show']"
                                           "/div[@class='loading__indicator']")))

                            new_color_name = _ele.text.split(' ')[-1]
                            global color_name
                            color_name = new_color_name
                            new_color_id = color.get_attribute('id')

                            if 'active' not in i.get_attribute('class'):
                                print(f"Fail:「{new_color_id}」切換顏色失敗")
                                result_list.append("False")
                                continue
                            else:
                                img_src = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                                    (By.XPATH, "//div[@class='product-images-wrap']"
                                               "//img[@class='fluid-img__img']"))).get_attribute('src')

                                if img_src == old_img_src:
                                    print(f"Fail:「{new_color_id}」切換後網址無變化")
                                    print(f"「{old_color_id}」舊網址:{old_img_src}")
                                    print(f"「{new_color_id}」新網址:{img_src}")
                                    result_list.append("False")
                                    continue
                                elif new_color_name == old_color_name:
                                    print(f"Fail:「{new_color_id}」切換後顏色名稱無變化")
                                    print(f"「{old_color_id}」舊名稱:{old_color_name}")
                                    print(f"「{new_color_id}」新名稱:{new_color_name}")
                                    result_list.append("False")
                                    continue
                                else:
                                    # 比對圖片

                                    if not isinstance(old_image, np.ndarray):
                                        # 新分頁，開舊圖片
                                        new_window = f"window.open('{old_img_src}');"
                                        self.driver.execute_script(new_window)
                                        time.sleep(2)

                                        handles = self.driver.window_handles
                                        for w in handles:
                                            if w not in all_handles:
                                                self.driver.switch_to.window(w)

                                        # 擷取當下畫面
                                        old_canvas_base64 = self.driver.get_screenshot_as_base64()
                                        old_canvas_png = base64.b64decode(old_canvas_base64)
                                        old_image = cv2.imdecode(np.frombuffer(old_canvas_png, np.uint8), 1)

                                        self.driver.close()
                                        self.driver.switch_to.window(current_id)

                                    # 新分頁，開新圖片
                                    new_window = f"window.open('{img_src}');"
                                    self.driver.execute_script(new_window)
                                    time.sleep(2)

                                    handles = self.driver.window_handles
                                    for w in handles:
                                        if w not in all_handles:
                                            self.driver.switch_to.window(w)

                                    # 擷取當下畫面
                                    canvas_base64 = self.driver.get_screenshot_as_base64()
                                    canvas_png = base64.b64decode(canvas_base64)
                                    target = cv2.imdecode(np.frombuffer(canvas_png, np.uint8), 1)

                                    res = cv2.matchTemplate(old_image, target, cv2.TM_CCOEFF_NORMED)
                                    _, max_v, _, _ = cv2.minMaxLoc(res)

                                    if max_v == 1:
                                        print(f"Fail:「{new_color_id}」圖片無變化")
                                        print(f"「{old_color_id}」圖片網址:{old_img_src}")
                                        print(f"「{new_color_id}」圖片網址:{img_src}")
                                        result_list.append("False")
                                    else:
                                        old_color_name = new_color_name
                                        old_color_id = new_color_id
                                        old_img_src = img_src
                                        old_image = target

                                    self.driver.close()
                                    self.driver.switch_to.window(current_id)
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
        title = None
        sub_title = None
        price = None

        print("\n======= 測試「加入購物車」=======")
        # 加入購物車
        try:
            # 取商品資訊
            title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='caseProduct']//h2[@class='product-form__content__title']"))).text
            sub_title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='caseProduct']//p[@class='product-form__content__subtitle']"))).text
            price = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='caseProduct']//span[@class='total-price']"))).text
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@class='add-to-cart-btn available']"))).click()

            # 加購頁面
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@data-title='保護貼']")))
            time.sleep(1)

            # 驗證數量
            car = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//li[@title='購物車']")))
            car_num = car.find_element(By.XPATH, "./a//span").text
            if "1" not in car_num:
                print(f"Fail: 「購物車-數量」顯示錯誤: {car_num}")
                result_list.append("False")

            # 移至購物車圖示判斷顯示商品
            ActionChains(self.driver).move_to_element(car).perform()
            time.sleep(1)
            car_product = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//p[text()='購物車']/following-sibling::div/div[./a]"))).text

            _check = [i for i in [title, sub_title, price, 'x 1'] if i not in car_product]
            if len(_check) != 0:
                print("Fail:「購物車-商品有誤」")
                print(f"「購物車-商品內容」: {car_product}")
                print(f"「商品頁-大標題」:{title}")
                print(f"「商品頁-副標題」:{sub_title}")
                print(f"「商品頁-價錢」:{price}")
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
                    (By.XPATH, "//button[text()='查看購物車']"))).click()
                time.sleep(1)
                # wait loading
                WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='loading__mask loading__mask__show']")))
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
                                        car_product.append(_)
                                else:
                                    car_product.append(product.text)

                        check1 = len([i for i in [title, sub_title] if i not in car_product[0]])
                        check2 = len([i for i in [color_name, price, '1'] if i not in car_product])
                        if (check1 or check2) != 0:
                            print(f"Fail:「購物車頁面-商品」顯示錯誤")
                            print(f"「購物車頁面-商品」: {car_product}")
                            print(f"「商品頁-大標題」:{title}")
                            print(f"「商品頁-副標題」:{sub_title}")
                            print(f"「商品頁-價錢」:{price}")
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
                            "應付金額": "",
                        }

                        for i in price_dict:
                            if i == '合計':
                                ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                                    (By.XPATH, "//div[@class='td sumprice not-mobile']")))
                                price_dict['合計'] = "".join(filter(lambda x: x in '0123456789', ele.text))
                            else:
                                ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                                    (By.XPATH, f"//p[text()='{i}']/..//p[@class='total__wrap__price']")))
                                price_dict[i] = "".join(filter(lambda x: x in '0123456789', ele.text))

                        # 數量
                        qty = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                            (By.XPATH, "//div[@class='td qty']//input"))).get_attribute("value")

                        # 金額
                        price = "".join(filter(lambda x: x in '0123456789', price))

                        # 驗證金額
                        if int(price) * int(qty) != int(price_dict['合計']):
                            print("Fail:「金額 x 數量」與「合計金額」不同")
                            print(f"「金額」: {price}")
                            print(f"「數量」: {qty}")
                            print(f"「合計金額」: {price_dict['合計']}")
                            result_list.append("False")
                        elif int(price_dict['合計']) != int(price_dict['商品金額']):
                            print("Fail: 「合計金額」與「商品金額」不同")
                            print(f"「合計金額」: {price_dict['合計']}")
                            print(f"「商品金額」: {price_dict['商品金額']}")
                            result_list.append("False")
                        elif int(price_dict['商品金額']) + int(price_dict['運費小計']) != int(price_dict['應付金額']):
                            print("Fail:「商品金額 + 運費小計」與「應付金額」不同顯示異常")
                            print(f"「商品金額」: {price_dict['商品金額']}")
                            print(f"「運費小計」: {price_dict['運費小計']}")
                            print(f"「應付金額」: {price_dict['應付金額']}")
                            result_list.append("False")
                    except:
                        print("Fail: 測試「金額」時失敗")
                        result_list.append("False")
                    print("*** 測試結束 ***\n")

                    print("======= 測試「清空購物車」=======")
                    # 清空購物車
                    try:
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH, "//div[@class='td remove']"))).click()
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
