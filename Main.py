from component.Tugas import *
from component.string_match import *

# Tugas('12', 'wqe', 'ewq', '213')
# Tugas('12', 'wqe', 'ewq', '215')

# for tugas in Tugas.list_tugas:
#     print(tugas.id, tugas.topik_tugas)
# print(KataPenting.list_kata_penting)
for kata in KataPenting.list_kata_penting:
    print(kata)
    for karakter in kata:
        print(karakter)
print(datetime.date.today())
print(KataPenting.list_kata_indikator[6])
# s1 = "32/15/2005 21 Apreel 2020 1 jan 21 5 apr 20 22/2/23"
# s2 = "Tubes tugas kEcIL praktikum IF2211  String Matching    pada 22/04/21"
# sx1 = "Deadline tasK 159 diundur menjadi 28/04/2021"
# sx2 = "Deadline tugas 1 diundur menjadi 28/04/2021"
# sx3 = "Deadline tugas 3 diundur menjadi 28/04/2021"
# # Tugas.get_command_type(s1)
# print(Tugas.show_help())
# print(boyer_moore(sx1, "undur"))
# print(sx1[16])
# print(Tugas.update_task(sx2))
# print(Tugas.update_task(sx3))