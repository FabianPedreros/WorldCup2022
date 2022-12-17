import streamlit as st

# Import required modules and functions
from bs4 import BeautifulSoup
import requests
import pandas as pd
import plost
from PIL import Image
import plotly.express as px


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


# Streamlit

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard FIFA World Cup Qatar 2022')

st.sidebar.subheader('Medidas')
medida = st.sidebar.selectbox('Medidas a comparar por equipo:', offensive_data.columns) 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created with ❤️ by [Data Professor](https://youtube.com/dataprofessor/).
''')


# Row A
st.markdown('### FIFA World Cup Qatar 2022')
a1, a2, a3 = st.columns(3)
a2.image(Image.open('logo.jpg'))


# Row B
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Comparación de selecciones')
    plost.bar_chart(
    data=offensive_data,
    bar=offensive_data['P'],
    value='National selection')
with c2:
    st.markdown('### Donut chart')
    plost.donut_chart(
        data=stocks,
        theta=donut_theta,
        color='company',
        legend='bottom', 
        use_container_width=True)

# Row C
st.markdown('### Line chart')
st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)

st.dataframe(offensive_data)

pie_chart = px.pie(offensive_data,
                    title = 'Pases generados',
                    values = 'P',
                    names = 'National selection')

st.plotly_chart(pie_chart)

bar_chart = px.bar(offensive_data,
                    x = 'National selection',
                    y = medida,
                    text= medida,
                    template = 'plotly_white')

st.plotly_chart(bar_chart)