import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Путь к ChromeDriver (если нужно указать вручную)


# Настройки браузера
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Открыть браузер в полном экране

# Инициализация браузера
with webdriver.Chrome(options=chrome_options) as driver:
    driver.set_window_size(877, 669)
    actions = ActionChains(driver)
    # Переход на сайт
    driver.get("https://www.atlantis.com/atlantis-the-palm")
    time.sleep(1)

    # Клик по кнопке "Accept All Cookies"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept All Cookies']"))
    ).click()
    time.sleep(2)
    elem = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[2]/div[4]/div/div/form/div["
                                              "1]/div/div/button")
    actions.move_to_element(elem).click().perform()
    time.sleep(3)
    elem_button_next_month = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[4]/div/div/form/div['
                                                           '2]/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/div/div[3]')
    actions.move_to_element(elem_button_next_month).click().perform()
    time.sleep(3)
    # Клик по кнопке конкретного месяца
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div[1]/div[2]/div[4]/div/div/form/div[2]/div/div["
                                              "1]/div[1]/div/div[3]/div[1]/div[1]/div/div[3]/span/span"))
    ).click()
    time.sleep(1)

    # Клик по дате "14"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[@role='gridcell' and text()='14']"))
    ).click()
    time.sleep(1)

    # Клик по дате "15"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[@role='gridcell' and text()='15']"))
    ).click()
    time.sleep(1)

    # Клик по кнопке "Check Availability"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Check Availability']"))
    ).click()
    time.sleep(5)
