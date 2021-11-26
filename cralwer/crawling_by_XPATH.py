from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import time

def get_image():
    
    URL = "https://blog.naver.com/gksekgus1268/222577476688"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("headless")
        
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.get(url=URL)

    #웹페이지가 로딩될때까지 기다리고 5초가 넘어가면 웹페이지가 로딩이 안됐더라도 다음 명령어를 실행.
    #로딩이 완료되면 그 즉시 다음 명령어로 이동한다.
    driver.implicitly_wait(time_to_wait=5)

    #네이버 blog 크롤링을 위함. id가 mainFrame인 요소를 찾아 focus
    iframe = driver.find_element_by_id("mainFrame")
    driver.switch_to.frame(iframe)

    imgUrl = driver.find_element(By.XPATH,'//*[@id="SE-b09578e8-9b45-4100-99dc-9ceb9244e0d0"]/div/div/div/a/img').get_attribute("src")
    urllib.request.urlretrieve(imgUrl, "image.jpg")
    sleep_time = 3
    time.sleep(sleep_time)
    
    driver.close()

get_image()