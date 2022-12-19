import streamlit as st

# Import required modules and functions
from bs4 import BeautifulSoup
import requests
import pandas as pd
import plost
from PIL import Image
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Web page to scrap offensive data

url = 'https://www.foxsports.com/soccer/fifa-world-cup-men/team-stats?category=offensive&sort=t_sog&season=2022&sortOrder=desc&groupId=12'

# Download the content

data = requests.get(url).text

# Creation of the BeatifulSoup object
soup = BeautifulSoup(data, 'html5lib')

# Find the html table in the web page
table = soup.find('tbody').find_all('tr')

offensive_data = pd.DataFrame(columns= ['National selection','Games Played', 'Shots', 'Shots On Goal', 'Shots On Post', 'Shots Off Target', 'Shot Attempts Blocked', 'Possession Time Minutes Avg', 'Crosses','Crosses Successful', 'Passes', 'Pass Completions', 'Pass Attempts - Long', 'Pass Completions - Long', 'Corner Kicks', 'Offsides'])

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

    offensive_data = offensive_data.append({'National selection':ns, 'Games Played':gp, 'Shots':s, 'Shots On Goal':sog, 'Shots On Post':sop, 'Shots Off Target':soff, 'Shot Attempts Blocked':sab, 'Possession Time Minutes Avg':pos, 'Crosses':c,'Crosses Successful':cs, 'Passes':p, 'Pass Completions':pc, 'Pass Attempts - Long':pl, 'Pass Completions - Long':plc, 'Corner Kicks':ck, 'Offsides':off}, ignore_index=True)

offensive_data[offensive_data.columns] = offensive_data.apply(lambda x: x.str.strip())

offensive_data["Passes"]=offensive_data["Passes"].replace(",", "", regex=True)
offensive_data["Pass Completions"]=offensive_data["Pass Completions"].replace(",", "", regex=True)

offensive_data.iloc[:,1:] = offensive_data.iloc[:,1:].astype('int64')


# Scrap defensive data

# Web page to scrap defensive data

url2 = 'https://www.foxsports.com/soccer/fifa-world-cup-men/team-stats?category=defensive&sort=t_int&season=2022&sortOrder=desc&groupId=12'

# Download the content

data2 = requests.get(url2).text

# Creation of the BeatifulSoup object
soup2 = BeautifulSoup(data2, 'html5lib')

# Find the html table in the web page
table = soup2.find('tbody').find_all('tr')

defensive_data = pd.DataFrame(columns= ['National selection','Games Played', 'Throw Ins', 'Interceptions', 'Tackles', 'Tackles Attempted', 'Goal Kicks', 'Fouls', 'Free Kicks','Own Goals'])

for row in soup2.find('tbody').find_all('tr'):
    col = row.find_all("td")
    ns = col[1].text
    gp = col[2].text
    ti = col[3].text
    ints = col[4].text
    tkl = col[5].text
    ta = col[6].text
    gk = col[7].text
    f = col[8].text
    fk = col[9].text
    og = col[10].text

    defensive_data = defensive_data.append({'National selection':ns, 'Games Played':gp ,'Throw Ins':ti, 'Interceptions':ints, 'Tackles':tkl, 'Tackles Attempted':ta, 'Goal Kicks':gk, 'Fouls':f, 'Free Kicks':fk, 'Own Goals':og}, ignore_index=True)

defensive_data[defensive_data.columns] = defensive_data.apply(lambda x: x.str.strip())

defensive_data.iloc[:,1:] = defensive_data.iloc[:,1:].astype('int64')


# Scrap general data

# Web page to scrap global data

url3 = 'https://www.foxsports.com/soccer/fifa-world-cup-men/team-stats?category=standard&sort=t_g&season=2022&sortOrder=desc&groupId=12'

# Download the content

data3 = requests.get(url3).text

# Creation of the BeatifulSoup object
soup3 = BeautifulSoup(data3, 'html5lib')

# Find the html table in the web page
table = soup3.find('tbody').find_all('tr')

global_data = pd.DataFrame(columns= ['National selection','Games Played', 'Goals', 'Kicked Goals', 'Header Goals', 'Goals First Half', 'Goals Second Half', 'Goals Conceded', 'Goals Conceded First Half','Goals Conceded Second Half', 'Assists', 'Penalty Kicks', 'Penalty Kick Goals', 'Yellow Cards', 'Red Cards', 'Yellow Red Cards'])

for row in soup3.find('tbody').find_all('tr'):
    col = row.find_all("td")
    ns = col[1].text
    gp = col[2].text
    gf = col[3].text
    kg = col[4].text
    hg = col[5].text
    g1 = col[6].text
    g2 = col[7].text
    gc = col[8].text
    gc1 = col[9].text
    gc2 = col[10].text
    a = col[11].text
    pk = col[12].text
    pkg = col[13].text
    yc = col[14].text
    rc = col[15].text
    yrc = col[16].text


    global_data = global_data.append({'National selection':ns,'Games Played':gp, 'Goals':gf, 'Kicked Goals':kg, 'Header Goals':hg, 'Goals First Half':g1, 'Goals Second Half':g2, 'Goals Conceded':gc, 'Goals Conceded First Half':gc1,'Goals Conceded Second Half':gc2, 'Assists':a, 'Penalty Kicks':pk, 'Penalty Kick Goals':pkg, 'Yellow Cards':yc, 'Red Cards':rc, 'Yellow Red Cards':yrc}, ignore_index=True)

global_data[global_data.columns] = global_data.apply(lambda x: x.str.strip())

global_data.iloc[:,1:] = global_data.iloc[:,1:].astype('int64')


# Scrap goalkeeping data

# Web page to scrap goalkeeping data

url4 = 'https://www.foxsports.com/soccer/fifa-world-cup-men/team-stats?category=goalkeeping&sort=t_sv&season=2022&sortOrder=desc&groupId=12'

# Download the content

data4 = requests.get(url4).text

# Creation of the BeatifulSoup object
soup4 = BeautifulSoup(data4, 'html5lib')

# Find the html table in the web page
table = soup4.find('tbody').find_all('tr')

goalkeeping_data = pd.DataFrame(columns= ['National selection','Games Played', 'Goals Conceded', 'Shots', 'Shots On Goal', 'Saves', 'Clearances', 'Clean Sheets', 'Penalty Kicks','Penalty Kick Goals'])

for row in soup4.find('tbody').find_all('tr'):
    col = row.find_all("td")
    ns = col[1].text
    gp = col[2].text
    gc = col[3].text
    s = col[4].text
    sog = col[5].text
    sv = col[6].text
    clr = col[7].text
    cs = col[8].text
    pk = col[9].text
    pkg = col[10].text


    goalkeeping_data = goalkeeping_data.append({'National selection':ns,'Games Played':gp, 'Goals Conceded':gc, 'Shots':s, 'Shots On Goal':sog, 'Saves':sv, 'Clearances':clr, 'Clean Sheets':cs, 'Penalty Kicks':pk,'Penalty Kick Goals':pkg}, ignore_index=True)

goalkeeping_data[goalkeeping_data.columns] = goalkeeping_data.apply(lambda x: x.str.strip())

goalkeeping_data.iloc[:,1:] = goalkeeping_data.iloc[:,1:].astype('int64')


# Streamlit

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Row A
st.markdown('## FIFA World Cup Qatar 2022')
st.image(Image.open('logo.jpg'))


# Tab creation
tab_titles = ['Datos generales', 'Datos ofensivos', 'Datos defensivos', 'Datos de portería']

tabs = st.tabs(tab_titles)

# Sidebar
st.sidebar.header('Dashboard FIFA World Cup Qatar 2022')

st.sidebar.subheader('Datos Generales')
medida_general = st.sidebar.selectbox('Medidas a comparar por equipo:', global_data.columns[1:]) 

st.sidebar.subheader('Datos Ofensivos')
medida = st.sidebar.selectbox('Medidas a comparar por equipo:', offensive_data.columns[1:]) 

st.sidebar.subheader('Datos Defensivos')
medida_defensiva = st.sidebar.selectbox('Medidas a comparar por equipo:', defensive_data.columns[1:]) 

st.sidebar.subheader('Datos de portería')
medida_goalkeeping = st.sidebar.selectbox('Medidas a comparar por equipo:', goalkeeping_data.columns[1:])

st.sidebar.markdown('''
---
Created by Fabian Pedreros 

- [Portfolio](https://fabianpedreros.github.io/Portfolio/)
- [Linkedin ](https://www.linkedin.com/in/ing-fabian-pedreros/)
''')

# Tab de datos ofensivos
with tabs[1]:   


    st.markdown('### Datos ofensivos')


    cm = sns.light_palette("red", as_cmap = True)


    st.dataframe(offensive_data.style.background_gradient(cmap=cm))


    # Bar chart offensive data
    bar_chart = px.bar(offensive_data,
                        x = 'National selection',
                        y = medida,
                        text= medida,
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'Offensive variable (Total): {medida}')

    bar_chart.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})

    st.plotly_chart(bar_chart)


    # transform offensive data por partido
    offensive_data_pp = offensive_data.copy()
    offensive_data_pp.iloc[:,1:] = offensive_data_pp.iloc[:,1:].astype(int)

    # offensive_data_pp

    #offensive_data_pp.iloc[:,1:] = offensive_data_pp.iloc[:,1:].div(pd.Series([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]), axis = 'index')

    offensive_data_pp.iloc[:,1:] = offensive_data_pp.iloc[:,1:].div(pd.Series(offensive_data['Games Played'], index = offensive_data_pp.index), axis = 'index')

    offensive_data_pp['Possession Time Minutes Avg'] = offensive_data['Possession Time Minutes Avg']

    offensive_data_pp=offensive_data_pp.round(1)


    # Show offensive avg data table
    st.markdown('**Datos promedio**')
    st.dataframe(offensive_data_pp.style.background_gradient(cmap=cm))

    # Bar chart offensive data por partido
    bar_chart_o_pp = px.bar(offensive_data_pp,
                        x = 'National selection',
                        y = medida,
                        text= medida,
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'Offensive variable (Avg): {medida}')

    bar_chart_o_pp.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})

    st.plotly_chart(bar_chart_o_pp)

    # Scatter for related measures

    c1, c2 = st.columns(2)

    with c1:
        medida_o_pp_1 = st.selectbox('Medidas a comparar por equipo:', ['Shots', 'Crosses', 'Passes','Corner Kicks', 'Offsides']) 

    with c2:
        medida_o_pp_2 = st.selectbox('Medidas a comparar por equipo:', ['Shots On Goal', 'Shots On Post', 'Shots Off Target', 'Shot Attempts Blocked','Possession Time Minutes Avg', 'Crosses Successful', 'Pass Completions', 'Pass Attempts - Long','Pass Completions - Long'])

    scatter_o_pp = px.scatter(offensive_data_pp,
                        x = medida_o_pp_1,
                        y = medida_o_pp_2,
                        text= 'National selection',
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'Offensive variable (Avg):',
                        trendline='ols')

    scatter_o_pp.update_traces(marker={'size': 20})

    st.plotly_chart(scatter_o_pp)

    offensive_data_pp_t=offensive_data_pp.transpose()
    offensive_data_pp_t=offensive_data_pp_t.reset_index()
    offensive_data_pp_t.columns = offensive_data_pp_t.iloc[0]
    offensive_data_pp_t= offensive_data_pp_t.drop(offensive_data_pp_t.index[0])
    #offensive_data_pp_t

    st.markdown('#### Comparación entre selecciones (Avg)')

    # Variables for butterfly plot

    d1, d2 = st.columns(2)

    s1 = offensive_data_pp_t.columns[1:].sort_values(ascending = False)
    s2 = offensive_data_pp_t.columns[1:].sort_values(ascending = True)

    with d1:
        medida_o_pp_b1 = st.selectbox('Selección:', s1)

    with d2:
        medida_o_pp_b2 = st.selectbox('Selección:', s2)


    #Butterfly plot offensive data

    fig = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=False,
                        shared_yaxes=True, horizontal_spacing=0)

    fig.append_trace(go.Bar(x=offensive_data_pp_t[medida_o_pp_b1],
                        y=offensive_data_pp_t.iloc[:,0], 
                        text=offensive_data_pp_t[medida_o_pp_b1].map('{:,.1f}'.format), #Display the numbers with thousands separators in hover-over tooltip 
                        textposition='inside',
                        orientation='h', 
                        width=0.7, 
                        showlegend=False, 
                        marker_color='#686cfc'), 
                        1, 1) # 1,1 represents row 1 column 1 in the plot grid


    fig.append_trace(go.Bar(x=offensive_data_pp_t[medida_o_pp_b2],
                        y=offensive_data_pp_t.iloc[:,0], 
                        text=offensive_data_pp_t[medida_o_pp_b2].map('{:,.1f}'.format),
                        textposition='inside',
                        orientation='h', 
                        width=0.7, 
                        showlegend=False, 
                        marker_color='#f0543c'), 
                        1, 2) # 1,2 represents row 1 column 2 in the plot grid

    fig.update_xaxes(showticklabels=False,title_text=medida_o_pp_b1, row=1, col=1, range=[100,0])
    fig.update_xaxes(showticklabels=False,title_text=medida_o_pp_b2, row=1, col=2, range=[0,100])

    fig.update_layout(title_text="Comparación entre selecciones", 
                    width=800, 
                    height=700,
                    title_x=0.9,
                    xaxis1={'side': 'top'},
                    xaxis2={'side': 'top'},)

    st.plotly_chart(fig)



# Tab de datos generales
with tabs[0]:   

    st.markdown('### Datos generales')


    cm = sns.light_palette("red", as_cmap = True)


    st.dataframe(global_data.style.background_gradient(cmap=cm))


    # Bar chart global data
    bar_chart_g = px.bar(global_data,
                        x = 'National selection',
                        y = medida_general,
                        text= medida_general,
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'General variable (Total): {medida_general}')

    bar_chart_g.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})

    st.plotly_chart(bar_chart_g)


    # transform offensive data por partido
    global_data_pp = global_data.copy()
    global_data_pp.iloc[:,1:] = global_data_pp.iloc[:,1:].astype(int)

    # global_data_pp

    global_data_pp.iloc[:,1:] = global_data_pp.iloc[:,1:].div(pd.Series(global_data['Games Played'], index = global_data_pp.index), axis = 'index')

    global_data_pp=global_data_pp.round(1)


    # Show global avg data table
    st.markdown('**Datos promedio**')
    st.dataframe(global_data_pp.style.background_gradient(cmap=cm))

    # Bar chart global data por partido
    bar_chart_g_pp = px.bar(global_data_pp,
                        x = 'National selection',
                        y = medida_general,
                        text= medida_general,
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'General variable (Avg): {medida_general}')

    bar_chart_g_pp.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})

    st.plotly_chart(bar_chart_g_pp)

    # Scatter for related measures

    g1 = global_data_pp.columns[1:].sort_values(ascending = False)
    g2 = global_data_pp.columns[1:].sort_values(ascending = True)

    c1, c2 = st.columns(2)

    with c1:
        medida_g_pp_1 = st.selectbox('Medidas a comparar por equipo:', g1) 

    with c2:
        medida_g_pp_2 = st.selectbox('Medidas a comparar por equipo:', g2)

    scatter_g_pp = px.scatter(global_data_pp,
                        x = medida_g_pp_1,
                        y = medida_g_pp_2,
                        text= 'National selection',
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'General variable (Avg):',
                        trendline='ols')

    scatter_g_pp.update_traces(marker={'size': 20})

    st.plotly_chart(scatter_g_pp)

    global_data_pp_t=global_data_pp.transpose()
    global_data_pp_t=global_data_pp_t.reset_index()
    global_data_pp_t.columns = global_data_pp_t.iloc[0]
    global_data_pp_t= global_data_pp_t.drop(global_data_pp_t.index[0])
    #offensive_data_pp_t

    st.markdown('#### Comparación entre selecciones (Avg)')

    # Variables for butterfly plot

    d1, d2 = st.columns(2)

    with d1:
        medida_g_pp_b1 = st.selectbox('Selección:', [ 'Uruguay', 'Wales','United States', 'Tunisia', 'Switzerland', 'Spain',
       'South Korea', 'Serbia', 'Senegal', 'Saudi Arabia', 'Qatar', 'Portugal',
       'Poland', 'Netherlands', 'Morocco', 'Mexico', 'Japan', 'Iran', 'Ghana',
       'Germany', 'France', 'England', 'Ecuador', 'Denmark', 'Croatia',
       'Costa Rica', 'Canada', 'Cameroon', 'Brazil', 'Belgium', 'Australia',
       'Argentina'])

    with d2:
        medida_g_pp_b2 = st.selectbox('Selección:', ['Argentina', 'Australia', 'Belgium', 'Brazil', 'Cameroon', 'Canada',
       'Costa Rica', 'Croatia', 'Denmark', 'Ecuador', 'England', 'France',
       'Germany', 'Ghana', 'Iran', 'Japan', 'Mexico', 'Morocco', 'Netherlands',
       'Poland', 'Portugal', 'Qatar', 'Saudi Arabia', 'Senegal', 'Serbia',
       'South Korea', 'Spain', 'Switzerland', 'Tunisia', 'United States',
       'Wales', 'Uruguay'])


    #Butterfly plot offensive data

    fig_g = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=False,
                        shared_yaxes=True, horizontal_spacing=0)

    fig_g.append_trace(go.Bar(x=global_data_pp_t[medida_g_pp_b1],
                        y=global_data_pp_t.iloc[:,0], 
                        text=global_data_pp_t[medida_g_pp_b1].map('{:,.1f}'.format), 
                        textposition='inside',
                        orientation='h', 
                        width=0.7, 
                        showlegend=False, 
                        marker_color='#686cfc'), 
                        1, 1) 


    fig_g.append_trace(go.Bar(x=global_data_pp_t[medida_g_pp_b2],
                        y=global_data_pp_t.iloc[:,0], 
                        text=global_data_pp_t[medida_g_pp_b2].map('{:,.1f}'.format),
                        textposition='inside',
                        orientation='h', 
                        width=0.7, 
                        showlegend=False, 
                        marker_color='#f0543c'), 
                        1, 2) 

    fig_g.update_xaxes(showticklabels=False,title_text=medida_g_pp_b1, row=1, col=1, range=[4,0])
    fig_g.update_xaxes(showticklabels=False,title_text=medida_g_pp_b2, row=1, col=2, range=[0,4])

    fig_g.update_layout(title_text="Comparación entre selecciones", 
                    width=800, 
                    height=700,
                    title_x=0.9,
                    xaxis1={'side': 'top'},
                    xaxis2={'side': 'top'},)

    st.plotly_chart(fig_g)


# Tab de datos defensivos
with tabs[2]:   

    st.markdown('### Datos defensivos')


    cm = sns.light_palette("red", as_cmap = True)


    st.dataframe(defensive_data.style.background_gradient(cmap=cm))


    # Bar chart defensive data
    bar_chart_d = px.bar(defensive_data,
                        x = 'National selection',
                        y = medida_defensiva,
                        text= medida_defensiva,
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'Defensive variable (Total): {medida_defensiva}')

    bar_chart_d.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})

    st.plotly_chart(bar_chart_d)


    # transform defensive data por partido
    defensive_data_pp = defensive_data.copy()
    defensive_data_pp.iloc[:,1:] = defensive_data_pp.iloc[:,1:].astype(int)

    # global_data_pp

    defensive_data_pp.iloc[:,1:] = defensive_data_pp.iloc[:,1:].div(pd.Series(defensive_data['Games Played'], index = defensive_data_pp.index), axis = 'index')

    defensive_data_pp=defensive_data_pp.round(1)


    # Show defensive avg data table
    st.markdown('**Datos promedio**')
    st.dataframe(defensive_data_pp.style.background_gradient(cmap=cm))

    # Bar chart defensive data por partido
    bar_chart_d_pp = px.bar(defensive_data_pp,
                        x = 'National selection',
                        y = medida_defensiva,
                        text= medida_defensiva,
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'Defensive variable (Avg): {medida_defensiva}')

    bar_chart_d_pp.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})

    st.plotly_chart(bar_chart_d_pp)

    # Scatter for related measures

    de1 = defensive_data_pp.columns[1:].sort_values(ascending = False)
    de2 = defensive_data_pp.columns[1:].sort_values(ascending = True)

    c1, c2 = st.columns(2)

    with c1:
        medida_d_pp_1 = st.selectbox('Medidas a comparar por equipo:', de1) 

    with c2:
        medida_d_pp_2 = st.selectbox('Medidas a comparar por equipo:', de2)

    scatter_d_pp = px.scatter(defensive_data_pp,
                        x = medida_d_pp_1,
                        y = medida_d_pp_2,
                        text= 'National selection',
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'Defensive variable (Avg):',
                        trendline='ols')

    scatter_d_pp.update_traces(marker={'size': 20})

    st.plotly_chart(scatter_d_pp)

    defensive_data_pp_t=defensive_data_pp.transpose()
    defensive_data_pp_t=defensive_data_pp_t.reset_index()
    defensive_data_pp_t.columns = defensive_data_pp_t.iloc[0]
    defensive_data_pp_t= defensive_data_pp_t.drop(defensive_data_pp_t.index[0])
    #offensive_data_pp_t

    st.markdown('#### Comparación entre selecciones (Avg)')

    # Variables for butterfly plot

    d1, d2 = st.columns(2)

    with d1:
        medida_d_pp_b1 = st.selectbox('Selección:', [ 'Wales','Uruguay','United States', 'Tunisia', 'Switzerland', 'Spain',
       'South Korea', 'Serbia', 'Senegal', 'Saudi Arabia', 'Qatar', 'Portugal',
       'Poland', 'Netherlands', 'Morocco', 'Mexico', 'Japan', 'Iran', 'Ghana',
       'Germany', 'France', 'England', 'Ecuador', 'Denmark', 'Croatia',
       'Costa Rica', 'Canada', 'Cameroon', 'Belgium', 'Brazil',  'Australia',
       'Argentina'])

    with d2:
        medida_d_pp_b2 = st.selectbox('Selección:', ['Argentina', 'Australia', 'Brazil', 'Belgium',  'Cameroon', 'Canada',
       'Costa Rica', 'Croatia', 'Denmark', 'Ecuador', 'England', 'France',
       'Germany', 'Ghana', 'Iran', 'Japan', 'Mexico', 'Morocco', 'Netherlands',
       'Poland', 'Portugal', 'Qatar', 'Saudi Arabia', 'Senegal', 'Serbia',
       'South Korea', 'Spain', 'Switzerland', 'Tunisia', 'United States',
       'Uruguay','Wales' ])


    #Butterfly plot offensive data

    fig_d = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=False,
                        shared_yaxes=True, horizontal_spacing=0)

    fig_d.append_trace(go.Bar(x=defensive_data_pp_t[medida_d_pp_b1],
                        y=defensive_data_pp_t.iloc[:,0], 
                        text=defensive_data_pp_t[medida_d_pp_b1].map('{:,.1f}'.format), 
                        textposition='inside',
                        orientation='h', 
                        width=0.7, 
                        showlegend=False, 
                        marker_color='#686cfc'), 
                        1, 1) 


    fig_d.append_trace(go.Bar(x=defensive_data_pp_t[medida_d_pp_b2],
                        y=defensive_data_pp_t.iloc[:,0], 
                        text=defensive_data_pp_t[medida_d_pp_b2].map('{:,.1f}'.format),
                        textposition='inside',
                        orientation='h', 
                        width=0.7, 
                        showlegend=False, 
                        marker_color='#f0543c'), 
                        1, 2) 

    fig_d.update_xaxes(showticklabels=False,title_text=medida_d_pp_b1, row=1, col=1, range=[31,0])
    fig_d.update_xaxes(showticklabels=False,title_text=medida_d_pp_b2, row=1, col=2, range=[0,31])

    fig_d.update_layout(title_text="Comparación entre selecciones", 
                    width=800, 
                    height=700,
                    title_x=0.9,
                    xaxis1={'side': 'top'},
                    xaxis2={'side': 'top'},)

    st.plotly_chart(fig_d)


# Tab de datos de portería
with tabs[3]:   

    st.markdown('### Datos de portería')


    cm = sns.light_palette("red", as_cmap = True)


    st.dataframe(goalkeeping_data.style.background_gradient(cmap=cm))


    # Bar chart goalkeeping data
    bar_chart_gk = px.bar(goalkeeping_data,
                        x = 'National selection',
                        y = medida_goalkeeping,
                        text= medida_goalkeeping,
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'Goalkeeping variable (Total): {medida_goalkeeping}')

    bar_chart_gk.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})

    st.plotly_chart(bar_chart_gk)


    # transform goalkeeping data por partido
    goalkeeping_data_pp = goalkeeping_data.copy()
    goalkeeping_data_pp.iloc[:,1:] = goalkeeping_data_pp.iloc[:,1:].astype(int)

    # global_data_pp

    goalkeeping_data_pp.iloc[:,1:] = goalkeeping_data_pp.iloc[:,1:].div(pd.Series(goalkeeping_data['Games Played'], index = goalkeeping_data_pp.index), axis = 'index')

    goalkeeping_data_pp=goalkeeping_data_pp.round(1)


    # Show goalkeeping avg data table
    st.markdown('**Datos promedio**')
    st.dataframe(goalkeeping_data_pp.style.background_gradient(cmap=cm))

    # Bar chart goalkeeping data por partido
    bar_chart_gk_pp = px.bar(goalkeeping_data_pp,
                        x = 'National selection',
                        y = medida_goalkeeping,
                        text= medida_goalkeeping,
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'Goalkeeping variable (Avg): {medida_goalkeeping}')

    bar_chart_gk_pp.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})

    st.plotly_chart(bar_chart_gk_pp)

    # Scatter for related measures

    gk1 = goalkeeping_data_pp.columns[1:].sort_values(ascending = False)
    gk2 = goalkeeping_data_pp.columns[1:].sort_values(ascending = True)

    c1, c2 = st.columns(2)

    with c1:
        medida_gk_pp_1 = st.selectbox('Medidas a comparar por equipo:', gk1) 

    with c2:
        medida_gk_pp_2 = st.selectbox('Medidas a comparar por equipo:', gk2)

    scatter_gk_pp = px.scatter(goalkeeping_data_pp,
                        x = medida_gk_pp_1,
                        y = medida_gk_pp_2,
                        text= 'National selection',
                        template = 'plotly_white',
                        color = 'National selection',
                        width = 1000,
                        height= 600,
                        title = f'Goalkeeping variable (Avg):',
                        trendline='ols')

    scatter_gk_pp.update_traces(marker={'size': 20})

    st.plotly_chart(scatter_gk_pp)

    goalkeeping_data_pp_t=goalkeeping_data_pp.transpose()
    goalkeeping_data_pp_t=goalkeeping_data_pp_t.reset_index()
    goalkeeping_data_pp_t.columns = goalkeeping_data_pp_t.iloc[0]
    goalkeeping_data_pp_t= goalkeeping_data_pp_t.drop(goalkeeping_data_pp_t.index[0])
    #offensive_data_pp_t

    st.markdown('#### Comparación entre selecciones (Avg)')

    # Variables for butterfly plot

    d1, d2 = st.columns(2)

    with d1:
        medida_gk_pp_b1 = st.selectbox('Selección:', [ 'Uruguay','Wales','United States', 'Tunisia', 'Switzerland', 'Spain',
       'South Korea', 'Serbia', 'Senegal', 'Saudi Arabia', 'Qatar', 'Portugal',
       'Poland', 'Netherlands', 'Morocco', 'Mexico', 'Japan', 'Iran', 'Ghana',
       'Germany', 'France', 'England', 'Ecuador', 'Denmark', 'Croatia',
       'Costa Rica', 'Canada', 'Cameroon', 'Belgium', 'Brazil',  'Australia',
       'Argentina'])

    with d2:
        medida_gk_pp_b2 = st.selectbox('Selección:', ['Argentina', 'Australia', 'Brazil', 'Belgium',  'Cameroon', 'Canada',
       'Costa Rica', 'Croatia', 'Denmark', 'Ecuador', 'England', 'France',
       'Germany', 'Ghana', 'Iran', 'Japan', 'Mexico', 'Morocco', 'Netherlands',
       'Poland', 'Portugal', 'Qatar', 'Saudi Arabia', 'Senegal', 'Serbia',
       'South Korea', 'Spain', 'Switzerland', 'Tunisia', 'United States',
       'Wales','Uruguay'])


    #Butterfly plot goalkeeping data

    fig_gk = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=False,
                        shared_yaxes=True, horizontal_spacing=0)

    fig_gk.append_trace(go.Bar(x=goalkeeping_data_pp_t[medida_gk_pp_b1],
                        y=goalkeeping_data_pp_t.iloc[:,0], 
                        text=goalkeeping_data_pp_t[medida_gk_pp_b1].map('{:,.1f}'.format), 
                        textposition='inside',
                        orientation='h', 
                        width=0.7, 
                        showlegend=False, 
                        marker_color='#686cfc'), 
                        1, 1) 


    fig_gk.append_trace(go.Bar(x=goalkeeping_data_pp_t[medida_gk_pp_b2],
                        y=goalkeeping_data_pp_t.iloc[:,0], 
                        text=goalkeeping_data_pp_t[medida_gk_pp_b2].map('{:,.1f}'.format),
                        textposition='inside',
                        orientation='h', 
                        width=0.7, 
                        showlegend=False, 
                        marker_color='#f0543c'), 
                        1, 2) 

    fig_gk.update_xaxes(showticklabels=False,title_text=medida_gk_pp_b1, row=1, col=1, range=[11,0])
    fig_gk.update_xaxes(showticklabels=False,title_text=medida_gk_pp_b2, row=1, col=2, range=[0,11])

    fig_gk.update_layout(title_text="Comparación entre selecciones", 
                    width=800, 
                    height=700,
                    title_x=0.9,
                    xaxis1={'side': 'top'},
                    xaxis2={'side': 'top'},)

    st.plotly_chart(fig_gk)
