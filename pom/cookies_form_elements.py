class CookiesForm:
    def __init__(self, page):
        self.page = page
        self.privacy_title = page.locator('//*[@id="popin_tc_privacy_text"]/p')
        self.title = 'Oney respecte votre vie privée'
        self.continue_without_accepting = page.locator('//*[@id="popin_tc_privacy_button_2"]')
        self.personalize_cookies = page.locator('//*[@id="popin_tc_privacy_button"]')
        self.accept_cookies = page.locator('//*[@id="popin_tc_privacy_button_3"]')

