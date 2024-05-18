import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a Service instance with the path to the ChromeDriver executable
service = Service("C:/Users/Smit/chromedriver.exe")

class Info:
    def __init__(self):
        # Initialize the WebDriver using the Service instance
        self.driver = webdriver.Chrome(service=service)

    def get_info_wikipedia(self, query):
        self.query = query
        self.driver.get(url='https://www.wikipedia.org/')
        
        # Find the search input field and perform the search
        search_wikipedia = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search_wikipedia.click()
        search_wikipedia.send_keys(self.query)
        enter = self.driver.find_element(By.XPATH,'//*[@id="search-form"]/fieldset/button')
        enter.click()
        #search_wikipedia.send_keys(Keys.RETURN)  # Press Enter to initiate the search
        
        # Optional: Wait to keep the browser open to view results
        time.sleep(100000)  # Keeps the browser open for 10 seconds for demonstration

    def open_youtube(self, query):
        self.query = query
        self.driver.get(url='https://www.youtube.com/results?search_query=' + query)
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()
        # search.send_keys(Keys.RETURN)  # Press Enter to initiate the search
        
        # Optional: Wait to keep the browser open to view results
        time.sleep(100000) 
# Instantiate the class

