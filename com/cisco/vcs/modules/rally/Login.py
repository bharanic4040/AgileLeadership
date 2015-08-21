from com.cisco.vcs.po.rally.LoginPage import LoginPage
from com.cisco.vcs.common.PageCommon import *

class Login:

    USER='jmuthusa'
    PASS='Ajju0306'

    def __init__(self):
        self.page=LoginPage()
        self.success = False

    def startLoginProcess(self):
        try:
            self.login()
            self.success = True
        except Exception as e:
            raise e

    def login(self):
        sleepFor(3)
        self.page.getLoginUsernameText(10).send_keys(Login.USER)
        self.page.getLoginPasswordText(2).send_keys(Login.PASS)
        sleepFor(2)
        self.page.getSubmitButton(3).click()
        sleepFor(2)
        clickAlert()
        sleepFor(3)
        #self.page.getLoginUsernameText(10).send_keys(Login.USER)
        #self.page.getLoginPasswordText(2).send_keys(Login.PASS)
        #sleepFor(3)
        #self.page.getSubmitButton(3).click()









