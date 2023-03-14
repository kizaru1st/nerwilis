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
    Indeks Pembangunan Manusia (IPM) menjelaskan bagaimana penduduk dapat mengakses hasil pembangunan dalam memperoleh pendapatan, kesehatan, pendidikan, dan sebagainya.
    Dimana tujuan utama dari pembangunan adalah menciptakan lingkungan yang memungkinkan bagi rakyatnya untuk menikmati umur panjang, sehat, dan  menjalankan kehidupan yang produktif.
    Pada Indeks Pembangunan Manusia terdapat beberapa indikator pembangun, seperti : 
    1. Umur Harapan Hidup
        UHH dapat didefinisikan sebagai rata-rata jumlah tahun yang dijalani oleh seseorang setelah orang tersebut mencapai ulang tahun yang ke-x.
    2. Rata-rata Lama Sekolah
        Rata-Rata Lama Sekolah Adalah Rata-rata jumlah tahun yang dihabiskan oleh penduduk berusia 15 tahun ke atas untuk menempuh semua jenis pendidikan yang pernah dijalani.
    3. Harapan Lama Sekolah
        Angka Harapan Lama Sekolah (HLS) didefinisikan sebagai lamanya sekolah (dalam tahun) yang diharapkan akan dirasakan oleh anak pada umur tertentu di masa mendatang.
    4. Pengeluaran Per Kapita yang Disesuaikan
        Pengeluaran per kapita adalah biaya yang dikeluarkan untuk konsumsi semua anggota rumah tangga.
    
    Terdapat tiga dimensi dalam indeks pembangunan manusia :
    1. Kesehatan dengan angka harapan hidup atau umur harapan hidup (UHH) sebagai tolak ukurnya.
    2. Pengetahuan yang dibagi menjadi dua indikator, yaitu harapan lama sekolah (HLS) dan rata-rata lama sekolah (RLS)
    3. Standar hidup layak yang diukur berdasarkan pengeluaran per kapita yang disesuaikan
        


    """
)

