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

    def switch_to_window(self, url):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            self.driver.switch_to.window(window_handle)
            if url in self.driver.current_url:
                return
        self.driver.switch_to.window(original_window)


    def open_to_site(self):
        return self.driver.get(self.base_url)