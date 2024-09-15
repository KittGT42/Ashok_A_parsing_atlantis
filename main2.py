import re
import time
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context(
    #     viewport={"width": 877, "height": 669}  # Установка размеров экрана
    # )
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.atlantis.com/")
    time.sleep(1)
    page.get_by_role("button", name="Accept All Cookies").click()
    time.sleep(1)
    page.get_by_role("tab", name="Atlantis Dubai").get_by_role("link").click()
    time.sleep(1)
    page.locator("div").filter(has_text=re.compile(r"^Dubai$")).nth(2).click()
    time.sleep(1)
    page.locator("#react-select-2-option-1").click()
    time.sleep(1)
    page.get_by_role("button", name="Select Dates").click()
    time.sleep(1)
    page.get_by_role("cell", name="15").first.click()
    time.sleep(1)
    page.get_by_role("cell", name="16").first.click()
    time.sleep(1)
    page.get_by_role("button", name="Check Availability").click()
    time.sleep(5)
    result_page = BeautifulSoup(page.content(), 'lxml')
    number_of_results = result_page.find('p', {'class': 'category-title--small inherit'})
    all_rooms = result_page.find('div', {'class': 'rooms-list rooms'}).find_all('div', {'class': 'DLw'})
    print(number_of_results)
    time.sleep(5)
    page.get_by_label("Modify booking").click()
    page.get_by_role("heading", name="Check-in date").click()
    page.get_by_role("cell", name="15").first.click()
    page.get_by_role("cell", name="17").first.click()
    page.get_by_role("button", name="Apply").first.click()
    time.sleep(10)
    result_page = BeautifulSoup(page.content(), 'lxml')
    number_of_results = result_page.find('p', {'class': 'category-title--small inherit'})
    all_rooms = result_page.find('div', {'class': 'rooms-list rooms'}).find_all('div', {'class': 'DLw'})
    page.get_by_label("Modify booking").click()
    page.get_by_role("heading", name="Check-in date").click()
    page.locator("div:nth-child(2) > .DKa1 > div:nth-child(3) > .DKas > .change-button-view").click()
    page.get_by_role("cell", name="1", exact=True).first
    time.sleep(4)
    page.get_by_role("cell", name="2", exact=True).first
    print(number_of_results)

    # print(result_page)


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

