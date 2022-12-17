import streamlit as st

# Import required modules and functions
from bs4 import BeautifulSoup
import requests
import pandas as pd


# Web page to scrap offensive data

url = 'https://www.foxsports.com/soccer/fifa-world-cup-men/team-stats?category=offensive&sort=t_sog&season=2022&sortOrder=desc&groupId=12'

# Download the content

data = requests.get(url).text

# Creation of the BeatifulSoup object
soup = BeautifulSoup(data, 'html5lib')

# Find the html table in the web page
table = soup.find('tbody').find_all('tr')

offensive_data = pd.DataFrame(columns= ['National selection','GP', 'S', 'SOG', 'SOP', 'SOFF', 'SAB', 'POS', 'C','CS', 'P', 'PC', 'PL', 'PLC', 'CK', 'OFF'])

for row in soup.find('tbody').find_all('tr'):
    col = row.find_all("td")
    ns = col[1].text
    gp = col[2].text
    s = col[3].text
    sog = col[4].text
    sop = col[5].text
    soff = col[6].text
    sab = col[7].text
    pos = col[8].text
    c = col[9].text
    cs = col[10].text
    p = col[11].text
    pc = col[12].text
    pl = col[13].text
    plc = col[14].text
    ck = col[15].text
    off = col[16].text

    offensive_data = offensive_data.append({'National selection':ns, 'GP':gp, 'S':s, 'SOG':sog, 'SOP':sop, 'SOFF':soff, 'SAB':sab, 'POS':pos, 'C':c,'CS':cs, 'P':p, 'PC':pc, 'PL':pl, 'PLC':plc, 'CK':ck, 'OFF':off}, ignore_index=True)

offensive_data[offensive_data.columns] = offensive_data.apply(lambda x: x.str.strip())

offensive_data["P"]=offensive_data["P"].replace(",", "", regex=True)
offensive_data["PC"]=offensive_data["PC"].replace(",", "", regex=True)

offensive_data.iloc[:,1:] = offensive_data.iloc[:,1:].astype(int)


print(offensive_data)
