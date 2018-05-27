import scrapy
import time
from selenium import webdriver

class FlightsSpider(scrapy.Spider):
    name = "Fly_scanner"

    btn_close_cookie = '//*[@id="home"]/cookie-pop-up/div/div[2]/core-icon'
    from_airport_name = '//*[@id="search-container"]/div[1]/div/form/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/input'
    to_airport_name = '//*[@id="search-container"]/div[1]/div/form/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/input'


    #date_from = '//*[@id="row-dates-pax"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]'
    #date_to = ''

    start_urls = [
        "https://www.ryanair.com/pl/pl"
    ]

    def __init__(self, *args, **kwargs): # do parametryzacji klasy w przyszlosci
        self.driver = webdriver.Chrome('./chromedriver')


    def parse(self, response):

        self.driver.set_window_size(1024, 768)
        self.driver.maximize_window()

        self.driver.get(response.url)


        time.sleep(5)

        btn_close_cookie_po = self.driver.find_element_by_xpath(self.btn_close_cookie)
        btn_close_cookie_po.click()

        from_airport = self.driver.find_element_by_xpath(self.from_airport_name)
        from_airport.clear()
        from_airport.send_keys('Warszawa-Modlin')

        to_airport = self.driver.find_element_by_xpath(self.to_airport_name)
        to_airport.clear()
        to_airport.send_keys('Londyn-Stansted')

        time.sleep(10)
        self.driver.quit()
        self.driver.quit()
        self.driver.quit()


