import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from PIL import Image

st.title("📥 Deteksi Stunting Anak")

# Mapping angka ke keterangan stunting
label_mapping = {
    1: "Normal",
    2: "Gizi Kurang",
    3: "Risiko Gizi Lebih",
    4: "Gizi Lebih",
    5: "Obesitas"
}

# MODELING
# Load dataset
df = pd.read_csv("Data_Antropometri_Anak.csv")  

# Pisahkan fitur dan label
x = df.drop(['bb/tb'], axis=1)
y = df['bb/tb']

# Split dan scaling
X_train, X_test, y_train, y_test = train_test_split(x.values, y, test_size=0.1, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
model = DecisionTreeClassifier().fit(X_train_scaled, y_train)

# INTEGRASI
# Form Input Data Anak
with st.form("form_input"):
    st.subheader("📝 Masukkan Data Anak")

    jk = st.number_input("Jenis kelamin (1 = laki-laki, 0 = perempuan):", min_value=0, max_value=1)
    umur = st.number_input("Umur (bulan):", min_value=0, max_value=60)
    bb = st.number_input("Berat Badan (kg):", min_value=0.0, step=0.1)
    tb = st.number_input("Tinggi Badan (cm):", min_value=0.0, step=0.1)

    uploaded_image = st.file_uploader("📷 Upload Foto Anak (opsional)", type=["jpg", "jpeg", "png"])

     # Tampilkan gambar jika ada
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Foto Anak", use_container_width=True)

    submit = st.form_submit_button("🔍 Prediksi")

    if submit:
        # Proses prediksi
        input_data = np.array([jk, umur, bb, tb]).reshape(1, -1)
        input_scaled = scaler.transform(input_data)
        pred = model.predict(input_scaled)[0]
        hasil_keterangan = label_mapping.get(pred, "Tidak Diketahui")

        st.success(f"🩺 Hasil Prediksi: **{hasil_keterangan}**")

        # saran makanan berdasarkan hasil prediksi
        saran = ""
        if hasil_keterangan == "Normal":
            saran = "Pertahankan pola makan seimbang tiga kali sehari. Berikan camilan sehat dan makanan kaya protein seperti telur, ikan, dan susu."
        elif hasil_keterangan == "Gizi Kurang":
            saran = "Tingkatkan asupan gizi dengan makanan tinggi energi dan protein seperti daging, telur, tempe, dan susu. Berikan camilan bernutrisi secara rutin."
        elif hasil_keterangan == "Risiko Gizi Lebih":
            saran = "Mulai atur pola makan. Kurangi makanan manis, tinggi lemak, dan gorengan. Perbanyak konsumsi buah, sayur, dan ajak anak beraktivitas fisik ringan."
        elif hasil_keterangan == "Gizi Lebih":
            saran = "Batasi porsi makan dan hindari makanan berlemak serta tinggi gula. Fokus pada makanan berserat seperti sayur dan buah, serta aktivitas fisik teratur."
        elif hasil_keterangan == "Obesitas":
            saran = "Segera konsultasikan ke tenaga kesehatan. Hindari makanan cepat saji, batasi konsumsi gula dan lemak, serta dorong anak untuk aktif bergerak setiap hari."

        if saran:
            st.info(f"🍽️ **Saran Makanan:** {saran}")