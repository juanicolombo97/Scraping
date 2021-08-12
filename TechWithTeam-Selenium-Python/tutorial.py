from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = '/usr/local/bin/chromedriver'

# CARGAMOS EL DRIVER
driver = webdriver.Chrome(PATH)

# Abrimos una pagina
driver.get('https://techwithtim.net')

# Buscamos 

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
finally:
    articles = element.find_elements_by_tag_name("article") 
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)



#Cerramos pagina
time.sleep(5)
driver.close()
