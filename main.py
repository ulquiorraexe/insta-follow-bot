from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

following_account = "travellifes_"
username = "minniepuf"
password = "yasemin1"

class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)
        mail_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        mail_input.send_keys(username, Keys.TAB)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password, Keys.ENTER)
        sleep(3)
        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            cookie_warning[0].click()
            sleep(1)
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Şimdi değil')]")
        if save_login_prompt:
            save_login_prompt.click()
        sleep(3)
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Şimdi Değil')]")
        if notifications_prompt:
            notifications_prompt.click()
            sleep(3)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/ogretmensitemiz/following/")
        sleep(3)
        # modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        # modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)

        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)

        # Pop-up içeriğinin yüklenmesini bekleyin
        for i in range(10):
            # Ana pencereyi hedefleyin ve aşağıya scroll yapın
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)
    def follow(self):
        all_buttons = self.driver.find_elements(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[2]/div/div/div/div[3]/div/button')

        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot = InstaFollower()

bot.login()
bot.find_followers()
bot.follow()