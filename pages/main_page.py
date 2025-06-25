from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get("https://saby.ru/")

    def click_contacts(self):
        contacts = self.driver.find_element(By.CLASS_NAME, "sbisru-Header-ContactsMenu")
        contacts.click()

    def click_more_contacts(self):
        link = self.driver.find_element(By.CSS_SELECTOR, "div.sbisru-Header-ContactsMenu__items a.sbisru-link")
        link.click()

    def click_downloads(self):
        downloads = self.driver.find_element(By.LINK_TEXT, "Скачать локальные версии")
        downloads.click()