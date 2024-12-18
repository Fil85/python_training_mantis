from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHepler
from fixture.mail import MailHepler
from fixture.soap import SoapHepler


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecogniced browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHepler(self)
        self.mail = MailHepler(self)
        self.soap = SoapHepler(self)
        self.config = config
        self.base_url = config["web"]["baseUrl"]
        self.project = ProjectHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
