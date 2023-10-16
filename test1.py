from bs4 import BeautifulSoup
import pandas as pd
import requests


session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
response = session.get('https://www.espn.com/mlb/history/leaders/_/sort/hits')

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')

world_titles = table.find('tr', class_ = 'colhead')

world_table_titles = [title.text.strip() for title in world_titles]


df = pd.DataFrame(columns = world_table_titles)
df
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

df
print(df)
df.to_csv(r'C:\Users\lbarrios\DownloadsCompanies.csv', index = False)