# Definisi kode untuk aplikasi BMI
# Perhatikan bahwa kode ini akan ditulis ke dalam file bmi_app.py
kode_bmi_aplikasi = """
import streamlit as st

st.title("Kalkulator BMI (Indeks Massa Tubuh)")

nama = st.text_input("Masukkan nama Anda")
tinggi = st.number_input("Masukkan tinggi badan (cm)", min_value=100, max_value=250)
berat = st.number_input("Masukkan berat badan (kg)", min_value=30, max_value=200)

if st.button("Hitung BMI"):
    if tinggi > 0 and berat > 0:
        bmi = berat / ((tinggi / 100) ** 2)
        st.write(f"Halo, **{nama}** 👋")
        st.write(f"Nilai BMI Anda adalah **{bmi:.2f}**")

        if bmi < 18.5:
            st.warning("Berat badan Anda kurang.")
        elif 18.5 <= bmi < 25:
            st.success("Berat badan Anda normal.")
        elif 25 <= bmi < 30:
            st.info("Berat badan Anda berlebih.")
        else:
            st.error("Anda termasuk obesitas.")
    else:
        st.error("Tinggi dan berat badan harus lebih dari 0.")
"""

# Tulis kode aplikasi BMI ke dalam file bmi_app.py
# Pastikan nama variabel yang digunakan untuk menyimpan kode (misal: kode_bmi_aplikasi)
# sesuai dengan yang dituliskan ke file (f.write(kode_bmi_aplikasi))
with open("bmi_app.py", "w") as f:
    f.write(kode_bmi_aplikasi)

print("File bmi_app.py berhasil dibuat.")
print("Sekarang Anda bisa menjalankan aplikasi Streamlit dengan perintah:")
print("!streamlit run bmi_app.py")
