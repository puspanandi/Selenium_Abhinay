from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
lists= driver.find_elements_by_class_name("g")

# get the number of elements found
print("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   #print (listitem.get_attribute("innerHTML"))
   print(listitem.get_attribute("href"))

   i=i+1
   #print(listitem.get_property("href"))
   if(i>10):
      break

# close the browser window
driver.quit()