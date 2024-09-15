import time
from datetime import datetime, timedelta
from urllib.parse import quote
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from dateutil.relativedelta import relativedelta

input_date = datetime(2024, 9, 14, 12, 0, 0)


def get_input_data(start_data, end_data):
    date_check_in = start_data
    date_check_out = end_data
    print(date_check_in)
    url_main = f'https://www.atlantis.com/dubai/reservations/resort-list?checkIn={date_check_in}&checkOut={date_check_out}&destination=Dubai&roomsCount=1&refererItemId=%7bFEE442E0-2348-4079-98D9-0C467BAE273A%7d&room0childrenCount=0&room0adultsCount=2'
    print(url_main)

    with uc.Chrome() as browser:
        browser.get(url_main)
        browser.implicitly_wait(10)

        browser.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(2)

        all_results_hotels = browser.find_elements(By.CLASS_NAME, 'EOy')
        counter_of_results = len(all_results_hotels)
        actions = ActionChains(browser)

        for i in range(counter_of_results):
            all_results_hotels_control = browser.find_elements(By.CLASS_NAME, 'EOy')
            find_button = all_results_hotels_control[i].find_element(By.CLASS_NAME, 'ESg').find_element(By.TAG_NAME,
                                                                                                        'button')
            actions.move_to_element(find_button).click().perform()
            time.sleep(2)
            browser.get(url_main)
            browser.implicitly_wait(10)


def format_date_for_url(date):
    # Проверяем, что время — полночь, и принудительно устанавливаем AM
    if date.hour == 12 and date.minute == 0 and date.second == 0:
        time_str = '12:00:00 AM'
    else:
        time_str = date.strftime('%I:%M:%S %p')

    # Форматируем строку даты без ведущих нулей вручную
    date_str = f"{date.month}/{date.day}/{date.year} {time_str}"

    # URL-кодируем строку даты с использованием quote и приводим к нижнему регистру
    encoded_date = quote(date_str, safe='').lower()

    # Заменяем %20 на '+'
    encoded_date = encoded_date.replace('%20', '+')

    return encoded_date


month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

for _ in range(91):
    max_day = month_days[input_date.month]
    if input_date.day < max_day:
        input_date += timedelta(days=1)
        formatted_date_check_In = format_date_for_url(input_date)
        formatted_date_check_Out = format_date_for_url(input_date + timedelta(days=1))
        get_input_data(formatted_date_check_In, formatted_date_check_Out)
    elif input_date.day == max_day:
        formatted_date_check_In = format_date_for_url(input_date)
        formatted_date_check_Out = (input_date + relativedelta(months=1)).replace(day=1)
        get_input_data(formatted_date_check_In, formatted_date_check_Out)
    else:
        input_date = (input_date + relativedelta(months=1)).replace(day=1)
