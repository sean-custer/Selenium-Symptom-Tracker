#run 'pip install selenium'
#go to https://www.selenium.dev/downloads/ and download the webdriver for your browser
#extract exe to the same folder as this file
#run this script
#To add as a .bat to allow your system to execute daily, do the following:
#   1) Create a .txt file following the template -> "Path where your Python exe is stored\python.exe" "Path where your Python script is stored\script name.py"
#       pause
# note: you can find the Path where your python.exe is by using which py(thon)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://rtforms.umbc.edu/rt_authenticated/legal/COVID_Contact_and_Symptoms.php')
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
#Enter info here
username.send_keys('')
password.send_keys('')

elem = driver.find_element_by_id('submitButton')
elem.click()

phoneNum = driver.find_element_by_id('reporterPhone')
#Enter info here
phoneNum.send_keys('')

temp = driver.find_element_by_id('temperature')
temp.send_keys('98')

noSimp = driver.find_element_by_id('symptoms_none')
noSimp.click()

submit = driver.find_element_by_id('submit')
submit.click()

