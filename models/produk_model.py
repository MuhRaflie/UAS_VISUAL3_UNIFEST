class ProdukModel:
    def __init__(self, db):
        self.db = db

    def kurangi_stok(self, id_produk, qty):
        cursor = self.db.cursor()
        cursor.execute(
            "UPDATE produk SET stok = stok - %s WHERE id_produk=%s",
            (qty, id_produk)
        )
        self.db.commit()

    def tambah_stok(self, id_produk, qty):
        cursor = self.db.cursor()
        cursor.execute(
            "UPDATE produk SET stok = stok + %s WHERE id_produk=%s",
            (qty, id_produk)
        )
        self.db.commit()
