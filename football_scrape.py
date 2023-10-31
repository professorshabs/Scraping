from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# options for easier browsing:
def get_driver(site_url):
    options = webdriver.ChromeOptions()
    options.add_argument("disaple-infobars")  # disable popup infor bars
    options.add_argument("start-maximized") #start the browser as maximized
    options.add_experimental_option("detach", True)
    options.add_argument("disable-dev-shn-usage")  # linux interactions problem
    options.add_argument("no-sandbox")  # nice privledges
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])  # enble scraping to "forbidden" sites

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(site_url)
    #driver.maximize_window()
    return driver


# https://www.adamchoi.co.uk/overs/detailed
driver = get_driver("https://www.adamchoi.co.uk/overs/detailed")
# xpath://*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]
all_matches_button = driver.find_element("xpath", "//label[@analytics-event='All matches']")
#all_matches_button = driver.find_element("xpath","//*[@id='side-menu']/li[1]/a")
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, "tr")
dates = []
home_team = []
scores = []
away_team = []
data_dict = []
for match in matches:
    diction = {}
    diction["date"] = str(match.find_element("xpath","./td[1]").text)
    diction["home_team"] = str(match.find_element("xpath", "./td[2]").text)
    diction["score"] = str(match.find_element("xpath", "./td[3]").text)
    diction["away_team"] = str(match.find_element("xpath", "./td[4]").text)

    data_dict.append(diction)

    print(f"date {diction['date']}, home team: {diction['home_team']} vs away {diction['away_team']} and score {diction['score']}")
    print(data_dict[3])
# driver. quit()
