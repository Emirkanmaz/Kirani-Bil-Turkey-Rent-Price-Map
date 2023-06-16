import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


class hepsiemlak:
    # service = Service(executable_path=r"C:\Users\emirk\Desktop\chromedriver.exe")
    service = Service(executable_path=r"D:\chromedriver\chromedriver.exe")

    def __init__(self):
        # service = Service(executable_path=r"C:\Users\emirk\Desktop\chromedriver.exe")
        service = Service(executable_path=r"D:\chromedriver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.clk = 1
        self.houseList = []


    def loadHouses(self):

        time.sleep(2)
        # self.driver.implicitly_wait(1)
        items = self.driver.find_elements(By.CLASS_NAME, "list-view-content")

        for item in items:
            prices = item.find_elements(By.CLASS_NAME, "list-view-price")
            for price in prices:
                if price.text != "TL":
                    price = price.text[:-3]
            meterSquare = item.find_element(By.CLASS_NAME, "squareMeter")
            rooumNum = item.find_element(By.CLASS_NAME, "houseRoomCount")
            district = item.find_element(By.CLASS_NAME, "list-view-location ")
            titleLink = item.find_element(By.CLASS_NAME, "card-link").get_attribute("href")
            # print(price, meterSquare.text.replace("m2", ""), rooumNum.text, district.text.split(",")[0],  titleLink)

            house = (
                price + " TL", meterSquare.text.replace("m2", ""), rooumNum.text.replace(" ", ""), district.text.split(",")[0], titleLink
            )
            # print(house)
            self.houseList.append(house)


        print(self.clk)
        self.clk += 1


    def getHouses(self, province):
        self.houseList = []
        self.driver.get("https://www.hepsiemlak.com/" + province + "-kiralik?sortField=PRICE&sortDirection=ASC")
        time.sleep(2)
        self.loadHouses()

        while True:
            link = None
            while not link:
                try:
                    link = self.driver.find_element(By.CLASS_NAME, "he-pagination__navigate-text--next")
                except NoSuchElementException:
                    time.sleep(2)
                    break
            if link == None:
                break

            if self.driver.find_element(By.CLASS_NAME, "he-pagination__navigate-text--next").get_attribute("href")[-1] != "#":
                self.driver.find_element(By.CLASS_NAME, "he-pagination__navigate-text--next").click()
                self.loadHouses()
            else:
                break

        print(self.houseList)
        print(len(self.houseList))
        # for house in self.houseList:
        #     print(house)
        time.sleep(5)
        # self.driver.quit()
        return self.houseList

# TEST

# app = hepsiemlak()
# turn = 0
# provinces = ["ardahan", "bingol", "ardahan"]
# for province in provinces:
#     print(f"{province.upper()} BAŞLATILDI!!!")
#     turn += 1
#     app.getHouses(province)
#     print(f"{province.upper()} EKLENDİ EKLENEN İL SAYISI {turn} KADARDIR. ")