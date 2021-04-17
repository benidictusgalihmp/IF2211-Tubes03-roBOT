class Tugas():
    num = 0 # diincrement setiap membuat tugas baru
    list_tugas = []
    def __init__(self, tanggal, kode_matkul, jenis_tugas, topik_tugas):

        Tugas.num += 1
        self.id = int(Tugas.num)
        self.tanggal = Tugas.parse_tanggal(tanggal) # tipe: date
        self.kode_matkul = kode_matkul # string
        self.jenis_tugas = jenis_tugas # string, diambil dari kata penting
        self.topik_tugas = topik_tugas # string
        
        self.selesai = False

        Tugas.list_tugas.append(self)
    
    # NOT DONE
    def parse_tanggal(raw_string):

        return # date object

    # DONE
    def set_selesai(id_tugas):
        for i in range(len(Tugas.list_tugas)):
            if(Tugas.list_tugas[i].id == int(id_tugas)):
                Tugas.list_tugas[i].selesai = True
                break

    # DONE
    def update_tanggal(id_tugas, tanggal_baru):
        for i in range(len(Tugas.list_tugas)):
            if(Tugas.list_tugas[i].id == int(id_tugas)):
                Tugas.list_tugas[i].tanggal = Tugas.parse_tanggal(tanggal_baru)
                break
    
                
                

