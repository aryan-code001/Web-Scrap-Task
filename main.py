import pandas
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from datetime import date

# Load the webpage
web_url = "https://search.earth911.com/?what=Electronics&where=1001&list_filter=all&max_distance=100&family_id=&latitude=&longitude=&country=&province=&city=&sponsor="
response = requests.get(web_url)
response_data = response.text

# Parse HTML
soup = BeautifulSoup(response_data, "lxml")

# Extract business names
name_list = [re.sub(r'[^a-zA-Z0-9\s]', '', a.text)
             for a in soup.select(".title a")]

# Extract addresses
address_list = [re.sub(r'[^a-zA-Z0-9\s]', '', p.text)
                for p in soup.findAll("p", class_="address1")]
addresss_list = [re.sub(r'[^a-zA-Z0-9\s]', '', p.text)
                 for p in soup.findAll("p", class_="address3")]

final_address_list = [
    f"{address_list[i]}, {addresss_list[i]}"
    for i in range(len(address_list))
]
# Getting update_date
today_str = str(date.today())
update_date = [today_str] * len(name_list)

# Compile DataFrame
data = {
    "Business_name": name_list,
    "Street_address": final_address_list,
    "last_update_date": update_date
}
df = pd.DataFrame(data)

#Checking whether there exits a csv file or not
try :
    # Moving data to a csv file
    pandas.read_csv("data.csv")
except:
    df.to_csv('data.csv', mode='a')

print(df)