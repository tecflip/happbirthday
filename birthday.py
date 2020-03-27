#Import necessary classes from different modules 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.keys import Keys 
import time 

chrome_options = webdriver.ChromeOptions()
path_to_chromedriver = "C:\HappyFB\chromedriver.exe"

#Disbale chrome popup notification.
chrome_options.add_argument("--disable-notifications")

prefs = {"profile.default_content_setting_values.notifications": 2} 
chrome_options.add_experimental_option("prefs", prefs) 
browser = webdriver.Chrome(path_to_chromedriver, chrome_options=chrome_options) 

# open facebook.com using get() method 
browser.get('https://www.facebook.com/') 

# user_name or e-mail id 
username = "akshaychauhan.simple@gmail.com"

# getting passowrd from text file 
with open('C:\HappyFB\pwd.txt', 'r') as myfile: 
	password = myfile.read().replace('\n', '') 

print("Let's Begin") 

#Search for EMAIL ID field
element = browser.find_elements_by_xpath('//*[@id ="email"]') 
element[0].send_keys(username) 

print("Username Entered") 

#Serach for Password Entry Field
element = browser.find_element_by_xpath('//*[@id ="pass"]') 
element.send_keys(password) 
time.sleep(3)
print("Password Entered") 

# logging in 
log_in = browser.find_elements_by_id('loginbutton') 
log_in[0].click() 

print("Login Successfull")
time.sleep(5)

#Traversing to Birthday Notification field
browser.get('https://www.facebook.com/events/birthdays/') 

feed = 'Happy Birthday !'

element = browser.find_elements_by_xpath("//*[@class ='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']") 

cnt = 0

for el in element: 
	cnt += 1
	element_id = str(el.get_attribute('id')) 
	XPATH = '//*[@id ="' + element_id + '"]'
	post_field = browser.find_element_by_xpath(XPATH) 
	post_field.send_keys(feed) 
	post_field.send_keys(Keys.RETURN) 
	print("Birthday Wish posted for friend" + str(cnt)) 
time.sleep(10)

#Close the browser 
browser.close() 
