import pickle
import streamlit as st
import locale
import time

model = pickle.load(open('prediksi_hargamobil.sav', 'rb'))

st.title('Aplikasi Prediksi Harga Mobil Bekas')

st.image('mobil.png', use_column_width=True)

year = st.number_input('Input Tahun Keluaran Mobil')
mileage = st.number_input('Input Jarak Tempuh Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size Mobil')

predict = ' '

# Set the locale to 'id' (Indonesian) if available, else set fallback to 'id_ID'
try:
    locale.setlocale(locale.LC_ALL, 'id')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'id_ID')
    except locale.Error:
        st.warning("Locale 'id' and 'id_ID' are not available. Number formatting may not be in Indonesian style.")

if st.button('Prediksi Harga Mobil Bekas', key='predict_button'):
    if year == 0 or mileage == 0 or tax == 0 or mpg == 0 or engineSize == 0:
        st.warning("Input data terlebih dahulu")
    else:
        with st.empty():
            st.info("Sedang memproses prediksi...")
            with st.spinner():
                time.sleep(2)
            st.success("Selesai!")
            time.sleep(1)

        predict = model.predict([[year, mileage, tax, mpg, engineSize]])
        predicted_price_in_rupiah = predict * 16741

        st.write('Prediksi Harga Mobil Bekas dalam EURO adalah', predict)
        st.write('Prediksi Harga Mobil Bekas dalam Rupiah adalah', predicted_price_in_rupiah)

        formatted_price = "{:,.0f}".format(predicted_price_in_rupiah)
        st.success(f"Kesimpulan: Harga mobil bekas berdasarkan data di atas adalah Rp {formatted_price}.")

st.image('mobil.png', use_column_width=True)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpapertag.com/wallpaper/middle/8/0/1/350871-website-background-1920x1200-high-resolution.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
