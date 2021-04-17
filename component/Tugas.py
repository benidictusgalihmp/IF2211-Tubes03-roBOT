class Tugas():
    num = 0 # diincrement setiap membuat tugas baru
    list_tugas = []
    def __init__(self, tanggal, kode_matkul, jenis_tugas, topik_tugas):
        
        is_valid = Tugas.validasi(tanggal, kode_matkul, jenis_tugas)
        
        if (is_valid):
            Tugas.num += 1
            self.id = int(Tugas.num)
            self.tanggal = tanggal # ubah ke tipe date
            self.kode_matkul = kode_matkul # string
            self.jenis_tugas = jenis_tugas # string, diambil dari kata penting
            self.topik_tugas = topik_tugas # string

            Tugas.list_tugas.append(self)

    
    def validasi(tanggal, kode_matkul, jenis_tugas):
        
        # cek tanggal. if not valid, return False       (re)
        # cek kode_matkul. if not valid, return False   (re)
        # cek jenis_tugas. if not valid, return False   (kata penting)

        # everything valid
        return True
