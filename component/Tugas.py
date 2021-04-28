import datetime
from os import truncate
# import tinydb # json database
import re
from component.KataPenting import KataPenting
from component.helper import *


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
        pass
    
    # DITO
    # "Apa saja deadline yang dimiliki sejauh ini?"
    # 
    def show_undone_task(raw_string):
        # local time right now
        # time_now = datetime.date.today()
        # if (len(Tugas.list_tugas > 0)):
            
        # else:
        #     stask = "Tidak ada tugas yang menantimu Yeay !"
        return stask

    # NAUFAL
    def show_deadline(raw_string):
        pass

    # DITO
    def update_task(raw_string):
        # kamus lokal
        ada = False
        # Contoh raw_string "Deadline task X diundur menjadi 28/04/2021"
        # id, tanggal, kode matkul, jenis tugas, topik
        # yang dapat diubah --> tanggal
        # database temporary
        data1 = [1, datetime.date(2020, 5, 7), "IF2210", "Tubes", "String matching"]
        data2 = [2, datetime.date(2020, 11, 20), "MA2230", "Tugas", "String matching"]
        data3 = [3, datetime.date(2020, 8, 13), "IF2230", "Praktikum", "String matching"]
        db = [data1, data2,data3]

        # tanggal 
        # deadline / dl /tenggat waktu
        # ganti ubah undur baru baharu
        # tugas besar kecil tubes tucil praktikum kuis ujian uts uas
 
        # unfixed butuh pencarian KataPenting.list_kata_penting[0] 
        # dengan indeks yang paling dekat dengan deadline / dl / tenggat waktu
        re_task = r""+KataPenting.list_kata_penting[0]+"\s\d+"
        re_id = r"\d"

        # unfixed butuh tanggal perubahan setelah kata menjadi / tanggal
        tggl = datetime.date(2030, 5, 12)
        task_num = re.findall(re_task, raw_string.lower())
        id = re.findall(re_id, task_num[0])
        time_now = datetime.date.today()

        # jika tanggal deadline baru sebelum tanggal saat ini
        if (tggl < time_now):
            response = "Maaf, tanggal Deadline telah dilalui"
        else:
            # memeriksa keberadaan id task di dalam database
            for row in db:
                if (str(row[0]) == id[0]):
                    ada = True

            # jika terdapat id task dalam database
            if (ada):
                db[int(id[0]) - 1][1] = tggl
                response = "Berhasil memperbarui deadline task " + str(id[0]) + "!"
            else:
                response = "Maaf, ID task " + str(id[0]) + " tidak dikenali."

        return response

    # NAUFAL
    def mark_as_done(raw_string):
        pass

    # DITO
    def show_help():
        # harus melihat cara kerja dari get command type
        response = "[Fitur]\n"
        
        # add_task
        response += "1. daftar kata2 untuk add_task\n"
        # show_task
        response += "2. daftar kata2 untuk show_task\n"
        # show_deadline
        response += "3. daftar kata2 untuk show_deadline\n"
        # update_task
        response += "4. daftar kata2 untuk update_task\n"
        # mark_as_done
        response += "5. daftar kata2 untuk mark_as_done\n"
        # show_help
        response += "6. daftar kata2 untuk show_help\n"
        # show_recommendation
        response += "7. daftar kata2 untuk show_recommendation\n"

        response += "\n[Daftar Kata Penting]\n"
        for i in range(len(KataPenting.list_kata_penting)):
            response += str(i + 1) + ". " + KataPenting.list_kata_penting[i] + "\n"
        
        response += "\n[Daftar Kata Indikator]\n"
        for i in range(len(KataPenting.list_kata_indikator)):

            # print keyword or kw
            for j in range(len(KataPenting.list_kata_indikator[i]["kw"])):
                # last index handling
                if(j == 0):
                    response += str(i + 1) + ". "
                if (j == len(KataPenting.list_kata_indikator[i]["kw"]) - 1):
                    response += KataPenting.list_kata_indikator[i]["kw"][j] + "\n"
                else:
                    response += KataPenting.list_kata_indikator[i]["kw"][j] + " / "
            
            # print pre keyword
            if (len(KataPenting.list_kata_indikator[i]["pre"]) > 0):
                response += "[pre keyword]: "
                for j in range(len(KataPenting.list_kata_indikator[i]["pre"])):
                    if (j == len(KataPenting.list_kata_indikator[i]["pre"]) - 1):
                        response += KataPenting.list_kata_indikator[i]["pre"][j] + "\n"
                    else:
                        response += KataPenting.list_kata_indikator[i]["pre"][j] + " / "
            
            # print post keyword
            if(len(KataPenting.list_kata_indikator[i]["pos"]) > 0):
                response += "[pos keyword]: "
                for j in range(len(KataPenting.list_kata_indikator[i]["pos"])):
                    if (j == len(KataPenting.list_kata_indikator[i]["pos"]) - 1):
                        response += KataPenting.list_kata_indikator[i]["pos"][j] + "\n"
                    else:
                        response += KataPenting.list_kata_indikator[i]["pos"][j] + " / "
        return response
    
    # DITO
    def show_recommendation(raw_string):
        pass
    
    # NAUFAL
    def get_command_type(raw_string):
        command_type = ""
        list_date = findall_date(raw_string)
        task_type = find_first_tugas_type(raw_string)
        matkul_code = find_first_matkul_code(raw_string)
        print(task_type, matkul_code, "pada", list_date[0])


        return command_type
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
    