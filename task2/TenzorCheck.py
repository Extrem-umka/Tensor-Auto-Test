import time
from task2.Baseapp import BasePage
from selenium.webdriver.common.by import By
import requests

class TenzorLocators:
    LOCATOR_TENZOR_CONTACTS_BUTTON = (By.XPATH, "//a[@class='sbisru-Header__menu-link sbisru-Header__menu-link--hover']"
                                                "[contains(text(),'Контакты')]")
    LOCATOR_TENZOR_CHECK_REGION = (By.CSS_SELECTOR, "span[class='sbis_ru-Region-Chooser ml-16 ml-xm-0'] "
                                                    "span[class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    LOCATOR_TENZOR_CHECK_PARTNERS = (By.XPATH, "(//div[@class='controls-BaseControl "
                                               "controls_list_theme-sbisru controls_toggle_theme-sbisru'])[1]")
    LOCATOR_TENZOR_FIND_REGION = (By.XPATH, "//span[contains(@title,'Камчатский край')]")
    LOCATOR_TENZOR_CHECK_PARTNERS_UPDATE =  (By.CSS_SELECTOR, "#city-id-2")

class SearchHelper(BasePage):

    def click_banner(self):
        search_button = self.find_element(TenzorLocators.LOCATOR_TENZOR_CONTACTS_BUTTON)
        search_button.click()

    def check_region(self, region, city):
        check_region  = self.find_element(TenzorLocators.LOCATOR_TENZOR_CHECK_REGION)
        assert check_region.text == region
        check_partners = self.find_elements(TenzorLocators.LOCATOR_TENZOR_CHECK_PARTNERS)
        partners = []
        for partner in check_partners:
            if len(partner.text) > 0:
                partners.append(partner.text)
                assert len(partners) > 0
        check_city = self.find_element(TenzorLocators.LOCATOR_TENZOR_CHECK_PARTNERS_UPDATE)
        assert check_city.text == city

    def change_region(self):
        search_button = self.find_element(TenzorLocators.LOCATOR_TENZOR_CHECK_REGION)
        search_button.click()
        find_region = self.find_element(TenzorLocators.LOCATOR_TENZOR_FIND_REGION)
        find_region.click()
        time.sleep(10)

    def check_region_url_title(self, region, city, kod_region):
        check_region = self.find_element(TenzorLocators.LOCATOR_TENZOR_CHECK_REGION)
        assert check_region.text == region
        check_partners = self.find_elements(TenzorLocators.LOCATOR_TENZOR_CHECK_PARTNERS)
        partners = []
        for partner in check_partners:
            if len(partner.text) > 0:
                partners.append(partner.text)
                assert len(partners) > 0
        check_city = self.find_element(TenzorLocators.LOCATOR_TENZOR_CHECK_PARTNERS_UPDATE)
        assert check_city.text == city
        title = self.driver.title
        assert region in title
        current_url = self.driver.current_url
        assert kod_region in current_url


















