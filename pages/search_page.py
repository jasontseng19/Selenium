# _*_ coding: UTF-8 _*_
from base_page import BasePage
import time
import cv2
import base64
import numpy as np


class SearchPage(BasePage):
    """ 搜尋頁面 """

    # locate
    search_icon = "//a[@href='https://shop.rhinoshield.tw/search/designs']"
    search_input = "//input[@type='search']"
    search_button = "//button[./span[text()='搜尋']]"
    search_msg = "//h1[text()='犀牛盾設計展間']/following-sibling::p"
    no_search_msg = "//p[text()='抱歉，無搜尋結果 ']"
    first_info = "//div[@data-tour-id='search-results']/a[1]//div[@class='search-result--card__content']"
    first_product = "//div[@data-tour-id='search-results']/a[1]"
    top_ad_close = "//div[@class='flex w-full bg-black']//*[name()='svg' and @viewBox='0 0 24 24']"
    right_ad_close = "//*[name()='svg' and @viewBox='0 0 26 26']"
    series = "//h1"
    footer = "//div[contains(@class, 'items-center') and contains(@class, 'py-3')]"
    phone_type = "//div[@class='relative h-full']//p"
    phone_type_color_button = "//div[@class='w-18']"
    phone_type_color_list = "//div[@class='w-18']//li/span"
    pic = "//div[@class='relative w-full h-full']"
    loading = "//div[@class='PhotoView__PhotoWrap']//img[@class='PhotoView__Photo' and contains(@src, 'data:image/svg')]"
    img_src = "//img[@class='PhotoView__Photo' and contains(@src, 'blob:http')]"
    pic_close = "//*[name()='svg' and @viewBox='0 0 768 768']"
    phone_case = "//p[text()='選擇產品']/following-sibling::p"
    phone_case_color = "//p[text()='顏色']/following-sibling::p"
    phone_case_color_list = "//div[./p[text()='顏色']]/../following-sibling::ul//span"

    # 搜尋產品
    search_name = '星際大戰'

    def test_search(self):
        print("\n======= 測試「搜尋商品」=======")
        result_list = []
        self.wait_until_element_is_clickable(self.search_icon).click()
        input_search = self.wait_until_element_is_clickable(self.search_input)
        input_search.send_keys("qwe")
        button = self.wait_until_element_is_clickable(self.search_button)
        button.click()
        time.sleep(1)
        search_msg_ele = self.wait_until_element_is_visibility(self.search_msg)
        if '無搜尋結果' not in search_msg_ele.text:
            print(f"Fail: 「搜尋-未銷售商品」時顯示錯誤:{search_msg_ele.text}")
            result_list.append("False")

        self.clear_text(self.search_input)
        time.sleep(1)
        input_search.send_keys(self.search_name)
        button.click()
        time.sleep(1)
        self.wait_until_element_is_invisibility(self.no_search_msg)
        time.sleep(1)
        if self.search_name not in search_msg_ele.text and '項' not in search_msg_ele.text:
            print(f"Fail: 「搜尋-銷售商品」時顯示錯誤:{search_msg_ele.text}")
            result_list.append("False")

        results = False if "False" in result_list else True
        return results

    def test_click_first_product(self):
        result_list = []
        search_text = self.wait_until_element_is_presence(self.first_info).text
        search_page_data = search_text.split("\n")
        # 點擊第一筆
        self.wait_until_element_is_clickable(self.first_product).click()
        time.sleep(1)
        self.switch_to_tab(-1)
        try:
            # 關閉上方廣告bar
            self.wait_until_element_is_clickable(self.top_ad_close).click()
            # 關閉右方廣告bar
            self.wait_until_element_is_clickable(self.right_ad_close).click()
        except:
            pass

        # 判斷跳轉後的商品資訊是否正確
        print("\n======= 測試「驗證 - 系列/金額 資訊」=======")
        # 系列
        product_series = self.wait_until_element_is_visibility(self.series).text
        if product_series not in search_page_data:
            print(f"Fail:「系列」顯示有誤:{product_series}")
            print(f"搜尋頁面資訊:{search_page_data}")
            result_list.append("False")

        # 系列/金額
        footer_text = self.wait_until_element_is_visibility(self.footer).text
        product_series_and_cost = footer_text.split("\n")
        product_series_and_cost = [i for i in product_series_and_cost if '購物車' not in i]
        diff = list(set(search_page_data).symmetric_difference(set(product_series_and_cost)))
        if diff:
            print(f"Fail:「系列/金額」顯示有誤:{product_series_and_cost}")
            print(f"搜尋頁面資訊:{search_page_data}")
            result_list.append("False")

        results = False if "False" in result_list else True
        return results

    def test_phone_type_color(self):
        old_img_src = None
        old_image = None
        result_list = []

        print("\n======= 測試「裝置顏色」=======")
        # 當前手機型號
        phone_type_text = self.wait_until_element_is_presence(self.phone_type).text
        print(f"---- 當前手機型號「{phone_type_text}」-----")
        phone_color_button = self.wait_until_element_is_clickable(self.phone_type_color_button)
        phone_color_button.click()
        time.sleep(1)
        phone_color_list = self.wait_until_any_elements_is_visibility(self.phone_type_color_list)
        for index, i in enumerate(phone_color_list):
            color_num = index + 1
            if ' before:opacity-100 ' in i.get_attribute('class') and color_num == 1:
                # 關閉下拉選單
                phone_color_button.click()
                time.sleep(1)

                old_color_num = color_num

                # 點開圖片
                self.wait_until_element_is_presence(self.pic).click()
                time.sleep(1)
                # wait loading
                self.wait_until_element_is_invisibility(self.loading)

                # 擷取當下畫面
                old_canvas_base64 = self.driver.get_screenshot_as_base64()
                old_canvas_png = base64.b64decode(old_canvas_base64)
                old_image = cv2.imdecode(np.frombuffer(old_canvas_png, np.uint8), 1)
                old_img_src = self.wait_until_element_is_visibility(self.img_src).get_attribute('src')
                self.wait_until_element_is_presence(self.pic_close).click()

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
                    self.wait_until_element_is_presence(self.pic).click()
                    time.sleep(1)
                    # wait loading
                    self.wait_until_element_is_invisibility(self.loading)
                    img_src = self.wait_until_element_is_visibility(self.img_src).get_attribute('src')

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

                    self.wait_until_element_is_presence(self.pic_close).click()

        results = False if "False" in result_list else True
        return results

    def test_phone_case_color(self):
        old_color_name = None
        old_img_src = None
        old_image = None
        new_color_name = None
        result_list = []

        print("\n======= 測試「手機殼顏色」=======")
        phone_case_text = self.wait_until_element_is_presence(self.phone_case).text
        print(f"---- 當前手機殼產品「{phone_case_text}」-----")
        phone_case_color_ele = self.wait_until_element_is_presence(self.phone_case_color)
        # 取得所有顏色
        color_list = self.wait_until_all_elements_is_presence(self.phone_case_color_list)
        for index, color in enumerate(color_list):
            color_num = index + 1
            try:
                color.click()
            except:
                self.run_script("window.scrollBy(0,450)")
                time.sleep(1)
                color.click()

            if color_num == 1:
                old_color_num = color_num
                old_color_name = phone_case_color_ele.text

                # 點開圖片
                self.wait_until_element_is_presence(self.pic).click()
                time.sleep(1)
                # wait loading
                self.wait_until_element_is_invisibility(self.loading)

                # 擷取當下畫面
                old_canvas_base64 = self.driver.get_screenshot_as_base64()
                old_canvas_png = base64.b64decode(old_canvas_base64)
                old_image = cv2.imdecode(np.frombuffer(old_canvas_png, np.uint8), 1)
                old_img_src = self.wait_until_element_is_visibility(self.img_src).get_attribute('src')
                self.wait_until_element_is_presence(self.pic_close).click()

                continue
            else:
                new_color_name = phone_case_color_ele.text
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
                    self.wait_until_element_is_presence(self.pic).click()
                    time.sleep(1)
                    # wait loading
                    self.wait_until_element_is_invisibility(self.loading)
                    img_src = self.wait_until_element_is_visibility(self.img_src).get_attribute('src')

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

                        self.wait_until_element_is_presence(self.pic_close).click()

        results = False if "False" in result_list else True
        return results