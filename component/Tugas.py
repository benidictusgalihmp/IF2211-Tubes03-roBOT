import datetime
from datetime import timedelta
from datetime import date

# import tinydb # json database
import re
from component.KataPenting import KataPenting
from component.helper import *

import pickle

DBFILE = "./db.pkl"


class Tugas():
    def first_init():
        with open(DBFILE, "wb") as db:
            pickle.dump([], db)


    num = 11110 # diincrement setiap membuat tugas baru

    # list_tugas: berisi instance tugas-tugas yang belum selesai
    # 
    list_tugas = [["1", [1,5,2021], "IF2210", "Tubes", "String matching"]]
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
        with open(DBFILE, "rb") as db:
            var = db.read()
            Tugas.list_tugas = pickle.loads(var)

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

        with open(DBFILE, "wb") as db:
            pickle.dump(Tugas.list_tugas, db)
        
        return result


    # ========================== #
    # string processing functions 
    # ========================== #

    # NAUFAL DONE
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
    # "Apa saja deadline yang dimiliki sejauh ini?"
    # 
    def show_undone_task(raw_string):
        # local time right now
        time_now = date.today()
        stask = []
        id = 1

        # database temporary
        data1 = ["1", [1,5,2021], "IF2210", "Tubes", "String matching"]
        data2 = ["2", [19,5,2021], "MA2230", "Tugas", "String matching"]
        data3 = ["3", [28,4,2021], "IF2230", "Praktikum", "String matching"]
        data4 = ["4", [12,7,2021], "MA9090", "Tucil", "String matching"]
        data5 = ["5", [28,7,2021], "MA2121", "Ujian", "String matching"]
        db = [data1, data2,data3]

        if (re.search("antara", raw_string) and (re.search("hingga", raw_string) or re.search("sampai", raw_string) or re.search("dan", raw_string))):
            print("antara")
            l_tgl = findall_date(raw_string)
            c_first_tgl = datetime.date(l_tgl[0][2], l_tgl[0][1], l_tgl[0][0])
            c_second_tgl = datetime.date(l_tgl[1][2], l_tgl[1][1], l_tgl[1][0])
            
            for row in db:
                t_date = datetime.date(row[1][2], row[1][1], row[1][0])
                if (t_date >= c_first_tgl and t_date <= c_second_tgl):
                    stask.append(row)
                # if ((row[1][0] >= l_tgl[0][0] and row[1][0] <= l_tgl[1][0]) or row[1][1] >= l_tgl[0][1] or row[1][2] >= l_tgl[0][2]) and (row[1][0] <= l_tgl[1][0] or row[1][1] <= l_tgl[1][1] or row[1][2] <= l_tgl[1][2])):
                #     stask.append(row)
        elif (re.search("sekarang", raw_string) or re.search("saat ini", raw_string) or re.search("hari ini", raw_string)):
            print("sekarang")
            for row in db:
                if (row[1][0] == time_now.day and row[1][1] == time_now.month and row[1][2] == time_now.year):
                    stask.append(row)
        elif (re.search("bulan ini", raw_string)):
            print("bulan ini")
            for row in db:
                if (row[1][1] == time_now.month and row[1][2] == time_now.year):
                    stask.append(row)
        elif (re.search("\d+\s\shari ke depan", raw_string)):
            print("n hari")
            s_hari = re.findall("\d+\s\shari ke depan", raw_string)
            print(s_hari[0])
            num_hari = re.findall("\d+", s_hari[0])
            print(num_hari[0])
            
            time_n_days = time_now + timedelta(days=int(num_hari[0]))
            
            for row in db:
                t_date = datetime.date(row[1][2], row[1][1], row[1][0])
                
                if (t_date <= time_n_days):
                    stask.append(row)
                # if (time_n_days.day >= row[1][0] or time_n_days.month >= row[1][1] or time_n_days.year >= row[1][2]):
                #     stask.append(row)
        elif (re.search("\d+\s\sminggu ke depan", raw_string)):
            print("n minggu")
            s_minggu = re.findall("\d+\s\sminggu ke depan", raw_string)
            print(s_minggu[0])
            num_minggu = re.findall("\d+", s_minggu[0])
            print(num_minggu[0])

            time_n_weeks = time_now + timedelta(months=int(num_minggu[0]))
            for row in db:
                t_date = datetime.date(row[1][2], row[1][1], row[1][0])

                if (t_date <= time_n_weeks):
                    stask.append(row)
                # if (time_n_weeks.day >= row[1][0] or time_n_weeks.month >= row[1][1] or time_n_weeks.year >= row[1][2]):
                #     stask.append(row)
        elif (re.search("\d+\s\sbulan ke depan", raw_string)):
            s_bulan = re.findall("\d+\s\sbulan ke depan", raw_string)
            print(s_bulan[0])
            num_bulan = re.findall("\d+", s_bulan[0])
            print(num_bulan[0])

            time_n_months = time_now + timedelta(months=int(num_bulan[0]))
            for row in db:
                t_date = datetime.date(row[1][2], row[1][1], row[1][0])

                if (t_date <= time_n_months):
                    stask.append(row)
                # if (time_n_months.day >= row[1][0] or time_n_months.month >= row[1][1] or time_n_months.year >= row[1][2]):
                #     stask.append(row)
        else:
            for row in db:
                stask.append(row)

        # mengambil konstrain berdasarkan jenis tugas jika ada
        for kata in KataPenting.list_kata_penting:
            type_constrain = re.search(kata, raw_string.lower())
            if (type_constrain):
                kp = kata.lower()
                break

        # mengambil data tugas berdasarkan jenis tugas
        if (type_constrain):
            temp = stask
            stask.clear
            for row in temp:
                if (row[3].lower() == kp):
                    stask.append(row)

        # mencetak ke layar
        if (len(stask) > 0):
            response = "[Daftar Deadline]\n"
            for row in stask:
                response += "   " + str(id) + ".\t(ID: " + str(row[0]) + ") " + str(row[1][0]) + "/" + str(row[1][1]) + "/" + str(row[1][2]) + " - " + row[2] + " - " + row[3] + " - " + row[4] + "\n"
                id += 1
        else:
            response = "Tidak ada tugas yang menantimu Yeay !"
        
        return response

    # NAUFAL
    def show_deadline(raw_string):
        matkul_code = find_first_matkul_code(raw_string).upper()
        response = ""
        for tugas in Tugas.list_tugas:
            print(tugas)
            if (tugas.code).upper() == matkul_code:
                response += str(tugas.date.day) +"/"+ str(tugas.date.month) +"/"+ str(tugas.date.year) + "\n"
        if response == "":
            response = "[TIDAK ADA TUGAS UNTUK MATA KULIAH %s]"%(matkul_code)
        else:
            response = response[:-1]
        return response

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
        all_id = Tugas.findall_id(raw_string)
        sukses = False
        success_id = []
        for tugas in Tugas.list_tugas:
            for i in all_id:
                if int(tugas.id) == int(i) and tugas.is_done == False:
                    sukses = True
                    tugas.is_done = True
                    success_id.append(str(tugas.id))
        response = ""
        if sukses:
            for si in success_id:
                response += "Tugas (ID: %s) telah diselesaikan\n"%(str(si))
            response = response[:-1]
        else:
            response = "[TIDAK ADA TUGAS DENGAN ID YANG DIMAKSUD]"
        return response


    # DITO
    def show_help():
        # harus melihat cara kerja dari get command type
        response = "[Fitur]\n"
        
        # add_task
        response += "1.\tdaftar kata2 untuk add_task\n"
        # show_task
        response += "2.\tdaftar kata2 untuk show_task\n"
        # show_deadline
        response += "3.\tdaftar kata2 untuk show_deadline\n"
        # update_task
        response += "4.\tdaftar kata2 untuk update_task\n"
        # mark_as_done
        response += "5.\tdaftar kata2 untuk mark_as_done\n"
        # show_help
        response += "6.\tdaftar kata2 untuk show_help\n"
        # show_recommendation
        response += "7.\tdaftar kata2 untuk show_recommendation\n"

        response += "\n[Daftar Kata Penting]\n"
        for i in range(len(KataPenting.list_kata_penting)):
            response += str(i + 1) + ".\t" + KataPenting.list_kata_penting[i] + "\n"
        
        response += "\n[Daftar Kata Indikator]\n"
        for i in range(len(KataPenting.list_kata_indikator)):

            # print keyword or kw
            for j in range(len(KataPenting.list_kata_indikator[i]["kw"])):
                # last index handling
                if(j == 0):
                    response += str(i + 1) + ".\t"
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
        id_valid = Tugas.is_id_valid(raw_string)
        keyword_update = find_keyword_update_task(raw_string)
        
        # mark_as_done
        task_done = is_task_done_exist(raw_string)

        # show_help
        help_keyword_exist = is_help_keyword_exist(raw_string)

        # print(id_exist, task)
        # print(task_type, matkul_code, nama_tugas, "pada", list_date[0])
        if help_keyword_exist and not (task_done or id_exist or periode_waktu_exist or deadline_keyword_exist):
            command_type = "show_help"
        elif id_valid and task_done:
            command_type = "mark_as_done"
        elif id_exist and len(keyword_update) > 0:
            command_type = "update_task"
        elif len(list_date) > 0 and len(matkul_code) > 0 and len(task_type) > 0 and len(nama_tugas) > 0 and not deadline_keyword_exist:
            command_type = "add_task"
        elif deadline_keyword_exist and len(matkul_code) > 0 and (task_type == "tugas" or task_type == "tubes" or task_type == "tucil"):
            command_type = "show_deadline"
        elif deadline_keyword_exist or periode_waktu_exist or len(task_type) > 0:
            command_type = "show_task"
        
        return command_type
        
    # NAUFAL
    def get_error_message():
        return "Maaf, pesan tidak dikenali"

    # =~ END SPF --- 

    def findall_id(raw_string):
        reg = r"\d{5,}"
        all_id = re.findall(reg, raw_string)
        for i in range(len(all_id)):
            all_id[i] = int(all_id[i])
        return all_id

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

    def is_id_valid(raw_string):
        valid = False
        reg = r"\d{5,}"
        l = re.findall(reg, raw_string)
        if len(l) > 0:
            valid = True
        return valid


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
    