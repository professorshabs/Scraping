from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#AI
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# options = Options()
# options.add_experimental_option("detach",True)
options = webdriver.ChromeOptions()
options.add_argument("--headless")

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver = webdriver.Chrome(executable_path='/Users/profshabangu/Downloads/ChromeSetup.exe', options=options)
#call and the website:
web_url = "https://www.pnp.co.za/"
#"https://www.adamchoi.co.uk/teamgoals/detailed"
#web_url ="https://www.neuralnine.com/"
driver.get(web_url)

button = WebDriverWait(driver, 30).until(
    # EC.element_to_be_clickable((By.XPATH,"//div//button[contains(., 'Do this later')]"))
    EC.element_to_be_clickable((By.CSS_SELECTOR, "address-popover__actions-do-later"))
)
button.click()
# try:
#     button = WebDriverWait(driver,10).until(
#         #EC.element_to_be_clickable((By.XPATH,"//div//button[contains(., 'Do this later')]"))
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "address-popover__actions-do-later"))
#     )
#     button.click()
#
# except Exception as e:
#     print("An error occurred:",str(e))
#
# finally:
#     driver.quit()
#Wait for the address popup to appear:
# try:
#     #WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[@class='address-popover__actions']")))
#     #button = driver.find_element_by_xpath("//button[@class='address-popover__actions-do-later']")
#     #button = driver.find_element(By.XPATH, "//button[@class='address-popover__actions-do-later']").click()
#     button = driver.find_element_by_css_selector(".address-popover__actions-do-later")
#     #button.click()
#     #Click the "Do this later" button:
#     button.click()
# except Exception as e:
#     print("An error occurred:", str(e))
#
# finally:
#     driver.quit()

# try:
#     button= driver.find_element_by_class_name("address-popover__actions-do-later")
#     button.click()
# except Exception as e:
#     print("An Error occurred:",str(e))
# finally:
#     driver.quit()

# popup = driver.find_elements("xpath","//div[@class='address-popover__actions']//button")
# #
# # # links = driver.find_elements("xpath","//a[@href]")
# for link in popup:
#     print(link.get_attribute("innerHTML"))


# links = driver.find_elements("xpath","//a[@href]")
# for link in links:
#     if "Books" in link.get_attribute("innerHTML"):
#         link.click()
#         break

#print(all_products.text())
#driver.quit()
#Token: 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