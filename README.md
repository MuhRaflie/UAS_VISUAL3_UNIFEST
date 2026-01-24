# UAS_VISUAL3_UNIFEST
Tugas UAS Visual 3 - 2310010432_Muhammad Raflie Ramadhan

UNIFEST adalah aplikasi desktop berbasis Python (PyQt5) yang digunakan untuk mengelola data produk, supplier, customer, pembelian, dan penjualan pada sebuah event atau usaha.
Aplikasi ini dirancang menggunakan konsep CRUD (Create, Read, Update, Delete) dan transaksi header–detail, serta terhubung dengan database MySQL/MariaDB.
Aplikasi ini dibuat sebagai tugas UAS Visual 3.

Fitur Utama:
1. Dashboard
- Menampilkan ringkasan: Total transaksi penjualan, Total produk, Total stok, Total pendapatan.
2. Manajemen Produk
- Tambah, ubah, hapus, dan lihat data produk
- Relasi dengan supplier
- Pengelolaan stok otomatis
3. Manajemen Supplier
- CRUD data supplier
4. Manajemen Customer
- CRUD data customer
5. Transaksi Penjualan
- Sistem keranjang (header & detail)
- Harga & subtotal otomatis
- Stok berkurang otomatis saat transaksi
- Metode pembayaran (Cash, Transfer, QRIS)
6. Transaksi Pembelian
- Sistem keranjang pembelian
- Harga & subtotal otomatis
- Stok bertambah otomatis
- Update harga beli produk

Cara Penggunaan Aplikasi:
1. Dashboard
- Menampilkan ringkasan data secara otomatis dari database
2. Produk / Supplier / Customer
- Klik menu → isi form → klik Simpan
- Klik data di tabel untuk Edit / Hapus
3.  Penjualan
- Pilih customer
- Pilih produk & jumlah
- Klik Tambah Item
- Klik Simpan Transaksi
4. Pembelian
- Pilih supplier
- Pilih produk & jumlah
- Klik Tambah Item
- Klik Simpan Pembelian
