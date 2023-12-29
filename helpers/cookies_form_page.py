from playwright.sync_api import expect
from pom.cookies_form_elements import CookiesForm


class CookiesFormPage:
    def __init__(self, page):
        self.cookies_page = CookiesForm(page)

    def click_on_personalize(self):
        self.cookies_page.personalize_cookies.click()

    def click_on_accept(self):
        self.cookies_page.accept_cookies.click()

    def click_on_continue_without_accepting(self):
        self.cookies_page.continue_without_accepting.click()

    def verify_cookies_title_page(self):
        expect(self.cookies_page.privacy_title).to_contain_text(self.cookies_page.title, timeout=15000)

