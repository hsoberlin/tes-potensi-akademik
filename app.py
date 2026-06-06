import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="Pusat Simulasi Ujian TPA & SKD", layout="wide")

# ==========================================
# 1. DATABASE SOAL (DENGAN PENOMORAN OTOMATIS)
# ==========================================
# Catatan: Teks soal di bawah ini tidak lagi memakai angka di depannya (misal "1. "), 
# karena angka akan dibuat otomatis oleh sistem saat ditampilkan.

soal_paket_1 = [
    {"soal": "8 x 7 = ...", "opsi": ["54", "56", "64", "48"], "jawaban": 1, "pembahasan": "Hafalan dasar perkalian 8 x 7 = 56."},
    {"soal": "63 : 9 = ...", "opsi": ["6", "7", "8", "9"], "jawaban": 1, "pembahasan": "Kebalikan dari 7 x 9 = 63."},
    {"soal": "9 x 6 = ...", "opsi": ["54", "56", "45", "64"], "jawaban": 0, "pembahasan": "Hafalan dasar perkalian 9 x 6 = 54."},
    {"soal": "72 : 8 = ...", "opsi": ["7", "8", "9", "10"], "jawaban": 2, "pembahasan": "Kebalikan dari 9 x 8 = 72."},
    {"soal": "5 + 4 x 3 = ...", "opsi": ["27", "17", "12", "32"], "jawaban": 1, "pembahasan": "Kali dikerjakan lebih dulu: 4x3 = 12. Lalu 5 + 12 = 17."}
]
# Mengisi sisa soal Paket 1 hingga genap 50 soal untuk keperluan testing UI
while len(soal_paket_1) < 50:
    soal_paket_1.append({"soal": "Soal Latihan Dasar (Contoh)", "opsi": ["A", "B", "C", "D"], "jawaban": 0, "pembahasan": "Penjelasan soal dasar."})

soal_paket_2 = [
    {"soal": "12 x 15 = ...", "opsi": ["160", "170", "180", "190"], "jawaban": 2, "pembahasan": "10x15 = 150, ditambah 2x15 = 30. Hasil = 180."},
    {"soal": "144 : 12 = ...", "opsi": ["10", "12", "14", "16"], "jawaban": 1, "pembahasan": "Akar kuadrat dari 144 adalah 12."},
    {"soal": "25 + 15 x 4 - 10 = ...", "opsi": ["150", "100", "75", "65"], "jawaban": 2, "pembahasan": "Kali dulu: 15x4 = 60. Lalu 25 + 60 - 10 = 75."},
    {"soal": "(18 - 6) x (10 + 2) = ...", "opsi": ["144", "124", "120", "100"], "jawaban": 0, "pembahasan": "Kerjakan dalam kurung: 12 x 12 = 144."},
    {"soal": "50% dari 0.8 adalah...", "opsi": ["0.4", "0.5", "4", "40"], "jawaban": 0, "pembahasan": "Setengah dari 0.8 adalah 0.4."}
]
# Mengisi sisa soal Paket 2 hingga genap 50 soal
while len(soal_paket_2) < 50:
    soal_paket_2.append({"soal": "Soal Latihan Lanjutan (Contoh)", "opsi": ["A", "B", "C", "D"], "jawaban": 0, "pembahasan": "Penjelasan soal lanjutan."})

# --- DATABASE PAKET 3 (SKD: TWK, TIU, TKP) ---
soal_twk = [
    {"soal": "Sila ke-4 Pancasila mengajarkan kita untuk mengutamakan musyawarah. Dalam kehidupan sehari-hari, hal ini paling tepat diterapkan saat...", "opsi": ["Menentukan menu makan siang pribadi", "Memilih ketua RT", "Menentukan tempat wisata keluarga", "Membeli barang kebutuhan pokok", "Jawaban B dan C benar"], "jawaban": 4, "pembahasan": "Musyawarah dilakukan untuk keputusan yang melibatkan banyak orang."},
    {"soal": "Menggunakan produk dalam negeri merupakan wujud dari nilai Pancasila ke...", "opsi": ["Satu", "Dua", "Tiga", "Empat", "Lima"], "jawaban": 2, "pembahasan": "Sila ke-3 (Persatuan Indonesia) mencakup rasa cinta tanah air."}
]
# Memastikan TWK berjumlah persis 30 soal
while len(soal_twk) < 30:
    soal_twk.append({"soal": "Soal TWK lainnya...", "opsi": ["A", "B", "C", "D", "E"], "jawaban": 0, "pembahasan": "Penjelasan TWK."})

soal_tiu = [
    {"soal": "85 + 15 x 2 - 10 = ...", "opsi": ["105", "190", "115", "100", "95"], "jawaban": 0, "pembahasan": "(15x2)=30. 85+30-10 = 105."},
    {"soal": "0,25 + 3/4 = ...", "opsi": ["0,5", "0,75", "1", "1,25", "1,5"], "jawaban": 2, "pembahasan": "3/4 = 0,75. 0,25 + 0,75 = 1."}
]
# Memastikan TIU berjumlah persis 35 soal
while len(soal_tiu) < 35:
    soal_tiu.append({"soal": "Soal TIU lainnya...", "opsi": ["A", "B", "C", "D", "E"], "jawaban": 0, "pembahasan": "Penjelasan TIU."})

soal_tkp = [
    {"soal": "Sistem IT kantor mengalami gangguan sehingga pekerjaan tertunda. Anda akan...", "opsi": ["Menunggu saja sampai teknisi datang", "Marah-marah karena target tidak tercapai", "Mencoba memperbaiki sendiri meski bukan ahli", "Menggunakan waktu luang untuk merapikan dokumen fisik sambil menunggu", "Pulang ke rumah"], "skor": [2, 1, 3, 5, 1], "pembahasan": "Poin maksimal (5) ada pada tindakan proaktif yang positif (D)."},
    {"soal": "Ada aturan baru untuk datang 15 menit lebih awal. Anda merasa keberatan. Sikap Anda...", "opsi": ["Datang seperti biasa", "Mengajak teman lain memprotes", "Mematuhi meski sambil menggerutu", "Mentaati aturan tersebut sebagai bentuk profesionalisme", "Datang awal jika ada atasan saja"], "skor": [1, 2, 3, 5, 2], "pembahasan": "Kepatuhan pada instansi dan profesionalisme bernilai 5 (D)."}
]
# Memastikan TKP berjumlah persis 45 soal
while len(soal_tkp) < 45:
    soal_tkp.append({"soal": "Situasi kerja: Anda diberikan tugas mendadak. Sikap Anda...", "opsi": ["Opsi A", "Opsi B", "Opsi C", "Opsi D", "Opsi E"], "skor": [1, 2, 3, 4, 5], "pembahasan": "Penjelasan TKP."})


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
    st.title("📚 Pusat Pelatihan TPA & SKD")
    st.markdown("---")
    
    st.session_state.pilihan_paket = st.radio(
        "Pilih Modul Ujian:",
        [
            "Paket 1: TIU Dasar (50 Soal / 60 Menit)", 
            "Paket 2: TIU Lanjutan (50 Soal / 60 Menit)", 
            "Paket 3: SKD Nasional (110 Soal / 100 Menit)"
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
        
        # --- A. PENGATURAN WAKTU OTOMATIS BERDASARKAN PAKET ---
        if "Paket 3" in st.session_state.pilihan_paket:
            durasi_ujian = 6000  # 100 Menit
        else:
            durasi_ujian = 3600  # 60 Menit
            
        waktu_berjalan = time.time() - st.session_state.waktu_mulai
        sisa_waktu_detik = int(durasi_ujian - waktu_berjalan)
        
        # --- B. SCRIPT TIMER ANTI-FLICKER (Diperbarui) ---
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
            
            if (parentDoc.timerInterval) {{
                clearInterval(parentDoc.timerInterval);
            }}
            
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

        # --- C. RENDER SOAL ---
        st.subheader(f"Mengerjakan: {st.session_state.pilihan_paket}")
        st.markdown("---")
        
        with st.form(key='form_ujian'):
            jawaban_sementara = {}
            
            # --- PAKET 1 / PAKET 2 ---
            if "Paket 1" in st.session_state.pilihan_paket or "Paket 2" in st.session_state.pilihan_paket:
                soal_aktif = soal_paket_1 if "Paket 1" in st.session_state.pilihan_paket else soal_paket_2
                for i, item in enumerate(soal_aktif):
                    st.markdown(f"**{i+1}. {item['soal']}**")
                    pilihan = st.radio(label=f"Soal {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"tiu_{i}")
                    jawaban_sementara[f"tiu_{i}"] = pilihan
                    st.write("")
                    
            # --- PAKET 3 (SKD 110 SOAL) ---
            elif "Paket 3" in st.session_state.pilihan_paket:
                st.markdown("#### Bagian I: TWK (Tes Wawasan Kebangsaan)")
                for i, item in enumerate(soal_twk):
                    st.markdown(f"**{i+1}. {item['soal']}**")
                    pilihan = st.radio(label=f"TWK {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"twk_{i}")
                    jawaban_sementara[f"twk_{i}"] = pilihan
                    st.write("")
                    
                st.markdown("#### Bagian II: TIU (Tes Intelegensia Umum)")
                for i, item in enumerate(soal_tiu):
                    # Melanjutkan nomor setelah 30 (berarti mulai 31)
                    st.markdown(f"**{i+31}. {item['soal']}**")
                    pilihan = st.radio(label=f"TIU {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"tiu_skd_{i}")
                    jawaban_sementara[f"tiu_skd_{i}"] = pilihan
                    st.write("")
                    
                st.markdown("#### Bagian III: TKP (Tes Karakteristik Pribadi)")
                for i, item in enumerate(soal_tkp):
                    # Melanjutkan nomor setelah 65 (berarti mulai 66)
                    st.markdown(f"**{i+66}. {item['soal']}**")
                    pilihan = st.radio(label=f"TKP {i}", options=item["opsi"], index=None, label_visibility="collapsed", key=f"tkp_{i}")
                    jawaban_sementara[f"tkp_{i}"] = pilihan
                    st.write("")

            submit_button = st.form_submit_button(label='Kumpulkan Jawaban', use_container_width=True)

        # --- D. LOGIKA PENILAIAN ---
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
                with st.expander(f"TIU No. {i+31} (Salah)"):
                    st.write(f"**Soal:** {item['soal']}")
                    st.write(f"❌ **Jawabanmu:** {j_user if j_user else 'Kosong'}")
                    st.write(f"✅ **Jawaban Benar:** {j_benar}")
                    st.info(f"**Pembahasan:** {item['pembahasan']}")
        
        st.markdown("### Evaluasi TKP (Tidak mendapat Poin Maksimal)")
        for i, item in enumerate(soal_tkp):
            j_user = st.session_state.jawaban_user.get(f"tkp_{i}")
            poin = item["skor"][item["opsi"].index(j_user)] if j_user else 0
            if poin < 5:
                terbaik = item["opsi"][item["skor"].index(5)]
                with st.expander(f"TKP No. {i+66} (Poin: {poin}/5)"):
                    st.write(f"**Soal:** {item['soal']}")
                    st.write(f"**Pilihanmu:** {j_user if j_user else 'Kosong'}")
                    st.write(f"**Tindakan Terbaik (Poin 5):** {terbaik}")
                    if "pembahasan" in item: st.info(f"**Pembahasan:** {item['pembahasan']}")

    st.markdown("---")
    if st.button("Kembali ke Menu Utama"):
        st.session_state.ujian_dimulai = False
        st.session_state.telah_submit = False
        st.rerun()
