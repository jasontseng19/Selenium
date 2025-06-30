# _*_ coding: UTF-8 _*_
from base_page import BasePage
import time
from selenium.webdriver.common.by import By


class ShoppingCarPage(BasePage):
    """ 購物車頁面 """

    # locate
    title = "//div[./h1]/following-sibling::a"
    product_type = "//p[text()='產品類型']/following-sibling::p"
    phone_price = "//div[contains(@class, 'items-center') and contains(@class, 'py-3')]//div[./p]"
    add_to_shopping_car_button = "//button/span[text()='加入購物車']"
    alert = "//p[text()='成功加入購物車！']"
    add_on = "//div[@data-title='手機保護貼']"
    car_icon = "//li[@title='購物車']"
    look_car = "//button/span[text()='查看購物車']"
    loading = "//div[@class='loading__mask loading__mask__show']"
    check_msg = "//div[@id='cart']//div[@class='expanded-message']"
    td = "//div[@id='CartProducts']//div[contains(@class, 'td')]"
    add_button = "//span[text()='+']"
    price_td = "//div[@class='td price']"
    sum_td = "//div[@class='td sumprice not-mobile']"
    price_ele = "//p[text()='{i}']/following-sibling::p"
    car_qty = "//div[@class='td qty']//input"
    remove = "//div[@class='td remove']"

    def test_add_to_shopping_car(self):
        result_list = []
        print("\n======= 測試「加入購物車」=======")
        # 取商品資訊
        product_title = self.wait_until_element_is_visibility(self.title).text
        # 產品類型
        product_type = self.wait_until_element_is_visibility(self.product_type).text
        # 價錢
        phone_price_text = self.wait_until_element_is_presence(self.phone_price).text
        phone_price_list = phone_price_text.split("\n")
        self.wait_until_element_is_clickable(self.add_to_shopping_car_button).click()
        # 判斷是否加入成功
        alert_msg = self.wait_until_element_is_visibility(self.alert)
        if not alert_msg:
            print("Fail: 「加入購物車」無顯示提示訊息")
            result_list.append("False")

        # 加購頁面
        self.wait_until_element_is_visibility(self.add_on)
        time.sleep(1)

        # 驗證數量
        car = self.wait_until_element_is_visibility(self.car_icon)
        car_num = car.find_element(By.XPATH, "./a//span").text
        if "1" not in car_num:
            print(f"Fail: 「購物車-數量」顯示錯誤: {car_num}")
            result_list.append("False")

        results = False if "False" in result_list else True
        return results

    def test_check_shopping_car_page(self):
        result_list = []
        self.wait_until_element_is_clickable(self.look_car).click()
        time.sleep(1)
        # wait loading
        self.wait_until_element_is_invisibility(self.loading)
        time.sleep(1)
        # 判斷購物車是否有商品
        try:
            ele = self.wait_until_element_is_visibility(self.check_msg).text
            if "空的" in ele:
                print(f"Fail: {ele}")
                result_list.append("False")
            else:
                print(f"Fail: 「購物車頁面」顯示錯誤訊息: {ele}")
                result_list.append("False")
        except:
            print("\n======= 測試「檢查購物車資訊」=======")
            try:
                product_td = self.wait_until_all_elements_is_visibility(self.td)
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

                # 暫時註解
                # check1 = len([i for i in [sub_title, color_name, '1'] if i not in car_product])
                # check2 = len([i for i in [product_style, product_type] if i not in car_product[1]])
                # check3 = len([i for i in phone_price_list if i not in car_product])
                # if (check1 or check2 or check3) != 0:
                #     print(f"Fail:「購物車頁面-商品」顯示錯誤")
                #     print(f"「購物車頁面-商品」: {car_product}")
                #     print(f"「商品頁-樣式」:{product_style}")
                #     print(f"「商品頁-類型」:{product_type}")
                #     print(f"「商品頁-副標題」:{sub_title}")
                #     print(f"「商品頁-價錢」:{phone_price_list}")
                #     print(f"「商品頁-顏色」:{color_name}")
                #     result_list.append("False")
            except:
                print("Fail: 檢查「購物車頁面-商品」時失敗")
                result_list.append("False")

            print("\n======= 測試「金額」=======")
            # 測試金額
            try:
                # 商品數+1
                self.wait_until_element_is_clickable(self.add_button).click()
                time.sleep(1)
                # wait loading
                self.wait_until_element_is_invisibility(self.loading)
                price_dict = {
                    "金額": "",
                    "數量": "",
                    "合計": "",
                    "商品金額": "",
                    "運費小計": "",
                    "應付金額": "",
                }

                for i in price_dict:
                    if i == '金額':
                        ele = self.wait_until_element_is_visibility(self.price_td)
                        price_dict['金額'] = "".join(filter(lambda x: x in '0123456789', ele.text))
                    elif i == '數量':
                        price_dict['數量'] = self.wait_until_element_is_visibility(self.car_qty).get_attribute("value")
                    elif i == '合計':
                        ele = self.wait_until_element_is_visibility(self.sum_td)
                        price_dict['合計'] = "".join(filter(lambda x: x in '0123456789', ele.text))
                    else:
                        _xpath = self.price_ele.replace('{i}', i)
                        ele = self.wait_until_element_is_visibility(_xpath)
                        price_dict[i] = "".join(filter(lambda x: x in '0123456789', ele.text))


                # 驗證金額
                if int(price_dict['金額']) * int(price_dict['數量']) != int(price_dict['合計']):
                    print("Fail:「金額 x 數量」與「合計金額」不同")
                    print(f"「金額」: {price_dict['金額']}")
                    print(f"「數量」: {price_dict['數量']}")
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

            print("\n======= 測試「清空購物車」=======")
            # 清空購物車
            try:
                self.wait_until_element_is_clickable(self.remove).click()
                time.sleep(1)
                # wait loading
                self.wait_until_element_is_invisibility(self.loading)
                ele = self.wait_until_element_is_visibility(self.check_msg)
                if "按這裡開始購物吧" not in ele.text:
                    print(f"Fail:「清空後購物車」顯示訊息異常: {ele.text}")
                    result_list.append("False")
            except:
                print("Fail: 測試「清空購物車」時失敗")
                result_list.append("False")

        results = False if "False" in result_list else True
        return results