# Instal library yang diperlukan
!pip install streamlit pyngrok --quiet

# Tulis kode Streamlit ke dalam file Python
# Ini adalah langkah penting agar streamlit dapat membaca skrip
with open('deret_aritmatika.py', 'w') as f:
    f.write("""
import streamlit as st
import time

def animate_formula(a, b, n):
    st.subheader("Animasi Penurunan Rumus Un")
    st.write(f"Misal deret aritmatika kita adalah:")
    st.write(f"$\\\\small U_1 = a$") # Menggunakan \\\\small untuk ukuran teks LaTeX
    st.write(f"$\\\\small U_2 = a + b$")
    st.write(f"$\\\\small U_3 = a + 2b$")
    st.write("...")
    st.write("Dari pola di atas, kita bisa lihat bahwa:")
    st.write(f"$U_n$ selalu memiliki $a$ sebagai suku pertamanya.")
    st.write(f"Koefisien $b$ selalu satu kurangnya dari indeks suku ($n$).")

    st.markdown("---")
    st.write("Mari kita lihat lebih dekat:")
    st.write(f"Untuk $U_1$, koefisien $b$ adalah $0$, yaitu $(1-1)b$.")
    st.write(f"Untuk $U_2$, koefisien $b$ adalah $1$, yaitu $(2-1)b$.")
    st.write(f"Untuk $U_3$, koefisien $b$ adalah $2$, yaitu $(3-1)b$.")

    st.markdown("---")
    st.write("Jadi, secara umum, untuk suku ke-$n$ ($U_n$):")
    st.markdown(f"**$\\\\large U_n = a + (n-1)b$**") # Menggunakan \\\\large untuk ukuran teks LaTeX
    st.success("Rumus Un ditemukan!")

def main():
    st.title("Kalkulator Deret Aritmatika")
    st.write("Temukan suku ke-$n$ dan pahami rumusnya dengan animasi sederhana.")

    st.sidebar.header("Input Deret Aritmatika")
    first_term = st.sidebar.number_input("Masukkan suku pertama (a):", value=1, step=1)
    common_difference = st.sidebar.number_input("Masukkan beda (b):", value=2, step=1)
    n_term = st.sidebar.number_input("Masukkan suku ke-n yang ingin dicari (n):", value=5, step=1, min_value=1)

    if st.sidebar.button("Hitung dan Tampilkan Animasi"):
        st.subheader("Hasil Perhitungan")
        un = first_term + (n_term - 1) * common_difference
        st.write(f"Suku pertama (a): {first_term}")
        st.write(f"Beda (b): {common_difference}")
        st.write(f"Suku ke-{n_term} ($U_{n_term}$): {un}")

        st.markdown("---")

        animate_formula(first_term, common_difference, n_term)

    st.markdown("---")
    st.write("### Cara Menggunakan:")
    st.write("1. Masukkan **suku pertama (a)** deret aritmatika di sidebar.")
    st.write("2. Masukkan **beda (b)** deret aritmatika di sidebar.")
    st.write("3. Masukkan **suku ke-n (n)** yang ingin Anda cari nilainya.")
    st.write("4. Klik tombol **'Hitung dan Tampilkan Animasi'**.")
    st.write("Anda akan melihat hasil perhitungan dan animasi penurunan rumus $U_n$.")

if __name__ == "__main__":
    main()
""")

# Konfigurasi authtoken ngrok
# PENTING: Pastikan Anda mengganti '2uzt3zck7DsFcgSphPuyEpHgUiN_3gijm7UyXNThGByqVsBhA'
# dengan authtoken ngrok Anda yang sebenarnya, yang didapatkan dari dasbor ngrok.
# Hindari spasi tambahan atau karakter tersembunyi saat menyalin token.
!ngrok config add-authtoken 2uzt3zck7DsFcgSphPuyEpHgUiN_3gijm7UyXNThGByqVsBhA

from pyngrok import ngrok
import os # Import os untuk mengakhiri sesi ngrok yang ada

# Pastikan untuk mengakhiri sesi ngrok yang ada jika ada
ngrok.kill()

# Jalankan Streamlit sebagai background process
# Pastikan nama file sesuai dengan yang kita tulis: deret_aritmatika.py
!streamlit run deret_aritmatika.py &>/dev/null &

# Hubungkan ke Streamlit via ngrok
# Port default Streamlit adalah 8501
public_url = ngrok.connect(addr="8501", proto="http")
print("Aplikasi bisa diakses di link berikut:")
print(public_url)
