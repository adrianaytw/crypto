from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict({
  "platformName": "iOS",
  "appium:bundleId": "com.apple.Preferences",
  "appium:automationName": "XCUITest",
  "appium:udid": "00008140-001A55DA3C53001C",
  "appium:xcodeOrgId": "adrianay2499@gmail.com"
})

appium_server_url = 'http://localhost:4723'

openlist = EC.presence_of_element_located((By.ACCESSIBILITY_ID, "目錄, 左邊彈出選單"))
forecast = EC.presence_of_element_located((By.ACCESSIBILITY_ID, "九天預報"))
openlist.click()
forecast.click()

day1data = appium_server_url.find_element(By.ID, "F5020000-0000-0000-A309-000000000000")

def checkdata():
    if day1data == "3月19日 (三)":
      print("Correct")

    else:
      print("incorrect")

checkdata
    
    


