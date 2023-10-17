from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd


START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"


browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(1)  # 10

scarped_data = []


def scrape():
    print("scrape called!")

    soup = BeautifulSoup(browser.page_source, "html.parser")

    # MUITO IMPORTANTE: A classe "wikitable" e os dados <tr> sáo os existentes no momento da criaCâo deste
    # código.
    # Isso pode ser atualizado no futuro, pois a página é atualizada pela Wikipedia.
    # Entenda a estrutura da página conrorme discutido na aula e execute a coleta de dados do zero.

    bright_star_table = soup.find("tbody")

    table_rows = bright_star_table.find_all("tr")  # table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)

        temp_list = []

        for col_data in table_cols:

            # Remova os espaCos em branco extras usando o método strip(), escolha o correto
            #data = coldata.text.strip()
            #data = col_data.text.strip()
            print("data:", data)

            temp_list.append(data)

        scarped_data.append(temp_list)


# Chamando o Método, escolha o correto
# scrape
# scrape()
# scape()

stars_data = []

for i in range(0, len(scarped_data)):
    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][4]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

# Defina o cabeçalho, escolha o correto
# headers = ["name", "distance(ly)",
    # "mass", "radius", "luminosity"]
# headers = ["name", "distance(ly)",


# Defina o dataframe do Pandas, escolha o correto
#star_df_1 = pd.DataFrame(stars_data, columns=headers)
#star = pd.DataFrame(stars_data, columns=headers)
#star_df_1 = DataFrame(stars_data, columns=headers)

print("stars_data:", stars_data)

# Converta para CSV, escolha o correto
#star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")
#star_df_1.to.csv('scraped_data.csv', index=True, index_label="id")
