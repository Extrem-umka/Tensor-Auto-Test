from task2.TenzorCheck import SearchHelper

def test_tenzor_check(browser):
    tenzor = SearchHelper(browser)
    tenzor.open_to_site()
    tenzor.click_banner()
    tenzor.check_region(region="Омская обл.", city="Омск")
    tenzor.change_region()
    tenzor.check_region_url_title(region="Камчатский край", city="Петропавловск-Камчатский", kod_region="41")
