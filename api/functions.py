import os
import time

from .webdriver.Controller import Driver
from .webdriver.Info import *


dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("\\", "\\\\")
print(info["driver_path"])
print(dir_path)

def login():
    driver = Driver(dir_path+info["driver_path"], dir_path+info["profile_path"])
    driver.get(info["primary_url"])

def sendMessage( mensagem, contatos):
        driver = Driver(dir_path+info["driver_path"], dir_path+info["profile_path"], True)
        msg = mensagem.replace(" ", "+")
        for contato in contatos:
            try:
                send = info["send_url"].format(contato, msg)
                driver.get(send)
                driver.click(info["send_button_class_name"])                   
                time.sleep(1);
                print("Mensagem enviada com sucesso para  {}".format(contato))
            except:
                print("Falha em enviar mensagem para {}".format(contato))

        driver.quit()

# Whatsapp.login()

