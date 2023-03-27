from uiautomator import Device
import time

d = Device("KJRKLNDAYLEYVO8T")
class uiLibrary():

    def _init_(self):

        pass

    def screenOnUi(self):
        d.screen.on()
        time.sleep(2)

    def launchApp(self, appName):
        d(text=appName).click()
        time.sleep(2)

    def userName(self):
        d.click(800, 500)

    def passwordUi(self):
        d.click(800, 750)

    def loginButtonUi(self):
        d.click(500, 900)

    def rememberButtonUi(self):
        d.click(500, 1250)

    def pressBack(self):
        for i in range(7):
            time.sleep(2)
            d.press.back()

###########################################

    def TurnOnScreen(self):
        "turn on screen"
        d.screen.on()

    def profileUi(self):
        d.click(900, 1800)

    def menuUi(self):
        d.click(1000, 100)

    def settingsUi(self):
        d.click(1000, 950)

    def languageUI(self):
        d.click(1000, 600)

    def lagSearchUI(self,search):
        d(text=search).click()
        d.clickable = ("true")

    def language2UI(self):
        d.click(1000, 600)

    def LagSearchUI(self,findelement):
        d(text=findelement).click()

    def clickLangUi(self):
        d.click(900, 350)
        time.sleep(5)

    def langsearchUI3(self, findelement2):
        d(text=findelement2).click()
        d.clickable = ("true")

    def scrollUI(self):
        for i in range(5):
            d(scrollable=True).scroll.forward(steps=10)