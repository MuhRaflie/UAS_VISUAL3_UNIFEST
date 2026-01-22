class PenjualanModel:
    def __init__(self, db):
        self.db = db

    def insert_penjualan(self, tanggal, id_customer, total):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO penjualan (tanggal, id_customer, total) VALUES (%s, %s, %s)",
            (tanggal, id_customer, total)
        )
        self.db.commit()
        return cursor.lastrowid

    def insert_detail(self, id_penjualan, id_produk, qty, harga, subtotal):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO penjualan_detail 
            (id_penjualan, id_produk, qty, harga, subtotal)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (id_penjualan, id_produk, qty, harga, subtotal)
        )
        self.db.commit()
