import streamlit as st

st.set_page_config(page_title="Sistem Deteksi Stunting", layout="centered")

st.title("👶 Sistem Deteksi Stunting dengan Decision Tree")
st.image("banner_stunting1.jpg")

st.markdown("""
Peraturan Menteri Kesehatan tentang Standar Antropometri Anak  
[Permenkes No 2 Tahun 2020](https://peraturan.bpk.go.id/Home/Details/152505/permenkes-no-2-tahun-2020)

---
**Apa itu Stunting?**  
Stunting adalah kondisi gagal tumbuh akibat kekurangan gizi kronis, biasanya ditandai dengan tinggi badan yang lebih pendek dari anak seusianya.

                 
🛠️ **Cara Menggunakan Aplikasi Ini:**
1. Buka menu sidebar kiri
2. Pilih **"Deteksi Stunting"**
3. Masukkan data anak
4. Lihat hasil & rekomendasi makanan
""")
st.image("perbandingan_stunting_normal.jpeg", "Perbedaan Anak Normal dan Stunting")