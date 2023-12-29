import string
import time

from pom.login_elements import LoginForm


class LoginFormPage:

    def __init__(self, page):
        self.login_page = LoginForm(page)

    def login(self, email: string, password: string):
        self.login_page.user_email.type(email)
        self.login_page.login_next_button.click()
        self.login_page.user_password.fill(password)
        self.login_page.login_button.click()
