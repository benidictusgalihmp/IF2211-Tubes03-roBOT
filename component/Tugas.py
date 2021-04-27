import datetime
# import tinydb # json database
import component.KataPenting

class Tugas():
    num = 0 # diincrement setiap membuat tugas baru

    # list_tugas: berisi instance tugas-tugas yang belum selesai
    # 
    list_tugas = []
    def __init__(self, tanggal, kode_matkul, jenis_tugas, topik_tugas):

        Tugas.num += 1
        self.id = int(Tugas.num)
        self.date = Tugas.parse_tanggal(tanggal) # tipe: date
        self.code = kode_matkul # string
        self.type = jenis_tugas # string, diambil dari kata penting
        self.topic = topik_tugas # string
        
        self.is_done = False

        Tugas.list_tugas.append(self)
        Tugas.num += 1
    
    # Tugas.parse(raw_string): fungsi ini dipanggil oleh flask. -> String hasil yang siap ditampilkan ke Frontend
    def parse(raw_string):
        result = ""
        command_type = get_command_type(raw_string)

        if command_type == "add_task":
            result = add_task(raw_string)
        elif command_type == "show_task":
            result = show_undone_task(raw_string)
        elif command_type == "show_deadline":
            result = show_deadline(raw_string)
        elif command_type == "update_task":
            result = update_task(raw_string)
        elif command_type == "mark_as_done":
            result = mark_as_done(raw_string)
        elif command_type == "show_help":
            result = show_help()
        elif command_type == "show_recommendation":
            result = show_recommendation(raw_string)
        else:
            result = get_error_message()
        return result


    # ========================== #
    # string processing functions 
    # ========================== #

    # NAUFAL
    def add_task(raw_string):
        pass
    
    # DITO
    def show_undone_task(raw_string):
        pass

    # NAUFAL
    def show_deadline(raw_string):
        pass

    # DITO
    def update_task(raw_string):
        pass

    # NAUFAL
    def mark_as_done(raw_string):
        pass

    # DITO
    def show_help():
        sHelp = "[Fitur]\n"
        # for i in range(len()):
            
        sHelp += "[Daftar Kata Penting]\n"
        for i in range(len(component.KataPenting.KataPenting.list_kata_penting)):
            sHelp += (i + 1) + ". " + component.KataPenting.KataPenting.list_kata_penting[i] + "\n"
        
        return sHelp

    
    # DITO
    def show_recommendation(raw_string):
        pass
    
    # NAUFAL
    def get_command_type(raw_string):
        pass
    
    # NAUFAL
    def get_error_message():
        pass

    # =~ END SPF --- 





    # NOT DONE
    def parse_tanggal(raw_string):
        date_in_list = raw_string.split('/')

        

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
    