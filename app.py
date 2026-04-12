import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time

# ----- SETUP HALAMAN -----
st.set_page_config(
    page_title="Sistem Prediksi Lalu Lintas",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ----- CUSTOM CSS (Premium & Profesional UI) -----
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    
    /* Tombol Utama */
    .stButton>button {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        font-weight: 600;
        font-size: 1.1rem;
        border: none;
        width: 100%;
        transition: 0.2s all ease-in-out;
    }
    .stButton>button:hover {
        background-color: #1D4ED8;
    }
    
    /* Kotak Hasil Prediksi */
    .predicted-box {
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-top: 25px;
        border: 1px solid #E5E7EB;
    }
    </style>
""", unsafe_allow_html=True)

# ----- LOAD MODEL & SCALER -----
@st.cache_resource
def load_assets():
    model = joblib.load('best_traffic_model.pkl')
    scaler = joblib.load('traffic_scaler.pkl')
    feature_order = joblib.load('feature_order.pkl')  # 🔥 TAMBAHAN

    try:
        label_map = joblib.load('label_map.pkl')
    except:
        label_map = {0: '0: Macet Ekstrem', 1: '1: Padat', 2: '2: Normal', 3: '3: Lancar', 4: '4: Sangat Lancar'}

    return model, scaler, label_map, feature_order

try:
    model, scaler, label_map, feature_order = load_assets()
except Exception as e:
    st.error("Gagal memuat model. Pastikan file best_traffic_model.pkl dan traffic_scaler.pkl berada di folder yang sama.")
    st.stop()

# ----- HEADER -----
st.title("Sistem Monitoring Lalu Lintas")
st.markdown("Aplikasi pintar berbasis Machine Learning untuk memprediksi tingkat kemacetan lalu lintas secara real-time berdasarkan volume dan kecepatan kendaraan.")
st.markdown("---")

# ----- FORM PARAMETER LALU LINTAS -----
st.markdown("### Parameter Jalan Saat Ini")

col1, col2 = st.columns(2)

with col1:
    junction = st.selectbox("ID Persimpangan", [1, 2, 3, 4], help="Pilih nomor jalur persimpangan jalan.")
    hour = st.slider("Jam Pengamatan", min_value=0, max_value=23, value=17, help="Format 24 jam (misal: 17 berarti jam 5 sore).")
    delay_time = st.number_input("Waktu Tunda (Menit)", min_value=0.0, max_value=60.0, value=5.0, step=0.5, help="Estimasi durasi hambatan perjalanan saat ini.")

with col2:
    vehicle_volume = st.number_input("Volume Kendaraan", min_value=0, max_value=1000, value=150, step=10, help="Jumlah hitungan kendaraan yang melintas.")
    average_speed = st.number_input("Kecepatan Rata-Rata (km/h)", min_value=0.0, max_value=120.0, value=25.0, step=1.0, help="Rata-rata kecepatan pergerakan kendaraan di area tersebut.")

st.write("")

# ----- LOGIKA PREDIKSI -----
if st.button("Proses Prediksi Kemacetan"):
    
    with st.spinner("Sistem sedang memproses data..."):
        time.sleep(0.8) # Simulasi processing untuk user experience yang profesional
        
        # Bentuk Input Data (Sesuai urutan saat training dataset: Junction, Hour, Average_Speed, Vehicle_Volume, Delay_Time)
        input_dict = {
    'Junction': junction,
    'Hour': hour,
    'Average_Speed': average_speed,
    'Vehicle_Volume': vehicle_volume,
    'Delay_Time': delay_time
}

    input_data = pd.DataFrame([input_dict])

# 🔥 WAJIB: samakan urutan dengan training
    input_data = input_data[feature_order]
        
        # Standardisasi data input
    input_scaled = scaler.transform(input_data)
        
        # Eksekusi Model Prediksi
    pred_level = model.predict(input_scaled)[0]
    desc_label = label_map.get(pred_level, f"Level {pred_level}")
    text_desc = desc_label.split(': ')[1] if ': ' in desc_label else desc_label
        
        # Desain Warna Simpel Berdasarkan Status Bahaya Kemacetan
    color_map = {
            4: {"bg": "#ECFDF5", "text": "#065F46", "border": "#34D399"}, # Sangat Lancar (Hijau pucat)
            3: {"bg": "#F0FDF4", "text": "#3F6212", "border": "#A3E635"}, # Lancar (Hijau kekuningan)
            2: {"bg": "#FEF3C7", "text": "#92400E", "border": "#FBBF24"}, # Normal (Kuning terang)
            1: {"bg": "#FFEDD5", "text": "#9A3412", "border": "#FB923C"}, # Padat (Oranye)
            0: {"bg": "#FEF2F2", "text": "#991B1B", "border": "#F87171"}  # Macet Ekstrem (Merah pucat)
        }
        
    theme = color_map.get(pred_level, color_map[4])
        
        # Output Hasil UI
    st.markdown(f"""
        <div class="predicted-box" style="background-color: {theme['bg']}; color: {theme['text']}; border: 2px solid {theme['border']};">
            <h4 style="margin: 0; opacity: 0.8; font-weight: 600;">Status Situasi Lalu Lintas</h4>
            <h1 style="margin: 10px 0; font-size: 2.5rem; font-weight: 800;">
                {text_desc.upper()}
            </h1>
            <p style="margin: 0; font-weight: 600;">(Level Kepadatan: {pred_level})</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Pesan Anjuran Formal
    if pred_level <= 1: # Macet Ekstrem (0) atau Padat (1)
            st.error("Catatan: Terjadi kepadatan lalu lintas di jalur tersebut. Sangat disarankan untuk memilih rute jalan alternatif.")
    else:
            st.success("Catatan: Perjalanan normal dan laju arus kendaraan terpantau stabil tanpa antrean ekstrem.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 0.85rem;'>Sistem Monitoring Cerdas | Integrasi Model Machine Learning Klasifikasi</p>", unsafe_allow_html=True)
