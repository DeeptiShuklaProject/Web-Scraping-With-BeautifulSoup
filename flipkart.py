import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="DOjaWF gdgoEp")

    if box:
        names = box.find_all("div", class_="KzDlHZ")
        prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
        descs = box.find_all("ul", class_="G4BRas")
        reviews = box.find_all("div", class_="XQDdHH")

        for name, price, desc, review in zip(names, prices, descs, reviews):
            Product_name.append(name.text)
            Prices.append(price.text)
            Description.append(desc.text)
            Reviews.append(review.text)

df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews})
print(df)

df.to_csv("flipkart_mobiles_under_50000.csv")