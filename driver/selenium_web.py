import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import cv2
import requests
from bs4 import BeautifulSoup

# Create a Service instance with the path to the ChromeDriver executable
service = Service("C:/Users/Smit/chromedriver.exe")

class Info:
    # def __init__(self):
    #     # Initialize the WebDriver using the Service instance
    #     self.driver = webdriver.Chrome(service=service)

    def get_info_wikipedia(self, query):
        self.driver = webdriver.Chrome(service=service)
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
        self.driver = webdriver.Chrome(service=service)
        self.query = query
        self.driver.get(url='https://www.youtube.com/results?search_query=' + query)
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()
        # search.send_keys(Keys.RETURN)  # Press Enter to initiate the search
        
        # Optional: Wait to keep the browser open to view results
        time.sleep(100000) 
# Instantiate the class


    def get_google(self,query):
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(url=f'https://www.google.com/search?q={query}&sca_esv=345267d81bec8f30&sxsrf=ADLYWILVbWdEHQ0BQxZeQfPb_SKyebeHng%3A1716108258417&source=hp&ei=4rtJZoCmFuel2roPrNilYA&iflsig=AL9hbdgAAAAAZknJ8ll4e2nW1H0Nzd6ShaGajCpLemKe&ved=0ahUKEwiAn4u5qZmGAxXnklYBHSxsCQwQ4dUDCBU&uact=5&oq=smi&gs_lp=Egdnd3Mtd2l6IgNzbWkyEBAuGIAEGLEDGEMYgwEYigUyEBAuGIAEGLEDGEMYgwEYigUyChAAGIAEGEMYigUyChAuGIAEGEMYigUyChAAGIAEGEMYigUyEBAuGIAEGLEDGEMYgwEYigUyExAuGIAEGLEDGNEDGEMYxwEYigUyDRAAGIAEGLEDGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigVIxwpQ6QRYjQhwAXgAkAEAmAGoAaAB6wOqAQMwLjO4AQPIAQD4AQGYAgSgAv0DqAIKwgIHECMYJxjqAsICDRAuGNEDGMcBGCcY6gLCAgoQIxiABBgnGIoFwgIEECMYJ8ICERAAGIAEGJECGLEDGIMBGIoFwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxjRAxiDARjHAcICDhAuGIAEGLEDGIMBGIoFwgIQEC4YgAQY0QMYQxjHARiKBcICCBAAGIAEGLEDwgIOEAAYgAQYsQMYgwEYigXCAggQLhiABBixA5gDB5IHAzEuM6AHxyc&sclient=gws-wiz')

        time.sleep(1000)

    def get_temperature(self,query):
        # self.driver = webdriver.Chrome(service=service) 
        url = f'https://www.google.com/search?q={query}&sca_esv=345267d81bec8f30&sxsrf=ADLYWILVbWdEHQ0BQxZeQfPb_SKyebeHng%3A1716108258417&source=hp&ei=4rtJZoCmFuel2roPrNilYA&iflsig=AL9hbdgAAAAAZknJ8ll4e2nW1H0Nzd6ShaGajCpLemKe&ved=0ahUKEwiAn4u5qZmGAxXnklYBHSxsCQwQ4dUDCBU&uact=5&oq=smi&gs_lp=Egdnd3Mtd2l6IgNzbWkyEBAuGIAEGLEDGEMYgwEYigUyEBAuGIAEGLEDGEMYgwEYigUyChAAGIAEGEMYigUyChAuGIAEGEMYigUyChAAGIAEGEMYigUyEBAuGIAEGLEDGEMYgwEYigUyExAuGIAEGLEDGNEDGEMYxwEYigUyDRAAGIAEGLEDGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigVIxwpQ6QRYjQhwAXgAkAEAmAGoAaAB6wOqAQMwLjO4AQPIAQD4AQGYAgSgAv0DqAIKwgIHECMYJxjqAsICDRAuGNEDGMcBGCcY6gLCAgoQIxiABBgnGIoFwgIEECMYJ8ICERAAGIAEGJECGLEDGIMBGIoFwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxjRAxiDARjHAcICDhAuGIAEGLEDGIMBGIoFwgIQEC4YgAQY0QMYQxjHARiKBcICCBAAGIAEGLEDwgIOEAAYgAQYsQMYgwEYigXCAggQLhiABBixA5gDB5IHAzEuM6AHxyc&sclient=gws-wiz'
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        return temp



