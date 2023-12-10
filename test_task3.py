from task3.TenzorDownload import SearchHelper

def test_tenzor_download_sbis(browser):
    tenzor_download = SearchHelper(browser)
    tenzor_download.open_to_site()
    tenzor_download.click_download_sbis()
    tenzor_download.download_file()
    tenzor_download.compare_file_size()


