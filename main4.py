import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":879,"height":699})
    page = context.new_page()
    page.locator("body").click(button="right")
    page.goto("https://www.atlantis.com/")
    page.get_by_role("button", name="Accept All Cookies").click()
    page.get_by_role("button").nth(2).click()
    page.get_by_role("tab", name="Atlantis Dubai").click()
    page.get_by_role("link", name="Atlantis The Palm From").click()
    page.get_by_role("button", name="Select Dates").click()
    time.sleep(10)
    page.locator("div:nth-child(3) > .dateRangePicker__global-styles_scss__wrapper > .dateRangePicker__global-styles_scss__change-button").first.click()
    print(1)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
