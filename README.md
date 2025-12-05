<!-- # SolarSystemSimulationPython
This is my program to explain solar system in python -->

# 🌌 Simulasi Tata Surya Interaktif dengan Python

**Simulasi tata surya real-time** yang menampilkan pergerakan planet-planet sesuai hukum fisika Newton. Program ini memberikan pengalaman edukatif tentang dinamika tata surya dengan visualisasi yang menarik dan informasi detail tentang setiap planet.

## ✨ Fitur Utama

### 🪐 Simulasi Fisika Realistis
- **Pergerakan planet** berdasarkan gravitasi Newton
- **Kecepatan orbit** sesuai data astronomi nyata
- **Skala waktu** 1 detik = 1 hari dalam simulasi
- **Trajectory/jejak orbit** untuk setiap planet

### 🔍 Informasi Planet Detail
- **Data fisik**: massa, radius, kecepatan orbit
- **Posisi real-time**: koordinat dalam AU dan kilometer
- **Jarak dari matahari** yang terus diperbarui
- **Deskripsi unik** untuk setiap planet

### 🎮 Kontrol Interaktif
- **Zoom in/out** untuk melihat detail atau panorama
- **Pause/Resume** simulasi
- **Klik planet** untuk melihat informasi detail
- **Panel informasi** dengan UI yang intuitif

### 🌟 Visualisasi Menawan
- **Background bintang** dengan variasi ukuran
- **Warna planet** sesuai karakteristik asli
- **Orbit planet** dengan warna berbeda
- **Efek glow** untuk matahari
- **Grid referensi** untuk skala jarak

## 📸 Screenshot

![Screenshot Simulasi](screenshot.png)

## 🚀 Cara Menjalankan

### Prasyarat
1. **Python 3.9** atau lebih tinggi
2. **Pygame library**

### Instalasi
```bash
# Clone repository
git clone https://github.com/username/SolarSystemSimulation.git
cd SolarSystemSimulation

# Install pygame
pip install pygame

# Jalankan program
python solar_simulation.py
```

## 🎮 Kontrol Keyboard

| Tombol | Fungsi |
|--------|---------|
| **Klik kiri** | Pilih planet untuk info detail |
| **+ / =** | Zoom in |
| **-** | Zoom out |
| **P** | Pause/Resume simulasi |
| **R** | Reset pilihan planet |
| **ESC** | Keluar dari program |

## 📊 Planet yang Disimulasikan

| Planet | Radius | Warna | Keunikan |
|--------|--------|-------|----------|
| **Matahari** | 20px | Kuning | Bintang pusat tata surya |
| **Merkurius** | 5px | Abu-abu | Planet terkecil dan terdekat |
| **Venus** | 9px | Putih kemerahan | Planet terpanas |
| **Bumi** | 10px | Biru | Planet dengan kehidupan |
| **Mars** | 7px | Merah | Planet merah dengan gunung tertinggi |
| **Jupiter** | 22px | Oranye | Planet terbesar |
| **Saturnus** | 19px | Coklat | Planet dengan cincin spektakuler |
| **Uranus** | 15px | Cyan | Planet dengan rotasi miring |
| **Neptunus** | 15px | Ungu | Planet dengan angin terkuat |

## 🧮 Parameter Fisika

### Konstanta yang Digunakan
```python
AU = 149.6e6 * 1000  # 1 Astronomical Unit dalam meter
G = 6.67428e-11      # Konstanta gravitasi
SCALE = 60 / AU      # Skala visualisasi
TIMESTEP = 3600*24   # 1 detik simulasi = 1 hari
```

### Rumus Fisika yang Diimplementasikan
1. **Hukum Gravitasi Newton**: `F = G * m1 * m2 / r²`
2. **Percepatan**: `a = F / m`
3. **Kecepatan**: `v = v0 + a * t`
4. **Posisi**: `x = x0 + v * t`

## 🏗️ Struktur Kode

```
SolarSystemSimulation/
│
├── solar_simulation.py    # Program utama
├── README.md              # Dokumentasi ini
├── requirements.txt       # Dependensi
└── screenshot.png         # Screenshot program
```

### Kelas Utama: `Planet`
```python
class Planet:
    def __init__(self, x, y, radius, color, mass, name, description)
    def draw(self, win, selected_planet)
    def attraction(self, other)
    def update_position(self, planets)
```

### Fungsi Penting
- `draw_sidebar()`: Panel informasi interaktif
- `get_planet_at_pos()`: Deteksi klik pada planet
- `main()`: Loop utama program

## 📈 Fitur Teknis

### 1. **Optimasi Performa**
- Batasan jumlah titik orbit (400 titik per planet)
- Update posisi 60 FPS
- Background statis untuk efisiensi

### 2. **UI/UX Design**
- Panel sidebar dengan informasi terstruktur
- Warna kontras untuk keterbacaan
- Feedback visual saat interaksi
- Petunjuk penggunaan yang jelas

### 3. **Akurasi Sains**
- Data massa planet dari sumber astronomi
- Kecepatan orbit awal sesuai pengamatan
- Skala jarak yang proporsional

## 🎯 Tujuan Edukasional

Program ini cocok untuk:
- **Pembelajaran fisika** tentang gravitasi dan orbit
- **Pengenalan astronomi** dasar
- **Demo visual** hukum Newton
- **Proyek programming** dengan Pygame

## 🛠️ Teknologi yang Digunakan

- **Python 3.9+**: Bahasa pemrograman utama
- **Pygame 2.6.1**: Library untuk grafis dan input
- **Matematika**: Modul `math` untuk perhitungan fisika
- **Random**: Untuk efek bintang background

## 🤝 Kontribusi

Kontribusi sangat diterima! Untuk berkontribusi:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -am 'Menambahkan fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

### Area Pengembangan yang Diinginkan
- [ ] Menambahkan bulan untuk setiap planet
- [ ] Efek visual cincin Saturnus
- [ ] Mode kecepatan waktu yang berbeda
- [ ] Ekspor data orbit ke file
- [ ] Multi-language support

## 📝 Lisensi

Proyek ini dilisensikan di bawah **MIT License** - lihat file [LICENSE](LICENSE) untuk detail.

## 🙏 Penghargaan

- Data planet dari **NASA Planetary Fact Sheet**
- Inspirasi dari berbagai simulasi tata surya online
- Komunitas Pygame untuk dukungan dan resources

## 📞 Kontak

**Nama Anda** - [@username](https://github.com/username) - email@example.com

Link Proyek: [https://github.com/username/SolarSystemSimulation](https://github.com/username/SolarSystemSimulation)

---

<div align="center">
  
**⭐ Jika Anda menyukai proyek ini, jangan lupa beri bintang! ⭐**

Dibuat dengan ❤️ menggunakan Python dan Pygame

</div>

## 📚 Referensi

1. [NASA Solar System Exploration](https://solarsystem.nasa.gov/)
2. [Pygame Documentation](https://www.pygame.org/docs/)
3. [Orbital Mechanics for Engineering Students](https://www.sciencedirect.com/book/9780080977478/orbital-mechanics-for-engineering-students)

---

**Catatan**: Program ini dibuat untuk tujuan edukasi dan simulasi. Skala visual telah disesuaikan untuk tujuan presentasi dan mungkin tidak merepresentasikan skala sebenarnya dengan sempurna.