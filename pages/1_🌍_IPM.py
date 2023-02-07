# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import matplotlib.pyplot as plt
import numpy as np
import sys

st.set_page_config(page_title='Dashboard Nerwillis',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌍 IPM (2018 - 2021)')

# ===== Setting =====
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ===== Use Column in excel =====
excel_file = 'Neraca.xlsx'
sheet_name = 'IPM'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:G',
                   header=0)
df_participants = pd.read_excel(excel_file,
                                sheet_name=sheet_name,
                                usecols='A:B')
df_participants.dropna(inplace=True)

# ===== Dropdown in Sidebar =====
option = st.sidebar.selectbox(
    'Filter',
    ('All', 'Provinsi'))

if(option == 'All'):
    # ===== STREAMLIT SELECTION =====
    provinsi = df['Kabupaten/Kota'].unique().tolist()
    provinsi_selection = st.multiselect('Provinsi:',
                                        provinsi,
                                        default=provinsi)

    # Selected option
    if len(provinsi_selection) == 0 or len(provinsi_selection) == 1:
        st.warning('Pilih 2 Provinsi atau lebih untuk membandingkan.')

    else:
        st.write("ALL")

elif(option == 'Provinsi'):
    provinsi = df['Kabupaten/Kota'].unique().tolist()
    provinsi_selection = st.selectbox('Pilih Provinsi : ', provinsi)
    m1, m2, m3 = st.columns((1, 1, 1))
    todf = pd.read_excel('Neraca.xlsx', sheet_name='IPM')
    to = todf[(todf['Kabupaten/Kota'] == provinsi_selection)]

    # ===== delta =====
    deltaResult = float(to['Tahun 2021']) - float(to['Tahun 2020'])
    format_float = "{:,.2f}".format(deltaResult)
    deltaFormat = format_float + "%"

    # ===== rata-rata 3 tahun =====
    tigaTahun = df["Tahun 2021"].mean()
    formatTigaTahun = "{:,.2f}".format(tigaTahun)

    m1.metric(label='Tahun 2021', value=float(
        to['Tahun 2021'].map('{:,.2f}'.format)), delta=deltaFormat)
    m2.metric(label='Rata-Rata 4 Tahun Terakhir',
              value=float(to['Rata2'].map('{:,.2f}'.format)))
    m3.metric(label='Rata-Rata IPM di seluruh Kota/Kabupaten',
              value=formatTigaTahun)

    # ----- MANIPULATION -----
    # ===== List for Years =====
    yearList = []
    for i in range(2018, 2022):
        yearList.append(i)

    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesIPM = []
    list_from_df = single_row_df.values.tolist()[0]
    for i in range(1, 5):
        listValuesIPM.append(list_from_df[i])
    # ----- END OF MANIPULATION -----

    # ===== Show Bar Chart =====
    provinsi_IPM = pd.DataFrame({
        'IPM': listValuesIPM
    }, index=['2018', '2019', '2020', '2021'])

    st.line_chart(provinsi_IPM,  y='IPM', use_container_width=True)


