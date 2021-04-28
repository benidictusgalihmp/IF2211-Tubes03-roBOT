import json
class KataPenting():
    list_kata_penting = []
    # 

    list_kata_indikator = []
    # contoh akses: list_kata_indikator[0]["kw"][2] ; len(list_kata_indikator[0]["pre"][2]) == 0

    list_indikator_waktu = ["pada", "tanggal", "nanti"]

    list_deadline_keyword = ["deadline", "dl", "tenggat waktu"]

    list_time_keyword = ["minggu ke depan", "hari ke depan", "hari ini"]

    list_update_task_keyword = ["undur", "maju", "ubah", "ganti", "jadi"]

    list_task_done_keyword = ["selesai", "beres"]

    list_help_keyword = ["help", "bisa", "bantu"]




    # DONE
    FILEPATH = "./data/"
    # baca data dari file, tambahkan ke KataPenting.list_kata
    with open(FILEPATH+"kata_penting.txt", "r") as f:
        list_kata_penting = f.read().split('\n')
    with open(FILEPATH+"kata_indikator.json", "r") as f:
        data = f.read()
        list_kata_indikator = json.loads(data)
    