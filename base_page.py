# _*_ coding: UTF-8 _*_
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_is_presence(self, xpath, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath)),
            message=f'{xpath} 等待逾期'
        )
        return element

    def wait_until_all_elements_is_presence(self, xpath, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath)),
            message=f'{xpath} 等待逾期'
        )
        return element

    def wait_until_element_is_visibility(self, xpath, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath)),
            message=f'{xpath} 等待逾期'
        )
        return element

    def wait_until_any_elements_is_visibility(self, xpath, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_any_elements_located((By.XPATH, xpath)),
            message=f'{xpath} 等待逾期'
        )
        return element

    def wait_until_all_elements_is_visibility(self, xpath, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located((By.XPATH, xpath)),
            message=f'{xpath} 等待逾期'
        )
        return element

    def wait_until_element_is_invisibility(self, xpath, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((By.XPATH, xpath)),
            message=f'{xpath} 等待逾期'
        )
        return element

    def wait_until_element_is_clickable(self, xpath, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath)),
            message=f'{xpath} 等待逾期'
        )
        return element

    def clear_text(self, xpath):
        element = self.wait_until_element_is_clickable(xpath)
        clean = False
        while not clean:
            value = element.get_attribute('value')
            if value == '':
                clean = True
            else:
                element.send_keys(Keys.BACK_SPACE)

    def switch_to_tab(self, index):
        tab = self.driver.window_handles
        self.driver.switch_to.window(tab[index])

    def run_script(self, script, *args):
        self.driver.execute_script(script, *args)
