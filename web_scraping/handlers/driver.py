from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def accept_cookies(driver):
    try:
        agree_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, './/button[text()="AGREE"]')))
    except BaseException as e:
        agree_button = None

    if agree_button:
        agree_button.click()
