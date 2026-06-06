import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="Pusat Simulasi Ujian TPA & SKD", layout="wide")

# ==========================================
# 1. DATABASE SOAL (PAKET 1 & PAKET 2)
# ==========================================
soal_paket_1 = [
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
    {"soal": "11. Bentuk desimal dari 1/4 adalah...", "opsi": ["0.14", "0.25", "0.40", "0.50"], "jawaban": 1, "pembahasan": "1/4 sama dengan 25/100 atau 0.25."},
    {"soal": "12. 50% dari Rp 120.000 adalah...", "opsi": ["Rp 50.000", "Rp 60.000", "Rp 70.000", "Rp 100.000"], "jawaban": 1, "pembahasan": "50% sama dengan setengahnya. 120.000 / 2 = 60.000."},
    {"soal": "13. Pecahan paling sederhana dari 15/20 adalah...", "opsi": ["1/2", "2/3", "3/4", "4/5"], "jawaban": 2, "pembahasan": "Atas dan bawah sama-sama dibagi 5. Menjadi 3/4."},
    {"soal": "14. 0.5 + 1/2 = ...", "opsi": ["0.5", "1", "1.5", "2"], "jawaban": 1, "pembahasan": "1/2 adalah 0.5. Maka 0.5 + 0.5 = 1."},
    {"soal": "15. Diskon 20% untuk barang seharga Rp 50.000. Berapa potongannya?", "opsi": ["Rp 5.000", "Rp 10.000", "Rp 15.000", "Rp 20.000"], "jawaban": 1, "pembahasan": "(20/100) x 50.000 = 10.000."},
    {"soal": "16. 2, 4, 6, 8, ...", "opsi": ["9", "10", "11", "12"], "jawaban": 1, "pembahasan": "Pola ditambah 2."},
    {"soal": "17. 3, 9, 27, 81, ...", "opsi": ["162", "243", "324", "100"], "jawaban": 1, "pembahasan": "Pola dikali 3. 81 x 3 = 243."},
    {"soal": "18. 100, 95, 85, 70, 50, ...", "opsi": ["25", "30", "35", "40"], "jawaban": 0, "pembahasan": "Pola pengurangan bertingkat: -5, -10, -15, -20. Selanjutnya -25. 50 - 25 = 25."},
    {"soal": "19. 1, 1, 2, 3, 5, 8, ...", "opsi": ["10", "11", "12", "13"], "jawaban": 3, "pembahasan": "Deret Fibonacci (menjumlahkan 2 angka sebelumnya). 5 + 8 = 13."},
    {"soal": "20. 2, 3, 6, 15, 42, ...", "opsi": ["84", "100", "123", "144"], "jawaban": 2, "pembahasan": "Selisihnya adalah 1, 3, 9, 27 (dikali 3). Selisih berikutnya 81. 42 + 81 = 123."},
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
    {"soal": "31. Semua pegawai memakai seragam. Andi adalah pegawai. Maka...", "opsi": ["Andi mungkin memakai seragam", "Andi memakai seragam", "Andi bukan pegawai", "Sebagian pegawai memakai seragam"], "jawaban": 1, "pembahasan": "Andi masuk kelompok pegawai, aturannya mutlak."},
    {"soal": "32. Jika hujan, maka jalan basah. Hari ini jalan tidak basah. Maka...", "opsi": ["Hari ini hujan", "Hari ini mungkin hujan", "Hari ini tidak hujan", "Jalan kering karena panas"], "jawaban": 2, "pembahasan": "Modus Tollens: Akibat tidak ada, sebab tidak ada."},
    {"soal": "33. Semua dokter pintar. Sebagian dokter suka membaca. Maka...", "opsi": ["Semua yang pintar suka membaca", "Sebagian dokter pintar", "Sebagian dokter pintar dan suka membaca", "Semua dokter pintar suka membaca"], "jawaban": 2, "pembahasan": "'Semua' bertemu 'Sebagian' kesimpulan pasti 'Sebagian'."},
    {"soal": "34. Jika Budi lulus, dibelikan sepeda. Jika dibelikan sepeda, keliling kota. Budi tidak keliling kota. Maka...", "opsi": ["Budi lulus", "Budi tidak lulus", "Budi malas", "Budi dibelikan sepeda"], "jawaban": 1, "pembahasan": "Silogisme berantai mundur."},
    {"soal": "35. Tidak ada pelaut yang penakut. Beberapa nelayan adalah penakut. Maka...", "opsi": ["Beberapa nelayan bukan pelaut", "Semua nelayan adalah pelaut", "Beberapa pelaut adalah nelayan", "Tidak ada nelayan yang berani"], "jawaban": 0, "pembahasan": "Nelayan penakut otomatis bukan pelaut."},
    {"soal": "36. Lapar : Makan = Haus : ...", "opsi": ["Air", "Minum", "Gelas", "Es"], "jawaban": 1, "pembahasan": "Jika lapar butuh makan, jika haus butuh minum."},
    {"soal": "37. Kayu : Lemari = Kain : ...", "opsi": ["Kapas", "Baju", "Jahit", "Benang"], "jawaban": 1, "pembahasan": "Kayu adalah bahan lemari. Kain adalah bahan baju."},
    {"soal": "38. Masinis : Kereta Api = Nahkoda : ...", "opsi": ["Pesawat", "Mobil", "Kapal Laut", "Bus"], "jawaban": 2, "pembahasan": "Masinis menyetir kereta. Nahkoda menyetir kapal."},
    {"soal": "39. Gandum : Roti : Makan = Benang : Pakaian : ...", "opsi": ["Jahit", "Pola", "Pakai", "Toko"], "jawaban": 2, "pembahasan": "Roti untuk dimakan. Pakaian untuk dipakai."},
    {"soal": "40. Gempa Bumi : Tsunami = Hujan Deras : ...", "opsi": ["Banjir Bandang", "Mendung", "Payung", "Basah"], "jawaban": 0, "pembahasan": "Bencana memicu bencana ekstrem lainnya."},
    {"soal": "41. 1️⃣ ⬜ \n\n 2️⃣ ⬜ ⬜ \n\n 3️⃣ ⬜ ⬜ ⬜ \n\n ➡️ ❓", "opsi": ["⬜", "⬜ ⬜ ⬜ ⬜", "⬜ ⬜ ⬜ ⬜ ⬜", "⚫"], "jawaban": 1, "pembahasan": "Pola nambah 1 kotak."},
    {"soal": "42. 1️⃣ ⬆️ \n\n 2️⃣ ➡️ \n\n 3️⃣ ⬇️ \n\n ➡️ ❓", "opsi": ["⬆️", "➡️", "⬇️", "⬅️"], "jawaban": 3, "pembahasan": "Putar 90 derajat searah jarum jam."},
    {"soal": "43. 1️⃣ 🔺 \n\n 2️⃣ ◼️ \n\n 3️⃣ ⬟ \n\n ➡️ ❓", "opsi": ["🟠", "⬡", "⭐", "🔶"], "jawaban": 1, "pembahasan": "Nambah 1 sisi bangun datar."},
    {"soal": "44. 🔠 **b** 🪞 ❓", "opsi": ["p", "q", "d", "c"], "jawaban": 2, "pembahasan": "Cermin huruf 'b' memantul jadi 'd'."},
    {"soal": "45. 1️⃣ ⚫⚫ \n\n 2️⃣ ⚫⚫⚫⚫ \n\n 3️⃣ ⚫⚫⚫⚫⚫⚫ \n\n ➡️ ❓", "opsi": ["⚫⚫⚫⚫⚫⚫⚫", "⚫⚫⚫⚫⚫⚫⚫⚫", "⚫⚫⚫⚫⚫⚫⚫⚫⚫", "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫"], "jawaban": 1, "pembahasan": "Ditambah 2 titik."},
    {"soal": "46. Posisi: A duduk kanan B. C duduk kiri B. Siapa di tengah?", "opsi": ["A", "B", "C", "Tidak ada"], "jawaban": 1, "pembahasan": "Urutan C - B - A."},
    {"soal": "47. Andi tidak Malam. Cici selalu Pagi. Doni setelah Andi. Budi Malam. Andi jaga kapan?", "opsi": ["Pagi", "Siang", "Sore", "Malam"], "jawaban": 1, "pembahasan": "Cici(Pagi), Budi(Malam). Sisa Siang & Sore. Andi(Siang), Doni(Sore)."},
    {"soal": "48. Budi menyalip posisi kedua. Posisi Budi sekarang...", "opsi": ["Pertama", "Kedua", "Ketiga", "Keempat"], "jawaban": 1, "pembahasan": "Menyalip posisi kedua artinya menempati posisi kedua tersebut."},
    {"soal": "49. Rumah Tono lebih jauh dari Tini. Tino lebih dekat dari Tini. Paling jauh?", "opsi": ["Tono", "Tini", "Tino", "Sama"], "jawaban": 0, "pembahasan": "Urutan: Tono(terjauh) - Tini - Tino."},
    {"soal": "50. Kereta A berangkat 08.00 tiba 10.00. Kereta B berangkat 08.00 tiba 09.30. Mana lebih cepat?", "opsi": ["Kereta A", "Kereta B", "Sama saja", "Tidak tahu"], "jawaban": 1, "pembahasan": "Kereta B butuh 1.5 jam, Kereta A butuh 2 jam."}
]

soal_paket_2 = [
    {"soal": "1. 12 x 15 = ...", "opsi": ["160", "170", "180", "190"], "jawaban": 2, "pembahasan": "10x15 = 150, ditambah 2x15 = 30. Hasil = 180."},
    {"soal": "2. 144 : 12 = ...", "opsi": ["10", "12", "14", "16"], "jawaban": 1, "pembahasan": "Akar kuadrat dari 144 adalah 12."},
    {"soal": "3. 25 + 15 x 4 - 10 = ...", "opsi": ["150", "100", "75", "65"], "jawaban": 2, "pembahasan": "Kali dulu: 15x4 = 60. Lalu 25 + 60 - 10 = 75."},
    {"soal": "4. (18 - 6) x (10 + 2) = ...", "opsi": ["144", "124", "120", "100"], "jawaban": 0, "pembahasan": "Kerjakan dalam kurung: 12 x 12 = 144."},
    {"soal": "5. 50% dari 0.8 adalah...", "opsi": ["0.4", "0.5", "4", "40"], "jawaban": 0, "pembahasan": "Setengah dari 0.8 adalah 0.4."},
    {"soal": "6. 1/3 + 1/6 = ...", "opsi": ["2/9", "2/6", "1/2", "3/9"], "jawaban": 2, "pembahasan": "Samakan penyebut (6). Jadi 2/6 + 1/6 = 3/6 = 1/2."},
    {"soal": "7. 0.25 x 400 = ...", "opsi": ["50", "100", "150", "200"], "jawaban": 1, "pembahasan": "0.25 sama dengan 1/4. 400 dibagi 4 = 100."},
    {"soal": "8. 10^2 - 8^2 = ...", "opsi": ["36", "64", "100", "164"], "jawaban": 0, "pembahasan": "100 - 64 = 36."},
    {"soal": "9. Akar 169 + Akar 144 = ...", "opsi": ["23", "25", "27", "29"], "jawaban": 1, "pembahasan": "13 + 12 = 25."},
    {"soal": "10. 2.5 x 4 + 10 : 2 = ...", "opsi": ["15", "20", "25", "30"], "jawaban": 0, "pembahasan": "(2.5 x 4) = 10. Lalu (10 : 2) = 5. 10 + 5 = 15."},
    {"soal": "11. Bentuk desimal dari 3/8 adalah...", "opsi": ["0.35", "0.375", "0.40", "0.45"], "jawaban": 1, "pembahasan": "1/8 adalah 0.125. Maka 3/8 adalah 3 x 0.125 = 0.375."},
    {"soal": "12. Harga Rp 200.000 diskon 50% lalu diskon lagi 20%. Harga akhir?", "opsi": ["Rp 60.000", "Rp 70.000", "Rp 80.000", "Rp 100.000"], "jawaban": 2, "pembahasan": "Diskon 50% = sisa 100rb. Diskon 20% dari 100rb = potong 20rb. Sisa 80.000."},
    {"soal": "13. 33.33% dari Rp 150.000 adalah...", "opsi": ["Rp 30.000", "Rp 40.000", "Rp 50.000", "Rp 60.000"], "jawaban": 2, "pembahasan": "33.33% sama dengan 1/3. 150.000 dibagi 3 = 50.000."},
    {"soal": "14. Barang dijual Rp 120.000 dengan untung 20%. Harga belinya?", "opsi": ["Rp 96.000", "Rp 100.000", "Rp 110.000", "Rp 144.000"], "jawaban": 1, "pembahasan": "Harga Jual = 120% x Modal. Maka Modal = 120.000 / 1.2 = 100.000."},
    {"soal": "15. 1.25 : 0.5 = ...", "opsi": ["0.25", "0.50", "2.0", "2.5"], "jawaban": 3, "pembahasan": "Sama dengan 12.5 dibagi 5 = 2.5."},
    {"soal": "16. 3, 4, 7, 11, 18, ...", "opsi": ["27", "28", "29", "30"], "jawaban": 2, "pembahasan": "Deret Fibonacci (11 + 18 = 29)."},
    {"soal": "17. 2, 5, 10, 17, 26, ...", "opsi": ["35", "37", "39", "41"], "jawaban": 1, "pembahasan": "Selisih angkanya bertambah ganjil: +3, +5, +7, +9. Berikutnya +11. 26 + 11 = 37."},
    {"soal": "18. 100, 50, 200, 100, 400, ...", "opsi": ["200", "300", "400", "800"], "jawaban": 0, "pembahasan": "Pola: Bagi 2, lalu Kali 4 secara bergantian. 400 dibagi 2 = 200."},
    {"soal": "19. 1, 8, 27, 64, ...", "opsi": ["100", "125", "144", "216"], "jawaban": 1, "pembahasan": "Pola pangkat tiga: 1^3, 2^3, 3^3, 4^3. Selanjutnya 5^3 = 125."},
    {"soal": "20. 5, 10, 30, 120, ...", "opsi": ["480", "500", "600", "720"], "jawaban": 2, "pembahasan": "Pola perkalian menaik: x2, x3, x4. Berikutnya 120 x 5 = 600."},
    {"soal": "21. A mengecat dinding 4 jam, B butuh 12 jam. Jika bersama-sama?", "opsi": ["3 jam", "4 jam", "8 jam", "16 jam"], "jawaban": 0, "pembahasan": "1/4 + 1/12 = 3/12 + 1/12 = 4/12. Dibalik jadi 12/4 = 3 jam."},
    {"soal": "22. Proyek butuh 6 pekerja selesai 15 hari. Agar selesai 10 hari butuh berapa pekerja total?", "opsi": ["8 pekerja", "9 pekerja", "10 pekerja", "12 pekerja"], "jawaban": 1, "pembahasan": "Perbandingan berbalik nilai. 6 x 15 = P x 10. 90 = 10P. P = 9 pekerja."},
    {"soal": "23. Beli 2 lusin buku Rp 48.000. Harga 5 buku?", "opsi": ["Rp 8.000", "Rp 10.000", "Rp 12.000", "Rp 15.000"], "jawaban": 1, "pembahasan": "2 lusin = 24 buku. 1 buku = 48.000 / 24 = 2.000. 5 buku = 10.000."},
    {"soal": "24. Tandon air 500 liter bocor 5 liter/menit. Habis dalam...", "opsi": ["1 jam", "1 jam 20 menit", "1 jam 40 menit", "2 jam"], "jawaban": 2, "pembahasan": "500 / 5 = 100 menit. 100 menit = 1 jam 40 menit."},
    {"soal": "25. Tabungan awal Rp 2.000.000, bunga 12% pertahun. Berapa nilai bunga setelah 6 bulan?", "opsi": ["Rp 120.000", "Rp 240.000", "Rp 360.000", "Rp 400.000"], "jawaban": 0, "pembahasan": "Bunga 1 tahun = 240.000. Setengah tahun (6 bulan) = 120.000."},
    {"soal": "26. Berangkat pukul 06.15, tiba 08.45. Di jalan istirahat 30 menit. Jarak 120 km. Kecepatannya?", "opsi": ["50 km/jam", "60 km/jam", "70 km/jam", "80 km/jam"], "jawaban": 1, "pembahasan": "Waktu tempuh 06.15 ke 08.45 = 2.5 jam. Kurangi istirahat 30 mnt = 2 jam bersih. Kecepatan = 120 / 2 = 60 km/jam."},
    {"soal": "27. Sepatu Rp 300.000. Diskon 30% lalu potongan tunai Rp 10.000. Total bayar?", "opsi": ["Rp 190.000", "Rp 200.000", "Rp 210.000", "Rp 220.000"], "jawaban": 1, "pembahasan": "Diskon 30% (90rb) -> Sisa 210.000. Potongan tunai 10.000 -> Sisa 200.000."},
    {"soal": "28. Roda berputar 20 kali menempuh 10 m. Untuk jarak 50 m butuh berapa putaran?", "opsi": ["50 putaran", "80 putaran", "100 putaran", "120 putaran"], "jawaban": 2, "pembahasan": "Jarak bertambah 5x lipat (10m ke 50m). Putaran juga 5x lipat: 20 x 5 = 100."},
    {"soal": "29. Uang Rp 100.000. Si A dapat 2/5, B dapat 1/4, sisanya untuk C. Bagian C adalah...", "opsi": ["Rp 25.000", "Rp 30.000", "Rp 35.000", "Rp 40.000"], "jawaban": 2, "pembahasan": "A = 40.000. B = 25.000. Total A+B = 65.000. Sisa untuk C = 100.000 - 65.000 = 35.000."},
    {"soal": "30. Pakan untuk 30 ayam habis 15 hari. Jika ayam ditambah 15 ekor, pakan habis dalam...", "opsi": ["5 hari", "10 hari", "20 hari", "22 hari"], "jawaban": 1, "pembahasan": "Total ayam jadi 45. Perbandingan berbalik: 30 x 15 = 45 x Y. 450 = 45Y. Y = 10 hari."},
    {"soal": "31. Jika rajin maka lulus. Jika lulus maka kerja. Budi saat ini menganggur. Maka...", "opsi": ["Budi rajin", "Budi lulus tapi tidak kerja", "Budi tidak rajin", "Budi tidak mau kerja"], "jawaban": 2, "pembahasan": "Logika Modus Tollens berantai mundur. Menganggur (tidak kerja) -> tidak lulus -> tidak rajin."},
    {"soal": "32. Semua dokter memakai jas putih. Sebagian pria memakai jas putih. Maka...", "opsi": ["Semua pria adalah dokter", "Sebagian dokter adalah pria", "Semua yang berjas putih adalah pria", "Tidak bisa ditarik kesimpulan pasti"], "jawaban": 3, "pembahasan": "Tidak ada penghubung langsung yang valid antara kelompok Pria dan Dokter."},
    {"soal": "33. Semua mahasiswa membawa laptop. Sebagian mahasiswa bersepeda. Maka...", "opsi": ["Semua yang membawa laptop bersepeda", "Sebagian yang bersepeda membawa laptop", "Sebagian mahasiswa tidak membawa laptop", "Semua bersepeda membawa laptop"], "jawaban": 1, "pembahasan": "Kelompok irisan (Sebagian mahasiswa) pasti memenuhi kedua syarat (bersepeda dan bawa laptop)."},
    {"soal": "34. Tidak ada harimau makan rumput. Semua kuda makan rumput. Maka...", "opsi": ["Beberapa kuda makan harimau", "Tidak ada kuda yang makan harimau", "Tidak ada harimau yang berupa kuda", "Harimau dan kuda tidak berteman"], "jawaban": 2, "pembahasan": "Kelompok Harimau dan Kuda saling terpisah mutlak berdasarkan makanan mereka."},
    {"soal": "35. Jika cuaca cerah, Andi berenang. Jika berenang, ia senang. Hari ini Andi tidak senang. Maka...", "opsi": ["Cuaca cerah", "Andi berenang", "Cuaca tidak cerah", "Andi malas berenang"], "jawaban": 2, "pembahasan": "Akibat akhir batal (tidak senang), berarti sebab awalnya juga batal (cuaca tidak cerah)."},
    {"soal": "36. Penyakit : Dokter = Mesin Rusak : ...", "opsi": ["Pabrik", "Oli", "Montir", "Listrik"], "jawaban": 2, "pembahasan": "Dokter memperbaiki penyakit, Montir memperbaiki mesin rusak."},
    {"soal": "37. Kecebong : Katak = Ulat : ...", "opsi": ["Daun", "Kepompong", "Kupu-kupu", "Bulu"], "jawaban": 2, "pembahasan": "Bentuk bayi/larva menjadi bentuk dewasa akhir."},
    {"soal": "38. Suhu : Termometer = Gempa : ...", "opsi": ["Richter", "Tsunami", "Seismograf", "Vulkanik"], "jawaban": 2, "pembahasan": "Suhu diukur dengan termometer, gempa diukur dengan seismograf."},
    {"soal": "39. Matahari : Terang = Api : ...", "opsi": ["Merah", "Panas", "Asap", "Kayu"], "jawaban": 1, "pembahasan": "Matahari menghasilkan sifat terang, api menghasilkan sifat panas."},
    {"soal": "40. Pengacara : Hukum = Guru : ...", "opsi": ["Sekolah", "Pendidikan", "Buku", "Murid"], "jawaban": 1, "pembahasan": "Profesi dan bidang ilmu utamanya."},
    {"soal": "41. 1️⃣ ⚪⚫ \n\n 2️⃣ ⚪⚪⚫ \n\n 3️⃣ ⚪⚪⚪⚫ \n\n ➡️ ❓", "opsi": ["⚪⚪⚫⚫", "⚪⚪⚪⚪⚫", "⚪⚪⚫⚪", "⚫⚪⚪⚪"], "jawaban": 1, "pembahasan": "Lingkaran putih terus bertambah 1 di sebelah kiri."},
    {"soal": "42. 1️⃣ ↖️ \n\n 2️⃣ ↗️ \n\n 3️⃣ ↘️ \n\n ➡️ ❓", "opsi": ["↖️", "↗️", "↘️", "↙️"], "jawaban": 3, "pembahasan": "Panah miring berputar 90 derajat searah jarum jam."},
    {"soal": "43. 1️⃣ ➖ \n\n 2️⃣ ➕ \n\n 3️⃣ ⨹ \n\n ➡️ ❓ (Garis nambah satu persatu memotong pusat)", "opsi": ["➖", "➕", "⨹", "⨰"], "jawaban": 3, "pembahasan": "Penambahan garis perpotongan di pusat."},
    {"soal": "44. 🔠 **M** 🪞 ❓ (Dicerminkan secara vertikal)", "opsi": ["W", "N", "M", "E"], "jawaban": 2, "pembahasan": "Huruf M simetris, dicerminkan tetap M."},
    {"soal": "45. A duduk depan B. C samping B. D depan C. Siapa di samping A?", "opsi": ["A", "B", "C", "D"], "jawaban": 3, "pembahasan": "Baris depan: A dan D. Baris belakang: B dan C."},
    {"soal": "46. Buku TPA lebih tebal dari Psikotes. Buku Matematika lebih tebal dari TPA. Paling tipis?", "opsi": ["TPA", "Psikotes", "Matematika", "Sama"], "jawaban": 1, "pembahasan": "Urutan tebal: Matematika - TPA - Psikotes(tipis)."},
    {"soal": "47. Piket: Senin, Selasa, Rabu. A tidak mau Rabu. B selalu Senin. Kapan C piket?", "opsi": ["Senin", "Selasa", "Rabu", "Kamis"], "jawaban": 2, "pembahasan": "B (Senin). Sisa Selasa & Rabu. A tidak mau Rabu, jadi A (Selasa). Maka C (Rabu)."},
    {"soal": "48. Anton lebih cepat dari Budi. Budi sama dengan Cici. Doni lebih lambat dari Cici. Paling lambat?", "opsi": ["Anton", "Budi", "Cici", "Doni"], "jawaban": 3, "pembahasan": "Doni berada di bawah kecepatan Budi dan Cici yang setara."},
    {"soal": "49. Antrian: Tono di depan Tini. Tini di depan Tino. Budi di depan Tono. Paling depan?", "opsi": ["Tono", "Tini", "Tino", "Budi"], "jawaban": 3, "pembahasan": "Budi - Tono - Tini - Tino."},
    {"soal": "50. 1️⃣ 🟩🔺 \n\n 2️⃣ 🟩🟩🔺 \n\n 3️⃣ 🟩🟩🟩🔺 \n\n ➡️ ❓", "opsi": ["🟩🟩🟩🟩🔺", "🟩🟩🔺🔺", "🟩🔺🟩🔺", "🔺🔺🔺🟩"], "jawaban": 0, "pembahasan": "Penambahan 1 kotak hijau setiap tahap."}
]

# ==========================================
# 2. DATABASE SOAL (PAKET 3 - FULL SKD)
# ==========================================
# Anda bisa menambahkan atau menimpa soal TWK, TIU, dan TKP di bawah ini sesuai format.
soal_twk = [
    {"soal": "1. Sila ke-4 Pancasila mengajarkan kita untuk mengutamakan musyawarah. Dalam kehidupan sehari-hari, hal ini paling tepat diterapkan saat...", "opsi": ["A. Menentukan menu makan siang pribadi", "B. Memilih ketua RT", "C. Menentukan tempat wisata keluarga besar", "D. Membeli barang kebutuhan pokok", "E. Jawaban B dan C benar"], "jawaban": 4, "pembahasan": "Musyawarah dilakukan untuk keputusan yang melibatkan banyak orang."},
    {"soal": "2. Menggunakan produk dalam negeri merupakan wujud dari nilai Pancasila ke...", "opsi": ["A. Satu", "B. Dua", "C. Tiga", "D. Empat", "E. Lima"], "jawaban": 2, "pembahasan": "Sila ke-3 (Persatuan Indonesia) mencakup rasa cinta tanah air dan bangga produk lokal."}
]

soal_tiu = [
    {"soal": "31. 85 + 15 x 2 - 10 = ...", "opsi": ["105", "190", "115", "100", "95"], "jawaban": 0, "pembahasan": "(15x2)=30. 85+30-10 = 105."},
    {"soal": "32. 0,25 + 3/4 = ...", "opsi": ["0,5", "0,75", "1", "1,25", "1,5"], "jawaban": 2, "pembahasan": "3/4 = 0,75. 0,25 + 0,75 = 1."}
]

soal_tkp = [
    {"soal": "66. Sistem IT kantor mengalami gangguan sehingga pekerjaan tertunda. Anda akan...", "opsi": ["A. Menunggu saja sampai teknisi datang", "B. Marah-marah karena target tidak tercapai", "C. Mencoba memperbaiki sendiri meski bukan ahli", "D. Menggunakan waktu luang untuk merapikan dokumen fisik sambil menunggu", "E. Pulang ke rumah"], "skor": [2, 1, 3, 5, 1]},
    {"soal": "67. Ada aturan baru untuk datang 15 menit lebih awal. Anda merasa keberatan. Sikap Anda...", "opsi": ["A. Datang seperti biasa", "B. Mengajak teman lain untuk memprotes", "C. Mematuhi meski sambil menggerutu", "D. Mentaati aturan tersebut sebagai bentuk profesionalisme", "E. Datang awal jika ada atasan saja"], "skor": [1, 2, 3, 5, 2]}
]

# ==========================================
# 3. INISIALISASI STATE (VARIABEL SESI)
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
    st.session_state.pilihan_paket = "Paket 1: TIU Dasar (50 Soal / 60 Menit)"
if 'jawaban_user' not in st.session_state:
    st.session_state.jawaban_user = {}

# ==========================================
# 4. LOGIKA UI: MENU UTAMA (SEBELUM UJIAN)
# ==========================================
if not st.session_state.ujian_dimulai:
    st.title("📚 Pusat Pelatihan TPA & SKD")
    st.markdown("---")
    st.info("Pilih paket latihan di bawah ini. Waktu dan sistem penilaian akan otomatis menyesuaikan dengan paket yang Anda pilih.")
    
    st.session_state.pilihan_paket = st.radio(
        "Daftar Modul Ujian Tersedia:",
        [
            "Paket 1: TIU Dasar (50 Soal / 60 Menit)", 
            "Paket 2: TIU Lanjutan (50 Soal / 60 Menit)", 
            "Paket 3: SKD Nasional (TWK, TIU, TKP / 100 Menit)"
        ]
    )
    
    if st.button("🚀 MULAI UJIAN SEKARANG", use_container_width=True):
        st.session_state.ujian_dimulai = True
        st.session_state.waktu_mulai = time.time()
        st.session_state.telah_submit = False 
        st.session_state.jawaban_user = {}
        st.rerun()

# ==========================================
# 5. LOGIKA UI: SAAT UJIAN BERJALAN
# ==========================================
else:
    if not st.session_state.telah_submit:
        
        # --- A. PENGATURAN WAKTU OTOMATIS ---
        if "Paket 3" in st.session_state.pilihan_paket:
            durasi_ujian = 6000  # 100 Menit
        else:
            durasi_ujian = 3600  # 60 Menit
            
        waktu_selesai_ms = (st.session_state.waktu_mulai + durasi_ujian) * 1000 
        
        # --- B. INJEKSI SCRIPT TIMER ---
        js_timer = f"""
        <script>
            var countDownDate = {waktu_selesai_ms};
            var parentDoc = window.parent.document;
            var timerElement = parentDoc.getElementById('custom_timer_display');
            
            if (!timerElement) {{
                timerElement = parentDoc.createElement('div');
                timerElement.id = 'custom_timer_display';
                timerElement.style.cssText = 'position: fixed; bottom: 20px; right: 20px; background-color: #2e7bcf; color: white; padding: 12px 20px; border-radius: 8px; font-weight: bold; font-family: sans-serif; z-index: 9999; box-shadow: 0px 4px 10px rgba(0,0,0,0.3); border: 2px solid white;';
                parentDoc.body.appendChild(timerElement);
            }}
            
            var x = setInterval(function() {{
                var now = new Date().getTime();
                var distance = countDownDate - now;
                
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);
                
                var m = minutes < 10 ? "0" + minutes : minutes;
                var s = seconds < 10 ? "0" + seconds : seconds;
                
                timerElement.innerHTML = "⏳ Sisa Waktu: " + m + ":" + s;
                
                if (distance < 0) {{
                    clearInterval(x);
                    timerElement.innerHTML = "WAKTU HABIS!";
                    timerElement.style.backgroundColor = "black";
                    
                    var buttons = parentDoc.querySelectorAll('button');
                    for (var i = 0; i < buttons.length; i++) {{
                        if (buttons[i].innerText.includes('Kumpulkan Jawaban')) {{
                            buttons[i].click();
                            break;
                        }}
                    }}
                }}
            }}, 1000);
        </script>
        """
        components.html(js_timer, height=0, width=0)

        # --- C. RENDER SOAL SESUAI TAB/PAKET ---
        st.subheader(f"Mengerjakan: {st.session_state.pilihan_paket}")
        st.markdown("---")
        
        with st.form(key='form_ujian'):
            jawaban_sementara = {}
            
            # Jika user memilih Paket 1 atau Paket 2
            if "Paket 1" in st.session_state.pilihan_paket or "Paket 2" in st.session_state.pilihan_paket:
                soal_aktif = soal_paket_1 if "Paket 1" in st.session_state.pilihan_paket else soal_paket_2
                
                for i, item in enumerate(soal_aktif):
                    st.markdown(f"**{item['soal']}**")
                    pilihan = st.radio(label=f"Soal {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"tiu_{i}")
                    jawaban_sementara[f"tiu_{i}"] = pilihan
                    st.write("")
                    
            # Jika user memilih Paket 3 (SKD Lengkap)
            elif "Paket 3" in st.session_state.pilihan_paket:
                st.markdown("#### Bagian I: TWK (Tes Wawasan Kebangsaan)")
                for i, item in enumerate(soal_twk):
                    st.markdown(f"**{item['soal']}**")
                    pilihan = st.radio(label=f"TWK {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"twk_{i}")
                    jawaban_sementara[f"twk_{i}"] = pilihan
                    st.write("")
                    
                st.markdown("#### Bagian II: TIU (Tes Intelegensia Umum)")
                for i, item in enumerate(soal_tiu):
                    st.markdown(f"**{item['soal']}**")
                    pilihan = st.radio(label=f"TIU {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"tiu_skd_{i}")
                    jawaban_sementara[f"tiu_skd_{i}"] = pilihan
                    st.write("")
                    
                st.markdown("#### Bagian III: TKP (Tes Karakteristik Pribadi)")
                for i, item in enumerate(soal_tkp):
                    st.markdown(f"**{item['soal']}**")
                    pilihan = st.radio(label=f"TKP {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"tkp_{i}")
                    jawaban_sementara[f"tkp_{i}"] = pilihan
                    st.write("")

            submit_button = st.form_submit_button(label='Kumpulkan Jawaban', use_container_width=True)

        # --- D. LOGIKA PENILAIAN OTOMATIS ---
        if submit_button:
            st.session_state.waktu_selesai = time.time()
            st.session_state.telah_submit = True
            st.session_state.jawaban_user = jawaban_sementara
            
            # Penilaian untuk Paket 1 & 2 (Persentase 1-100)
            if "Paket 1" in st.session_state.pilihan_paket or "Paket 2" in st.session_state.pilihan_paket:
                soal_aktif = soal_paket_1 if "Paket 1" in st.session_state.pilihan_paket else soal_paket_2
                benar = 0
                for i, item in enumerate(soal_aktif):
                    if jawaban_sementara.get(f"tiu_{i}") == item["opsi"][item["jawaban"]]:
                        benar += 1
                st.session_state.skor_tiu = (benar / len(soal_aktif)) * 100
                st.session_state.benar = benar
                st.session_state.salah = len(soal_aktif) - benar
                
            # Penilaian untuk Paket 3 (Skala 550)
            elif "Paket 3" in st.session_state.pilihan_paket:
                skor_twk, skor_tiu, skor_tkp = 0, 0, 0
                
                # Cek TWK (+5 poin per benar)
                for i, item in enumerate(soal_twk):
                    if jawaban_sementara.get(f"twk_{i}") == item["opsi"][item["jawaban"]]:
                        skor_twk += 5
                        
                # Cek TIU (+5 poin per benar)
                for i, item in enumerate(soal_tiu):
                    if jawaban_sementara.get(f"tiu_skd_{i}") == item["opsi"][item["jawaban"]]:
                        skor_tiu += 5
                        
                # Cek TKP (Poin 1 sampai 5)
                for i, item in enumerate(soal_tkp):
                    jawaban = jawaban_sementara.get(f"tkp_{i}")
                    if jawaban:
                        idx = item["opsi"].index(jawaban)
                        skor_tkp += item["skor"][idx]
                        
                st.session_state.skor_twk = skor_twk
                st.session_state.skor_tiu = skor_tiu
                st.session_state.skor_tkp = skor_tkp

            st.rerun()

# ==========================================
# 6. LOGIKA UI: SETELAH SUBMIT (EVALUASI)
# ==========================================
if st.session_state.telah_submit:
    # Hilangkan JS Timer yang melayang
    remove_js = "<script>var timerElement = window.parent.document.getElementById('custom_timer_display'); if (timerElement) { timerElement.remove(); }</script>"
    components.html(remove_js, height=0, width=0)

    # Kalkulasi Durasi Pengerjaan
    durasi_detik = int(st.session_state.waktu_selesai - st.session_state.waktu_mulai)
    if ("Paket 3" in st.session_state.pilihan_paket and durasi_detik >= 6000) or ("Paket 3" not in st.session_state.pilihan_paket and durasi_detik >= 3600):
        st.error("⏰ WAKTU HABIS! Jawaban dikumpulkan otomatis.")
    else:
        st.success(f"⏱️ Waktu Terpakai: {durasi_detik // 60} Menit {durasi_detik % 60} Detik")

    st.title("HASIL EVALUASI")
    st.markdown("---")

    # --- TAMPILAN HASIL PAKET 1 ATAU 2 ---
    if "Paket 1" in st.session_state.pilihan_paket or "Paket 2" in st.session_state.pilihan_paket:
        col1, col2, col3 = st.columns(3)
        col1.metric("Skor Total", f"{st.session_state.skor_tiu:g} / 100")
        col2.metric("Jawaban Benar", st.session_state.benar)
        col3.metric("Jawaban Salah/Kosong", st.session_state.salah)
        
        st.markdown("### Daftar Jawaban yang Salah:")
        soal_aktif = soal_paket_1 if "Paket 1" in st.session_state.pilihan_paket else soal_paket_2
        
        for i, item in enumerate(soal_aktif):
            jawaban_user = st.session_state.jawaban_user.get(f"tiu_{i}")
            jawaban_benar = item["opsi"][item["jawaban"]]
            
            if jawaban_user != jawaban_benar:
                with st.expander(f"Soal No. {i+1} (Salah)"):
                    st.write(f"**Soal:** {item['soal']}")
                    st.write(f"❌ **Jawabanmu:** {jawaban_user if jawaban_user else 'Kosong'}")
                    st.write(f"✅ **Jawaban Benar:** {jawaban_benar}")
                    st.info(f"**Pembahasan:** {item['pembahasan']}")

    # --- TAMPILAN HASIL PAKET 3 (SKD) ---
    elif "Paket 3" in st.session_state.pilihan_paket:
        total_skor = st.session_state.skor_twk + st.session_state.skor_tiu + st.session_state.skor_tkp
        col1, col2, col3, col4 = st.columns(4)
        
        # Asumsi bobot maksimal berdasarkan jumlah array saat ini.
        # Jika Anda memasukkan full 110 soal (TWK 30, TIU 35, TKP 45), angka pembagi di bawah bisa diubah menjadi 550, 150, 175, 225.
        max_twk = len(soal_twk) * 5
        max_tiu = len(soal_tiu) * 5
        max_tkp = len(soal_tkp) * 5
        max_total = max_twk + max_tiu + max_tkp
        
        col1.metric("SKOR TOTAL", f"{total_skor} / {max_total}")
        col2.metric("TWK", f"{st.session_state.skor_twk} / {max_twk}")
        col3.metric("TIU", f"{st.session_state.skor_tiu} / {max_tiu}")
        col4.metric("TKP", f"{st.session_state.skor_tkp} / {max_tkp}")
        
        st.markdown("### Evaluasi TWK & TIU (Yang Salah)")
        for i, item in enumerate(soal_twk):
            jawaban_user = st.session_state.jawaban_user.get(f"twk_{i}")
            jawaban_benar = item["opsi"][item["jawaban"]]
            if jawaban_user != jawaban_benar:
                with st.expander(f"TWK No. {i+1} (Salah)"):
                    st.write(f"**Soal:** {item['soal']}")
                    st.write(f"❌ **Jawabanmu:** {jawaban_user if jawaban_user else 'Kosong'}")
                    st.write(f"✅ **Jawaban Benar:** {jawaban_benar}")
                    st.info(f"**Pembahasan:** {item['pembahasan']}")
        
        for i, item in enumerate(soal_tiu):
            jawaban_user = st.session_state.jawaban_user.get(f"tiu_skd_{i}")
            jawaban_benar = item["opsi"][item["jawaban"]]
            if jawaban_user != jawaban_benar:
                with st.expander(f"TIU No. {i+31} (Salah)"):
                    st.write(f"**Soal:** {item['soal']}")
                    st.write(f"❌ **Jawabanmu:** {jawaban_user if jawaban_user else 'Kosong'}")
                    st.write(f"✅ **Jawaban Benar:** {jawaban_benar}")
                    st.info(f"**Pembahasan:** {item['pembahasan']}")
        
        st.markdown("### Evaluasi TKP (Tidak mendapat Poin Maksimal)")
        for i, item in enumerate(soal_tkp):
            jawaban_user = st.session_state.jawaban_user.get(f"tkp_{i}")
            poin = 0
            if jawaban_user:
                idx = item["opsi"].index(jawaban_user)
                poin = item["skor"][idx]
            
            terbaik_idx = item["skor"].index(5)
            jawaban_terbaik = item["opsi"][terbaik_idx]
            
            if poin < 5:
                with st.expander(f"TKP No. {i+66} (Poin: {poin}/5)"):
                    st.write(f"**Soal:** {item['soal']}")
                    st.write(f"**Pilihanmu:** {jawaban_user if jawaban_user else 'Kosong'}")
                    st.write(f"**Tindakan Terbaik (Poin 5):** {jawaban_terbaik}")

    st.markdown("---")
    if st.button("Kembali ke Menu Utama"):
        st.session_state.ujian_dimulai = False
        st.session_state.telah_submit = False
        st.rerun()
