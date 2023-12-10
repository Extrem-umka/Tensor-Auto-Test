from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Не могу найти элемент{locator}")

    def find_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Не могу найти элементы{locator}")

    def find_iframe(self, locator, time=30):
        return WebDriverWait(self.driver, time). until(EC.frame_to_be_available_and_switch_to_it(locator),
                                                       message=f"Не могу найти элементы{locator}")

    def open_to_site(self):
        return self.driver.get(self.base_url)