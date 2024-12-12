import streamlit as st
import joblib
import pandas as pd
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), '../model/model_svr_jeruk.pkl')
model = joblib.load(model_path)

# Judul aplikasi
st.title("Prediksi Kualitas Jeruk")

# Form input menggunakan Streamlit
st.sidebar.header("Masukkan Data Jeruk")
size = st.sidebar.number_input("Size(cm)", min_value=0.0, step=0.01)
weight = st.sidebar.number_input("Weight(g)", min_value=0, step=10)
brix = st.sidebar.number_input("Brix(Sweetness)", min_value=0.0, step=0.01)
ph = st.sidebar.number_input("Ph(Acidity)", min_value=0.0, step=0.01)
softness = st.sidebar.number_input("Softness(1-5)", min_value=1, step=1, max_value=5)
harvest_time = st.sidebar.number_input("Harvest Time(days)", min_value=0, step=1)
ripeness = st.sidebar.number_input("Ripeness(1-5)", min_value=1, step=1, max_value=5)

# Dropdown untuk input color, variety, dan blemishes
color = st.sidebar.selectbox(
    "Color",
    options=['Deep Orange', 'Light Orange', 'Orange-Red', 'Orange', 'Yellow-Orange']
)

variety = st.sidebar.selectbox(
    "Variety",
    options=[
        'Valencia', 'Navel', 'Cara Cara', 'Blood Orange', 'Hamlin',
        'Tangelo (Hybrid)', 'Murcott (Hybrid)', 'Moro (Blood)', 'Jaffa',
        'Clementine', 'Washington Navel', 'Star Ruby', 'Tangerine',
        'Ambiance', 'California Valencia', 'Honey Tangerine',
        'Navel (Late Season)', 'Clementine (Seedless)', 'Temple',
        'Minneola (Hybrid)', 'Satsuma Mandarin', 'Midsweet (Hybrid)',
        'Navel (Early Season)', 'Ortanique (Hybrid)'
    ]
)

blemishes = st.sidebar.selectbox(
    "Blemishes",
    options=[
        'N', 'Y (Minor)', 'Y (Sunburn)', 'Y (Mold Spot)', 'Y (Bruise)',
        'Y (Split Skin)', 'Y (Sunburn Patch)', 'Y (Scars)',
        'Y (Minor Insect Damage)', 'Y (Bruising)', 'N (Minor)',
        'N (Split Skin)'
    ]
)

# Tombol untuk prediksi
if st.sidebar.button("Prediksi"):
    # Data input dalam format DataFrame
    input_data = pd.DataFrame([{
        "size": size,
        "weight": weight,
        "brix": brix,
        "ph": ph,
        "softness": softness,
        "harvestTime": harvest_time,
        "ripeness": ripeness,
        "color": color,
        "variety": variety,
        "blemishes": blemishes
    }])

    # Prediksi menggunakan model
    try:
        prediction = model.predict(input_data)
        result = round(prediction[0], 2)
        st.success(f"Prediksi Kualitas Jeruk: ⭐ {result}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.info("Masukkan data di Sidebar dan tekan tombol Prediksi.")
