"""
Program uses RapidTags to get tag list for youtube viudeo upload

Takes one argument in cmd to run as search term
'python script.py searchterm'
"""
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import sys

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#THIS INITIALIZES THE DRIVER (AKA THE WEB BROWSER)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#Search Item
searchItem = "minecraft"
if (len(sys.argv) == 1):
    searchItem = "minecraft"
else:
    searchItem = str(sys.argv[1]).replace('_'," ")

#RapidTags
link = ("https://rapidtags.io/api/generator?query=" + searchItem +"&type=YouTube")

driver.get("" + link)
time.sleep(2)

output = driver.find_element(by=By.XPATH, value='/html/body/pre').text

#print(output[29:-2])
#Output without square brackets and double quotes, converted into an array of tags!
outputArray = output[29:-2].replace('"',"").split(",")

print(outputArray)
#print(outputArray[0])


#cd /d path
#To change paths into folder of script in different drive

#https://rapidtags.io/api/generator?query=minecraft&type=YouTube
#Change query=minecraft into any query item for string of tags listed from RapidTags.com

