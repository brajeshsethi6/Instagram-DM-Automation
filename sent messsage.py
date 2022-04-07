import auth
from selenium import webdriver
import time

instaID = input('ID: ')
instaMS = input('Message: ')
r = int(input('Repeatability: '))


PATH="location of your chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")
time.sleep(2.0)

uname = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
uname.send_keys(auth.username)
time.sleep(2.0)

pword = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pword.send_keys(auth.password)
time.sleep(2.0)

Button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
Button.click()
time.sleep(4.0)

driver.get('https://www.instagram.com/'+instaID+'/')
time.sleep(2.0)

Button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div')
Button.click()
time.sleep(2.0)

notnow = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
notnow.click()
time.sleep(2.0)

i=0
while (i<=r):

    message = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    message.send_keys(instaMS)
    time.sleep(2.0)

    button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
    button.click()
    time.sleep(2.0)

    i+=1


