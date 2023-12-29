import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from helpers.cookies_form_page import CookiesFormPage
from helpers.login_form_page import LoginFormPage

def tests_login(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://login.oney.fr/login")

    cookies_page = CookiesFormPage(page)
    login_page = LoginFormPage(page)

    cookies_page.verify_cookies_title_page()
    cookies_page.click_on_continue_without_accepting()
    login_page.login('mk1@yopmail.com', 'Passw0rd')

    context.close()
    browser.close()
