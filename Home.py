#Libraries
import streamlit as st

st.set_page_config(page_title='Dashboard Nerwillis', page_icon=':bar_chart:', layout='wide')

# Setting
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Layout
st.title('⭐ IPM Provinsi Sumatera Barat')

st.subheader('Overview')
st.write(
    """
    IPM Adalah
    """
)

st.subheader('Methodology')
st.write(
    """
    Pureshare
    """
)