# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import altair as alt

st.set_page_config(page_title='Dashboard Nerwillis',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌍 IPM (2018 - 2021)')

# ===== Setting =====
hide_streamlit_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ===== Use Column in excel =====
excel_file = 'Neraca.xlsx'
nasional_excel = 'IPM Nasional.xlsx'
sheet_name = 'IPM'
nasional_sheet = 'Provinsi'
wilayah_sheet = 'Pembagian'
barat_sheet = 'IDN Barat'
tengah_sheet = 'IDN Tengah'
timur_sheet = 'IDN Timur'

# Sumatera Barat
df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:G',
                   header=0)

df_multi = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:E',
                   header=0)

df_participants = pd.read_excel(excel_file,
                                sheet_name=sheet_name,
                                usecols='A:B')
df_participants.dropna(inplace=True)

# Nasional
df_nasional = pd.read_excel(nasional_excel,
                   sheet_name=nasional_sheet,
                   usecols='A:G',
                   header=0)

df_multi_nasional = pd.read_excel(nasional_excel,
                   sheet_name=nasional_sheet,
                   usecols='A:E',
                   header=0)

df_participants_nasional = pd.read_excel(nasional_excel,
                                sheet_name=nasional_sheet,
                                usecols='A:B')
df_participants_nasional.dropna(inplace=True)

# Pembagian Wilayah
df_wilayah = pd.read_excel(nasional_excel,
                   sheet_name=wilayah_sheet,
                   usecols='A:G',
                   header=0)

df_multi_wilayah = pd.read_excel(nasional_excel,
                   sheet_name=wilayah_sheet,
                   usecols='A:E',
                   header=0)

df_participants_wilayah = pd.read_excel(nasional_excel,
                                sheet_name=wilayah_sheet,
                                usecols='A:B')
df_participants_wilayah.dropna(inplace=True)

# IDN Barat
df_barat = pd.read_excel(nasional_excel,
                   sheet_name=barat_sheet,
                   usecols='A:G',
                   header=0)

df_multi_barat = pd.read_excel(nasional_excel,
                   sheet_name=barat_sheet,
                   usecols='A:E',
                   header=0)

df_participants_barat = pd.read_excel(nasional_excel,
                                sheet_name=barat_sheet,
                                usecols='A:B')
df_participants_barat.dropna(inplace=True)

# IDN Tengah
df_tengah = pd.read_excel(nasional_excel,
                   sheet_name=tengah_sheet,
                   usecols='A:G',
                   header=0)

df_multi_tengah = pd.read_excel(nasional_excel,
                   sheet_name=tengah_sheet,
                   usecols='A:E',
                   header=0)

df_participants_tengah = pd.read_excel(nasional_excel,
                                sheet_name=tengah_sheet,
                                usecols='A:B')
df_participants_tengah.dropna(inplace=True)

# IDN Timur
df_timur = pd.read_excel(nasional_excel,
                   sheet_name=timur_sheet,
                   usecols='A:G',
                   header=0)

df_multi_timur = pd.read_excel(nasional_excel,
                   sheet_name=timur_sheet,
                   usecols='A:E',
                   header=0)

df_participants_timur = pd.read_excel(nasional_excel,
                                sheet_name=timur_sheet,
                                usecols='A:B')
df_participants_timur.dropna(inplace=True)

# ===== Dropdown in Sidebar =====
option = st.sidebar.selectbox(
    'Filter',
    ('Sumbar', 'Kabupaten/Kota', 'Nasional', 'Nasional Provinsi', 'Wilayah Indonesia', 'Indonesia Barat', 'Indonesia Tengah', 'Indonesia Timur'))

# ===== SUMATERA BARAT =====
if(option == 'Sumbar'):
    # ===== STREAMLIT SELECTION =====
    # provinsi = df['Kabupaten/Kota'].unique().tolist()
    provinsi = df_multi['Kabupaten/Kota'].unique()
    provinsi_selection = st.multiselect('Kabupaten/Kota:',
                                        provinsi,
                                        default=provinsi)

    # Selected option
    if len(provinsi_selection) == 0 or len(provinsi_selection) == 1:
        st.warning('Pilih 2 Provinsi atau lebih untuk membandingkan.')

    else:
        if(provinsi_selection):
            filter_provinsi_df = df_multi[df_multi['Kabupaten/Kota'].isin(
                provinsi_selection)]
            
            st.subheader('Tahun 2018')
            fig1 = px.bar(filter_provinsi_df, x='Kabupaten/Kota', y='Tahun 2018', color='Kabupaten/Kota', range_y=[60,90])
            fig1.update_layout(width=800)
            st.write(fig1)

            st.subheader('Tahun 2019')
            fig2 = px.bar(filter_provinsi_df, x='Kabupaten/Kota', y='Tahun 2020', color='Kabupaten/Kota', range_y=[60,90])
            fig2.update_layout(width=800)
            st.write(fig2)

            st.subheader('Tahun 2020')
            fig3 = px.bar(filter_provinsi_df, x='Kabupaten/Kota', y='Tahun 2019', color='Kabupaten/Kota', range_y=[60,90])
            fig3.update_layout(width=800)
            st.write(fig3)

            st.subheader('Tahun 2021')
            fig4 = px.bar(filter_provinsi_df, x='Kabupaten/Kota', y='Tahun 2021', color='Kabupaten/Kota', range_y=[60,90])
            fig4.update_layout(width=800)
            st.write(fig4)  

# ===== KABUPATEN / KOTA =====
elif(option == 'Kabupaten/Kota'):
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
    m3.metric(label='Rata-Rata IPM di seluruh Kota/Kabupaten 2021',
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
        'IPM': listValuesIPM,
    }, index=['2018', '2019', '2020', '2021'])
    st.line_chart(provinsi_IPM,  y='IPM', use_container_width=True)

# ===== NASIONAL =====
elif(option == 'Nasional Provinsi'):
    nasional = df_nasional['Provinsi'].unique().tolist()
    nasional_selection = st.selectbox('Pilih nasional : ', nasional)
    m1, m2, m3 = st.columns((1, 1, 1))
    todf = pd.read_excel('IPM Nasional.xlsx', sheet_name='Provinsi')
    to = todf[(todf['Provinsi'] == nasional_selection)]

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
    m3.metric(label='Rata-Rata IPM di seluruh Provinsi 2021',
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
        'IPM': listValuesIPM,
    }, index=['2018', '2019', '2020', '2021'])
    st.line_chart(provinsi_IPM,  y='IPM', use_container_width=True)

elif(option == 'Nasional'):
    nasional = df_multi_nasional['Provinsi'].unique()
    nasional_selection = st.multiselect('Provinsi:',
                                        nasional,
                                        default=nasional)

    # Selected option
    if len(nasional_selection) == 0 or len(nasional_selection) == 1:
        st.warning('Pilih 2 Provinsi atau lebih untuk membandingkan.')
    else:
        if(nasional_selection):
                filter_nasional_df = df_multi_nasional[df_multi_nasional['Provinsi'].isin(
                    nasional_selection)]

                st.subheader('Tahun 2018')
                fig1 = px.bar(filter_nasional_df, x='Provinsi', y='Tahun 2018', color='Provinsi', range_y=[60,90])
                fig1.update_layout(width=800)
                st.write(fig1)

                st.subheader('Tahun 2019')
                fig2 = px.bar(filter_nasional_df, x='Provinsi', y='Tahun 2020', color='Provinsi', range_y=[60,90])
                fig2.update_layout(width=800)
                st.write(fig2)              

                st.subheader('Tahun 2020')
                fig3 = px.bar(filter_nasional_df, x='Provinsi', y='Tahun 2019', color='Provinsi', range_y=[60,90])
                fig3.update_layout(width=800)
                st.write(fig3)

                st.subheader('Tahun 2021')
                fig4 = px.bar(filter_nasional_df, x='Provinsi', y='Tahun 2021', color='Provinsi', range_y=[60,90])
                fig4.update_layout(width=800)
                st.write(fig4)

elif(option == 'Wilayah Indonesia'):
    nasional = df_multi_wilayah['Pembagian'].unique()
    nasional_selection = st.multiselect('Pembagian Wilayah:',
                                        nasional,
                                        default=nasional)

    # Selected option
    if len(nasional_selection) == 0 or len(nasional_selection) == 1:
        st.warning('Pilih 2 Pembagian Wilayah atau lebih untuk membandingkan.')
    else:
        if(nasional_selection):
                filter_wilayah_df = df_multi_wilayah[df_multi_wilayah['Pembagian'].isin(
                    nasional_selection)]
                c1, c2 = st.columns(2)

                with c1:
                    st.subheader('Tahun 2018')
                    fig1 = px.bar(filter_wilayah_df, x='Pembagian', y='Tahun 2018', color='Pembagian', range_y=[60,80])
                    fig1.update_layout(width=500)
                    st.write(fig1)

                    st.subheader('Tahun 2020')
                    fig3 = px.bar(filter_wilayah_df, x='Pembagian', y='Tahun 2019', color='Pembagian', range_y=[60,80])
                    fig3.update_layout(width=500)
                    st.write(fig3)
                with c2:
                    st.subheader('Tahun 2019')
                    fig2 = px.bar(filter_wilayah_df, x='Pembagian', y='Tahun 2020', color='Pembagian', range_y=[60,80])
                    fig2.update_layout(width=500)
                    st.write(fig2)              

                    st.subheader('Tahun 2021')
                    fig4 = px.bar(filter_wilayah_df, x='Pembagian', y='Tahun 2021', color='Pembagian', range_y=[60,80])
                    fig4.update_layout(width=500)
                    st.write(fig4)

elif(option == 'Indonesia Barat'):
    nasional = df_barat['Provinsi'].unique().tolist()
    nasional_selection = st.selectbox('Pilih Provinsi : ', nasional)
    m1, m2, m3 = st.columns((1, 1, 1))
    todf = pd.read_excel('IPM Nasional.xlsx', sheet_name='IDN Barat')
    to = todf[(todf['Provinsi'] == nasional_selection)]

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
    m3.metric(label='Rata-Rata IPM di seluruh Provinsi 2021',
              value=formatTigaTahun)

    wilayah_barat = df_multi_barat
    st.subheader('Tahun 2018')
    fig1 = px.bar(wilayah_barat, x='Provinsi', y='Tahun 2018', color='Provinsi', range_y=[60,90])
    fig1.update_layout(width=800)
    st.write(fig1)

    st.subheader('Tahun 2019')
    fig2 = px.bar(wilayah_barat, x='Provinsi', y='Tahun 2020', color='Provinsi', range_y=[60,90])
    fig2.update_layout(width=800)
    st.write(fig2)              

    st.subheader('Tahun 2020')
    fig3 = px.bar(wilayah_barat, x='Provinsi', y='Tahun 2019', color='Provinsi', range_y=[60,90])
    fig3.update_layout(width=800)
    st.write(fig3)

    st.subheader('Tahun 2021')
    fig4 = px.bar(wilayah_barat, x='Provinsi', y='Tahun 2021', color='Provinsi', range_y=[60,90])
    fig4.update_layout(width=800)
    st.write(fig4)

elif(option == 'Indonesia Tengah'):
    nasional = df_tengah['Provinsi'].unique().tolist()
    nasional_selection = st.selectbox('Pilih Provinsi : ', nasional)
    m1, m2, m3 = st.columns((1, 1, 1))
    todf = pd.read_excel('IPM Nasional.xlsx', sheet_name='IDN Tengah')
    to = todf[(todf['Provinsi'] == nasional_selection)]

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
    m3.metric(label='Rata-Rata IPM di seluruh Provinsi 2021',
              value=formatTigaTahun)

    wilayah_tengah = df_multi_tengah
    st.subheader('Tahun 2018')
    fig1 = px.bar(wilayah_tengah, x='Provinsi', y='Tahun 2018', color='Provinsi', range_y=[60,90])
    fig1.update_layout(width=800)
    st.write(fig1)

    st.subheader('Tahun 2019')
    fig2 = px.bar(wilayah_tengah, x='Provinsi', y='Tahun 2020', color='Provinsi', range_y=[60,90])
    fig2.update_layout(width=800)
    st.write(fig2)              

    st.subheader('Tahun 2020')
    fig3 = px.bar(wilayah_tengah, x='Provinsi', y='Tahun 2019', color='Provinsi', range_y=[60,90])
    fig3.update_layout(width=800)
    st.write(fig3)

    st.subheader('Tahun 2021')
    fig4 = px.bar(wilayah_tengah, x='Provinsi', y='Tahun 2021', color='Provinsi', range_y=[60,90])
    fig4.update_layout(width=800)
    st.write(fig4)

elif(option == 'Indonesia Timur'):
    nasional = df_timur['Provinsi'].unique().tolist()
    nasional_selection = st.selectbox('Pilih Provinsi : ', nasional)
    m1, m2, m3 = st.columns((1, 1, 1))
    todf = pd.read_excel('IPM Nasional.xlsx', sheet_name='IDN Timur')
    to = todf[(todf['Provinsi'] == nasional_selection)]

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
    m3.metric(label='Rata-Rata IPM di seluruh Provinsi 2021',
              value=formatTigaTahun)

    wilayah_timur = df_multi_timur
    st.subheader('Tahun 2018')
    fig1 = px.bar(wilayah_timur, x='Provinsi', y='Tahun 2018', color='Provinsi', range_y=[60,90])
    fig1.update_layout(width=800)
    st.write(fig1)

    st.subheader('Tahun 2019')
    fig2 = px.bar(wilayah_timur, x='Provinsi', y='Tahun 2020', color='Provinsi', range_y=[60,90])
    fig2.update_layout(width=800)
    st.write(fig2)              

    st.subheader('Tahun 2020')
    fig3 = px.bar(wilayah_timur, x='Provinsi', y='Tahun 2019', color='Provinsi', range_y=[60,90])
    fig3.update_layout(width=800)
    st.write(fig3)

    st.subheader('Tahun 2021')
    fig4 = px.bar(wilayah_timur, x='Provinsi', y='Tahun 2021', color='Provinsi', range_y=[60,90])
    fig4.update_layout(width=800)
    st.write(fig4)
    
