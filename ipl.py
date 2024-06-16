import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_ = "ih-td-tab auction-tbl")
# print(table)
title = table.find_all("th")
header = []
for i in title:
    name = i.text
    header.append(name)

df = pd.DataFrame(columns=header)
# print(df)

rows = table.find_all("tr")
# print(rows)

for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div", class_ = "ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0,first_td)
    l = len(df)
    df.loc[l] = row
    
print(df)

df.to_csv("ipl Auction stats.csv")