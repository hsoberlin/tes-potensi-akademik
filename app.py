import streamlit as st

st.set_page_config(page_title="Simulasi TPA & Psikotes", layout="wide")

st.title("Latihan Ujian TPA & Psikotes Dasar")
st.markdown("Kerjakan 50 soal di bawah ini. Pilih jawaban yang paling tepat. Nilai dan pembahasan akan muncul setelah kamu menekan tombol **Kumpulkan Jawaban** di bagian paling bawah.")
st.markdown("---")

# Database 50 Soal TPA
# Struktur: "soal", "opsi", "jawaban" (index dari opsi), "pembahasan"
soal_tpa = [
    # --- MATEMATIKA DASAR & KUKABATAKU (1-10) ---
    {"soal": "1. 8 x 7 = ...", "opsi": ["54", "56", "64", "48"], "jawaban": 1, "pembahasan": "Hafalan dasar perkalian 8 x 7 = 56."},
    {"soal": "2. 63 : 9 = ...", "opsi": ["6", "7", "8", "9"], "jawaban": 1, "pembahasan": "Kebalikan dari 7 x 9 = 63."},
    {"soal": "3. 9 x 6 = ...", "opsi": ["54", "56", "45", "64"], "jawaban": 0, "pembahasan": "Hafalan dasar perkalian 9 x 6 = 54."},
    {"soal": "4. 72 : 8 = ...", "opsi": ["7", "8", "9", "10"], "jawaban": 2, "pembahasan": "Kebalikan dari 9 x 8 = 72."},
    {"soal": "5. 5 + 4 x 3 = ...", "opsi": ["27", "17", "12", "32"], "jawaban": 1, "pembahasan": "Kali dikerjakan lebih dulu: 4x3 = 12. Lalu 5 + 12 = 17."},
    {"soal": "6. (5 + 4) x 3 = ...", "opsi": ["27", "17", "12", "32"], "jawaban": 0, "pembahasan": "Dalam kurung dikerjakan lebih dulu: 9 x 3 = 27."},
    {"soal": "7. 20 - 10 : 2 = ...", "opsi": ["5", "10", "15", "25"], "jawaban": 2, "pembahasan": "Bagi dikerjakan lebih dulu: 10:2 = 5. Lalu 20 - 5 = 15."},
    {"soal": "8. 30 : 5 + 2 x 4 = ...", "opsi": ["32", "14", "10", "16"], "jawaban": 1, "pembahasan": "Bagi dan kali dikerjakan dulu: (30:5) + (2x4) = 6 + 8 = 14."},
    {"soal": "9. 15 + 15 : 3 - 2 = ...", "opsi": ["18", "8", "20", "12"], "jawaban": 0, "pembahasan": "Bagi dikerjakan dulu: 15 + 5 - 2 = 18."},
    {"soal": "10. 100 - (20 + 30) x 2 = ...", "opsi": ["100", "0", "40", "50"], "jawaban": 1, "pembahasan": "Kurung dulu: 50. Lalu kali: 50 x 2 = 100. Lalu 100 - 100 = 0."},
    
    # --- PECAHAN, DESIMAL, PERSENTASE (11-15) ---
    {"soal": "11. Bentuk desimal dari 1/4 adalah...", "opsi": ["0.14", "0.25", "0.40", "0.50"], "jawaban": 1, "pembahasan": "1/4 sama dengan 25/100 atau 0.25."},
    {"soal": "12. 50% dari Rp 120.000 adalah...", "opsi": ["Rp 50.000", "Rp 60.000", "Rp 70.000", "Rp 100.000"], "jawaban": 1, "pembahasan": "50% sama dengan setengahnya. 120.000 / 2 = 60.000."},
    {"soal": "13. Pecahan paling sederhana dari 15/20 adalah...", "opsi": ["1/2", "2/3", "3/4", "4/5"], "jawaban": 2, "pembahasan": "Atas dan bawah sama-sama dibagi 5. Menjadi 3/4."},
    {"soal": "14. 0.5 + 1/2 = ...", "opsi": ["0.5", "1", "1.5", "2"], "jawaban": 1, "pembahasan": "1/2 adalah 0.5. Maka 0.5 + 0.5 = 1."},
    {"soal": "15. Diskon 20% untuk barang seharga Rp 50.000. Berapa potongannya?", "opsi": ["Rp 5.000", "Rp 10.000", "Rp 15.000", "Rp 20.000"], "jawaban": 1, "pembahasan": "(20/100) x 50.000 = 10.000."},

    # --- DERET ANGKA (16-20) ---
    {"soal": "16. 2, 4, 6, 8, ...", "opsi": ["9", "10", "11", "12"], "jawaban": 1, "pembahasan": "Pola ditambah 2."},
    {"soal": "17. 3, 9, 27, 81, ...", "opsi": ["162", "243", "324", "100"], "jawaban": 1, "pembahasan": "Pola dikali 3. 81 x 3 = 243."},
    {"soal": "18. 100, 95, 85, 70, 50, ...", "opsi": ["25", "30", "35", "40"], "jawaban": 0, "pembahasan": "Pola pengurangan bertingkat: -5, -10, -15, -20. Selanjutnya -25. 50 - 25 = 25."},
    {"soal": "19. 1, 1, 2, 3, 5, 8, ...", "opsi": ["10", "11", "12", "13"], "jawaban": 3, "pembahasan": "Deret Fibonacci (menjumlahkan 2 angka sebelumnya). 5 + 8 = 13."},
    {"soal": "20. 2, 3, 6, 15, 42, ...", "opsi": ["84", "100", "123", "144"], "jawaban": 2, "pembahasan": "Selisihnya adalah 1, 3, 9, 27 (dikali 3). Selisih berikutnya 81. 42 + 81 = 123."},

    # --- SOAL CERITA LOGIKA WARUNG & PERBANDINGAN (21-30) ---
    {"soal": "21. Kamu menjual gula Rp12.000/kg. Jika pembeli membeli 3 kg dan membayar dengan uang Rp50.000, kembaliannya adalah...", "opsi": ["Rp 14.000", "Rp 16.000", "Rp 24.000", "Rp 36.000"], "jawaban": 0, "pembahasan": "Total belanja = 3 x 12.000 = 36.000. Kembalian = 50.000 - 36.000 = 14.000."},
    {"soal": "22. Beli kopi 5 saset harganya Rp 10.000. Kalau beli 8 saset harganya berapa?", "opsi": ["Rp 12.000", "Rp 15.000", "Rp 16.000", "Rp 18.000"], "jawaban": 2, "pembahasan": "Harga 1 saset = 10.000 : 5 = 2.000. Harga 8 saset = 8 x 2.000 = 16.000."},
    {"soal": "23. Pekerjaan selesai dalam 12 hari oleh 5 tukang. Jika dikerjakan 10 tukang, selesai dalam berapa hari?", "opsi": ["6 hari", "10 hari", "24 hari", "30 hari"], "jawaban": 0, "pembahasan": "Perbandingan berbalik nilai. Pekerja 2x lebih banyak, waktu 2x lebih cepat. 12 : 2 = 6 hari."},
    {"soal": "24. Jarak stasiun A ke B 120 km. Kereta melaju 60 km/jam. Butuh waktu berapa jam?", "opsi": ["1 jam", "2 jam", "3 jam", "4 jam"], "jawaban": 1, "pembahasan": "Waktu = Jarak / Kecepatan. 120 / 60 = 2 jam."},
    {"soal": "25. Andi berangkat pukul 07.00 dan menempuh perjalanan 2 jam. Pukul berapa ia tiba?", "opsi": ["08.00", "09.00", "10.00", "11.00"], "jawaban": 1, "pembahasan": "07.00 + 2 jam = 09.00."},
    {"soal": "26. Jika 3 liter bensin bisa menempuh 30 km. Berapa liter yang dibutuhkan untuk 50 km?", "opsi": ["4 liter", "5 liter", "6 liter", "7 liter"], "jawaban": 1, "pembahasan": "1 liter = 10 km. 50 km membutuhkan 50 / 10 = 5 liter."},
    {"soal": "27. Modal Rp 100.000, untung 20%. Berapa total uang sekarang?", "opsi": ["Rp 110.000", "Rp 120.000", "Rp 130.000", "Rp 150.000"], "jawaban": 1, "pembahasan": "Untung = 20.000. Total = 100.000 + 20.000 = 120.000."},
    {"soal": "28. Baju seharga Rp 200.000 didiskon 50% + 20%. Harga akhirnya adalah...", "opsi": ["Rp 60.000", "Rp 70.000", "Rp 80.000", "Rp 90.000"], "jawaban": 2, "pembahasan": "Diskon 50% -> sisa 100.000. Diskon lagi 20% dari 100.000 -> dipotong 20.000. Akhir = 80.000."},
    {"soal": "29. Andi mengecat rumah 3 hari, Budi mengecat 6 hari. Kalau dikerjakan bersama, selesai dalam...", "opsi": ["2 hari", "4.5 hari", "6 hari", "9 hari"], "jawaban": 0, "pembahasan": "(1/3) + (1/6) = 2/6 + 1/6 = 3/6. Dibalik menjadi 6/3 = 2 hari."},
    {"soal": "30. Pak RT punya Rp100.000. 1/4 bagian untuk beli paku, 1/2 bagian untuk cat. Sisa uang Pak RT?", "opsi": ["Rp 15.000", "Rp 25.000", "Rp 50.000", "Rp 75.000"], "jawaban": 1, "pembahasan": "Paku = 25.000. Cat = 50.000. Sisa = 100.000 - 75.000 = 25.000."},

    # --- SILOGISME (31-35) ---
    {"soal": "31. Semua pegawai memakai seragam. Andi adalah pegawai. Maka...", "opsi": ["Andi mungkin memakai seragam", "Andi memakai seragam", "Andi bukan pegawai", "Sebagian pegawai memakai seragam"], "jawaban": 1, "pembahasan": "Andi masuk ke dalam kelompok pegawai yang aturannya mutlak (semua)."},
    {"soal": "32. Jika hujan, maka jalan basah. Hari ini jalan tidak basah. Maka...", "opsi": ["Hari ini hujan", "Hari ini mungkin hujan", "Hari ini tidak hujan", "Jalan kering karena panas"], "jawaban": 2, "pembahasan": "Modus Tollens: Jika akibat tidak terjadi, maka sebabnya tidak ada."},
    {"soal": "33. Semua dokter pintar. Sebagian dokter suka membaca. Maka...", "opsi": ["Semua yang pintar suka membaca", "Sebagian dokter pintar", "Sebagian dokter pintar dan suka membaca", "Semua dokter pintar suka membaca"], "jawaban": 2, "pembahasan": "Jika 'Semua' bertemu 'Sebagian', kesimpulan pasti 'Sebagian'."},
    {"soal": "34. Jika Budi lulus, dibelikan sepeda. Jika dibelikan sepeda, ia keliling kota. Budi tidak keliling kota. Maka...", "opsi": ["Budi lulus", "Budi tidak dibelikan sepeda karena tidak lulus", "Budi tidak lulus", "Budi malas keliling kota"], "jawaban": 2, "pembahasan": "Silogisme berantai mundur. Karena tidak keliling kota, berarti syarat pertamanya (lulus) tidak terpenuhi."},
    {"soal": "35. Tidak ada pelaut yang penakut. Beberapa nelayan adalah penakut. Maka...", "opsi": ["Beberapa nelayan bukan pelaut", "Semua nelayan adalah pelaut", "Beberapa pelaut adalah nelayan", "Tidak ada nelayan yang berani"], "jawaban": 0, "pembahasan": "Nelayan yang penakut otomatis tidak bisa dikategorikan sebagai pelaut."},

    # --- ANALOGI KATA (36-40) ---
    {"soal": "36. Lapar : Makan = Haus : ...", "opsi": ["Air", "Minum", "Gelas", "Es"], "jawaban": 1, "pembahasan": "Jika lapar butuh makan, jika haus butuh minum."},
    {"soal": "37. Kayu : Lemari = Kain : ...", "opsi": ["Kapas", "Baju", "Jahit", "Benang"], "jawaban": 1, "pembahasan": "Kayu adalah bahan baku lemari. Kain adalah bahan baku baju."},
    {"soal": "38. Masinis : Kereta Api = Nahkoda : ...", "opsi": ["Pesawat", "Mobil", "Kapal Laut", "Bus"], "jawaban": 2, "pembahasan": "Masinis menyetir kereta. Nahkoda menyetir kapal laut."},
    {"soal": "39. Gandum : Roti : Makan = Benang : Pakaian : ...", "opsi": ["Jahit", "Pola", "Pakai", "Toko"], "jawaban": 2, "pembahasan": "Roti dibuat untuk dimakan. Pakaian dibuat untuk dipakai."},
    {"soal": "40. Gempa Bumi : Tsunami = Hujan Deras : ...", "opsi": ["Banjir Bandang", "Mendung", "Payung", "Basah"], "jawaban": 0, "pembahasan": "Bencana alam ekstrem memicu bencana susulan ekstrem lainnya."},

    # --- LOGIKA VISUAL & POSISI (DESKRIPTIF) (41-50) ---
    {"soal": "41. Gambar 1: Kotak. Gambar 2: 2 Kotak. Gambar 3: 3 Kotak. Gambar 4 adalah...", "opsi": ["1 Kotak", "4 Kotak", "5 Kotak", "Lingkaran"], "jawaban": 1, "pembahasan": "Pola penambahan 1 kotak secara berurutan."},
    {"soal": "42. Panah Atas, Panah Kanan, Panah Bawah. Selanjutnya panah ke arah...", "opsi": ["Atas", "Kanan", "Bawah", "Kiri"], "jawaban": 3, "pembahasan": "Panah berputar 90 derajat searah jarum jam."},
    {"soal": "43. Segitiga (3 sisi), Segi Empat (4 sisi), Segi Lima (5 sisi). Selanjutnya...", "opsi": ["Lingkaran", "Segi Enam", "Segi Tujuh", "Segi Delapan"], "jawaban": 1, "pembahasan": "Penambahan 1 sisi pada bangun datar."},
    {"soal": "44. Huruf 'b' dicerminkan ke kaca akan menjadi huruf...", "opsi": ["p", "q", "d", "c"], "jawaban": 2, "pembahasan": "Bayangan cermin dari 'b' memantul menjadi 'd'."},
    {"soal": "45. Ada 2 titik, lalu 4 titik, lalu 6 titik. Gambar selanjutnya memiliki berapa titik?", "opsi": ["7 titik", "8 titik", "9 titik", "10 titik"], "jawaban": 1, "pembahasan": "Pola ditambah 2 titik secara berurutan."},
    
    {"soal": "46. Posisi: A duduk di sebelah kanan B. C duduk di sebelah kiri B. Siapa di tengah?", "opsi": ["A", "B", "C", "Tidak ada"], "jawaban": 1, "pembahasan": "Urutannya: C - B - A. B berada di tengah."},
    {"soal": "47. Andi tidak jaga Malam. Cici selalu Pagi. Doni jaga setelah Andi. Jika Budi jaga Malam, Andi jaga kapan?", "opsi": ["Pagi", "Siang", "Sore", "Malam"], "jawaban": 1, "pembahasan": "Pagi: Cici. Malam: Budi. Sisa Siang & Sore. Doni harus setelah Andi, jadi Andi (Siang), Doni (Sore)."},
    {"soal": "48. Dalam balapan, Budi menyalip pelari posisi kedua. Posisi Budi sekarang adalah...", "opsi": ["Pertama", "Kedua", "Ketiga", "Keempat"], "jawaban": 1, "pembahasan": "Jika kamu menyalip orang posisi kedua, kamu mengambil alih posisinya, yaitu posisi kedua."},
    {"soal": "49. Rumah Tono lebih jauh dari rumah Tini. Rumah Tino lebih dekat dari rumah Tini. Rumah siapa yang paling jauh?", "opsi": ["Tono", "Tini", "Tino", "Semua sama"], "jawaban": 0, "pembahasan": "Urutan dari terjauh: Tono - Tini - Tino."},
    {"soal": "50. Kereta A berangkat jam 08.00 tiba jam 10.00. Kereta B berangkat jam 08.00 tiba jam 09.30. Mana yang lebih cepat?", "opsi": ["Kereta A", "Kereta B", "Sama saja", "Tidak bisa dihitung"], "jawaban": 1, "pembahasan": "Kereta B hanya butuh 1,5 jam, sedangkan Kereta A butuh 2 jam."}
]

# Inisialisasi state untuk mengecek apakah form sudah di-submit
if 'telah_submit' not in st.session_state:
    st.session_state.telah_submit = False
    st.session_state.skor = 0
    st.session_state.jawaban_user = []

# Membuat Form Kuis
with st.form(key='kuis_tpa'):
    jawaban_sementara = []
    
    for i, item in enumerate(soal_tpa):
        st.write(item["soal"])
        
        # Radio button untuk opsi jawaban. index=None agar tidak terisi otomatis (kosong di awal).
        pilihan = st.radio(
            label=f"Opsi soal {i+1}", 
            options=item["opsi"], 
            index=None,
            label_visibility="collapsed",
            key=f"soal_{i}"
        )
        jawaban_sementara.append(pilihan)
        st.write("") # Spasi antar soal
        
    submit_button = st.form_submit_button(label='Kumpulkan Jawaban')

# Proses saat tombol Submit ditekan
if submit_button:
    st.session_state.telah_submit = True
    st.session_state.jawaban_user = jawaban_sementara
    
    benar = 0
    salah = 0
    
    for i, item in enumerate(soal_tpa):
        jawaban_benar_teks = item["opsi"][item["jawaban"]]
        if jawaban_sementara[i] == jawaban_benar_teks:
            benar += 1
        else:
            salah += 1
            
    # Menghitung skor skala 100
    skor_akhir = (benar / len(soal_tpa)) * 100
    st.session_state.skor = skor_akhir
    st.session_state.benar = benar
    st.session_state.salah = salah

# Menampilkan Hasil dan Evaluasi
if st.session_state.telah_submit:
    st.markdown("---")
    st.header("HASIL EVALUASI")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Skor Total", f"{st.session_state.skor:g} / 100")
    col2.metric("Jawaban Benar", st.session_state.benar)
    col3.metric("Jawaban Salah/Kosong", st.session_state.salah)
    
    st.markdown("### Daftar Jawaban yang Salah dan Pembahasannya:")
    
    kesalahan_ditemukan = False
    for i, item in enumerate(soal_tpa):
        jawaban_benar_teks = item["opsi"][item["jawaban"]]
        jawaban_user_sekarang = st.session_state.jawaban_user[i]
        
        if jawaban_user_sekarang != jawaban_benar_teks:
            kesalahan_ditemukan = True
            with st.expander(f"Soal {i+1} (Salah)"):
                st.write(f"**Pertanyaan:** {item['soal']}")
                st.write(f"❌ **Jawabanmu:** {jawaban_user_sekarang if jawaban_user_sekarang else 'Tidak Dijawab'}")
                st.write(f"✅ **Jawaban Benar:** {jawaban_benar_teks}")
                st.info(f"**Pembahasan:** {item['pembahasan']}")
                
    if not kesalahan_ditemukan:
        st.success("Luar biasa! Semua jawaban benar. Kamu sudah siap mengikuti ujian TPA sebenarnya!")
    else:
        st.warning("Silakan pelajari pembahasan dari jawaban yang salah di atas agar tidak mengulanginya di tes sebenarnya.")
