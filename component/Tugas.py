import datetime
import tinydb # json database
import re
from component.KataPenting import KataPenting
from component.helper import *


class Tugas():
    num = 11110 # diincrement setiap membuat tugas baru

    # list_tugas: berisi instance tugas-tugas yang belum selesai
    # 
    list_tugas = []
    def __init__(self, tanggal, kode_matkul, jenis_tugas, topik_tugas):
        Tugas.num += 1
        self.id = int(Tugas.num)
        self.date = Tugas.parse_tanggal(tanggal) # tipe: date
        self.code = str(kode_matkul).upper() # string
        self.type = jenis_tugas # string, diambil dari kata penting
        self.topic = topik_tugas # string
        
        self.is_done = False

        Tugas.list_tugas.append(self)
        Tugas.num += 1
    
    # Tugas.parse(raw_string): fungsi ini dipanggil oleh flask. -> String hasil yang siap ditampilkan ke Frontend
    def parse(raw_string):
        result = ""
        command_type = Tugas.get_command_type(raw_string)

        if command_type == "add_task":
            result = Tugas.add_task(raw_string)
        elif command_type == "show_task":
            result = Tugas.show_undone_task(raw_string)
        elif command_type == "show_deadline":
            result = Tugas.show_deadline(raw_string)
        elif command_type == "update_task":
            result = Tugas.update_task(raw_string)
        elif command_type == "mark_as_done":
            result = Tugas.mark_as_done(raw_string)
        elif command_type == "show_help":
            result = Tugas.show_help()
        elif command_type == "show_recommendation":
            result = Tugas.show_recommendation(raw_string)
        else:
            result = Tugas.get_error_message()
        return result


    # ========================== #
    # string processing functions 
    # ========================== #

    # NAUFAL
    def add_task(raw_string):
        # REQs
        # |- 1 tanggal (first)
        # |- 1 kode matkul (first)
        # |- 1 jenis tugas
        # |- 1 topik tugas 

        list_date = findall_date(raw_string)
        date = list_date[0]
        task_type = find_first_tugas_type(raw_string).lower()
        matkul_code = find_first_matkul_code(raw_string)
        nama_tugas = find_nama_tugas(raw_string)
        t = Tugas(date, matkul_code, task_type, nama_tugas)

        response = "[TASK BERHASIL DICATAT]\n(ID: %d) %d/%d/%d - %s - %s - %s"%(t.id, t.date.day, t.date.month, t.date.year, t.code, t.type, t.topic)

        return response
    
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
        pass
    
    # DITO
    def show_recommendation(raw_string):
        pass
    
    # NAUFAL
    def get_command_type(raw_string):
        command_type = ""

        # add_task
        list_date = findall_date(raw_string)
        task_type = find_first_tugas_type(raw_string).lower()
        matkul_code = find_first_matkul_code(raw_string)
        nama_tugas = find_nama_tugas(raw_string)

        # show_task
        #show_deadline
        deadline_keyword_exist = is_dl_keyword_exist(raw_string)
        periode_waktu_exist = is_waktu_exist(raw_string)
        if len(list_date) > 1:
            periode_waktu_exist= True
        
        # update task
        id_exist = Tugas.is_id_exist(raw_string)
        keyword_update = find_keyword_update_task(raw_string)
        
        # mark_as_done
        task_done = is_task_done_exist(raw_string)

        # show_help
        help_keyword_exist = is_help_keyword_exist(raw_string)

        print(id_exist, keyword_update)
        # print(task_type, matkul_code, nama_tugas, "pada", list_date[0])
        if help_keyword_exist and not (task_done or id_exist or periode_waktu_exist or deadline_keyword_exist):
            command_type = "show_help"
        elif id_exist and task_done:
            command_type = "mark_as_done"
        elif id_exist and len(keyword_update) > 0:
            command_type = "update_task"
        elif len(list_date) > 0 and len(matkul_code) > 0 and len(task_type) > 0 and len(nama_tugas) > 0 and not deadline_keyword_exist:
            command_type = "add_task"
        elif deadline_keyword_exist and len(task_type) > 0 and (task_type == "tugas" or task_type == "tubes" or task_type == "tucil"):
            command_type = "show_deadline"
        elif deadline_keyword_exist or periode_waktu_exist or len(task_type) > 0:
            command_type = "show_task"
        
        return command_type
        
    # NAUFAL
    def get_error_message():
        pass

    # =~ END SPF --- 


    def is_id_exist(raw_string):
        exist = False
        reg = r"\d{5,}"
        l = re.findall(reg, raw_string)
        if len(l)>0:
            id = int(l[0])
            for tugas in Tugas.list_tugas:
                if (int(tugas.id) == int(id)):
                    exist = True
                    break
        return exist


    # DONE
    def parse_tanggal(tanggal):
        return datetime.date(tanggal[2], tanggal[1], tanggal[0])

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
    
                
                

