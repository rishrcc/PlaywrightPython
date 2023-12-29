class LoginForm:
    def __init__(self, page):
        self.page = page
        self.user_email = page.get_by_role("textbox")
        self.login_next_button = page.get_by_role("button", name="Suivant")
        self.user_password = page.locator("input[name=\"password\"]")
        self.login_button = page.get_by_role("button", name="Se connecter")