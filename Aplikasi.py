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

predict = None

locale.setlocale(locale.LC_ALL, 'id_ID')

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

        try:
            predict = model.predict([[year, mileage, tax, mpg, engineSize]])
            predicted_price_in_rupiah = predict[0] * 19000

            st.write('Prediksi Harga Mobil Bekas dalam EURO adalah', predict[0])
            st.write('Prediksi Harga Mobil Bekas dalam Rupiah adalah', predicted_price_in_rupiah)

            formatted_price = locale.format_string("%.0f", predicted_price_in_rupiah, grouping=True)
            st.success(f"Kesimpulan: Harga mobil bekas berdasarkan data di atas adalah Rp {formatted_price}.")
        except Exception as e:
            st.error("Terjadi kesalahan saat melakukan prediksi.")
            st.error(f"Detail error: {e}")
