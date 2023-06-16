# from sahibinden import sahibinden
# from sqlconnection import sqlConnection
from hepsiemlak import hepsiemlak

# sahibinden = sahibinden()
hepsiemlak = hepsiemlak()
# sqlConnection = sqlConnection()

# provinces = ["adana", "adiyaman", "afyonkarahisar", "agri", "aksaray", "amasya", "ankara", "antalya", "ardahan",
#              "artvin", "aydin", "balikesir", "bartin", "batman", "bayburt", "bilecik", "bingol", "bitlis", "bolu",
#              "burdur", "bursa", "canakkale", "cankiri", "corum", "denizli", "diyarbakir", "duzce", "edirne", "elazig",
#              "erzincan", "erzurum", "eskisehir", "gaziantep", "giresun", "gumushane", "hakkari", "hatay", "igdir",
#              "isparta", "istanbul", "izmir", "kahramanmaras", "karabuk", "karaman", "kars", "kastamonu", "kayseri",
#              "kilis", "kirikkale", "kirklareli", "kirsehir", "kocaeli", "konya", "kutahya", "malatya", "manisa",
#              "mardin", "mersin", "mugla", "mus", "nevsehir", "nigde", "ordu", "osmaniye", "rize", "sakarya", "samsun",
#              "sanliurfa", "siirt", "sinop", "sivas", "sirnak", "tekirdag", "tokat", "trabzon", "tunceli", "usak", "van",
#              "yalova", "yozgat", "zonguldak"
#              ]

turn = 0
# ***************************************************   SAHİBİNDEN ************************
# for province in provinces:
#     print(f"{province.upper()} BAŞLATILDI!!!")
#     sqlConnection.autoComplete(sahibinden.getHouses(province, turn), province)
#     turn += 1
#     print(f"{province.upper()} EKLENDİ EKLENEN İL SAYISI {turn} KADARDIR. ")

# # ***************************************************   HEPSİEMLAK ************************
# # #
#
#
provinces = ["adiyaman", "aksaray"
             ]


for province in provinces:
    print(f"{province.upper()} BAŞLATILDI!!!")
    # sqlConnection.autoComplete(hepsiemlak.getHouses(province), province)
    hepsiemlak.getHouses(province)
    turn += 1
    print(f"{province.upper()} EKLENDİ EKLENEN İL SAYISI {turn} KADARDIR. ")
hepsiemlak.driver.quit()
