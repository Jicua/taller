from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys

# inicializacion
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

input("Escanee el código QR y presione Enter")

wait = WebDriverWait(driver, 10)

def send_msg(target, text):
        x_arg = '//span[contains(@title,' + target + ')]'
        time.sleep(1)
        group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
        time.sleep(1)
        group_title.click()
        message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        message.send_keys(mensaje)
        sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()

while True:
        mensaje = input("Ingrese el mensaje\n")
        target = input("Ingrese el destinatario\n")
        target = "'" + target + "'"
        send_msg(target, mensaje)

#driver.close()
