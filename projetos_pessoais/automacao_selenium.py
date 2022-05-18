from selenium import webdriver

navegador = webdriver.Chrome()
url_base = 'https://www.youtube.com/c/prantoniojunior/videos'
navegador.get(url_base)
navegador.find_element_by_xpath('//*[@id="video-title"]').click()
url_atual = navegador.current_url
navegador.execute_script('''window.open("https://web.whatsapp.com/","_blank");''')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')


# from selenium import webdriver
# import pywhatkit as kit



