import json
class KataPenting():
    
    FILEPATH = "../data/"
    list_kata_penting = []
    # 

    list_kata_indikator = []
    # contoh akses: list_kata_indikator[0]["kw"][2] ; len(list_kata_indikator[0]["pre"][2]) == 0

    # DONE
    def init():
        # baca data dari file, tambahkan ke KataPenting.list_kata
        with open(KataPenting.FILEPATH+"kata_penting.txt", "r") as f:
            KataPenting.list_kata_penting = f.read().split('\n')
        with open(KataPenting.FILEPATH+"kata_indikator.txt", "r") as f:
            data = f.read()
            KataPenting.list_kata_indikator = json.loads(data)

    KataPenting.init()