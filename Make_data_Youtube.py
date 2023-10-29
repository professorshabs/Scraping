from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

from bs4 import BeautifulSoup

site_url = "https://www.youtube.com/@AdamMarczakYT/videos"

# set selenium driver:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(site_url)

# Scroll down the page multiple times
for _ in range(5):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    #driver.find_element_by_tag_name('html').send_keys(Keys.END)
    time.sleep(2)

page_html = driver.page_source
soup = BeautifulSoup(page_html, 'html.parser')
# print(soup.prettify())
#Extract the video titles
video_titles = []
for vid in soup.find_all("div",{"id":"details"}):
    #print(video)
    title = vid.find("a", {"id":"video-title-link"}).text
    vid_url = vid.find("a", {"id": "video-title-link"})["href"]
    meta = vid.find("div", {"id":"meta"}).find_all("span")
    views = meta[0].text
    video_age = meta[1].text
    print(f"Videos {title} on {vid_url} with {views} and made: {video_age}")
    video_titles.append(vid.find('a'))
# Close the Selenium WebDriver instance
driver.quit()

# # Print the video titles
# for video_title in video_titles:
#     print(video_title)
print(len(video_titles))
#


#
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time
#
# from bs4 import BeautifulSoup
#
# site_url = "https://www.youtube.com/@AdamMarczakYT/videos"
#
# # set selenium driver:
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# # Set the implicitly wait time
# #driver.implicitly_wait(5)
#
# # Open the YouTube video page
# driver.get(site_url)
#
# # Scroll down the page multiple times
# for _ in range(10):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(1)
#
# # Get the page source
# page_html = driver.page_source
#
# # Parse the HTML
# soup = BeautifulSoup(page_html, "html.parser")
#
# #print(soup.prettify())
# #id="dismissible"
# #Extract the video titles
# video_titles = []
# for video in soup.find_all("div",{"id":"meta"}):
#     print(video)
#     video_titles.append(video.find('a'))
#
# # Close the Selenium WebDriver instance
# driver.quit()
#
# # # Print the video titles
# # for video_title in video_titles:
# #     print(video_title)
# print(len(video_titles))
#



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time
#
# from bs4 import BeautifulSoup
#
# site_url = "https://www.youtube.com/@AdamMarczakYT/videos"
#
# # set selenium driver:
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# driver.get(site_url)
#
# # Scroll down the page multiple times
# scroll_pause_time = 3  # Time between scrolling (adjust as needed)
# scrolls = 4  # Number of times to scroll
#
# for _ in range(scrolls):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(scroll_pause_time)
#
# # Get the page source
# page_html = driver.page_source
#
# # Parse the HTML
# soup = BeautifulSoup(page_html, 'html.parser')
#
# # Close the Selenium WebDriver instance
# driver.quit()
#
# # Print the prettified HTML for inspection
# print(soup.prettify())
