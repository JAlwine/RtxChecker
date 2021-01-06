import requests
import time
import winsound
import datetime
import webbrowser

links = {   "RTX 3080 Founders Edition": "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440",
            "RTX 3080 EVGA FTW3 Ultra": "https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6436196.p?skuId=6436196",
            "RTX 3080 EVGA FTW3": "https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6436191.p?skuId=6436191",
            "RTX 3070 Founder Edition": "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442",
            "RTX 3070 EVGA XC3 Ultra": "https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439299.p?skuId=6439299",
            "RTX 3070 EVGA FTW3 Ultra": "https://www.bestbuy.com/site/evga-geforce-rtx-3070-ftw3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439301.p?skuId=6439301",
            "RTX 3070 EVGA XC3 Black": "https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-black-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439300.p?skuId=6439300",
        }

headers = {"User-Agent":"Mozilla/5.0","cache-control":"max-age=0"}

def check():

    for cardName, link in links.items():
        print(".", end="")

        if not check_link(link):
            print(datetime.datetime.now(), cardName + " is in stock: " + link)
            signal()


def check_link(link_url):
    try:
        source = requests.get(link_url, headers=headers).text

        is_sold_out = source.__contains__("class=\"btn btn-disabled btn-lg btn-block add-to-cart-button\"")

        if not is_sold_out:
            webbrowser.open(links[link_url])
            save_file = open(link_url+".html","w")
            save_file.write(source)
            save_file.close()
        time.sleep(0.2)
    except requests.exceptions.ConnectionError:
        print("Connection Error.")
        return True

    return is_sold_out


def signal():
    while True:
        for i in range(1, 10):
            winsound.Beep(i * 100, 200)
        time.sleep(0.5)

while True:
    check()
    time.sleep(10)
