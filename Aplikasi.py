import pickle
import streamlit as st
import time

model = pickle.load(open('prediksi_hargamobil.sav', 'rb'))

st.title('Aplikasi Prediksi Harga Mobil Bekas')

st.image('mobil.png', use_column_width=True)

year = st.number_input('Input Tahun Keluaran Mobil', min_value=0, step=1, format="%d")
mileage = st.number_input('Input Jarak Tempuh Mobil (Kilometer)')
tax = st.number_input('Input Biaya Pajak Mobil (Euro)')
mpg = st.number_input('Input Konsumsi BBM Mobil (Liter)')
engineSize = st.number_input('Input Engine Size Mobil')

predict = ' '

def format_number_with_dots(number):
    # Convert the number to an integer to remove decimal digits
    integer_value = int(number)
    # Format the integer with dots as a thousands separator
    return "{:,}".format(integer_value).replace(",", ".")

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
        predicted_price_in_rupiah = predict[0] * 16741  # Assuming predict is a 1D array with a single value

        st.write('Prediksi Harga Mobil Bekas dalam EURO adalah', format_number_with_dots(predict[0]))
        st.write('Prediksi Harga Mobil Bekas dalam Rupiah adalah', format_number_with_dots(predicted_price_in_rupiah))

        formatted_price = format_number_with_dots(predicted_price_in_rupiah)
        st.success(f"Kesimpulan: Harga mobil bekas berdasarkan data di atas adalah Rp {formatted_price}.")
        st.snow()

st.image('mobil.png', use_column_width=True)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cutewallpaper.org/27/blue-black-hd-high-res-wallpaper/170426645.jpg");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
