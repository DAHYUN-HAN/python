from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_image():
    
    URL = "https://blog.naver.com/gksekgus1268/222579385102"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("headless")
        
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.get(url=URL)
    
    try :
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept() # 확인 버튼 클릭
        # alert.dismiss() # 취소 버튼 클릭
        print("alert")
    except :
        print("no alert")
    
    # driver.close()

get_image()