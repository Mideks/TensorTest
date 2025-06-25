from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


class TensorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def has_people_block(self) -> bool:
        try:
            self.driver.find_element(By.XPATH, "//*[contains(text(), 'Сила в людях')]")
            return True
        except NoSuchElementException:
            return False

    def click_more_button(self):
        button = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Сила в людях')]/..//a")
        button.click()

    def all_work_images_same_size(self) -> bool:
        images = self.driver.find_elements(By.CLASS_NAME, "tensor_ru-About__block3-image")
        sizes = {(img.get_property("width"), img.get_property("height")) for img in images}
        return len(sizes) == 1
