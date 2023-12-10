from task1.TenzorPages import SearchHelper

def test_tenzor_search(browser):
    tenzor_main_page = SearchHelper(browser)
    tenzor_main_page.open_to_site()
    tenzor_main_page.click_banner()
    tenzor_main_page.click_tenzor()
    tenzor_main_page.switch_to_windows(url="https://tensor.ru/")
    tenzor_main_page.power_in_people()
    tenzor_main_page.power_in_people_description()
    tenzor_main_page.work()





