import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="Pusat Simulasi Ujian SKD CPNS", layout="wide")

# ==============================================================================
# DATABASE LENGKAP 110 SOAL SKD (30 TWK, 35 TIU, 45 TKP)
# ==============================================================================

soal_twk_lengkap = [
    {"soal": "Sila ke-4 Pancasila mengajarkan kita untuk mengutamakan musyawarah. Dalam kehidupan sehari-hari, hal ini paling tepat diterapkan saat...", "opsi": ["Menentukan menu makan siang", "Memilih ketua RT", "Menentukan tempat liburan pribadi", "Membeli barang kebutuhan pokok", "Tidur siang"], "jawaban": 1, "pembahasan": "Musyawarah mufakat dilakukan untuk keputusan kepentingan bersama di lingkungan masyarakat."},
    {"soal": "Menggunakan produk dalam negeri merupakan wujud nyata dari pengamalan nilai Pancasila ke...", "opsi": ["1", "2", "3", "4", "5"], "jawaban": 2, "pembahasan": "Sila ke-3 (Persatuan Indonesia) mencakup rasa cinta tanah air dan bangga menggunakan produk buatan dalam negeri."},
    {"soal": "Tujuan utama dari amandemen UUD 1945 yang dilakukan oleh MPR adalah untuk...", "opsi": ["Memperluas kekuasaan absolut Presiden", "Menyesuaikan aturan dasar negara dengan dinamika perkembangan zaman", "Mengubah bentuk negara dari kesatuan menjadi federal", "Membubarkan lembaga tinggi negara", "Mengganti ideologi negara"], "jawaban": 1, "pembahasan": "Amandemen bertujuan menyempurnakan aturan dasar, bukan mengubah dasar negara atau bentuk negara."},
    {"soal": "Sikap yang paling mencerminkan integritas tinggi bagi seorang ASN di tempat kerja adalah...", "opsi": ["Datang tepat waktu hanya saat diawasi oleh atasan", "Menyelesaikan tanggung jawab tugas secara tuntas walau tanpa pengawasan", "Membawa pulang fasilitas kantor untuk keperluan pribadi", "Menutupi kesalahan rekan sekantor demi solidaritas sempit", "Mengabaikan SOP demi mempercepat pekerjaan"], "jawaban": 1, "pembahasan": "Integritas adalah keselarasan perbuatan dengan kejujuran meski tidak ada orang yang mengawasi."},
    {"soal": "Semboyan 'Bhinneka Tunggal Ika' tertulis pada pita burung Garuda Pancasila, yang pertama kali dikutip dari kitab...", "opsi": ["Negarakertagama", "Sutasoma", "Arjunawiwaha", "Pararaton", "Bharatayuddha"], "jawaban": 1, "pembahasan": "Kitab Sutasoma dikarang oleh Mpu Tantular pada masa kerajaan Majapahit."},
    {"soal": "Hak Asasi Manusia (HAM) di dalam UUD 1945 diatur secara komprehensif khusus pada pasal...", "opsi": ["Pasal 27", "Pasal 28A sampai 28J", "Pasal 29", "Pasal 30", "Pasal 31"], "jawaban": 1, "pembahasan": "Pasal 28A hingga 28J merupakan hasil amandemen yang merinci perlindungan HAM di Indonesia."},
    {"soal": "Asas wawasan nusantara memandang wilayah Indonesia sebagai...", "opsi": ["Pulau-pulau yang terpisah oleh lautan luas", "Satu kesatuan politik, ekonomi, sosial budaya, dan pertahanan keamanan", "Kawasan bebas tanpa batas administratif", "Wilayah terisolasi dari pengaruh internasional", "Daerah otonom yang berdiri sendiri"], "jawaban": 1, "pembahasan": "Wawasan nusantara memandang Indonesia sebagai satu kesatuan utuh (ekopolstaghankam)."},
    {"soal": "Paham radikalisme dan terorisme sangat berbahaya karena secara fundamental melanggar prinsip...", "opsi": ["Keadilan ekonomi pasar", "Toleransi dan nilai kemanusiaan universal", "Sistem demokrasi perwakilan", "Musyawarah mufakat desa", "Undang-undang perpajakan"], "jawaban": 1, "pembahasan": "Radikalisme merusak nilai kemanusiaan (Sila ke-2) dan memecah persatuan."},
    {"soal": "Berdasarkan UUD 1945, lembaga negara yang memegang kekuasaan kehakiman (yudikatif) adalah...", "opsi": ["Presiden dan Wakil Presiden", "DPR dan DPD", "Mahkamah Agung, Mahkamah Konstitusi, dan Komisi Yudisial", "Badan Pemeriksa Keuangan", "Komisi Pemilihan Umum"], "jawaban": 2, "pembahasan": "Kekuasaan yudikatif dijalankan oleh MA, MK, dan KY secara independen."},
    {"soal": "Pengakuan de facto kemerdekaan Republik Indonesia untuk pertama kalinya secara internasional diberikan oleh negara...", "opsi": ["Belanda", "Australia", "Mesir", "India", "Amerika Serikat"], "jawaban": 2, "pembahasan": "Mesir adalah negara pertama yang memberikan pengakuan kemerdekaan Indonesia secara de facto."},
    {"soal": "Peristiwa Sumpah Pemuda 28 Oktober 1928 memiliki makna historis mendalam sebagai...", "opsi": ["Tonggak awal pembentukan militer nasional", "Tonggak bersatunya tekad pemuda lintas daerah melawan penjajah", "Deklarasi proklamasi kemerdekaan", "Pembentukan partai politik pertama", "Perjanjian damai dengan pemerintah kolonial"], "jawaban": 1, "pembahasan": "Sumpah Pemuda menyatukan berbagai organisasi pemuda kedaerahan menjadi satu kebangsaan."},
    {"soal": "Kedudukan Pancasila sebagai 'sumber dari segala sumber hukum negara' mengandung arti bahwa...", "opsi": ["Pancasila adalah alat kekuasaan penguasa", "Setiap produk hukum tidak boleh bertentangan dengan nilai Pancasila", "Pancasila hanya digunakan saat upacara kenegaraan", "Undang-undang dasar tidak terikat pada Pancasila", "Pancasila bersifat tertutup dan kaku"], "jawaban": 1, "pembahasan": "Semua peraturan perundang-undangan harus bersumber dan selaras dengan Pancasila."},
    {"soal": "Prinsip dasar politik luar negeri Republik Indonesia adalah...", "opsi": ["Aliansi militer blok barat", "Bergabung dengan blok timur", "Bebas aktif", "Isolasi mandiri dari dunia internasional", "Ketergantungan ekonomi global"], "jawaban": 2, "pembahasan": "Bebas aktif berarti bebas menentukan sikap dan aktif menjaga perdamaian dunia."},
    {"soal": "Ketentuan mengenai hak dan kewajiban warga negara dalam usaha pertahanan dan keamanan negara diatur dalam...", "opsi": ["Pasal 27 UUD 1945", "Pasal 30 UUD 1945", "Pasal 31 UUD 1945", "Pasal 33 UUD 1945", "Pasal 34 UUD 1945"], "jawaban": 1, "pembahasan": "Pasal 30 menegaskan pertahanan dan keamanan negara merupakan hak dan kewajiban warga negara."},
    {"soal": "Kebebasan pers di Indonesia dijamin oleh undang-undang, namun pelaksanaannya harus disertai dengan...", "opsi": ["Sensor ketat dari pemerintah pusat", "Tanggung jawab moral dan kepatuhan pada hukum yang berlaku", "Izin khusus dari kepolisian daerah", "Persetujuan dari pemilik modal media", "Pembatasan kritik terhadap pejabat"], "jawaban": 1, "pembahasan": "Kebebasan pers yang bertanggung jawab menjunjung tinggi etika dan hukum."},
    {"soal": "Berikut ini yang BUKAN merupakan elemen perusak integritas nasional adalah...", "opsi": ["Nepotisme dalam jabatan", "Korupsi anggaran publik", "Patriotisme dan cinta tanah air", "Etnosentrisme sempit", "Politik uang dalam pemilu"], "jawaban": 2, "pembahasan": "Patriotisme adalah sifat positif penopang integritas nasional."},
    {"soal": "Lembaga negara yang memiliki kewenangan melakukan pengujian undang-undang terhadap UUD 1945 adalah...", "opsi": ["Mahkamah Agung", "Mahkamah Konstitusi", "Dewan Perwakilan Rakyat", "Badan Pemeriksa Keuangan", "Komisi Yudisial"], "jawaban": 1, "pembahasan": "Judicial review undang-undang merupakan wewenang utama Mahkamah Konstitusi (MK)."},
    {"soal": "Sistem demokrasi yang dianut oleh negara Indonesia berdasarkan Pancasila adalah demokrasi yang...", "opsi": ["Mengutamakan pengambilan suara mayoritas mutlak", "Dipimpin oleh kaum elit militer", "Berlandaskan hikmat kebijaksanaan dalam permusyawaratan/perwakilan", "Memberikan kebebasan tanpa batas individu", "Berdasarkan kekuatan modal ekonomi"], "jawaban": 2, "pembahasan": "Demokrasi Pancasila menempatkan musyawarah mufakat sebagai ciri khas utama."},
    {"soal": "Contoh bentuk bela negara yang dapat dilakukan oleh warga sipil di era modern adalah...", "opsi": ["Mengikuti wajib militer tempur di perbatasan", "Taat membayar pajak tepat waktu dan menjaga fasilitas umum", "Menyebarkan informasi tanpa saring", "Menolak aturan yang ditetapkan pemerintah", "Bersikap apatis terhadap kebijakan publik"], "jawaban": 1, "pembahasan": "Membayar pajak dan merawat fasilitas umum adalah wujud bela negara non-militer."},
    {"soal": "Lagu kebangsaan Indonesia Raya pertama kali diperdengarkan secara resmi pada peristiwa...", "opsi": ["Sidang BPUPKI", "Kongres Pemuda II (Sumpah Pemuda)", "Proklamasi 17 Agustus 1945", "Konferensi Meja Bundar", "Perundingan Renville"], "jawaban": 1, "pembahasan": "Diciptakan oleh W.R. Supratman dan diperdengarkan pada 28 Oktober 1928."},
    {"soal": "Lembaga negara yang bertugas memeriksa pengelolaan dan tanggung jawab keuangan negara adalah...", "opsi": ["KPK", "Bank Indonesia", "Badan Pemeriksa Keuangan (BPK)", "Otoritas Jasa Keuangan", "Kejaksaan Agung"], "jawaban": 2, "pembahasan": "BPK adalah lembaga mandiri yang memeriksa keuangan negara."},
    {"soal": "Sikap toleransi antarumat beragama dalam kehidupan majemuk paling tepat ditunjukkan dengan cara...", "opsi": ["Ikut serta dalam tata cara ibadah agama lain", "Membiarkan umat agama lain beribadah dengan tenang tanpa gangguan", "Mencampuradukkan ajaran berbagai agama", "Menutup rumah ibadah kelompok lain", "Berdebat mencari kebenaran doktrin"], "jawaban": 1, "pembahasan": "Toleransi berarti saling menghormati ruang ibadah masing-masing agama."},
    {"soal": "Perubahan (amandemen) terhadap UUD 1945 secara konstitusional dilakukan oleh...", "opsi": ["Presiden Republik Indonesia", "Dewan Perwakilan Rakyat (DPR)", "Majelis Permusyawaratan Rakyat (MPR)", "Mahkamah Agung", "Dewan Perwakilan Daerah (DPD)"], "jawaban": 2, "pembahasan": "Sesuai Pasal 37 UUD 1945, wewenang mengubah UUD ada di tangan MPR."},
    {"soal": "Tindak pidana korupsi secara filosofis merupakan pelanggaran berat terhadap nilai Pancasila sila ke...", "opsi": ["1", "2", "3", "4", "5"], "jawaban": 4, "pembahasan": "Korupsi merampas hak orang banyak dan merusak Keadilan Sosial (Sila ke-5)."},
    {"soal": "Sifat dasar dari Undang-Undang Dasar 1945 adalah...", "opsi": ["Memuat aturan yang sangat panjang dan kaku", "Singkat, supel, dan memuat aturan pokok saja", "Mudah diubah setiap tahun oleh menteri", "Tidak mengikat bagi warga negara", "Hanya berupa hukum adat istiadat"], "jawaban": 1, "pembahasan": "UUD 1945 bersifat singkat dan fleksibel mengikuti perkembangan zaman."},
    {"soal": "Pengamalan Pancasila secara objektif berarti pelaksanaan nilai-nilai Pancasila pada...", "opsi": ["Sikap mental pribadi warga negara", "Penyelenggaraan negara, pemerintahan, dan hukum", "Kehidupan beragama individu di rumah", "Pergaulan antar pemuda di sekolah", "Kegiatan ekonomi perdagangan pasar"], "jawaban": 1, "pembahasan": "Objektif berkaitan dengan pengaturan hukum dan kenegaraan secara nyata."},
    {"soal": "Jika usulan program Anda ditolak dalam rapat RT, sikap profesional Anda adalah...", "opsi": ["Marah dan keluar dari ruangan rapat", "Menerima keputusan dengan lapang dada dan mendukung hasil mufakat", "Menggugat keputusan tersebut ke pengadilan", "Menolak melaksanakan hasil keputusan warga", "Diam saja namun sabotase kegiatan"], "jawaban": 1, "pembahasan": "Menjunjung tinggi hasil musyawarah adalah wujud kedewasaan berdemokrasi."},
    {"soal": "Hari Kesaktian Pancasila diperingati bangsa Indonesia setiap tanggal...", "opsi": ["1 Juni", "17 Agustus", "30 September", "1 Oktober", "10 November"], "jawaban": 3, "pembahasan": "Diperingati setiap tanggal 1 Oktober untuk mengenang keutuhan ideologi negara."},
    {"soal": "Bendera negara Sang Merah Putih diatur secara resmi di dalam UUD 1945 pada...", "opsi": ["Pasal 35", "Pasal 36", "Pasal 36A", "Pasal 36B", "Pasal 36C"], "jawaban": 0, "pembahasan": "Pasal 35 UUD 1945 menyatakan bendera negara Indonesia ialah Sang Merah Putih."},
    {"soal": "Segala bentuk sikap yang dapat membahayakan persatuan dan kesatuan bangsa, KECUALI...", "opsi": ["Primordialisme berlebihan", "Etnosentrisme", "Chauvinisme", "Patriotisme", "Separatisme"], "jawaban": 3, "pembahasan": "Patriotisme adalah cinta tanah air yang positif, bukan ancaman persatuan."}
]

soal_tiu_lengkap = [
    {"soal": "85 + 15 x 2 - 10 = ...", "opsi": ["105", "190", "115", "100", "95"], "jawaban": 0, "pembahasan": "Perkalian dikerjakan dulu: 15x2=30. Lalu 85+30-10 = 105."},
    {"soal": "0,25 + 3/4 = ...", "opsi": ["0,5", "0,75", "1", "1,25", "1,5"], "jawaban": 2, "pembahasan": "3/4 sama dengan 0,75. Maka 0,25 + 0,75 = 1."},
    {"soal": "2, 4, 8, 16, 32, ...", "opsi": ["48", "54", "64", "72", "80"], "jawaban": 2, "pembahasan": "Pola dikali 2. 32 x 2 = 64."},
    {"soal": "3, 5, 8, 12, 17, ...", "opsi": ["21", "22", "23", "24", "25"], "jawaban": 2, "pembahasan": "Penambahan bertingkat: +2, +3, +4, +5, selanjutnya +6. 17+6=23."},
    {"soal": "Uang Rp 150.000, dipakai beli 3 kg telur (Rp 28.000/kg). Sisa uangnya adalah...", "opsi": ["Rp 56.000", "Rp 66.000", "Rp 76.000", "Rp 86.000", "Rp 96.000"], "jawaban": 1, "pembahasan": "Belanja = 3 x 28.000 = 84.000. Sisa = 150.000 - 84.000 = 66.000."},
    {"soal": "10 pekerja dapat menyelesaikan pekerjaan dalam 6 hari. Agar selesai dalam 4 hari, butuh berapa pekerja total?", "opsi": ["12", "15", "18", "20", "24"], "jawaban": 1, "pembahasan": "Perbandingan berbalik nilai: 10 x 6 = P x 4. Maka P = 60/4 = 15 pekerja."},
    {"soal": "Sebuah baju didiskon 20%, dibayar Rp 80.000. Berapa harga awal baju tersebut?", "opsi": ["Rp 90.000", "Rp 100.000", "Rp 120.000", "Rp 150.000", "Rp 160.000"], "jawaban": 1, "pembahasan": "Harga bayar 80% = 80rb. Harga 100% = 100.000."},
    {"soal": "Jarak kota A ke B adalah 150 km. Kecepatan mobil 50 km/jam. Berangkat pukul 08.00, tiba pukul...", "opsi": ["10.00", "10.30", "11.00", "11.30", "12.00"], "jawaban": 2, "pembahasan": "Waktu = 150/50 = 3 jam. 08.00 + 3 jam = 11.00."},
    {"soal": "SINONIM: Evokasi =", "opsi": ["Penggugah", "Nilai", "Ubah", "Fungsi", "Saran"], "jawaban": 0, "pembahasan": "Evokasi berarti daya penggugah rasa."},
    {"soal": "ANTONIM: Skeptis ><", "opsi": ["Ragu", "Yakin", "Cemas", "Takut", "Berani"], "jawaban": 1, "pembahasan": "Skeptis (ragu-ragu) berlawanan dengan Yakin."},
    {"soal": "Mobil : Bensin = Pelari : ...", "opsi": ["Trek", "Sepatu", "Makan", "Lari", "Juara"], "jawaban": 2, "pembahasan": "Mobil butuh bensin sebagai energi, pelari butuh makanan."},
    {"soal": "Buku : Perpustakaan = ... : ...", "opsi": ["Uang : Bank", "Dokter : RS", "Guru : Sekolah", "Pohon : Hutan", "Baju : Lemari"], "jawaban": 0, "pembahasan": "Tempat penyimpanan khusus publik."},
    {"soal": "Semua A adalah B. Beberapa B adalah C. Kesimpulan yang sah adalah...", "opsi": ["Semua A adalah C", "Beberapa A adalah C", "Semua C adalah A", "Tidak dapat ditarik kesimpulan pasti", "Tidak ada hubungan"], "jawaban": 3, "pembahasan": "Karena premis kedua menggunakan 'Beberapa', irisan dengan A tidak pasti."},
    {"soal": "Jika hujan, maka jalan licin. Jika jalan licin, maka macet. Hari ini tidak macet. Kesimpulannya...", "opsi": ["Hari ini hujan deras", "Jalanan licin", "Hari ini tidak hujan", "Banyak polisi lalu lintas", "Jalanan sepi"], "jawaban": 2, "pembahasan": "Modus Tollens berantai mundur: Tidak macet -> tidak licin -> tidak hujan."},
    {"soal": "Budi lebih tinggi dari Andi. Cici lebih pendek dari Andi. Siapa yang paling pendek?", "opsi": ["Budi", "Andi", "Cici", "Sama saja", "Tidak tentu"], "jawaban": 2, "pembahasan": "Urutan tinggi: Budi > Andi > Cici (paling pendek Cici)."},
    {"soal": "120% dari 50 adalah...", "opsi": ["55", "60", "65", "70", "75"], "jawaban": 1, "pembahasan": "1,2 x 50 = 60."},
    {"soal": "Pekerjaan A selesai 6 jam, B selesai 3 jam. Jika dikerjakan bersama selesai dalam...", "opsi": ["1 jam", "2 jam", "3 jam", "4 jam", "5 jam"], "jawaban": 1, "pembahasan": "1/6 + 1/3 = 3/6. Dibalik jadi 6/3 = 2 jam."},
    {"soal": "1, 4, 9, 16, 25, ...", "opsi": ["30", "32", "36", "42", "49"], "jawaban": 2, "pembahasan": "Bilangan kuadrat berurutan. Angka berikutnya 6^2 = 36."},
    {"soal": "Jika 2X + 5 = 15, maka nilai X adalah...", "opsi": ["3", "4", "5", "6", "7"], "jawaban": 2, "pembahasan": "2X = 10 -> X = 5."},
    {"soal": "A di belakang B. C di depan B. D di belakang A. E di depan C. Siapa yang paling depan?", "opsi": ["E", "C", "B", "A", "D"], "jawaban": 0, "pembahasan": "Urutan dari depan ke belakang: E - C - B - A - D."},
    {"soal": "Harga barang naik dari 10.000 menjadi 12.000. Persentase kenaikannya adalah...", "opsi": ["10%", "15%", "20%", "25%", "30%"], "jawaban": 2, "pembahasan": "(2000 / 10000) x 100% = 20%."},
    {"soal": "Rata-rata dari nilai 5, 7, 9, dan 11 adalah...", "opsi": ["7", "8", "9", "10", "11"], "jawaban": 1, "pembahasan": "Jumlah data = 32. Dibagi 4 = 8."},
    {"soal": "SINONIM: Fiktif =", "opsi": ["Nyata", "Asli", "Imajinasi", "Akurat", "Valid"], "jawaban": 2, "pembahasan": "Fiktif berarti bersifat khayalan atau imajinasi."},
    {"soal": "Hidung : Mencium = Telinga : ...", "opsi": ["Melihat", "Mendengar", "Meraba", "Bernapas", "Bersuara"], "jawaban": 1, "pembahasan": "Fungsi organ panca indera."},
    {"soal": "Semua orang Jakarta adalah WNI. Budi lahir di Jakarta. Maka...", "opsi": ["Budi bukan WNI", "Budi suku Jawa", "Budi pasti WNI", "Budi tinggal di luar negeri", "Tidak tahu"], "jawaban": 2, "pembahasan": "Penerapan silogisme mutlak universal."},
    {"soal": "1/2 : 1/4 = ...", "opsi": ["1/8", "1/4", "1/2", "1", "2"], "jawaban": 4, "pembahasan": "1/2 x 4/1 = 2."},
    {"soal": "Akar kuadrat dari 625 adalah...", "opsi": ["15", "20", "25", "30", "35"], "jawaban": 2, "pembahasan": "25 x 25 = 625."},
    {"soal": "3 jam 45 menit sama dengan berapa detik?", "opsi": ["12000", "12500", "13000", "13500", "14000"], "jawaban": 3, "pembahasan": "225 menit x 60 detik = 13.500 detik."},
    {"soal": "Sebuah kubus memiliki panjang rusuk 4 cm. Berapa volumenya?", "opsi": ["16", "32", "48", "64", "128"], "jawaban": 3, "pembahasan": "Volume kubus = r^3 = 4 x 4 x 4 = 64 cm^3."},
    {"soal": "ANTONIM: Konkret ><", "opsi": ["Nyata", "Jelas", "Abstrak", "Bentuk", "Padat"], "jawaban": 2, "pembahasan": "Konkret (berwujud) berlawanan dengan Abstrak."},
    {"soal": "Pola gambar: 1 titik, 2 titik, 3 titik, selanjutnya...", "opsi": ["1", "2", "3", "4", "5"], "jawaban": 3, "pembahasan": "Deret penambahan 1 titik, maka berikutnya 4 titik."},
    {"soal": "0.1 x 0.1 = ...", "opsi": ["0.1", "0.01", "0.001", "1", "10"], "jawaban": 1, "pembahasan": "Perkalian desimal dua angka di belakang koma = 0.01."},
    {"soal": "Angka 100 dikurangi 25% adalah...", "opsi": ["25", "50", "75", "100", "125"], "jawaban": 2, "pembahasan": "25% dari 100 adalah 25. 100 - 25 = 75."},
    {"soal": "A, C, E, G, ...", "opsi": ["H", "I", "J", "K", "L"], "jawaban": 1, "pembahasan": "Huruf melompat 1 tingkat: A(b)C(d)E(f)G(h)I."},
    {"soal": "Jika 10 km ditempuh dalam 15 menit, berapa kecepatan per jamnya?", "opsi": ["20", "30", "40", "50", "60"], "jawaban": 2, "pembahasan": "15 menit adalah 1/4 jam. Kecepatan = 10 / (1/4) = 40 km/jam."}
]

soal_tkp_lengkap = [
    {"soal": "Sistem IT kantor mengalami mati total saat jam sibuk pelayanan. Tindakan Anda...", "opsi": ["Pulang karena pekerjaan tidak bisa dilanjutkan", "Marah kepada bagian teknis di depan umum", "Bermain handphone sambil menunggu", "Merapikan arsip fisik dan membantu pelayanan manual secara sabar", "Tidur di ruang istirahat"], "skor": [1, 2, 3, 5, 1]},
    {"soal": "Kantor mengeluarkan aturan baru wajib datang 15 menit sebelum jam kerja. Sikap Anda...", "opsi": ["Menolak aturan karena terlalu pagi", "Protes bersama rekan kerja lain", "Mematuhi dengan terpaksa dan ngedumel", "Mentaati aturan tersebut sebagai wujud profesionalisme", "Mengabaikannya jika tidak diawasi bos"], "skor": [1, 2, 3, 5, 1]},
    {"soal": "Pelanggan menanyakan informasi layanan yang belum pernah Anda ketahui sebelumnya. Anda...", "opsi": ["Menjawab asal-asalan agar terlihat tahu", "Menolak melayani pelanggan tersebut", "Memberikan brosur kantor secara acak", "Berkoordinasi dengan rekan yang lebih tahu untuk membantu pelanggan", "Menyuruh pelanggan pergi mencari sendiri"], "skor": [2, 1, 3, 5, 1]},
    {"soal": "Proyek tim Anda gagal memenuhi target, dan ketua tim secara tidak adil menyalahkan Anda di depan umum...", "opsi": ["Membalas menuduh ketua tim di hadapan semua orang", "Diam saja menyimpan dendam", "Memberikan klarifikasi secara tenang dengan data objektif", "Mengajukan pengunduran diri saat itu juga", "Menangis dan meninggalkan ruangan"], "skor": [2, 3, 5, 1, 1]},
    {"soal": "Anda memergoki rekan sekantor menggunakan WiFi kantor untuk menonton film streaming selama jam kerja...", "opsi": ["Ikut menonton bersama mereka", "Membiarkan saja bukan urusan saya", "Menegurnya secara sopan agar kembali fokus bekerja", "Melaporkannya langsung ke pimpinan tertinggi", "Mencabut kabel jaringan komputer mereka"], "skor": [2, 3, 5, 4, 1]},
    {"soal": "Anda diminta lembur mendadak padahal sudah berjanji mendampingi keluarga di rumah...", "opsi": ["Langsung pulang tanpa pamit", "Menerima lembur namun handphone sengaja dimatikan", "Menghubungi keluarga menjelaskan situasi, lalu menyelesaikan lembur dengan profesional", "Mengerjakan tugas lembur dengan asal-asalan", "Meminta rekan lain menggantikan tanpa izin"], "skor": [1, 2, 5, 3, 2]},
    {"soal": "Instansi mewajibkan penggunaan aplikasi digital baru yang belum Anda kenal sama sekali...", "opsi": ["Menolak menggunakan aplikasi karena sudah nyaman cara lama", "Meminta bagian IT mengganti sistem", "Mengeluhkan kerumitan aplikasi tersebut", "Mempelajari aplikasi tersebut dengan cepat secara mandiri", "Menggunakan cara manual sembunyi-sembunyi"], "skor": [1, 2, 1, 5, 3]},
    {"soal": "Rekan dari divisi lain meminta data internal kantor yang bersifat rahasia kepada Anda...", "opsi": ["Langsung memberikan data tersebut karena kasihan", "Menolak memberikan data sesuai prosedur SOP kerahasiaan kantor", "Meminta imbalan uang sebagai syarat", "Pura-pura tidak mendengarkan permintaan tersebut", "Mengancam akan melaporkan rekan tersebut ke polisi"], "skor": [1, 5, 1, 3, 2]},
    {"soal": "Anda mendapat SK mutasi ke cabang daerah terpencil yang fasilitasnya sangat minim...", "opsi": ["Mengajukan surat pengunduran diri (resign)", "Menolak mutasi secara tegas kepada HRD", "Meminta kenaikan tunjangan besar jika ingin pindah", "Menerima penugasan tersebut sebagai tantangan dan kesempatan mengabdi", "Mengeluh setiap hari di tempat baru"], "skor": [1, 2, 3, 5, 2]},
    {"soal": "Rekan kerja Anda sedang berpuasa, sementara Anda membawa makanan ringan di sebelah mejanya...", "opsi": ["Makan dengan sengaja tepat di depan wajahnya", "Memindahkan aktivitas makan ke kantin atau ruang istirahat", "Menawari makanan tersebut kepadanya secara terus menerus", "Ikut berpura-pura berpuasa", "Memarahinya karena membuat Anda tidak bebas makan"], "skor": [2, 5, 1, 3, 1]},
    {"soal": "Seorang pelanggan marah-marah di loket karena antrean yang dianggap terlalu lama...", "opsi": ["Mengabaikannya agar dia lelah sendiri", "Ikut terpancing emosi dan membalas marahnya", "Memanggil petugas keamanan untuk menyeretnya", "Mendengarkan keluh kesahnya dengan sabar dan menjelaskan situasi secara humanis", "Memberikan nomor antrean baru secara paksa"], "skor": [1, 2, 3, 5, 4]},
    {"soal": "Aturan penyimpanan data kantor beralih menggunakan sistem cloud computing...", "opsi": ["Tetap mencetak semua dokumen ke kertas fisik", "Menyuruh staf junior mengurus semuanya", "Mematuhinya secara pasif tanpa antusias", "Mempelajari tutorial penggunaan cloud sepulang kerja secara mandiri", "Mencari kelemahan sistem untuk diprotes"], "skor": [1, 2, 3, 5, 4]},
    {"soal": "Atasan memberikan tugas tambahan di saat meja kerja Anda sedang menumpuk...", "opsi": ["Menolak tugas tersebut secara mentah-mentah", "Mengerjakan tugas dengan hasil seadanya", "Menunda pekerjaan rutin demi tugas baru", "Mengatur ulang prioritas kerja secara terstruktur dan menyelesaikannya", "Meminta bantuan orang lain tanpa usaha"], "skor": [1, 2, 3, 5, 4]},
    {"soal": "Rekan kerja Anda sering datang terlambat dan mengganggu produktivitas tim...", "opsi": ["Membiarkan saja karena bukan urusan saya", "Langsung melaporkannya kepada atasan", "Mengambil alih seluruh pekerjaannya", "Mengajaknya bicara secara empat mata untuk mengingatkan secara kekeluargaan", "Menceritakan kebiasaan buruknya kepada orang lain"], "skor": [1, 4, 3, 5, 2]},
    {"soal": "Anda menemukan dompet berisi uang tunai cukup banyak di area parkir kantor...", "opsi": ["Membiarkan dompet tersebut tergeletak", "Mengambil sebagian uangnya untuk keperluan mendadak", "Menyerahkan dompet kepada pos satpam", "Menyimpan dompet di laci meja pribadi", "Berusaha mencari pemilik dompet melalui identitas di dalamnya atau melaporkan ke bagian umum"], "skor": [2, 1, 4, 3, 5]},
    {"soal": "Kebijakan baru pimpinan dinilai rumit oleh sebagian besar pegawai...", "opsi": ["Mengabaikan kebijakan tersebut di bagian saya", "Melakukan aksi protes keras bersama pegawai lain", "Menjalankan dengan pasrah tanpa inovasi", "Mencari celah kelemahan aturan", "Mempelajari maksud kebijakan dan memberikan usul perbaikan konstruktif berlandaskan data"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Tim kerja Anda kedatangan anggota baru yang memiliki latar belakang suku dan budaya berbeda...", "opsi": ["Meminta atasan memindahkan anggota tersebut", "Menjaga jarak dan menyendiri", "Bersikap sopan sebatas formalitas pekerjaan", "Berbaur secara terbuka dan membangun kerja sama yang inklusif", "Mempelajari kebudayaannya secara mendalam agar bisa akrab"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Seorang lansia datang ke kantor tepat saat jam layanan loket akan ditutup...", "opsi": ["Menolak melayani karena sudah waktunya tutup", "Menyuruhnya datang kembali besok pagi", "Melayani dengan ekspresi terpaksa dan terburu-buru", "Mengerjakan secara manual seadanya", "Tetap melayani dengan ramah dan tuntas hingga urusannya selesai"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Rekan kerja Anda kesulitan mengoperasikan mesin pencetak dokumen baru...", "opsi": ["Membiarkannya belajar sendiri sampai frustrasi", "Menertawakan ketidaktahuannya", "Mengerjakan pencetakan dokumen untuknya setiap hari", "Memberikan buku manual untuk dibaca", "Menyimak kesulitannya dan membimbing langsung cara penggunaannya"], "skor": [2, 1, 3, 4, 5]},
    {"soal": "Anda mengikuti seminar kantor yang materinya terasa membosankan dan monoton...", "opsi": ["Tidur di kursi peserta seminar", "Bermain game di handphone sepanjang acara", "Keluar ruangan diam-diam kabur", "Mendengarkan seadanya sambil lalu", "Tetap fokus mencatat poin penting sebagai bentuk tanggung jawab"], "skor": [1, 2, 1, 4, 5]},
    {"soal": "Rekan kerja Anda jatuh sakit dan tugasnya terbengkalai di kantor...", "opsi": ["Membiarkan pekerjaan tersebut menumpuk", "Menunggu perintah atasan baru bergerak", "Membantu sebagian kecil saja", "Mengkoordinasikan rekan lain untuk membantu menyelesaikan tugas tersebut hingga tuntas", "Memprotes kenapa tugasnya dilimpahkan ke orang lain"], "skor": [1, 2, 3, 5, 1]},
    {"soal": "Anda mendapati kelebihan uang kembalian transaksi di kasir kantin kantor...", "opsi": ["Mengambil uang tersebut untuk jajan", "Diam saja dan menyimpannya", "Memberikan kepada teman lain", "Melaporkan dan mengembalikan kelebihan uang tersebut secara jujur", "Membelikan barang sumbangan amal tanpa izin"], "skor": [1, 1, 1, 5, 1]},
    {"soal": "Tamu penting instansi datang berkunjung secara mendadak tanpa jadwal terkonfirmasi...", "opsi": ["Mengusirnya keluar karena tidak ada janji", "Menyuruhnya menunggu di luar tanpa kepastian", "Bersikap acuh tak acuh", "Menyambut dengan sopan, ramah, dan sigap melaporkan ke pimpinan", "Memanggil pimpinan dengan nada membentak"], "skor": [1, 2, 1, 5, 4]},
    {"soal": "Anda ditawari sejumlah uang oleh rekanan agar mempercepat pengurusan izin proyek...", "opsi": ["Menerima uang tersebut secara sembunyi-sembunyi", "Meminta nominal tambahan yang lebih besar", "Merasa ragu-ragu apakah harus ambil", "Menolak tawaran tersebut secara tegas", "Menolak secara tegas dan melaporkan tindakan suap tersebut ke instansi berwenang"], "skor": [1, 1, 3, 5, 4]},
    {"soal": "Anda dikritik secara pedas oleh atasan di dalam forum rapat resmi...", "opsi": ["Marah dan membentak balik atasan", "Menangis tersedu-sedu di ruangan", "Membela diri secara agresif", "Menerima evaluasi tersebut dengan kepala dingin", "Mencatat masukan tersebut, mengevaluasi diri, dan memperbaiki kinerja ke depan"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Komputer rekan kerja Anda mengalami kerusakan total menjelang presentasi...", "opsi": ["Menyukuri musibah yang dialaminya", "Membiarkan saja bukan urusan saya", "Meminjamkan laptop cadangan milik pribadi untuk digunakan", "Membantu memperbaiki sistem komputernya", "Menyuruhnya membeli perangkat baru saat itu juga"], "skor": [1, 2, 5, 4, 1]},
    {"soal": "Atasan meminta Anda menyetujui laporan fiktif demi citra baik instansi...", "opsi": ["Menyetujuinya demi mencari aman di mata bos", "Melakukan negosiasi jumlah nominal fiktif", "Menolak secara kasar", "Melaporkan langsung ke media sosial publik", "Menolak secara santun dan menawarkan alternatif solusi pelaporan yang transparan dan legal"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Anak buah di bawah koordinasi Anda melakukan kesalahan fatal yang merugikan tim...", "opsi": ["Langsung memecatnya saat itu juga", "Memarahi dan mempermalukannya di depan staf lain", "Melakukan pembinaan terarah dan mengevaluasi sistem kerja", "Menutupi kesalahan tersebut agar tidak ketahuan atasan", "Mengajaknya berdiskusi empat mata untuk mencari akar masalah dan solusi"], "skor": [1, 1, 4, 2, 5]},
    {"soal": "Ada penawaran pelatihan pengembangan kompetensi gratis dari lembaga negara lain...", "opsi": ["Mengabaikan informasi tersebut", "Ikut mendaftar hanya jika dipaksa atasan", "Berangkat daftar hanya untuk mengambil uang saku", "Mengikuti seleksi dengan semangat belajar tinggi", "Mendaftar secara antusias dan berkomitmen menyebarkan ilmu setelahnya"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Perjalanan menuju kantor mengalami kemacetan lalu lintas total akibat kecelakaan...", "opsi": ["Mengeluh dan langsung kembali pulang", "Membolos kerja hari itu", "Datang terlambat tanpa konfirmasi", "Mencari jalur alternatif lain yang lebih lancar", "Berangkat lebih pagi pada hari-hari berikutnya sebagai langkah antisipasi"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Atasan Anda sering memberikan instruksi yang berubah-ubah dan membingungkan...", "opsi": ["Mengajukan pengunduran diri dari kantor", "Melawan kebijakan atasan secara terbuka", "Diam memendam rasa kesal", "Tetap menjalankan tugas sambil meminta kejelasan instruksi tertulis", "Mengajak atasan berdiskusi empat mata secara profesional untuk menyamakan persepsi"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Di hari libur akhir pekan, Anda dihubungi atasan untuk urusan kantor yang mendesak...", "opsi": ["Mematikan handphone agar tidak terganggu", "Mengabaikan panggilan tersebut", "Menjawab ketus jika sedang mood jelek", "Membantu koordinasi penyelesaian masalah dari jarak jauh", "Segera bergegas mendatangi kantor saat itu juga"], "skor": [1, 2, 3, 4, 5]},
    {"soal": "Ide cemerlang Anda diakui oleh rekan kerja sebagai ide miliknya di depan atasan...", "opsi": ["Memukul rekan tersebut di tempat", "Menyindirnya lewat status media sosial", "Melapor ke pimpinan sambil marah-marah", "Mengajak rekan tersebut berbicara secara empat mata untuk meluruskan", "Diam saja mengalah demi kebaikan"], "skor": [1, 2, 3, 5, 1]},
    {"soal": "Anda mendapatkan fasilitas mobil dinas operasional dari kantor...", "opsi": ["Menggunakannya untuk keperluan jalan-jalan pribadi keluarga", "Meminjamkannya kepada tetangga", "Menjualnya untuk modal usaha", "Memakainya semata-mata untuk menunjang kelancaran tugas kedinasan", "Merawat dan menjaga kebersihannya dengan penuh tanggung jawab"], "skor": [1, 1, 1, 4, 5]},
    {"soal": "Aliran listrik di kantor padam mendadak saat dokumen penting belum tersimpan...", "opsi": ["Memutuskan langsung pulang ke rumah", "Tidur di meja kerja", "Bergosip bersama rekan lain", "Memeriksa genset atau menunggu instruksi penanganan", "Berinisiatif menggunakan penyimpanan cadangan/genset mandiri jika ada"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Beredar berita viral di media sosial yang memojokkan instansi tempat Anda bekerja...", "opsi": ["Ikut membagikan berita tersebut tanpa verifikasi", "Memberikan komentar hujatan di kolom komentar", "Diam tidak peduli", "Membabi buta membela tanpa argumen jelas", "Mencari fakta dan data valid dari sumber resmi sebelum merespons"], "skor": [1, 1, 3, 2, 5]},
    {"soal": "Intensitas lembur kerja yang tinggi mulai menurunkan kondisi kesehatan fisik Anda...", "opsi": ["Menyalahkan atasan atas beban kerja", "Mengajukan pengunduran diri", "Sering membolos kerja", "Mengkonsumsi obat penahan sakit terus menerus", "Mengatur manajemen waktu dengan baik dan menerapkan pola hidup sehat"], "skor": [1, 2, 2, 3, 5]},
    {"soal": "Rekan kerja di sebelah meja gemar membicarakan keburukan orang lain (gosip)...", "opsi": ["Ikut nimbrung nimbrung dalam topik gosip", "Mendengarkan dengan antusias", "Menjauhi pergaulan kantor secara total", "Menegur secara keras di depan umum", "Memberikan nasihat baik secara halus dan menghindari topik tersebut"], "skor": [1, 2, 4, 3, 5]},
    {"soal": "Proyek besar harus berjalan namun anggaran dana dari instansi sangat minim...", "opsi": ["Membatalkan seluruh kegiatan proyek", "Meminta iuran paksa kepada warga/rekan", "Menggunakan uang pribadi tanpa kejelasan", "Mencari alternatif sponsor atau mitra kerja sama legal", "Melakukan optimasi anggaran secara efisien dan kreatif"], "skor": [1, 1, 3, 4, 5]},
    {"soal": "Ketua tim Anda terkesan pilih kasih dalam membagikan tugas dan fasilitas...", "opsi": ["Mengadakan aksi demonstrasi di kantor", "Mengajukan surat pengunduran diri", "Mengeluh di media sosial", "Membuktikan kualitas diri melalui prestasi kerja", "Mengajak ketua tim berdiskusi secara profesional dan terbuka"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Terjadi perdebatan argumen yang sangat panas antar anggota dalam rapat tim...", "opsi": ["Walk out meninggalkan ruangan rapat", "Ikut berteriak-teriak melampiaskan emosi", "Diam aman tidak bersuara", "Memisahkan pihak yang berdebat", "Menengahi perdebatan dan memfasilitasi titik temu solusi"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Jaringan internet kantor terputus total saat batas waktu pengiriman laporan krusial...", "opsi": ["Panik berlebihan dan menangis", "Menyalahkan penyedia layanan internet (provider)", "Menggunakan koneksi tethering handphone pribadi secara mandiri", "Segera mencari lokasi atau ruangan dengan jaringan alternatif terdekat", "Membiarkan laporan terlambat terkumpul"], "skor": [1, 1, 2, 4, 5]},
    {"soal": "Anda mendapatkan promosi jabatan kenaikan pangkat, namun rekan terdekat Anda merasa iri...", "opsi": ["Menyombongkan diri di hadapannya", "Menjauhi rekan tersebut secara permanen", "Bersikap biasa saja seperti tidak terjadi apa-apa", "Mentraktirnya makan secara terpaksa", "Tetap rendah hati, ramah, dan merangkulnya seperti biasa"], "skor": [1, 2, 3, 2, 5]},
    {"soal": "Atasan menyuruh Anda membelikan barang kebutuhan pribadi keluarganya menggunakan jam kerja kantor...", "opsi": ["Marah dan membentak atasan", "Menolak dengan kata-kata kasar", "Melaporkan langsung ke bagian disiplin", "Mengerjakannya demi mencari muka", "Menolak secara halus dengan alasan sedang fokus menyelesaikan tugas kedinasan"], "skor": [2, 3, 4, 1, 5]},
    {"soal": "Pekerjaan harian di kantor terasa sangat monoton dan tidak ada tantangan baru...", "opsi": ["Merasa bosan dan malas-malasan bekerja", "Mengerjakan tugas dengan sangat lambat", "Bermain game di komputer kantor", "Tetap fokus menjaga kualitas kerja", "Mencari bentuk inovasi atau metode baru yang lebih efektif untuk menyelesaikan tugas tersebut"], "skor": [1, 2, 1, 5, 4]}
]

# ==========================================
# INISIALISASI STATE
# ==========================================
if 'ujian_dimulai' not in st.session_state: st.session_state.ujian_dimulai = False
if 'waktu_mulai' not in st.session_state: st.session_state.waktu_mulai = 0
if 'waktu_selesai' not in st.session_state: st.session_state.waktu_selesai = 0
if 'telah_submit' not in st.session_state: st.session_state.telah_submit = False
if 'jawaban_user' not in st.session_state: st.session_state.jawaban_user = {}

# ==========================================
# MENU UTAMA
# ==========================================
if not st.session_state.ujian_dimulai:
    st.title("📚 Pusat Simulasi SKD CPNS 100 Menit")
    st.info("Paket Ujian Komprehensif: 110 Soal (30 TWK, 35 TIU, 45 TKP) Sesuai Standar CAT BKN Resmi.")
    st.markdown("---")
    
    if st.button("🚀 MULAI UJIAN SKD SEKARANG", use_container_width=True):
        st.session_state.ujian_dimulai = True
        st.session_state.waktu_mulai = time.time()
        st.session_state.telah_submit = False 
        st.session_state.jawaban_user = {}
        st.rerun()

# ==========================================
# SAAT UJIAN BERJALAN
# ==========================================
else:
    if not st.session_state.telah_submit:
        durasi_ujian = 6000  # 100 Menit dalam detik
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
                timerElement.style.cssText = 'position: fixed; bottom: 20px; right: 20px; background-color: #d32f2f; color: white; padding: 12px 20px; border-radius: 8px; font-weight: bold; font-family: sans-serif; z-index: 9999; box-shadow: 0px 4px 10px rgba(0,0,0,0.3); border: 2px solid white;';
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
                    var buttons = parentDoc.querySelectorAll('button');
                    for (var i = 0; i < buttons.length; i++) {{
                        if (buttons[i].innerText.includes('Kumpulkan Jawaban')) {{ buttons[i].click(); break; }}
                    }}
                }}
            }}, 1000);
        </script>
        """
        components.html(js_timer, height=0, width=0)

        st.subheader("Simulasi CAT BKN: 110 Soal (TWK, TIU, TKP)")
        st.markdown("---")
        
        with st.form(key='form_ujian_lengkap'):
            jawaban_sementara = {}
            
            st.markdown("### 🇮🇩 Bagian I: TWK (Soal 1 - 30)")
            for i, item in enumerate(soal_twk_lengkap):
                st.markdown(f"**{i+1}. {item['soal']}**")
                jawaban_sementara[f"twk_{i}"] = st.radio(label=f"TWK_{i}", options=item["opsi"], index=None, label_visibility="collapsed")
                st.write("")
                
            st.markdown("### 🧠 Bagian II: TIU (Soal 31 - 65)")
            for i, item in enumerate(soal_tiu_lengkap):
                st.markdown(f"**{i + 31}. {item['soal']}**")
                jawaban_sementara[f"tiu_{i}"] = st.radio(label=f"TIU_{i}", options=item["opsi"], index=None, label_visibility="collapsed")
                st.write("")
                
            st.markdown("### 🤝 Bagian III: TKP (Soal 66 - 110)")
            for i, item in enumerate(soal_tkp_lengkap):
                st.markdown(f"**{i + 66}. {item['soal']}**")
                jawaban_sementara[f"tkp_{i}"] = st.radio(label=f"TKP_{i}", options=item["opsi"], index=None, label_visibility="collapsed")
                st.write("")

            if st.form_submit_button(label='Kumpulkan Jawaban', use_container_width=True):
                st.session_state.waktu_selesai = time.time()
                st.session_state.telah_submit = True
                st.session_state.jawaban_user = jawaban_sementara
                st.rerun()

# ==========================================
# HASIL EVALUASI & SKORING
# ==========================================
if st.session_state.telah_submit:
    components.html("<script>var t = window.parent.document.getElementById('custom_timer_display'); if(t) t.remove();</script>", height=0, width=0)
    
    st.title("📊 HASIL EVALUASI UJIAN SKD")
    st.markdown("---")

    skor_twk, skor_tiu, skor_tkp = 0, 0, 0
    
    # Hitung TWK (Benar=5, Salah=0)
    for i, item in enumerate(soal_twk_lengkap):
        if st.session_state.jawaban_user.get(f"twk_{i}") == item["opsi"][item["jawaban"]]: 
            skor_twk += 5
            
    # Hitung TIU (Benar=5, Salah=0)
    for i, item in enumerate(soal_tiu_lengkap):
        if st.session_state.jawaban_user.get(f"tiu_{i}") == item["opsi"][item["jawaban"]]: 
            skor_tiu += 5
            
    # Hitung TKP (Skor 1-5)
    for i, item in enumerate(soal_tkp_lengkap):
        jwb = st.session_state.jawaban_user.get(f"tkp_{i}")
        if jwb: 
            skor_tkp += item["skor"][item["opsi"].index(jwb)]

    total_skor = skor_twk + skor_tiu + skor_tkp
    lulus = (skor_twk >= 65) and (skor_tiu >= 80) and (skor_tkp >= 166)

    if lulus:
        st.success(f"🎉 LUAR BIASA! Anda **MEMENUHI PASSING GRADE** dengan Total Skor {total_skor} (Maks: 550)")
    else:
        st.error(f"❌ Sayang sekali, Anda **BELUM MEMENUHI PASSING GRADE**. Total Skor: {total_skor}")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("SKOR TOTAL", f"{total_skor}")
    c2.metric("TWK", f"{skor_twk} / 150", delta="Ambang: 65", delta_color="off" if skor_twk >= 65 else "inverse")
    c3.metric("TIU", f"{skor_tiu} / 175", delta="Ambang: 80", delta_color="off" if skor_tiu >= 80 else "inverse")
    c4.metric("TKP", f"{skor_tkp} / 225", delta="Ambang: 166", delta_color="off" if skor_tkp >= 166 else "inverse")
    
    st.markdown("---")
    if st.button("Kembali ke Menu Utama"):
        st.session_state.ujian_dimulai = False
        st.session_state.telah_submit = False
        st.rerun()
