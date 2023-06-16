import mysql.connector
import statistics
import time
import pyodbc


class sqlConnection:
    def __init__(self):

        self.mydb = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=DESKTOP-3S9P1V9;'
            'Database=new_schema;'
            'Trusted_Connection=yes;')

        self.mycursor = self.mydb.cursor()

    def createTable(self, province):
        try:
            self.mycursor.execute(
                "CREATE TABLE `new_schema`." + province + " (`id` INT NOT NULL AUTO_INCREMENT,`price` VARCHAR(45) NULL,`meterSquare` VARCHAR(45) NULL,`roomNum` VARCHAR(45) NULL,`district` VARCHAR(45) NULL,`link` LONGTEXT NULL,`meterSquarePrice` FLOAT NULL,PRIMARY KEY (`id`),UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)")
            print(f"{province} Table created.")
        except:
            print("Table exist")

    def insertList(self, rentList, province):

        sql = "INSERT INTO " + province + " (price, meterSquare, roomNum, district, link) VALUES (%s, %s, %s, %s, %s)"
        # houselist type bu şekilde olmalı
        # houseList = [
        #     ('1.000 TL', '70', '1+1', 'Merkez', 'https://www.sahibinden.com/ilan/emlak-konut-kiralik-sifir-esyali-1-plus1-1027879402/detay'),
        #     ('1.100 TL', '75', '1+1', 'Merkez', 'https://www.sahibinden.com/ilan/emlak-konut-kiralik-kucuk-bolcek-mah-kultur-merkezi-civari-kiralik-1-plus1-daire-1040440614/detay')
        # ]
        self.mycursor.executemany(sql, rentList)
        # mycursor.executemany(sql, houseList)
        self.mydb.commit()
        print(self.mycursor.rowcount, "was inserted.")

    def convertTuple(self, tup):
        str = ''
        for item in tup:
            str = str + item
        return str

    def convertintTuple(self, tup):
        intg = int()
        for item in tup:
            intg = intg + item
        return intg

    def getPriceList(self, province):
        sql = "SELECT price FROM " + province
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()

        priceList = []
        for price in myresult:
            str = self.convertTuple(price)
            # print(int(str.strip("TL").replace(".", "")))
            priceList.append(int(str.strip("TL").replace(".", "")))
        return priceList

    def getMeterSquareList(self, province):
        sql = "SELECT meterSquare FROM " + province
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()

        m2List = []
        for m2 in myresult:
            str = self.convertTuple(m2)
            m2List.append(int(str.replace(".", "")))
        return m2List

    def meanPrice(self, province):
        return statistics.mean(self.getPriceList(province))

    def meterSquarePriceList(self, province):
        m2PriceList = []
        if len(self.getMeterSquareList(province)) == len(self.getPriceList(province)):
            for i in range(len(self.getPriceList(province))):
                m2PriceList.append(self.getPriceList(province)[i] / self.getMeterSquareList(province)[i])
            return m2PriceList
        else:
            print("Price List lenght and Meter Square List lenght are not equal!!!")

    def getIdList(self, province):
        sql = "SELECT id FROM " + province
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()

        idList = []
        for id in myresult:
            intg = self.convertintTuple(id)
            idList.append(intg)
        return idList

    def insertm2Price(self, province):
        idList = self.getIdList(province)
        m2PriceList = self.meterSquarePriceList(province)
        if len(idList) == len(m2PriceList):
            for i in range(len(idList)):
                sql = "UPDATE " + province + " SET meterSquarePrice = %s WHERE id = %s"
                val = (m2PriceList[i], idList[i])
                self.mycursor.execute(sql, val)
                self.mydb.commit()
            print("All datas have inserted")

        else:
            print("Id List lenght and Meter Square List lenght are not equal!!!")

    def meanMeterSquarePrice(self, province):
        sql = "SELECT meterSquarePrice FROM " + province
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        m2List = []
        for m2 in myresult:
            intg = self.convertintTuple(m2)
            m2List.append(intg)
        return statistics.mean(m2List)

    def insertMean(self, province):
        sql = "INSERT INTO mean (province, meanPrice, meanMeterSquarePrice) VALUES (%s, %s, %s)"
        vals = [
            (province),
            (self.meanPrice(province)),
            (self.meanMeterSquarePrice(province))
        ]
        self.mycursor.execute(sql, vals)
        self.mydb.commit()
        print(province, "was inserted.")

    def autoComplete(self, rentList, province):
        time.sleep(1)
        self.createTable(province)
        time.sleep(1)
        self.insertList(rentList, province)
        time.sleep(1)
        self.insertm2Price(province)
        time.sleep(1)
        print(f"Mean Price of {province} is {self.meanPrice(province)}")
        time.sleep(1)
        # self.mydb.close()


# TEST

# app = sqlConnection()
# app.insertMean("artvin")
# provinces = ["adana", "adiyaman", "afyonkarahisar", "agri", "aksaray", "amasya", "ankara", "ardahan",
#              "artvin", "bolu", "burdur"
#              ]
# for province in provinces:
#     app.insertMean(province)
