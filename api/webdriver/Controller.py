from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


 
class Driver(object):
    def __init__(self, driver_path, profile_path, headless = False):
      
        option = Options()
        option.headless = headless #Seta se o navegador irá exibir interface gráfica ou não
        profile = webdriver.FirefoxProfile(profile_path)#Carrega o perfil, e com ele os cookies resistentes
        self.browser = webdriver.Firefox(options = option, executable_path = driver_path, firefox_profile = profile)
        


    def get(self, url):
        self.browser.get(url)

    def click(self, name):
        try:
            wait = WebDriverWait(self.browser, 20)
            element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, name)))
            element.click()
        except NoSuchElementException:
            raise Exception ("Elemento  não encontrado.")


    def quit(self):
        self.browser.quit()