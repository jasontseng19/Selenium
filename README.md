# 網頁自動化測試

## 介紹

- 模擬使用者操作進行註冊、搜尋以及加入購物車的行為來進行驗證測項。

## 功能

- 註冊頁面：
  - 測試輸入正確與錯誤的顯示訊息。
- 搜尋頁面：
  - 測試無銷售商品、銷售商品。
  - 針對銷售商品進行資料確認、顏色切換等等是否正常。
- 購物車：
  - 測試加入購物車後顯示資訊是否正確。
  - 清空購物車是否正常。

## 先決條件

- Python 3.9.13 版本。

## 執行

1. 安裝所需的依賴：
    ```bash
    pip3 install -r requirements.txt
    ```

2. 執行測試
   使用以下命令運行網頁自動化測試：
    ```bash
    python3 main.py  # 執行自動化測試
    ```

## 相關測試畫面

> 註冊
<img src='https://github.com/jasontseng19/Selenium/blob/master/test_register.gif' width='560'>

> 搜尋
<img src='https://github.com/jasontseng19/Selenium/blob/master/test_search.gif' width='560'>

> 產出Report
<img src='https://github.com/jasontseng19/Selenium/blob/master/Report.png' width='560'>
