from features.pageobjects.Base import BaseSettingsPage
import time

class SendmailPage(BaseSettingsPage):

    def __init__(self,driver):
        super().__init__(driver)

    def clickWriteMail(self):
        self.DynamicImplicitWait(40)
        self.ClickLinks("writeMail_XPATH")
        time.sleep(5)

    def setTo(self, to):
        self.DynamicImplicitWait(40)
        self.TypeEditBoxEmail("toField_XPATH", to)
        time.sleep(5)

    def setSubjectArea(self, subject):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("subject_XPATH",subject)
        time.sleep(5)

    def setComposeArea(self,compose):
        self.DynamicImplicitWait(40)
        self.SwitchFrameAddress("frameCompose_CSSSELECTOR")
        self.TypeEditBox("composeArea_XPATH",compose)
        time.sleep(5)

    def clickSendMail(self):
        self.DynamicImplicitWait(40)
        self.SwitchOutFrameAddress()
        self.ClickButton("send_XPATH")
        time.sleep(7)


    def clickLogout(self):
        self.DynamicImplicitWait(40)
        self.ClickLinks("logout_XPATH")
        time.sleep(7)

    def validlogout(self, expectedTextVal):
        self.DynamicImplicitWait(40)
        self.AssertText("logoutText_XPATH", expectedTextVal)
        time.sleep(7)