#Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import subprocess
import sys
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Dashboard Nerwillis', page_icon=':bar_chart:', layout='wide')
st.title('🌍 IPM')

# Setting
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Filter years
excel_file = 'Neraca.xlsx'
sheet_name = 'IPM'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:G',
                   header=0)
df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name,
                                usecols='A:B')
df_participants.dropna(inplace=True)

# --- STREAMLIT SELECTION
provinsi = df['Kabupaten/Kota'].unique().tolist()
department_selection = st.multiselect('Department:',
                                    provinsi,
                                    default=provinsi)