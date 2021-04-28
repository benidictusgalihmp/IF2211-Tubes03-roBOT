import json
class KataPenting():
    list_kata_penting = []
    # 

    list_kata_indikator = []
    # contoh akses: list_kata_indikator[0]["kw"][2] ; len(list_kata_indikator[0]["pre"][2]) == 0






    # DONE
    FILEPATH = "./data/"
    # baca data dari file, tambahkan ke KataPenting.list_kata
    with open(FILEPATH+"kata_penting.txt", "r") as f:
        list_kata_penting = f.read().split('\n')
    with open(FILEPATH+"kata_indikator.json", "r") as f:
        data = f.read()
        list_kata_indikator = json.loads(data)
    