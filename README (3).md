# 🚦 Sistem Monitoring Lalu Lintas

> Aplikasi pintar berbasis **Machine Learning** untuk memprediksi tingkat kemacetan lalu lintas secara real-time berdasarkan volume dan kecepatan kendaraan.

🔗 **Akses Aplikasi:** [https://trafficbase.streamlit.app](https://trafficbase.streamlit.app)

---

## 📋 Tentang Aplikasi

Sistem Monitoring Lalu Lintas adalah aplikasi web interaktif yang membantu pengguna — seperti pengemudi, petugas lalu lintas, maupun perencana kota — untuk mengetahui **status kepadatan lalu lintas** di suatu persimpangan berdasarkan data kondisi jalan saat ini. Sistem ini menggunakan model **Machine Learning Klasifikasi** untuk menghasilkan prediksi yang akurat dan cepat.

---

## 🚀 Cara Menggunakan Aplikasi

### Langkah 1 — Buka Aplikasi
Kunjungi [https://trafficbase.streamlit.app](https://trafficbase.streamlit.app) melalui browser Anda. Tidak perlu login atau instalasi apapun.

### Langkah 2 — Isi Parameter Jalan
Pada bagian **"Parameter Jalan Saat Ini"**, lengkapi semua inputan berikut:

| No | Nama Input | Cara Mengisi |
|----|-----------|-------------|
| 1 | **ID Persimpangan** | Pilih nomor persimpangan dari dropdown |
| 2 | **Volume Kendaraan** | Masukkan jumlah kendaraan yang melintas (klik `+` / `-` atau ketik langsung) |
| 3 | **Jam Pengamatan** | Geser slider ke jam saat pengamatan dilakukan (0–23) |
| 4 | **Kecepatan Rata-Rata (km/h)** | Masukkan kecepatan rata-rata kendaraan (klik `+` / `-` atau ketik langsung) |
| 5 | **Waktu Tunda (Menit)** | Masukkan estimasi waktu tunda/delay kendaraan di persimpangan |

### Langkah 3 — Proses Prediksi
Klik tombol **"Proses Prediksi Kemacetan"** (tombol biru) setelah semua parameter terisi.

### Langkah 4 — Baca Hasil Prediksi
Sistem akan menampilkan **Status Situasi Lalu Lintas** beserta rekomendasi tindakan.

---

## 📥 Panduan Detail Setiap Inputan

### 🔹 ID Persimpangan
- **Apa itu?** Identitas unik dari titik persimpangan jalan yang ingin dipantau.
- **Cara isi:** Pilih dari daftar dropdown (contoh: 1, 2, 3, dst.)
- **Tips:** Pastikan memilih persimpangan yang sesuai dengan lokasi pengamatan Anda.

---

### 🔹 Volume Kendaraan
- **Apa itu?** Jumlah total kendaraan yang melintas di persimpangan dalam periode pengamatan.
- **Cara isi:** Klik tombol **`+`** untuk menambah atau **`−`** untuk mengurangi nilai, atau ketik langsung angkanya.
- **Contoh:** `150` berarti ada 150 kendaraan yang melintas.
- **Tips:** Semakin tinggi volume, semakin besar kemungkinan kemacetan.

---

### 🔹 Jam Pengamatan
- **Apa itu?** Waktu (jam) saat data lalu lintas dicatat, dalam format 24 jam.
- **Cara isi:** Geser **slider** ke kiri atau kanan sesuai jam saat ini (0 = tengah malam, 17 = pukul 17.00).
- **Contoh:** Posisi slider di angka `17` berarti pengamatan dilakukan pukul 17.00 (jam 5 sore).
- **Tips:** Jam sibuk biasanya pukul 07.00–09.00 (pagi) dan 16.00–19.00 (sore).

---

### 🔹 Kecepatan Rata-Rata (km/h)
- **Apa itu?** Rata-rata kecepatan kendaraan yang melintas di persimpangan tersebut.
- **Cara isi:** Klik **`+`** / **`−`** atau ketik nilai kecepatan dalam satuan km/jam.
- **Contoh:** `25,00` berarti kendaraan rata-rata melaju 25 km/jam.
- **Tips:** Kecepatan rendah (di bawah 30 km/h) biasanya mengindikasikan kondisi macet.

---

### 🔹 Waktu Tunda (Menit)
- **Apa itu?** Estimasi waktu tambahan yang dibutuhkan kendaraan akibat antrian atau kemacetan di persimpangan.
- **Cara isi:** Klik **`+`** / **`−`** atau ketik nilai dalam satuan menit.
- **Contoh:** `5,00` berarti kendaraan mengalami keterlambatan sekitar 5 menit.
- **Tips:** Waktu tunda yang tinggi menandakan antrian panjang di persimpangan.

---

## 📊 Memahami Hasil Prediksi

Setelah menekan tombol **"Proses Prediksi Kemacetan"**, sistem akan menampilkan kartu hasil berisi:

### Status Situasi Lalu Lintas

| Status | Level Kepadatan | Arti | Rekomendasi |
|--------|----------------|------|-------------|
| **LANCAR** | Level 0 | Arus kendaraan mengalir normal | Tidak ada tindakan khusus |
| **PADAT** | Level 1 | Terjadi kepadatan di jalur tersebut | Pertimbangkan rute alternatif |
| **MACET** | Level 2 | Kemacetan parah | Sangat disarankan hindari jalur ini |

> 💡 **Contoh hasil:** Status **PADAT (Level Kepadatan: 1)** disertai catatan *"Terjadi kepadatan lalu lintas di jalur tersebut. Sangat disarankan untuk memilih rute jalan alternatif."*

---

## ❓ Pertanyaan Umum (FAQ)

**Q: Apakah perlu akun untuk menggunakan aplikasi ini?**
A: Tidak. Aplikasi dapat langsung digunakan tanpa registrasi atau login.

**Q: Apakah data yang saya masukkan disimpan?**
A: Tidak. Setiap sesi bersifat mandiri dan data tidak disimpan secara permanen.

**Q: Seberapa akurat prediksinya?**
A: Sistem menggunakan model Machine Learning Klasifikasi yang dilatih dari data historis lalu lintas. Akurasi tergantung pada kelengkapan dan keakuratan data yang dimasukkan.

**Q: Apa yang terjadi jika saya tidak mengisi semua kolom?**
A: Kolom memiliki nilai default. Namun untuk hasil yang akurat, pastikan semua nilai diisi sesuai kondisi nyata di lapangan.

---

## 🛠️ Teknologi yang Digunakan

- **Streamlit** — Framework tampilan web interaktif
- **Machine Learning Klasifikasi** — Model prediksi tingkat kepadatan
- **Python** — Bahasa pemrograman utama

---

## 📞 Informasi Aplikasi

```
Sistem Monitoring Cerdas | Integrasi Model Machine Learning Klasifikasi
URL: https://trafficbase.streamlit.app
```
