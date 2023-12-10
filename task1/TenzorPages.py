import time
from task1.BaseApp import BasePage
from selenium.webdriver.common.by import By



class TenzorLocators:
    LOCATOR_TENZOR_CONTACTS_BUTTON = (By.XPATH, "//a[@class='sbisru-Header__menu-link sbisru-Header__menu-link--hover']"
                                                "[contains(text(),'Контакты')]")
    LOCATOR_TENZOR_BANNERTENZOR_BUTTON =(By.XPATH, "(//img[@alt='Разработчик системы СБИС — компания «Тензор»'])[1]")
    LOCATOR_TENZOR_POWERPEOPLE_FIND = (By.XPATH, "(//p[contains(text(),'Сила в людях')])[1]")
    LOCATOR_TENZOR_POWERPEOPLE_ABOUT_BUTTON = (By.XPATH, "(//a[@href='/about'][contains(text(),'Подробнее')])[1]")
    LOCATOR_TENZOR_WORK_IMAGE = (By.XPATH, "//div[@class='tensor_ru-About__block3-image-wrapper']//img")

class SearchHelper(BasePage):

    def click_banner(self):
        search_button = self.find_element(TenzorLocators.LOCATOR_TENZOR_CONTACTS_BUTTON)
        search_button.click()

    def click_tenzor(self):
        search_button = self.find_element(TenzorLocators.LOCATOR_TENZOR_BANNERTENZOR_BUTTON)
        search_button.click()


    def switch_to_windows(self, url):
        self.switch_to_window(url)


    def power_in_people(self):
        search_words = self.find_element(TenzorLocators.LOCATOR_TENZOR_POWERPEOPLE_FIND)

    def power_in_people_description(self):
        search_button = self.find_element(TenzorLocators.LOCATOR_TENZOR_POWERPEOPLE_ABOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", search_button)


    def work(self):
        photos = self.find_elements(TenzorLocators.LOCATOR_TENZOR_WORK_IMAGE)
        if len(photos) > 0:
            first_photo = photos[0]
            first_photo_height = first_photo.get_attribute("height")
            first_photo_width = first_photo.get_attribute("width")
        for photo in photos:
            photo_height = photo.get_attribute("height")
            photo_width = photo.get_attribute("width")
            assert photo_height == first_photo_height and photo_width == first_photo_width

