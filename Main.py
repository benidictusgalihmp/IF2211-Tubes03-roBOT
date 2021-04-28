from component.Tugas import *
from component.string_match import *

# Tugas('12', 'wqe', 'ewq', '213')
# Tugas('12', 'wqe', 'ewq', '215')

# for tugas in Tugas.list_tugas:
#     print(tugas.id, tugas.topik_tugas)
# print(KataPenting.list_kata_penting)
# for kata in KataPenting.list_kata_penting:
#     print(kata)
#     for karakter in kata:
#         print(karakter)
# print(datetime.date.today().day)
# print(KataPenting.list_kata_indikator[6])
# s1 = "32/15/2005 21 Apreel 2020 1 jan 21 5 apr 20 22/2/23"
# s2 = "Tubes tugas kEcIL praktikum IF2211  String Matching    pada 22/04/21"
# sx1 = "Deadline tasK 159 diundur menjadi 28/04/2021"
# sx2 = "Deadline tugas 1 diundur menjadi 28/04/2021"
# sx3 = "Deadline tugas 3 diundur menjadi 28/04/2021"
# raw = "antara x sampai y tugas tucil"
# # Tugas.get_command_type(s1)
# print(Tugas.show_help())
# print(boyer_moore(sx1, "undur"))
# print(sx1[16])
# print(Tugas.update_task(sx2))
# print(Tugas.update_task(sx3))
# for kata in KataPenting.list_kata_penting:
#     ada = re.search(kata, raw)
#     if (ada):
#         print(kata)
# data1 = ["1", [5,12,2440], "IF2210", "Tubes", "String matching"]
# data2 = ["2", [20,11,2300], "MA2230", "Tugas", "String matching"]
# data3 = ["3", [28,4,2021], "IF2230", "Praktikum", "String matching"]
# db = [data1, data2,data3]
# duar = []
# for row in db:
#     print(row)
#     duar.append(row)
#     print("\tduar: ", duar)
# print("duar\n")
# for row in duar:
#     print(row[0])
st1 = "Apa saja deadline yang dimiliki sejauh ini?"
st2 = "Apa saja deadline antara 03/04/2021 sampai 15/04/2021?"
st3 = "Deadline sekarang ada apa saja?"
st4 = "Deadline bulan ini ada apa saja?"
st5 = "Deadline 3 hari ke depan ada apa saja?"
st6 = "Deadline 3 minggu ke depan ada apa saja?"
st7 = "Deadline 3 bulan ke depan ada apa saja?"
print("selain itu\n")
print(Tugas.show_undone_task(st1))
print("\nantara\n")
print(Tugas.show_undone_task(st2))
print("\nsekarang\n")
print(Tugas.show_undone_task(st3))
print("\nbulan ini\n")
print(Tugas.show_undone_task(st4))
print("\n n hari ke depan\n")
print(Tugas.show_undone_task(st5))
print("\n n minggu ke depan\n")
print(Tugas.show_undone_task(st6))
print("\n n bulan ke depan\n")
print(Tugas.show_undone_task(st7))

# print(Tugas.list_tugas)