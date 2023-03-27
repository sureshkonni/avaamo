from selenium import webdriver


class LoginPage:

    popupMessage="//strong[contains(text(),'This is how the chat agent shows up')]"
    welcomePage="//small[contains(text(),'Welcome to Pizza Shoppe')]"
    getStartedButton="//button[contains(text(),'Get Started')]"
    chatAgentButton="//body/div[@id='avm_chat_widget_c767654d-6709-43f6-bb0c-ce1d2c559f6a']/div[3]/a[1]/img[1]"


    def __init__(self, driver):
        self.driver = driver

    def pizzaImageButton(self):
        #self.driver.(self.welcomePage).click()
        self.driver.find_element_by_xpath(self.chatAgentButton).click()

