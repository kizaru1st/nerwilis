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
st.title('🌍 Pengeluaran Per Kapita (2018 - 2021)')

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
sheet_uhh = 'UHH'
sheet_rls = 'RLS'
sheet_hls = 'HLS'
sheet_perkapita = 'Perkapita'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_perkapita,
                   usecols='A:F',
                   header=0)
df_participants = pd.read_excel(excel_file,
                                sheet_name=sheet_perkapita,
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
    todf = pd.read_excel('Neraca.xlsx', sheet_name='Perkapita')
    to = todf[(todf['Kabupaten/Kota'] == provinsi_selection)]

    # ===== delta =====
    deltaResult = int(to['Tahun 2021']) - int(to['Tahun 2020'])
    format_int = "{:,.2f}".format(deltaResult)
    deltaFormat = format_int + "%"

    # ===== rata-rata 3 tahun =====
    tigaTahun = df["Tahun 2021"].mean()
    formatTigaTahun = "{:,.2f}".format(tigaTahun)

    m1.metric(label='Tahun 2021', value=int(
        to['Tahun 2021']), delta=deltaFormat)
    m2.metric(label='Rata-Rata 4 Tahun Terakhir',
              value=int(to['Rata2']))
    m3.metric(label='Rata-Rata Pengeluaran Per Kapita di seluruh Kota/Kabupaten 2021',
              value=formatTigaTahun)

