class KataPenting():
    
    FILEPATH = "../data/kata_penting.txt"
    list_kata = []

    # DONE
    def init():
        # baca data dari file, tambahkan ke KataPenting.list_kata
        with open(KataPenting.FILEPATH, "r") as f:
            KataPenting.list_kata = f.read().split('\n')
