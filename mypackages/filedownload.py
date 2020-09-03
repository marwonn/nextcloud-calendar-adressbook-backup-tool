def start_backup():
    import os
    import progressbar

    from selenium import webdriver
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.firefox.options import Options

    from mypackages.config import Config

    cwd = os.getcwd()

# Firefox and Driver settings
    options = Options()
    options.headless = True
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", cwd)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/calendar, text/x-vcard, text/vcard, text/directory")
    driver = webdriver.Firefox(options=options, firefox_profile=profile)
    print("Headless Firefox started. Load data from website...please wait...")
    driver.get(Config.nextcloud_url)
    driver.find_element_by_id("user").send_keys(Config.username)
    driver.find_element_by_id("password").send_keys(Config.password)
    driver.find_element_by_id("submit-wrapper").click()


# Creates list of the different calendars and add the adressbook
    url = Config.nextcloud_url + "remote.php/dav/"

    url_list = []

    for i in Config.name_of_calendars:
        url_list.append(url + "calendars/" + Config.username + "/" + i + "?export")

    url_list.append(url + "addressbooks/users/" + Config.username + "/contacts/?export")


# Download section wrapped in a progressbar
    for i in progressbar.progressbar(url_list):
        try:
            driver.set_page_load_timeout(5)
            driver.get(i)
        except TimeoutException:
            pass

    driver.close()


if __name__ == "__main__":
    start_backup()
else:
    print("module 'Filedownload' is imported")
