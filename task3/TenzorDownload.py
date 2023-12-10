import time
from task3.BaseApp import BasePage
from selenium.webdriver.common.by import By
import requests
import os
import re

class TenzorLocators:
    LOCATOR_TENZOR_DOWNLOAD_BUTTON = (By.XPATH, "//a[contains(text(),'Скачать СБИС')]")
    LOCATOR_TENZOR_SBIS_PLAGIN_BUTTON = (By.XPATH, "(//div[@class='controls-tabButton__overlay'])[2]")
    LOCATOR_TENZOR_DOWNLOAD_FILE = (By.XPATH, "(//a[contains(text(),'Скачать (Exe 6.94 МБ)')])[1]")


class SearchHelper(BasePage):

    def click_download_sbis(self):
        search_button = self.find_element(TenzorLocators.LOCATOR_TENZOR_DOWNLOAD_BUTTON)
        self.driver.execute_script("arguments[0].click();", search_button)

    def download_file(self):
        search_button1 = self.find_element(TenzorLocators.LOCATOR_TENZOR_SBIS_PLAGIN_BUTTON)
        search_button1.click()
        search_link = self.find_element(TenzorLocators.LOCATOR_TENZOR_DOWNLOAD_FILE)
        file_url = search_link.get_attribute("href")
        response = requests.get(file_url)
        file_name = "Веб установщик Windows.exe"
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, "wb") as file:
            file.write(response.content)
            assert os.path.exists(file_path)

    def compare_file_size(self):
        link_text = self.find_element(TenzorLocators.LOCATOR_TENZOR_DOWNLOAD_FILE)
        pattern = r"(\d+\.\d+)"
        match = re.search(pattern, link_text.text)
        if match:
            number = float(match.group(1))
            file_name = "Веб установщик Windows.exe"
            file_path = os.path.join(os.getcwd(), file_name)
            file_size_b = os.path.getsize(file_path)
            file_size_mb = round(file_size_b / (1024 * 1024), 2)
            assert number == file_size_mb










