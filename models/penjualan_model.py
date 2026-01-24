class PenjualanModel:
    def __init__(self, db):
        self.db = db

    def insert_penjualan(self, tanggal, id_customer, metode, total):
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO penjualan (tanggal, id_customer, metode_bayar, total)
            VALUES (%s, %s, %s, %s)
        """, (tanggal, id_customer, metode, total))
        self.db.commit()
        return cursor.lastrowid


    def insert_detail(self, id_penjualan, id_produk, jumlah, harga_jual, subtotal):
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO detail_penjualan
            (id_penjualan, id_produk, jumlah, harga_jual, subtotal)
            VALUES (%s, %s, %s, %s, %s)
        """, (id_penjualan, id_produk, jumlah, harga_jual, subtotal))
        self.db.commit()


