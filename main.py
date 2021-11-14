from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


profile_path = r'C:\Users\Wop1x\AppData\Roaming\Mozilla\Firefox\Profiles\nahd6ha2.default'

options=Options()
options.set_preference('profile', profile_path)
service = Service(r'C:\Users\Wop1x\Downloads\geckodriver\geckodriver.exe')
browser = Firefox(service=service, options=options)

url = 'https://www.youtube.com/watch?v=xNCld4arGec'

browser.get(url)

like = r'#top-level-buttons-computed > ytd-toggle-button-renderer:nth-child(1)'

browser.find_element(By.CSS_SELECTOR, like).click()



