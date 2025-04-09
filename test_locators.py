import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
 with sync_playwright()as playwright:
     yield playwright
     playwright.stop()
@pytest.fixture(scope="session")
def browser(playwright):
    browser= playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
@pytest.fixture(scope="module")
def page(browser):
    page=browser.new_page()
    yield page
    page.close()


def test_goto_url(page):
    page.goto("https://playwright.dev/")
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="Get started").is_visible()
    page.get_by_role("link", name="Get started").is_enabled()
    page.get_by_role("link", name="Get started").hover()
    page.get_by_role("link", name="Get started").focus()
    page.get_by_role("link", name="Get started").click(button="left")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 10000)
    page.wait_for_timeout(1000)


    install =page.get_by_role("heading", name="Installation").focus()
    page.wait_for_timeout(1000)









