import pytest
from playwright.sync_api import sync_playwright
with sync_playwright()as playwright:

    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
    page.wait_for_timeout(1000)
    label_h1=page.locator("text='Automation Demo Site '").text_content()
    print(label_h1)
    page.pause()
    submit_button=page.locator("text='Submit'").click()
    page.wait_for_timeout(1000)
    refresh_button=page.locator("form button",has_text="Refresh")
    page.wait_for_timeout(1000)
    page.get_by_label("")





