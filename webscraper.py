import csv
import requests
from bs4 import BeautifulSoup


open("hotels.csv", "w")
h_name = []
h_addr = []
h_price = []
h_rating = []
h_amen = []

url = "https://www.oyorooms.com/search/?checkin=30%2F07%2F2022&checkout=31%2F07%2F2022&city=" \
      "&coupon=&guests=1&latitude=19.0939136&location=Around%20me&longitude=72.8891392" \
      "&roomConfig%5B%5D=1&rooms=1&searchType=locality"

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/103.0.0.0 Safari/537.36'}
req = requests.get(url, headers=header)
soup = BeautifulSoup(req.text, "html.parser")
all_hotels = soup.find_all('div', {'class': "oyo-cell--12-col oyo-cell--8-col-tablet oyo-cell--4-col-phone"})
amenities = soup.find_all('div', {'class': "amenityWrapper__amenity"})
print(amenities)
for hotels in all_hotels:
    h_name.append(hotels.find("h3", {"class": "listingHotelDescription__hotelName d-textEllipsis"}).text)
    h_addr.append(hotels.find("span", {"itemprop": "streetAddress"}).text)
    h_price.append(int(hotels.find("span", {"class": "listingPrice__finalPrice"}).text[1:]))
    h_amen.append(hotels.find("span", {"class": "d-body-sm d-textEllipsis"}).text)
    try:
        h_rating.append(float(hotels.find("span", {"class": "is-fontBold hotelRating__rating hotelRating__rating--fair hotelRating__rating--clickable"}).text))
    except AttributeError:
        h_rating.append(0)


with open("hotels.csv", "a", newline='') as csv_file:
    writer = csv.writer(csv_file)
    if csv_file.tell() == 0:
        writer.writerow(("Hotel Name", "Hotel Address", "Hotel Price", "Hotel Ratings"))
    for hotels in range(len(h_name)):
        writer.writerow((h_name[hotels], h_addr[hotels], h_price[hotels], h_rating[hotels]))