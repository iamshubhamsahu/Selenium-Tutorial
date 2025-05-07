import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # <-- Import this

service = Service(r'C:\Users\Shubham Sahu\Desktop\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.NAME, "enter-name").send_keys("Shubham Sahu")
driver.find_element(By.ID, "confirmbtn").click()

time.sleep(10)

