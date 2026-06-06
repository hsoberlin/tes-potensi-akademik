import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="Pusat Simulasi Ujian TPA & SKD", layout="wide")

# ==========================================
# 1. DATABASE SOAL (FULL 210 SOAL ASLI)
# ==========================================

soal_paket_1 = [
    {"soal": "8 x 7 = ...", "opsi": ["54", "56", "64", "48"], "jawaban": 1, "pembahasan": "Hafalan dasar perkalian 8 x 7 = 56."},
    {"soal": "63 : 9 = ...", "opsi": ["6", "7", "8", "9"], "jawaban": 1, "pembahasan": "Kebalikan dari 7 x 9 = 63."},
    {"soal": "9 x 6 = ...", "opsi": ["54", "56", "45", "64"], "jawaban": 0, "pembahasan": "Hafalan dasar perkalian 9 x 6 = 54."},
    {"soal": "72 : 8 = ...", "opsi": ["7", "8", "9", "10"], "jawaban": 2, "pembahasan": "Kebalikan dari 9 x 8 = 72."},
    {"soal": "5 + 4 x 3 = ...", "opsi": ["27", "17", "12", "32"], "jawaban": 1, "pembahasan": "Kali dikerjakan lebih dulu: 4x3 = 12. Lalu 5 + 12 = 17."},
    {"soal": "(5 + 4) x 3 = ...", "opsi": ["27", "17", "12", "32"], "jawaban": 0, "pembahasan": "Dalam kurung dikerjakan lebih dulu: 9 x 3 = 27."},
    {"soal": "20 - 10 : 2 = ...", "opsi": ["5", "10", "15", "25"], "jawaban": 2, "pembahasan": "Bagi dikerjakan lebih dulu: 10:2 = 5. Lalu 20 - 5 = 15."},
    {"soal": "30 : 5 + 2 x 4 = ...", "opsi": ["32", "14", "10", "16"], "jawaban": 1, "pembahasan": "Bagi dan kali dikerjakan dulu: (30:5) + (2x4) = 6 + 8 = 14."},
    {"soal": "15 + 15 : 3 - 2 = ...", "opsi": ["18", "8", "20", "12"], "jawaban": 0, "pembahasan": "Bagi dikerjakan dulu: 15 + 5 - 2 = 18."},
    {"soal": "100 - (20 + 30) x 2 = ...", "opsi": ["100", "0", "40", "50"], "jawaban": 1, "pembahasan": "Kurung dulu: 50. Lalu kali: 50 x 2 = 100. Lalu 100 - 100 = 0."},
    {"soal": "Bentuk desimal dari 1/4 adalah...", "opsi": ["0.14", "0.25", "0.40", "0.50"], "jawaban": 1, "pembahasan": "1/4 sama dengan 25/100 atau 0.25."},
    {"soal": "50% dari Rp 120.000 adalah...", "opsi": ["Rp 50.000", "Rp 60.000", "Rp 70.000", "Rp 100.000"], "jawaban": 1, "pembahasan": "50% sama dengan setengahnya. 120.000 / 2 = 60.000."},
    {"soal": "Pecahan paling sederhana dari 15/20 adalah...", "opsi": ["1/2", "2/3", "3/4", "4/5"], "jawaban": 2, "pembahasan": "Atas dan bawah sama-sama dibagi 5. Menjadi 3/4."},
    {"soal": "0.5 + 1/2 = ...", "opsi": ["0.5", "1", "1.5", "2"], "jawaban": 1, "pembahasan": "1/2 adalah 0.5. Maka 0.5 + 0.5 = 1."},
    {"soal": "Diskon 20% untuk barang seharga Rp 50.000. Berapa potongannya?", "opsi": ["Rp 5.000", "Rp 10.000", "Rp 15.000", "Rp 20.000"], "jawaban": 1, "pembahasan": "(20/100) x 50.000 = 10.000."},
    {"soal": "2, 4, 6, 8, ...", "opsi": ["9", "10", "11", "12"], "jawaban": 1, "pembahasan": "Pola ditambah 2."},
    {"soal": "3, 9, 27, 81, ...", "opsi": ["162", "243", "324", "100"], "jawaban": 1, "pembahasan": "Pola dikali 3. 81 x 3 = 243."},
    {"soal": "100, 95, 85, 70, 50, ...", "opsi": ["25", "30", "35", "40"], "jawaban": 0, "pembahasan": "Pola pengurangan bertingkat: -5, -10, -15, -20. Selanjutnya -25. 50 - 25 = 25."},
    {"soal": "1, 1, 2, 3, 5, 8, ...", "opsi": ["10", "11", "12", "13"], "jawaban": 3, "pembahasan": "Deret Fibonacci (menjumlahkan 2 angka sebelumnya). 5 + 8 = 13."},
    {"soal": "2, 3, 6, 15, 42, ...", "opsi": ["84", "100", "123", "144"], "jawaban": 2, "pembahasan": "Selisihnya adalah 1, 3, 9, 27 (dikali 3). Selisih berikutnya 81. 42 + 81 = 123."},
    {"soal": "Kamu menjual gula Rp12.000/kg. Jika pembeli membeli 3 kg dan membayar dengan uang Rp50.000, kembaliannya adalah...", "opsi": ["Rp 14.000", "Rp 16.000", "Rp 24.000", "Rp 36.000"], "jawaban": 0, "pembahasan": "Total belanja = 3 x 12.000 = 36.000. Kembalian = 50.000 - 36.000 = 14.000."},
    {"soal": "Beli kopi 5 saset harganya Rp 10.000. Kalau beli 8 saset harganya berapa?", "opsi": ["Rp 12.000", "Rp 15.000", "Rp 16.000", "Rp 18.000"], "jawaban": 2, "pembahasan": "Harga 1 saset = 10.000 : 5 = 2.000. Harga 8 saset = 8 x 2.000 = 16.000."},
    {"soal": "Pekerjaan selesai dalam 12 hari oleh 5 tukang. Jika dikerjakan 10 tukang, selesai dalam berapa hari?", "opsi": ["6 hari", "10 hari", "24 hari", "30 hari"], "jawaban": 0, "pembahasan": "Perbandingan berbalik nilai. Pekerja 2x lebih banyak, waktu 2x lebih cepat. 12 : 2 = 6 hari."},
    {"soal": "Jarak stasiun A ke B 120 km. Kereta melaju 60 km/jam. Butuh waktu berapa jam?", "opsi": ["1 jam", "2 jam", "3 jam", "4 jam"], "jawaban": 1, "pembahasan": "Waktu = Jarak / Kecepatan. 120 / 60 = 2 jam."},
    {"soal": "Andi berangkat pukul 07.00 dan menempuh perjalanan 2 jam. Pukul berapa ia tiba?", "opsi": ["08.00", "09.00", "10.00", "11.00"], "jawaban": 1, "pembahasan": "07.00 + 2 jam = 09.00."},
    {"soal": "Jika 3 liter bensin bisa menempuh 30 km. Berapa liter yang dibutuhkan untuk 50 km?", "opsi": ["4 liter", "5 liter", "6 liter", "7 liter"], "jawaban": 1, "pembahasan": "1 liter = 10 km. 50 km membutuhkan 50 / 10 = 5 liter."},
    {"soal": "Modal Rp 100.000, untung 20%. Berapa total uang sekarang?", "opsi": ["Rp 110.000", "Rp 120.000", "Rp 130.000", "Rp 150.000"], "jawaban": 1, "pembahasan": "Untung = 20.000. Total = 100.000 + 20.000 = 120.000."},
    {"soal": "Baju seharga Rp 200.000 didiskon 50% + 20%. Harga akhirnya adalah...", "opsi": ["Rp 60.000", "Rp 70.000", "Rp 80.000", "Rp 90.000"], "jawaban": 2, "pembahasan": "Diskon 50% -> sisa 100.000. Diskon lagi 20% dari 100.000 -> dipotong 20.000. Akhir = 80.000."},
    {"soal": "Andi mengecat rumah 3 hari, Budi mengecat 6 hari. Kalau dikerjakan bersama, selesai dalam...", "opsi": ["2 hari", "4.5 hari", "6 hari", "9 hari"], "jawaban": 0, "pembahasan": "(1/3) + (1/6) = 2/6 + 1/6 = 3/6. Dibalik menjadi 6/3 = 2 hari."},
    {"soal": "Pak RT punya Rp100.000. 1/4 bagian untuk beli paku, 1/2 bagian untuk cat. Sisa uang Pak RT?", "opsi": ["Rp 15.000", "Rp 25.000", "Rp 50.000", "Rp 75.000"], "jawaban": 1, "pembahasan": "Paku = 25.000. Cat = 50.000. Sisa = 100.000 - 75.000 = 25.000."},
    {"soal": "Semua pegawai memakai seragam. Andi adalah pegawai. Maka...", "opsi": ["Andi mungkin memakai seragam", "Andi memakai seragam", "Andi bukan pegawai", "Sebagian pegawai memakai seragam"], "jawaban": 1, "pembahasan": "Andi masuk kelompok pegawai, aturannya mutlak."},
    {"soal": "Jika hujan, maka jalan basah. Hari ini jalan tidak basah. Maka...", "opsi": ["Hari ini hujan", "Hari ini mungkin hujan", "Hari ini tidak hujan", "Jalan kering karena panas"], "jawaban": 2, "pembahasan": "Modus Tollens: Akibat tidak ada, sebab tidak ada."},
    {"soal": "Semua dokter pintar. Sebagian dokter suka membaca. Maka...", "opsi": ["Semua yang pintar suka membaca", "Sebagian dokter pintar", "Sebagian dokter pintar dan suka membaca", "Semua dokter pintar suka membaca"], "jawaban": 2, "pembahasan": "'Semua' bertemu 'Sebagian' kesimpulan pasti 'Sebagian'."},
    {"soal": "Jika Budi lulus, dibelikan sepeda. Jika dibelikan sepeda, keliling kota. Budi tidak keliling kota. Maka...", "opsi": ["Budi lulus", "Budi tidak lulus", "Budi malas", "Budi dibelikan sepeda"], "jawaban": 1, "pembahasan": "Silogisme berantai mundur."},
    {"soal": "Tidak ada pelaut yang penakut. Beberapa nelayan adalah penakut. Maka...", "opsi": ["Beberapa nelayan bukan pelaut", "Semua nelayan adalah pelaut", "Beberapa pelaut adalah nelayan", "Tidak ada nelayan yang berani"], "jawaban": 0, "pembahasan": "Nelayan penakut otomatis bukan pelaut."},
    {"soal": "Lapar : Makan = Haus : ...", "opsi": ["Air", "Minum", "Gelas", "Es"], "jawaban": 1, "pembahasan": "Jika lapar butuh makan, jika haus butuh minum."},
    {"soal": "Kayu : Lemari = Kain : ...", "opsi": ["Kapas", "Baju", "Jahit", "Benang"], "jawaban": 1, "pembahasan": "Kayu adalah bahan lemari. Kain adalah bahan baju."},
    {"soal": "Masinis : Kereta Api = Nahkoda : ...", "opsi": ["Pesawat", "Mobil", "Kapal Laut", "Bus"], "jawaban": 2, "pembahasan": "Masinis menyetir kereta. Nahkoda menyetir kapal."},
    {"soal": "Gandum : Roti : Makan = Benang : Pakaian : ...", "opsi": ["Jahit", "Pola", "Pakai", "Toko"], "jawaban": 2, "pembahasan": "Roti untuk dimakan. Pakaian untuk dipakai."},
    {"soal": "Gempa Bumi : Tsunami = Hujan Deras : ...", "opsi": ["Banjir Bandang", "Mendung", "Payung", "Basah"], "jawaban": 0, "pembahasan": "Bencana memicu bencana ekstrem lainnya."},
    {"soal": "1️⃣ ⬜ \n 2️⃣ ⬜ ⬜ \n 3️⃣ ⬜ ⬜ ⬜ \n ➡️ ❓", "opsi": ["⬜", "⬜ ⬜ ⬜ ⬜", "⬜ ⬜ ⬜ ⬜ ⬜", "⚫"], "jawaban": 1, "pembahasan": "Pola nambah 1 kotak."},
    {"soal": "1️⃣ ⬆️ \n 2️⃣ ➡️ \n 3️⃣ ⬇️ \n ➡️ ❓", "opsi": ["⬆️", "➡️", "⬇️", "⬅️"], "jawaban": 3, "pembahasan": "Putar 90 derajat searah jarum jam."},
    {"soal": "1️⃣ 🔺 \n 2️⃣ ◼️ \n 3️⃣ ⬟ \n ➡️ ❓", "opsi": ["🟠", "⬡", "⭐", "🔶"], "jawaban": 1, "pembahasan": "Nambah 1 sisi bangun datar."},
    {"soal": "🔠 **b** 🪞 ❓", "opsi": ["p", "q", "d", "c"], "jawaban": 2, "pembahasan": "Cermin huruf 'b' memantul jadi 'd'."},
    {"soal": "1️⃣ ⚫⚫ \n 2️⃣ ⚫⚫⚫⚫ \n 3️⃣ ⚫⚫⚫⚫⚫⚫ \n ➡️ ❓", "opsi": ["⚫⚫⚫⚫⚫⚫⚫", "⚫⚫⚫⚫⚫⚫⚫⚫", "⚫⚫⚫⚫⚫⚫⚫⚫⚫", "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫"], "jawaban": 1, "pembahasan": "Ditambah 2 titik."},
    {"soal": "Posisi: A duduk kanan B. C duduk kiri B. Siapa di tengah?", "opsi": ["A", "B", "C", "Tidak ada"], "jawaban": 1, "pembahasan": "Urutan C - B - A."},
    {"soal": "Andi tidak Malam. Cici selalu Pagi. Doni setelah Andi. Budi Malam. Andi jaga kapan?", "opsi": ["Pagi", "Siang", "Sore", "Malam"], "jawaban": 1, "pembahasan": "Cici(Pagi), Budi(Malam). Sisa Siang & Sore. Andi(Siang), Doni(Sore)."},
    {"soal": "Budi menyalip posisi kedua. Posisi Budi sekarang...", "opsi": ["Pertama", "Kedua", "Ketiga", "Keempat"], "jawaban": 1, "pembahasan": "Menyalip posisi kedua artinya menempati posisi kedua tersebut."},
    {"soal": "Rumah Tono lebih jauh dari Tini. Tino lebih dekat dari Tini. Paling jauh?", "opsi": ["Tono", "Tini", "Tino", "Sama"], "jawaban": 0, "pembahasan": "Urutan: Tono(terjauh) - Tini - Tino."},
    {"soal": "Kereta A berangkat 08.00 tiba 10.00. Kereta B berangkat 08.00 tiba 09.30. Mana lebih cepat?", "opsi": ["Kereta A", "Kereta B", "Sama saja", "Tidak tahu"], "jawaban": 1, "pembahasan": "Kereta B butuh 1.5 jam, Kereta A butuh 2 jam."}
]

soal_paket_2 = [
    {"soal": "12 x 15 = ...", "opsi": ["160", "170", "180", "190"], "jawaban": 2, "pembahasan": "10x15 = 150, ditambah 2x15 = 30. Hasil = 180."},
    {"soal": "144 : 12 = ...", "opsi": ["10", "12", "14", "16"], "jawaban": 1, "pembahasan": "Akar kuadrat dari 144 adalah 12."},
    {"soal": "25 + 15 x 4 - 10 = ...", "opsi": ["150", "100", "75", "65"], "jawaban": 2, "pembahasan": "Kali dulu: 15x4 = 60. Lalu 25 + 60 - 10 = 75."},
    {"soal": "(18 - 6) x (10 + 2) = ...", "opsi": ["144", "124", "120", "100"], "jawaban": 0, "pembahasan": "Kerjakan dalam kurung: 12 x 12 = 144."},
    {"soal": "50% dari 0.8 adalah...", "opsi": ["0.4", "0.5", "4", "40"], "jawaban": 0, "pembahasan": "Setengah dari 0.8 adalah 0.4."},
    {"soal": "1/3 + 1/6 = ...", "opsi": ["2/9", "2/6", "1/2", "3/9"], "jawaban": 2, "pembahasan": "Samakan penyebut (6). Jadi 2/6 + 1/6 = 3/6 = 1/2."},
    {"soal": "0.25 x 400 = ...", "opsi": ["50", "100", "150", "200"], "jawaban": 1, "pembahasan": "0.25 sama dengan 1/4. 400 dibagi 4 = 100."},
    {"soal": "10^2 - 8^2 = ...", "opsi": ["36", "64", "100", "164"], "jawaban": 0, "pembahasan": "100 - 64 = 36."},
    {"soal": "Akar 169 + Akar 144 = ...", "opsi": ["23", "25", "27", "29"], "jawaban": 1, "pembahasan": "13 + 12 = 25."},
    {"soal": "2.5 x 4 + 10 : 2 = ...", "opsi": ["15", "20", "25", "30"], "jawaban": 0, "pembahasan": "(2.5 x 4) = 10. Lalu (10 : 2) = 5. 10 + 5 = 15."},
    {"soal": "Bentuk desimal dari 3/8 adalah...", "opsi": ["0.35", "0.375", "0.40", "0.45"], "jawaban": 1, "pembahasan": "1/8 adalah 0.125. Maka 3/8 adalah 3 x 0.125 = 0.375."},
    {"soal": "Harga Rp 200.000 diskon 50% lalu diskon lagi 20%. Harga akhir?", "opsi": ["Rp 60.000", "Rp 70.000", "Rp 80.000", "Rp 100.000"], "jawaban": 2, "pembahasan": "Diskon 50% = sisa 100rb. Diskon 20% dari 100rb = potong 20rb. Sisa 80.000."},
    {"soal": "33.33% dari Rp 150.000 adalah...", "opsi": ["Rp 30.000", "Rp 40.000", "Rp 50.000", "Rp 60.000"], "jawaban": 2, "pembahasan": "33.33% sama dengan 1/3. 150.000 dibagi 3 = 50.000."},
    {"soal": "Barang dijual Rp 120.000 dengan untung 20%. Harga belinya?", "opsi": ["Rp 96.000", "Rp 100.000", "Rp 110.000", "Rp 144.000"], "jawaban": 1, "pembahasan": "Harga Jual = 120% x Modal. Maka Modal = 120.000 / 1.2 = 100.000."},
    {"soal": "1.25 : 0.5 = ...", "opsi": ["0.25", "0.50", "2.0", "2.5"], "jawaban": 3, "pembahasan": "Sama dengan 12.5 dibagi 5 = 2.5."},
    {"soal": "3, 4, 7, 11, 18, ...", "opsi": ["27", "28", "29", "30"], "jawaban": 2, "pembahasan": "Deret Fibonacci (11 + 18 = 29)."},
    {"soal": "2, 5, 10, 17, 26, ...", "opsi": ["35", "37", "39", "41"], "jawaban": 1, "pembahasan": "Selisih angkanya bertambah ganjil: +3, +5, +7, +9. Berikutnya +11. 26 + 11 = 37."},
    {"soal": "100, 50, 200, 100, 400, ...", "opsi": ["200", "300", "400", "800"], "jawaban": 0, "pembahasan": "Pola: Bagi 2, lalu Kali 4 secara bergantian. 400 dibagi 2 = 200."},
    {"soal": "1, 8, 27, 64, ...", "opsi": ["100", "125", "144", "216"], "jawaban": 1, "pembahasan": "Pola pangkat tiga: 1^3, 2^3, 3^3, 4^3. Selanjutnya 5^3 = 125."},
    {"soal": "5, 10, 30, 120, ...", "opsi": ["480", "500", "600", "720"], "jawaban": 2, "pembahasan": "Pola perkalian menaik: x2, x3, x4. Berikutnya 120 x 5 = 600."},
    {"soal": "A mengecat dinding 4 jam, B butuh 12 jam. Jika bersama-sama?", "opsi": ["3 jam", "4 jam", "8 jam", "16 jam"], "jawaban": 0, "pembahasan": "1/4 + 1/12 = 3/12 + 1/12 = 4/12. Dibalik jadi 12/4 = 3 jam."},
    {"soal": "Proyek butuh 6 pekerja selesai 15 hari. Agar selesai 10 hari butuh berapa pekerja total?", "opsi": ["8 pekerja", "9 pekerja", "10 pekerja", "12 pekerja"], "jawaban": 1, "pembahasan": "Perbandingan berbalik nilai. 6 x 15 = P x 10. 90 = 10P. P = 9 pekerja."},
    {"soal": "Beli 2 lusin buku Rp 48.000. Harga 5 buku?", "opsi": ["Rp 8.000", "Rp 10.000", "Rp 12.000", "Rp 15.000"], "jawaban": 1, "pembahasan": "2 lusin = 24 buku. 1 buku = 48.000 / 24 = 2.000. 5 buku = 10.000."},
    {"soal": "Tandon air 500 liter bocor 5 liter/menit. Habis dalam...", "opsi": ["1 jam", "1 jam 20 menit", "1 jam 40 menit", "2 jam"], "jawaban": 2, "pembahasan": "500 / 5 = 100 menit. 100 menit = 1 jam 40 menit."},
    {"soal": "Tabungan awal Rp 2.000.000, bunga 12% pertahun. Berapa nilai bunga setelah 6 bulan?", "opsi": ["Rp 120.000", "Rp 240.000", "Rp 360.000", "Rp 400.000"], "jawaban": 0, "pembahasan": "Bunga 1 tahun = 240.000. Setengah tahun (6 bulan) = 120.000."},
    {"soal": "Berangkat pukul 06.15, tiba 08.45. Di jalan istirahat 30 menit. Jarak 120 km. Kecepatannya?", "opsi": ["50 km/jam", "60 km/jam", "70 km/jam", "80 km/jam"], "jawaban": 1, "pembahasan": "Waktu tempuh 06.15 ke 08.45 = 2.5 jam. Kurangi istirahat 30 mnt = 2 jam bersih. Kecepatan = 120 / 2 = 60 km/jam."},
    {"soal": "Sepatu Rp 300.000. Diskon 30% lalu potongan tunai Rp 10.000. Total bayar?", "opsi": ["Rp 190.000", "Rp 200.000", "Rp 210.000", "Rp 220.000"], "jawaban": 1, "pembahasan": "Diskon 30% (90rb) -> Sisa 210.000. Potongan tunai 10.000 -> Sisa 200.000."},
    {"soal": "Roda berputar 20 kali menempuh 10 m. Untuk jarak 50 m butuh berapa putaran?", "opsi": ["50 putaran", "80 putaran", "100 putaran", "120 putaran"], "jawaban": 2, "pembahasan": "Jarak bertambah 5x lipat (10m ke 50m). Putaran juga 5x lipat: 20 x 5 = 100."},
    {"soal": "Uang Rp 100.000. Si A dapat 2/5, B dapat 1/4, sisanya untuk C. Bagian C adalah...", "opsi": ["Rp 25.000", "Rp 30.000", "Rp 35.000", "Rp 40.000"], "jawaban": 2, "pembahasan": "A = 40.000. B = 25.000. Total A+B = 65.000. Sisa untuk C = 100.000 - 65.000 = 35.000."},
    {"soal": "Pakan untuk 30 ayam habis 15 hari. Jika ayam ditambah 15 ekor, pakan habis dalam...", "opsi": ["5 hari", "10 hari", "20 hari", "22 hari"], "jawaban": 1, "pembahasan": "Total ayam jadi 45. Perbandingan berbalik: 30 x 15 = 45 x Y. 450 = 45Y. Y = 10 hari."},
    {"soal": "Jika rajin maka lulus. Jika lulus maka kerja. Budi saat ini menganggur. Maka...", "opsi": ["Budi rajin", "Budi lulus tapi tidak kerja", "Budi tidak rajin", "Budi tidak mau kerja"], "jawaban": 2, "pembahasan": "Logika Modus Tollens berantai mundur. Menganggur (tidak kerja) -> tidak lulus -> tidak rajin."},
    {"soal": "Semua dokter memakai jas putih. Sebagian pria memakai jas putih. Maka...", "opsi": ["Semua pria adalah dokter", "Sebagian dokter adalah pria", "Semua yang berjas putih adalah pria", "Tidak bisa ditarik kesimpulan pasti"], "jawaban": 3, "pembahasan": "Tidak ada penghubung langsung yang valid antara kelompok Pria dan Dokter."},
    {"soal": "Semua mahasiswa membawa laptop. Sebagian mahasiswa bersepeda. Maka...", "opsi": ["Semua yang membawa laptop bersepeda", "Sebagian yang bersepeda membawa laptop", "Sebagian mahasiswa tidak membawa laptop", "Semua bersepeda membawa laptop"], "jawaban": 1, "pembahasan": "Kelompok irisan (Sebagian mahasiswa) pasti memenuhi kedua syarat (bersepeda dan bawa laptop)."},
    {"soal": "Tidak ada harimau makan rumput. Semua kuda makan rumput. Maka...", "opsi": ["Beberapa kuda makan harimau", "Tidak ada kuda yang makan harimau", "Tidak ada harimau yang berupa kuda", "Harimau dan kuda tidak berteman"], "jawaban": 2, "pembahasan": "Kelompok Harimau dan Kuda saling terpisah mutlak berdasarkan makanan mereka."},
    {"soal": "Jika cuaca cerah, Andi berenang. Jika berenang, ia senang. Hari ini Andi tidak senang. Maka...", "opsi": ["Cuaca cerah", "Andi berenang", "Cuaca tidak cerah", "Andi malas berenang"], "jawaban": 2, "pembahasan": "Akibat akhir batal (tidak senang), berarti sebab awalnya juga batal (cuaca tidak cerah)."},
    {"soal": "Penyakit : Dokter = Mesin Rusak : ...", "opsi": ["Pabrik", "Oli", "Montir", "Listrik"], "jawaban": 2, "pembahasan": "Dokter memperbaiki penyakit, Montir memperbaiki mesin rusak."},
    {"soal": "Kecebong : Katak = Ulat : ...", "opsi": ["Daun", "Kepompong", "Kupu-kupu", "Bulu"], "jawaban": 2, "pembahasan": "Bentuk bayi/larva menjadi bentuk dewasa akhir."},
    {"soal": "Suhu : Termometer = Gempa : ...", "opsi": ["Richter", "Tsunami", "Seismograf", "Vulkanik"], "jawaban": 2, "pembahasan": "Suhu diukur dengan termometer, gempa diukur dengan seismograf."},
    {"soal": "Matahari : Terang = Api : ...", "opsi": ["Merah", "Panas", "Asap", "Kayu"], "jawaban": 1, "pembahasan": "Matahari menghasilkan sifat terang, api menghasilkan sifat panas."},
    {"soal": "Pengacara : Hukum = Guru : ...", "opsi": ["Sekolah", "Pendidikan", "Buku", "Murid"], "jawaban": 1, "pembahasan": "Profesi dan bidang ilmu utamanya."},
    {"soal": "1️⃣ ⚪⚫ \n 2️⃣ ⚪⚪⚫ \n 3️⃣ ⚪⚪⚪⚫ \n ➡️ ❓", "opsi": ["⚪⚪⚫⚫", "⚪⚪⚪⚪⚫", "⚪⚪⚫⚪", "⚫⚪⚪⚪"], "jawaban": 1, "pembahasan": "Lingkaran putih terus bertambah 1 di sebelah kiri."},
    {"soal": "1️⃣ ↖️ \n 2️⃣ ↗️ \n 3️⃣ ↘️ \n ➡️ ❓", "opsi": ["↖️", "↗️", "↘️", "↙️"], "jawaban": 3, "pembahasan": "Panah miring berputar 90 derajat searah jarum jam."},
    {"soal": "1️⃣ ➖ \n 2️⃣ ➕ \n 3️⃣ ⨹ \n ➡️ ❓", "opsi": ["➖", "➕", "⨹", "⨰"], "jawaban": 3, "pembahasan": "Penambahan garis perpotongan di pusat."},
    {"soal": "🔠 **M** 🪞 ❓ (Dicerminkan secara vertikal)", "opsi": ["W", "N", "M", "E"], "jawaban": 2, "pembahasan": "Huruf M simetris, dicerminkan tetap M."},
    {"soal": "A duduk depan B. C samping B. D depan C. Siapa di samping A?", "opsi": ["A", "B", "C", "D"], "jawaban": 3, "pembahasan": "Baris depan: A dan D. Baris belakang: B dan C."},
    {"soal": "Buku TPA lebih tebal dari Psikotes. Buku Matematika lebih tebal dari TPA. Paling tipis?", "opsi": ["TPA", "Psikotes", "Matematika", "Sama"], "jawaban": 1, "pembahasan": "Urutan tebal: Matematika - TPA - Psikotes(tipis)."},
    {"soal": "Piket: Senin, Selasa, Rabu. A tidak mau Rabu. B selalu Senin. Kapan C piket?", "opsi": ["Senin", "Selasa", "Rabu", "Kamis"], "jawaban": 2, "pembahasan": "B (Senin). Sisa Selasa & Rabu. A tidak mau Rabu, jadi A (Selasa). Maka C (Rabu)."},
    {"soal": "Anton lebih cepat dari Budi. Budi sama dengan Cici. Doni lebih lambat dari Cici. Paling lambat?", "opsi": ["Anton", "Budi", "Cici", "Doni"], "jawaban": 3, "pembahasan": "Doni berada di bawah kecepatan Budi dan Cici yang setara."},
    {"soal": "Antrian: Tono di depan Tini. Tini di depan Tino. Budi di depan Tono. Paling depan?", "opsi": ["Tono", "Tini", "Tino", "Budi"], "jawaban": 3, "pembahasan": "Budi - Tono - Tini - Tino."},
    {"soal": "1️⃣ 🟩🔺 \n 2️⃣ 🟩🟩🔺 \n 3️⃣ 🟩🟩🟩🔺 \n ➡️ ❓", "opsi": ["🟩🟩🟩🟩🔺", "🟩🟩🔺🔺", "🟩🔺🟩🔺", "🔺🔺🔺🟩"], "jawaban": 0, "pembahasan": "Penambahan 1 kotak hijau setiap tahap."}
]

soal_twk = [
    {"soal": "Sila ke-4 Pancasila mengajarkan kita untuk mengutamakan musyawarah. Dalam kehidupan sehari-hari, hal ini paling tepat diterapkan saat...", "opsi": ["Menentukan menu makan siang", "Memilih ketua RT", "Menentukan tempat liburan pribadi", "Membeli barang kebutuhan pokok", "Tidur siang"], "jawaban": 1, "pembahasan": "Musyawarah dilakukan untuk keputusan bersama."},
    {"soal": "Menggunakan produk dalam negeri merupakan wujud dari nilai Pancasila ke...", "opsi": ["1", "2", "3", "4", "5"], "jawaban": 2, "pembahasan": "Sila ke-3 (Persatuan Indonesia) mencakup rasa cinta tanah air."},
    {"soal": "Tujuan utama dari amandemen UUD 1945 adalah untuk...", "opsi": ["Memperluas kekuasaan Presiden", "Menyesuaikan aturan dasar dengan perkembangan zaman", "Mengubah bentuk negara", "Membubarkan MPR", "Mengganti ideologi"], "jawaban": 1, "pembahasan": "Amandemen menyempurnakan aturan dasar, bukan mengubah dasar negara."},
    {"soal": "Sikap yang mencerminkan integritas tinggi di tempat kerja adalah...", "opsi": ["Datang tepat waktu saat diawasi", "Menyelesaikan tugas walau tidak diawasi", "Membawa pulang fasilitas kantor", "Menutupi kesalahan teman", "Mengabaikan SOP"], "jawaban": 1, "pembahasan": "Integritas adalah keselarasan perbuatan dengan kejujuran meski tanpa pengawasan."},
    {"soal": "Bhinneka Tunggal Ika tertulis pada pita burung Garuda. Berasal dari kitab...", "opsi": ["Negarakertagama", "Sutasoma", "Arjunawiwaha", "Pararaton", "Bharatayuddha"], "jawaban": 1, "pembahasan": "Karangan Mpu Tantular pada masa Majapahit."},
    {"soal": "Hak asasi manusia diatur secara khusus pada pasal...", "opsi": ["27", "28A-28J", "29", "30", "31"], "jawaban": 1, "pembahasan": "Pasal 28A sampai 28J adalah hasil amandemen yang merinci HAM."},
    {"soal": "Asas wawasan nusantara berarti cara pandang bangsa terhadap...", "opsi": ["Negara lain", "Masa lalu", "Diri dan lingkungannya", "Perekonomian", "Teknologi"], "jawaban": 2, "pembahasan": "Cara pandang terhadap diri dan lingkungan sebagai satu kesatuan."},
    {"soal": "Paham radikalisme melanggar prinsip...", "opsi": ["Keadilan ekonomi", "Toleransi dan kemanusiaan", "Demokrasi", "Musyawarah", "Pemilu"], "jawaban": 1, "pembahasan": "Radikalisme melanggar nilai Sila ke-2 (Kemanusiaan)."},
    {"soal": "Yang memegang kekuasaan yudikatif adalah...", "opsi": ["Presiden", "DPR", "MA, MK, dan KY", "BPK", "KPU"], "jawaban": 2, "pembahasan": "Yudikatif adalah kekuasaan kehakiman."},
    {"soal": "Pengakuan kemerdekaan Indonesia pertama kali diberikan oleh...", "opsi": ["Belanda", "Australia", "Mesir", "India", "AS"], "jawaban": 2, "pembahasan": "Mesir mengakui secara de facto."},
    {"soal": "Sumpah Pemuda 1928 bermakna...", "opsi": ["Membentuk TNI", "Tonggak persatuan pemuda", "Deklarasi merdeka", "Membentuk partai", "Membela Belanda"], "jawaban": 1, "pembahasan": "Menyatukan pemuda berbagai daerah."},
    {"soal": "Pancasila sebagai dasar negara berarti...", "opsi": ["Alat kekuasaan", "Sumber dari segala sumber hukum", "Panduan ekonomi", "Simbol di luar negeri", "Ideologi tertutup"], "jawaban": 1, "pembahasan": "Semua hukum harus bersumber pada Pancasila."},
    {"soal": "Prinsip politik luar negeri Indonesia adalah...", "opsi": ["Blok Barat", "Blok Timur", "Bebas Aktif", "Isolasi", "Ketergantungan"], "jawaban": 2, "pembahasan": "Bebas menentukan sikap dan aktif menjaga perdamaian."},
    {"soal": "Pasal 30 UUD 1945 mengatur tentang...", "opsi": ["Pendidikan", "Pertahanan dan keamanan", "Pajak", "Pemilu", "Agama"], "jawaban": 1, "pembahasan": "Bela negara adalah hak dan kewajiban."},
    {"soal": "Kebebasan pers dijamin asalkan...", "opsi": ["Mengkritik pemerintah", "Memihak partai", "Bertanggung jawab secara hukum", "Menghibur", "Mendapat izin"], "jawaban": 2, "pembahasan": "Harus diiringi tanggung jawab."},
    {"soal": "Bukan elemen integritas nasional...", "opsi": ["Kejujuran", "Nepotisme", "Disiplin", "Tanggung Jawab", "Adil"], "jawaban": 1, "pembahasan": "Nepotisme merusak integritas."},
    {"soal": "Wewenang MK adalah...", "opsi": ["Mengadili koruptor", "Menguji UU terhadap UUD", "Memilih DPR", "Memberi grasi", "Melantik Presiden"], "jawaban": 1, "pembahasan": "Judicial Review ada di MK."},
    {"soal": "Sistem demokrasi Indonesia berdasarkan...", "opsi": ["Voting", "Militer", "Pancasila", "Otoriter", "Liberal"], "jawaban": 2, "pembahasan": "Demokrasi yang mengutamakan mufakat."},
    {"soal": "Contoh bela negara warga sipil...", "opsi": ["Wajib militer", "Menyebar hoaks", "Membayar pajak", "Melanggar hukum", "Apatis"], "jawaban": 2, "pembahasan": "Pajak membantu negara."},
    {"soal": "Pencipta Indonesia Raya...", "opsi": ["W.R. Supratman", "Ibu Sud", "Ismail Marzuki", "Kusbini", "C. Simanjuntak"], "jawaban": 0, "pembahasan": "Diperdengarkan pada Sumpah Pemuda."},
    {"soal": "Pemeriksa keuangan negara adalah...", "opsi": ["KPK", "BI", "BPK", "OJK", "Kejaksaan"], "jawaban": 2, "pembahasan": "Badan Pemeriksa Keuangan."},
    {"soal": "Toleransi beragama ditunjukkan dengan...", "opsi": ["Ikut ibadah", "Membiarkan orang beribadah", "Mencampur agama", "Menutup gereja", "Berdebat"], "jawaban": 1, "pembahasan": "Saling menghargai."},
    {"soal": "Amandemen UUD dilakukan oleh...", "opsi": ["Presiden", "DPR", "MPR", "MK", "MA"], "jawaban": 2, "pembahasan": "Hanya MPR yang berhak."},
    {"soal": "Korupsi melanggar Sila ke...", "opsi": ["1", "2", "3", "4", "5"], "jawaban": 4, "pembahasan": "Merampas hak orang banyak (Keadilan Sosial)."},
    {"soal": "Sifat UUD 1945...", "opsi": ["Singkat dan fleksibel", "Panjang kaku", "Mudah diubah", "Tidak mengikat", "Adat"], "jawaban": 0, "pembahasan": "Memuat aturan pokok saja."},
    {"soal": "Pengamalan Pancasila objektif...", "opsi": ["Dihafal", "Diterapkan di pemerintahan", "Sikap pribadi", "Pajangan", "Sekolah"], "jawaban": 1, "pembahasan": "Terkait penyelenggaraan negara."},
    {"soal": "Usulan ditolak di rapat RT, sikap Anda...", "opsi": ["Marah", "Menerima lapang dada", "Menggugat", "Menolak hasil", "Diam"], "jawaban": 1, "pembahasan": "Menjunjung tinggi mufakat."},
    {"soal": "Hari Kesaktian Pancasila...", "opsi": ["1 Juni", "17 Agt", "30 Sept", "1 Okt", "10 Nov"], "jawaban": 3, "pembahasan": "Pasca G30S/PKI."},
    {"soal": "Bendera negara diatur pada Pasal...", "opsi": ["35", "36", "36A", "36B", "36C"], "jawaban": 0, "pembahasan": "Pasal 35: Bendera Merah Putih."},
    {"soal": "Membahayakan persatuan, KECUALI...", "opsi": ["Primordialisme", "Etnosentrisme", "Chauvinisme", "Patriotisme", "Separatisme"], "jawaban": 3, "pembahasan": "Patriotisme adalah cinta tanah air."}
]

soal_tiu = [
    {"soal": "85 + 15 x 2 - 10 = ...", "opsi": ["105", "190", "115", "100", "95"], "jawaban": 0, "pembahasan": "(15x2)=30. 85+30-10 = 105."},
    {"soal": "0,25 + 3/4 = ...", "opsi": ["0,5", "0,75", "1", "1,25", "1,5"], "jawaban": 2, "pembahasan": "3/4 = 0,75. 0,25 + 0,75 = 1."},
    {"soal": "2, 4, 8, 16, 32, ...", "opsi": ["48", "54", "64", "72", "80"], "jawaban": 2, "pembahasan": "Pola dikali 2."},
    {"soal": "3, 5, 8, 12, 17, ...", "opsi": ["21", "22", "23", "24", "25"], "jawaban": 2, "pembahasan": "Penambahan naik: +2, +3, +4, +5, selanjutnya +6. 17+6=23."},
    {"soal": "Uang Rp 150.000, beli 3 kg telur (Rp 28.000/kg). Sisa?", "opsi": ["56.000", "66.000", "76.000", "86.000", "96.000"], "jawaban": 1, "pembahasan": "150k - 84k = 66k."},
    {"soal": "10 pekerja = 6 hari. Agar 4 hari butuh berapa pekerja total?", "opsi": ["12", "15", "18", "20", "24"], "jawaban": 1, "pembahasan": "10x6 = Px4. P = 15."},
    {"soal": "Baju diskon 20%, bayar Rp 80.000. Harga awal?", "opsi": ["90.000", "100.000", "120.000", "150.000", "160.000"], "jawaban": 1, "pembahasan": "80% = 80rb. 100% = 100rb."},
    {"soal": "Jarak 150 km, 50 km/jam. Berangkat 08.00, tiba?", "opsi": ["10.00", "10.30", "11.00", "11.30", "12.00"], "jawaban": 2, "pembahasan": "Waktu 3 jam. 08.00 + 3 = 11.00."},
    {"soal": "SINONIM: Evokasi =", "opsi": ["Penggugah", "Nilai", "Ubah", "Fungsi", "Saran"], "jawaban": 0, "pembahasan": "Daya penggugah."},
    {"soal": "ANTONIM: Skeptis ><", "opsi": ["Ragu", "Yakin", "Cemas", "Takut", "Berani"], "jawaban": 1, "pembahasan": "Skeptis = ragu."},
    {"soal": "Mobil : Bensin = Pelari : ...", "opsi": ["Trek", "Sepatu", "Makan", "Lari", "Juara"], "jawaban": 2, "pembahasan": "Sumber energi."},
    {"soal": "Buku : Perpustakaan = ... : ...", "opsi": ["Uang : Bank", "Dokter : RS", "Guru : Sekolah", "Pohon : Hutan", "Baju : Lemari"], "jawaban": 0, "pembahasan": "Tempat penyimpanan khusus."},
    {"soal": "Semua A adalah B. Beberapa B adalah C. Kesimpulan?", "opsi": ["Semua A = C", "Beberapa A = C", "Semua C = A", "Beberapa C != A", "Tidak ada"], "jawaban": 4, "pembahasan": "Tidak ada irisan pasti."},
    {"soal": "Hujan -> licin -> macet. Tidak macet. Maka...", "opsi": ["Deras", "Licin", "Tidak hujan", "Polisi", "Sepi"], "jawaban": 2, "pembahasan": "Modus Tollens mundur."},
    {"soal": "Budi > Andi. Cici < Andi. Paling pendek?", "opsi": ["Budi", "Andi", "Cici", "Sama", "Gak tau"], "jawaban": 2, "pembahasan": "Budi - Andi - Cici."},
    {"soal": "120% dari 50...", "opsi": ["55", "60", "65", "70", "75"], "jawaban": 1, "pembahasan": "1.2 x 50 = 60."},
    {"soal": "A 6 jam, B 3 jam. Bersama?", "opsi": ["1 jam", "2 jam", "3 jam", "4 jam", "5 jam"], "jawaban": 1, "pembahasan": "1/6 + 1/3 = 3/6 -> 2 jam."},
    {"soal": "1, 4, 9, 16, 25, ...", "opsi": ["30", "32", "36", "42", "49"], "jawaban": 2, "pembahasan": "Kuadrat (6^2)."},
    {"soal": "2X + 5 = 15. X = ...", "opsi": ["3", "4", "5", "6", "7"], "jawaban": 2, "pembahasan": "2X = 10 -> X=5."},
    {"soal": "A belakang B. C depan B. D belakang A. E depan C. Paling depan?", "opsi": ["E", "C", "B", "A", "D"], "jawaban": 0, "pembahasan": "E - C - B - A - D."},
    {"soal": "10.000 ke 12.000 naik berapa %?", "opsi": ["10", "15", "20", "25", "30"], "jawaban": 2, "pembahasan": "2000/10000 = 20%."},
    {"soal": "Rata-rata 5, 7, 9, 11...", "opsi": ["7", "8", "9", "10", "11"], "jawaban": 1, "pembahasan": "32/4 = 8."},
    {"soal": "Fiktif =", "opsi": ["Nyata", "Asli", "Imajinasi", "Akurat", "Valid"], "jawaban": 2, "pembahasan": "Khayalan."},
    {"soal": "Hidung : Mencium = Telinga : ...", "opsi": ["Melihat", "Mendengar", "Raba", "Napas", "Suara"], "jawaban": 1, "pembahasan": "Fungsi indera."},
    {"soal": "Lahir Jakarta -> Betawi. Budi lahir Jakarta. Maka...", "opsi": ["Tidak Betawi", "Jawa", "Bisa Betawi", "Mungkin Betawi", "Gak tau"], "jawaban": 2, "pembahasan": "Silogisme mutlak."},
    {"soal": "1/2 : 1/4 = ...", "opsi": ["1/8", "1/4", "1/2", "1", "2"], "jawaban": 4, "pembahasan": "1/2 x 4 = 2."},
    {"soal": "Akar 625...", "opsi": ["15", "20", "25", "30", "35"], "jawaban": 2, "pembahasan": "25x25 = 625."},
    {"soal": "3 jam 45 menit = ... detik", "opsi": ["12000", "12500", "13000", "13500", "14000"], "jawaban": 3, "pembahasan": "225 x 60 = 13500."},
    {"soal": "Kubus rusuk 4 cm. Volume?", "opsi": ["16", "32", "48", "64", "128"], "jawaban": 3, "pembahasan": "4x4x4 = 64."},
    {"soal": "Konkret ><", "opsi": ["Nyata", "Jelas", "Abstrak", "Bentuk", "Padat"], "jawaban": 2, "pembahasan": "Konkret = berwujud."},
    {"soal": "Pola: 1 titik, 2 titik, 3 titik...", "opsi": ["1", "2", "3", "4", "5"], "jawaban": 3, "pembahasan": "Deret nambah 1."},
    {"soal": "0.1 x 0.1 =", "opsi": ["0.1", "0.01", "0.001", "1", "10"], "jawaban": 1, "pembahasan": "Dua angka di belakang koma."},
    {"soal": "100 dikurangi 25%...", "opsi": ["25", "50", "75", "100", "125"], "jawaban": 2, "pembahasan": "Sisa 75."},
    {"soal": "A, C, E, G, ...", "opsi": ["H", "I", "J", "K", "L"], "jawaban": 1, "pembahasan": "Lompat 1 huruf."},
    {"soal": "10 km dalam 15 menit. Kecepatan /jam?", "opsi": ["20", "30", "40", "50", "60"], "jawaban": 2, "pembahasan": "10 / (1/4) = 40."}
]

soal_tkp = [
    {"soal": "Sistem IT kantor mati total. Tindakan Anda...", "opsi": ["Pulang", "Marah", "Main HP", "Merapikan meja/arsip fisik", "Tidur"], "skor": [1, 2, 3, 5, 1]},
    {"soal": "Ada aturan datang 15 menit awal. Anda...", "opsi": ["Tolak", "Protes", "Patuhi terpaksa", "Taati sbg profesional", "Abaikan"], "skor": [1, 2, 3, 5, 1]},
    {"soal": "Pelanggan tanya layanan yg Anda tidak tahu. Anda...", "opsi": ["Asal jawab", "Tolak", "Kasih brosur", "Tanya rekan yg tahu", "Kabur"], "skor": [2, 1, 3, 5, 1]},
    {"soal": "Tim gagal, ketua salahkan Anda...", "opsi": ["Balas salah", "Diam", "Jelaskan tanpa emosi", "Resign", "Nangis"], "skor": [2, 3, 5, 1, 1]},
    {"soal": "Teman pakai wifi kantor buat nonton film...", "opsi": ["Ikut nonton", "Biarin", "Tegur sopan", "Lapor bos", "Putus kabel"], "skor": [2, 3, 5, 4, 1]},
    {"soal": "Harus lembur padahal janji keluarga...", "opsi": ["Pulang", "Lembur HP mati", "Telepon kluarga & lanjut kerja", "Kerja asal", "Suruh teman"], "skor": [1, 2, 5, 3, 2]},
    {"soal": "Tugas pakai aplikasi baru...", "opsi": ["Tolak", "Minta ganti", "Ngeluh", "Belajar cepat", "Pakai cara lama"], "skor": [1, 2, 1, 5, 3]},
    {"soal": "Beda divisi minta data rahasia...", "opsi": ["Kasih", "Tolak sesuai SOP", "Minta bayar", "Pura-pura budek", "Lapor polisi"], "skor": [1, 5, 1, 3, 2]},
    {"soal": "Pindah ke cabang terpencil...", "opsi": ["Resign", "Tolak", "Minta naik gaji", "Terima sbg tantangan", "Ngeluh terus"], "skor": [1, 2, 3, 5, 2]},
    {"soal": "Teman puasa, Anda bawa makanan...", "opsi": ["Makan depannya", "Makan di tempat lain", "Tawari", "Ikut puasa", "Marahin"], "skor": [2, 5, 1, 3, 1]},
    {"soal": "Pelanggan marah antrian...", "opsi": ["Abaikan", "Balas marah", "Panggil satpam", "Jelaskan sabar", "Kasih nomor baru"], "skor": [1, 2, 3, 5, 4]},
    {"soal": "Aturan pakai cloud...", "opsi": ["Pakai kertas", "Suruh junior", "Patuhi pasif", "Minta ajarin istirahat", "Belajar dr Youtube sepulang kerja"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Tugas tambahan atasan...", "opsi": ["Tolak", "Asal jadi", "Tunda rutin", "Lembur", "Atur prioritas siang ini"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Teman telat terus...", "opsi": ["Biarin", "Lapor bos", "Ambil alih", "Tegur personal", "Gosipin"], "skor": [1, 4, 3, 5, 2]},
    {"soal": "Nemu dompet isi uang...", "opsi": ["Biarin", "Ambil dikit", "Kasih satpam", "Simpan", "Hubungi pemilik"], "skor": [2, 1, 4, 3, 5]},
    {"soal": "Kebijakan baru ribet...", "opsi": ["Abaikan", "Protes keras", "Patuhi pasrah", "Cari kelemahan", "Usul perbaikan ke bos dgn data"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Tim baru beda suku...", "opsi": ["Minta pindah", "Menyendiri", "Sopan seperlunya", "Berbaur umum", "Pelajari budaya mrk"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Lansia datang pas mau tutup...", "opsi": ["Tolak", "Suruh ke loket lain", "Layan terpaksa", "Manual", "Layan ramah tuntas"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Teman gak bisa mesin baru...", "opsi": ["Biarin mandiri", "Ketawain", "Kerjain buat dia", "Kasih buku manual", "Bimbing langsung"], "skor": [2, 1, 3, 4, 5]},
    {"soal": "Seminar membosankan...", "opsi": ["Tidur", "Main HP", "Kabur", "Dengar seadanya", "Fokus catat sbg amanah"], "skor": [1, 2, 1, 4, 5]},
    {"soal": "Rekan sakit, kerjanya numpuk...", "opsi": ["Biarin", "Tunggu bos", "Bantu sikit", "Bantu tuntas", "Protes"], "skor": [1, 2, 3, 5, 1]},
    {"soal": "Ada uang lebih di kasir...", "opsi": ["Ambil", "Diemin", "Kasih teman", "Lapor jujur", "Buat jajan"], "skor": [1, 1, 1, 5, 1]},
    {"soal": "Tamu penting datang tiba-tiba...", "opsi": ["Usir", "Suruh nunggu", "Cuek", "Sambut baik", "Panggil bos cepat"], "skor": [1, 2, 1, 5, 4]},
    {"soal": "Ditawari suap urus izin...", "opsi": ["Terima", "Minta lebih", "Ragu", "Tolak tegas", "Lapor polisi langsung"], "skor": [1, 1, 3, 5, 4]},
    {"soal": "Dikritik pedas saat rapat...", "opsi": ["Marah", "Nangis", "Bela diri keras", "Terima evaluasi", "Minta maaf & perbaiki"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Komputer rekan rusak...", "opsi": ["Sukurin", "Biarin", "Pinjemi laptop cadangan", "Bantu perbaiki", "Suruh beli baru"], "skor": [1, 2, 5, 4, 1]},
    {"soal": "Disuruh bohong demi instansi...", "opsi": ["Mau", "Nego", "Tolak", "Lapor publik", "Tolak sopan & cari solusi legal"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Anak buah bikin salah besar...", "opsi": ["Pecat", "Maki", "Bina", "Tutupi", "Ajak diskusi evaluasi"], "skor": [1, 1, 4, 2, 5]},
    {"soal": "Ada pelatihan gratis dari kantor...", "opsi": ["Gak ikut", "Ikut kalau dipaksa", "Ikut absen", "Ikut rajin", "Daftar antusias"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Jalanan macet parah...", "opsi": ["Ngeluh", "Bolos", "Telat wajar", "Cari jalan tikus", "Berangkat lebih awal besok"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Atasan sering marah tak jelas...", "opsi": ["Resign", "Lawan", "Diam nahan dendam", "Tetap kerja baik", "Ajak bicara empat mata baik-baik"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Lagi libur dihubungi bos...", "opsi": ["Matikan HP", "Abaikan", "Jawab kalau mood", "Bantu jarak jauh", "Langsung ke kantor"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Rekan curi ide Anda...", "opsi": ["Pukul", "Sindirin", "Lapor bos emosi", "Klarifikasi 4 mata", "Diam saja"], "skor": [1, 2, 3, 5, 1]},
    {"soal": "Dapat fasilitas mobil dinas...", "opsi": ["Pakai pribadi", "Kasih istri", "Jual", "Pakai kerja dinas saja", "Rawat baik-baik"], "skor": [1, 1, 1, 4, 5]},
    {"soal": "Listrik kantor padam tiba-tiba...", "opsi": ["Pulang", "Tidur", "Gosip", "Cek genset/tunggu lampu", "Lanjut kerja manual"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Ada berita viral soal instansi...", "opsi": ["Ikut share", "Komen benci", "Diam", "Bela membabi buta", "Cari fakta valid"], "skor": [1, 1, 3, 2, 5]},
    {"soal": "Sering lembur bikin sakit...", "opsi": ["Salahin bos", "Resign", "Bolos", "Minum obat", "Atur pola sehat & time management"], "skor": [1, 2, 2, 3, 5]},
    {"soal": "Rekan suka gosip...", "opsi": ["Ikut", "Dengerin", "Jauhi", "Tegur keras", "Beri nasehat baik & hindari"], "skor": [1, 2, 4, 3, 5]},
    {"soal": "Proyek butuh dana besar, budget minim...", "opsi": ["Batalin", "Minta donasi paksa", "Nombok", "Cari sponsor", "Optimasi budget efisien"], "skor": [1, 1, 3, 4, 5]},
    {"soal": "Ketua tim pilih kasih...", "opsi": ["Demo", "Resign", "Ngeluh", "Tunjuk prestasi", "Ajak bicara profesional"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Terjadi beda pendapat keras di tim...", "opsi": ["Keluar tim", "Ikut ribut", "Diam aman", "Pisahkan", "Fasilitasi mediasi"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Internet mati saat deadline...", "opsi": ["Panik", "Nangis", "Salahin provider", "Tethering HP pribadi", "Cari wifi terdekat segera"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Mendapat promosi tapi teman iri...", "opsi": ["Sombong", "Jauhi", "Biasa saja", "Traktir paksa", "Tetap rendah hati & rangkul"], "skor": [1, 2, 3, 2, 5]},
    {"soal": "Disuruh atasan beli barang pribadi...", "opsi": ["Marah", "Tolak", "Lapor HRD", "Beli dgn ikhlas jika luang", "Tolak halus krn bukan tupoksi"], "skor": [2, 3, 4, 1, 5]},
    {"soal": "Pekerjaan monoton tiap hari...", "opsi": ["Bosankan", "Kerja lambat", "Main game", "Inovasi cara kerja baru", "Tetap fokus"], "skor": [1, 2, 1, 5, 4]}
]

# ==========================================
# 2. INISIALISASI STATE
# ==========================================
if 'ujian_dimulai' not in st.session_state:
    st.session_state.ujian_dimulai = False
if 'waktu_mulai' not in st.session_state:
    st.session_state.waktu_mulai = 0
if 'waktu_selesai' not in st.session_state:
    st.session_state.waktu_selesai = 0
if 'telah_submit' not in st.session_state:
    st.session_state.telah_submit = False
if 'pilihan_paket' not in st.session_state:
    st.session_state.pilihan_paket = "Paket 1: TIU Dasar (50 Soal)"
if 'jawaban_user' not in st.session_state:
    st.session_state.jawaban_user = {}

# ==========================================
# 3. LOGIKA UI: MENU UTAMA (SEBELUM UJIAN)
# ==========================================
if not st.session_state.ujian_dimulai:
    st.title("📚 Pusat Pelatihan TPA & SKD Nasional")
    st.markdown("---")
    
    st.session_state.pilihan_paket = st.radio(
        "Pilih Modul Ujian (Semua Soal Sudah Diperbarui Penuh):",
        [
            "Paket 1: TIU Dasar (50 Soal / 60 Menit)", 
            "Paket 2: TIU Lanjutan (50 Soal / 60 Menit)", 
            "Paket 3: SKD Nasional Lengkap (110 Soal / 100 Menit)"
        ]
    )
    
    if st.button("🚀 MULAI UJIAN SEKARANG", use_container_width=True):
        st.session_state.ujian_dimulai = True
        st.session_state.waktu_mulai = time.time()
        st.session_state.telah_submit = False 
        st.session_state.jawaban_user = {}
        st.rerun()

# ==========================================
# 4. LOGIKA UI: SAAT UJIAN BERJALAN
# ==========================================
else:
    if not st.session_state.telah_submit:
        
        # --- A. PENGATURAN WAKTU & TIMER ---
        if "Paket 3" in st.session_state.pilihan_paket:
            durasi_ujian = 6000  # 100 Menit
        else:
            durasi_ujian = 3600  # 60 Menit
            
        waktu_berjalan = time.time() - st.session_state.waktu_mulai
        sisa_waktu_detik = int(durasi_ujian - waktu_berjalan)
        
        js_timer = f"""
        <script>
            var sisaWaktu = {sisa_waktu_detik};
            var parentDoc = window.parent.document;
            var timerElement = parentDoc.getElementById('custom_timer_display');
            
            if (!timerElement) {{
                timerElement = parentDoc.createElement('div');
                timerElement.id = 'custom_timer_display';
                timerElement.style.cssText = 'position: fixed; bottom: 20px; right: 20px; background-color: #2e7bcf; color: white; padding: 12px 20px; border-radius: 8px; font-weight: bold; font-family: sans-serif; z-index: 9999; box-shadow: 0px 4px 10px rgba(0,0,0,0.3); border: 2px solid white;';
                parentDoc.body.appendChild(timerElement);
            }}
            
            if (parentDoc.timerInterval) {{ clearInterval(parentDoc.timerInterval); }}
            
            parentDoc.timerInterval = setInterval(function() {{
                sisaWaktu--;
                var minutes = Math.floor(sisaWaktu / 60);
                var seconds = sisaWaktu % 60;
                var m = minutes < 10 ? "0" + minutes : minutes;
                var s = seconds < 10 ? "0" + seconds : seconds;
                
                timerElement.innerHTML = "⏳ Sisa Waktu: " + m + ":" + s;
                
                if (sisaWaktu <= 0) {{
                    clearInterval(parentDoc.timerInterval);
                    timerElement.innerHTML = "WAKTU HABIS!";
                    timerElement.style.backgroundColor = "black";
                    var buttons = parentDoc.querySelectorAll('button');
                    for (var i = 0; i < buttons.length; i++) {{
                        if (buttons[i].innerText.includes('Kumpulkan Jawaban')) {{ buttons[i].click(); break; }}
                    }}
                }}
            }}, 1000);
        </script>
        """
        components.html(js_timer, height=0, width=0)

        # --- B. RENDER SOAL (DENGAN PENOMORAN OTOMATIS BERURUTAN) ---
        st.subheader(f"Mengerjakan: {st.session_state.pilihan_paket}")
        st.markdown("---")
        
        with st.form(key='form_ujian'):
            jawaban_sementara = {}
            
            if "Paket 1" in st.session_state.pilihan_paket or "Paket 2" in st.session_state.pilihan_paket:
                soal_aktif = soal_paket_1 if "Paket 1" in st.session_state.pilihan_paket else soal_paket_2
                for i, item in enumerate(soal_aktif):
                    st.markdown(f"**{i+1}. {item['soal']}**")
                    pilihan = st.radio(label=f"Soal {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"tiu_{i}")
                    jawaban_sementara[f"tiu_{i}"] = pilihan
                    st.write("")
                    
            elif "Paket 3" in st.session_state.pilihan_paket:
                st.markdown("#### Bagian I: TWK (Tes Wawasan Kebangsaan)")
                # Nomor urut TWK dari 1 - 30
                for i, item in enumerate(soal_twk):
                    nomor_soal = i + 1
                    st.markdown(f"**{nomor_soal}. {item['soal']}**")
                    pilihan = st.radio(label=f"TWK {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"twk_{i}")
                    jawaban_sementara[f"twk_{i}"] = pilihan
                    st.write("")
                    
                st.markdown("#### Bagian II: TIU (Tes Intelegensia Umum)")
                # Nomor urut TIU melompat secara otomatis melanjutkan TWK (Mulai 31)
                offset_tiu = len(soal_twk)
                for i, item in enumerate(soal_tiu):
                    nomor_soal = offset_tiu + i + 1
                    st.markdown(f"**{nomor_soal}. {item['soal']}**")
                    pilihan = st.radio(label=f"TIU {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"tiu_skd_{i}")
                    jawaban_sementara[f"tiu_skd_{i}"] = pilihan
                    st.write("")
                    
                st.markdown("#### Bagian III: TKP (Tes Karakteristik Pribadi)")
                # Nomor urut TKP melompat melanjutkan TIU (Mulai 66)
                offset_tkp = offset_tiu + len(soal_tiu)
                for i, item in enumerate(soal_tkp):
                    nomor_soal = offset_tkp + i + 1
                    st.markdown(f"**{nomor_soal}. {item['soal']}**")
                    pilihan = st.radio(label=f"TKP {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"tkp_{i}")
                    jawaban_sementara[f"tkp_{i}"] = pilihan
                    st.write("")

            submit_button = st.form_submit_button(label='Kumpulkan Jawaban', use_container_width=True)

        # --- C. LOGIKA PENILAIAN ---
        if submit_button:
            st.session_state.waktu_selesai = time.time()
            st.session_state.telah_submit = True
            st.session_state.jawaban_user = jawaban_sementara
            
            if "Paket 1" in st.session_state.pilihan_paket or "Paket 2" in st.session_state.pilihan_paket:
                soal_aktif = soal_paket_1 if "Paket 1" in st.session_state.pilihan_paket else soal_paket_2
                benar = sum([1 for i, item in enumerate(soal_aktif) if jawaban_sementara.get(f"tiu_{i}") == item["opsi"][item["jawaban"]]])
                st.session_state.skor_tiu = (benar / len(soal_aktif)) * 100
                st.session_state.benar = benar
                st.session_state.salah = len(soal_aktif) - benar
                
            elif "Paket 3" in st.session_state.pilihan_paket:
                skor_twk, skor_tiu, skor_tkp = 0, 0, 0
                for i, item in enumerate(soal_twk):
                    if jawaban_sementara.get(f"twk_{i}") == item["opsi"][item["jawaban"]]: skor_twk += 5
                for i, item in enumerate(soal_tiu):
                    if jawaban_sementara.get(f"tiu_skd_{i}") == item["opsi"][item["jawaban"]]: skor_tiu += 5
                for i, item in enumerate(soal_tkp):
                    jawaban = jawaban_sementara.get(f"tkp_{i}")
                    if jawaban: skor_tkp += item["skor"][item["opsi"].index(jawaban)]
                        
                st.session_state.skor_twk = skor_twk
                st.session_state.skor_tiu = skor_tiu
                st.session_state.skor_tkp = skor_tkp

            st.rerun()

# ==========================================
# 5. LOGIKA UI: HASIL EVALUASI
# ==========================================
if st.session_state.telah_submit:
    remove_js = "<script>var timerElement = window.parent.document.getElementById('custom_timer_display'); if (timerElement) { timerElement.remove(); }</script>"
    components.html(remove_js, height=0, width=0)

    durasi_detik = int(st.session_state.waktu_selesai - st.session_state.waktu_mulai)
    if ("Paket 3" in st.session_state.pilihan_paket and durasi_detik >= 6000) or ("Paket 3" not in st.session_state.pilihan_paket and durasi_detik >= 3600):
        st.error("⏰ WAKTU HABIS! Jawaban dikumpulkan otomatis.")
    else:
        st.success(f"⏱️ Waktu Terpakai: {durasi_detik // 60} Menit {durasi_detik % 60} Detik")

    st.title("HASIL EVALUASI")
    st.markdown("---")

    if "Paket 1" in st.session_state.pilihan_paket or "Paket 2" in st.session_state.pilihan_paket:
        col1, col2, col3 = st.columns(3)
        col1.metric("Skor Total", f"{st.session_state.skor_tiu:g} / 100")
        col2.metric("Jawaban Benar", st.session_state.benar)
        col3.metric("Jawaban Salah/Kosong", st.session_state.salah)
        
        st.markdown("### Daftar Jawaban yang Salah:")
        soal_aktif = soal_paket_1 if "Paket 1" in st.session_state.pilihan_paket else soal_paket_2
        for i, item in enumerate(soal_aktif):
            j_user = st.session_state.jawaban_user.get(f"tiu_{i}")
            j_benar = item["opsi"][item["jawaban"]]
            if j_user != j_benar:
                with st.expander(f"Soal No. {i+1} (Salah)"):
                    st.write(f"**Soal:** {item['soal']}")
                    st.write(f"❌ **Jawabanmu:** {j_user if j_user else 'Kosong'}")
                    st.write(f"✅ **Jawaban Benar:** {j_benar}")
                    st.info(f"**Pembahasan:** {item['pembahasan']}")

    elif "Paket 3" in st.session_state.pilihan_paket:
        total_skor = st.session_state.skor_twk + st.session_state.skor_tiu + st.session_state.skor_tkp
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("SKOR TOTAL", f"{total_skor} / 550")
        col2.metric("TWK", f"{st.session_state.skor_twk} / 150")
        col3.metric("TIU", f"{st.session_state.skor_tiu} / 175")
        col4.metric("TKP", f"{st.session_state.skor_tkp} / 225")
        
        st.markdown("### Evaluasi TWK & TIU (Yang Salah)")
        offset_tiu = len(soal_twk)
        for i, item in enumerate(soal_twk):
            j_user = st.session_state.jawaban_user.get(f"twk_{i}")
            j_benar = item["opsi"][item["jawaban"]]
            if j_user != j_benar:
                with st.expander(f"TWK No. {i+1} (Salah)"):
                    st.write(f"**Soal:** {item['soal']}")
                    st.write(f"❌ **Jawabanmu:** {j_user if j_user else 'Kosong'}")
                    st.write(f"✅ **Jawaban Benar:** {j_benar}")
                    st.info(f"**Pembahasan:** {item['pembahasan']}")
        
        for i, item in enumerate(soal_tiu):
            j_user = st.session_state.jawaban_user.get(f"tiu_skd_{i}")
            j_benar = item["opsi"][item["jawaban"]]
            if j_user != j_benar:
                with st.expander(f"TIU No. {offset_tiu + i + 1} (Salah)"):
                    st.write(f"**Soal:** {item['soal']}")
                    st.write(f"❌ **Jawabanmu:** {j_user if j_user else 'Kosong'}")
                    st.write(f"✅ **Jawaban Benar:** {j_benar}")
                    st.info(f"**Pembahasan:** {item['pembahasan']}")
        
        st.markdown("### Evaluasi TKP (Tidak mendapat Poin Maksimal 5)")
        offset_tkp = offset_tiu + len(soal_tiu)
        for i, item in enumerate(soal_tkp):
            j_user = st.session_state.jawaban_user.get(f"tkp_{i}")
            poin = item["skor"][item["opsi"].index(j_user)] if j_user else 0
            if poin < 5:
                terbaik = item["opsi"][item["skor"].index(5)]
                with st.expander(f"TKP No. {offset_tkp + i + 1} (Poin: {poin}/5)"):
                    st.write(f"**Soal:** {item['soal']}")
                    st.write(f"**Pilihanmu:** {j_user if j_user else 'Kosong'}")
                    st.write(f"**Tindakan Terbaik (Poin 5):** {terbaik}")
                    if "pembahasan" in item: st.info(f"**Pembahasan:** {item['pembahasan']}")

    st.markdown("---")
    if st.button("Kembali ke Menu Utama"):
        st.session_state.ujian_dimulai = False
        st.session_state.telah_submit = False
        st.rerun()
