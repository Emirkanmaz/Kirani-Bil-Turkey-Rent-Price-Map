import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


class sahibinden:
    # service = Service(executable_path=r"C:\Users\emirk\Desktop\chromedriver.exe")
    service = Service(executable_path=r"D:\chromedriver\chromedriver.exe")

    def __init__(self):
        # service = Service(executable_path=r"C:\Users\emirk\Desktop\chromedriver.exe")
        service = Service(executable_path=r"D:\chromedriver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.clk = 1
        self.houseList = []

    def loadHouses(self):
        # link = None
        # while not link:
        #     try:
        #         link = driver.find_element_by_xpath(linkAddress)
        #     except NoSuchElementException:
        #         time.sleep(2)

        # clk = driver.find_element(By.CLASS_NAME, "feature-discovery__celebrity") .click()
        time.sleep(2)
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        items = self.driver.find_elements(By.CLASS_NAME, "searchResultsItem")
        try:
            items.pop(3)
        except:
            pass
        for item in items:
            titleLink = item.find_element(By.CLASS_NAME, "classifiedTitle").get_attribute("href")
            price = item.find_element(By.CLASS_NAME, "searchResultsPriceValue")
            attrvalues = item.find_elements(By.CLASS_NAME, "searchResultsAttributeValue")
            while True:
                if len(attrvalues) == 2:
                    break
                else:
                    attrvalues = item.find_elements(By.CLASS_NAME, "searchResultsAttributeValue")
                    time.sleep(5)
                    print("döngü girildi")

            district = item.find_element(By.CLASS_NAME, "searchResultsLocationValue")
            # house = {
            #     "price": price.text,
            #     "meterSquare": attrvalues[0].text,
            #     "roomNum": attrvalues[1].text,
            #     "district": district.text.split()[0],
            #     "link": titleLink
            # }
            if len(attrvalues) == 2 and len(district.text.split()) >= 1:
                house = (
                    price.text, attrvalues[0].text, attrvalues[1].text, district.text.split()[0], titleLink
                )
                # print(house)
                self.houseList.append(house)

        print(self.clk)
        self.clk += 1

    def getHouses(self, province, turn):
        self.houseList = []
        self.driver.get("https://www.sahibinden.com/kiralik-daire/" + province + "?pagingSize=50&sorting=price_asc")
        self.driver.refresh()
        time.sleep(2)

        if turn == 0:
            closebtn = self.driver.find_element(By.ID, "onetrust-close-btn-container")
            closebtn.click()
        self.loadHouses()
        while True:
            time.sleep(1)
            prevnextbutton = self.driver.find_elements(By.CLASS_NAME, "prevNextBut")
            if len(prevnextbutton) == 1:
                if prevnextbutton[0].text == "Sonraki":
                    prevnextbutton[0].click()
                    self.loadHouses()
                else:
                    break
            elif len(prevnextbutton) == 0:
                break
            else:
                prevnextbutton[1].click()
                self.loadHouses()
        print(self.houseList)
        print(len(self.houseList))
        time.sleep(2)
        return self.houseList


# TEST

# app = sahibinden()
# turn = 0
# provinces = ["ardahan", "bingol", "ardahan"]
# for province in provinces:
#     print(f"{province.upper()} BAŞLATILDI!!!")
#     turn += 1
#     app.getHouses(province, turn)
#     print(f"{province.upper()} EKLENDİ EKLENEN İL SAYISI {turn} KADARDIR. ")
