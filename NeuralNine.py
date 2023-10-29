import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True) #keep the window open

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.neuralnine.com/")
driver.maximize_window()

links  = driver.find_elements("xpath","//a[@href]")

for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break
    #print(link.get_attribute("innerHTML"))

#//div[@class='elementor-image'][.//h2[contains(., '7 IN 1')]]

#//*[@id="content"]/article/div/div/div/div/section/div/div/div/div/div/section[1]/div/div/div[1]/div/div/div[1]/div/div/a
#'//*[@id="content"]/article/div/div/div/div/section/div/div/div/div/div/section[1]/div/div/div[3]/div/div/div[1]/div/div/a'
books =driver.find_elements("xpath",
 '//*[@id="content"]/article/div/div/div/div/section/div/div/div/div/div/section[1]/div/div/div[3]//a')
                            #"//div[@class='elementor-image']//a[@href]")
# for book in books:
#     print(book.get_attribute("href"))

books[0].click()
driver.switch_to.window(driver.window_handles[1]) #switch to new tab

time.sleep(5)
buttons  = driver.find_elements("xpath",
                                "//a[.//span[contains(., 'Paperback')]]//span[contains(., '$')]//span")

for button in buttons:
    print(button.get_attribute("innerHTML"))
driver.quit()