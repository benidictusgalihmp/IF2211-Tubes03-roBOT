import re
from component.KataPenting import KataPenting
from component.string_match import *


raw_string = "Tubes tugas kEcIL praktikum iF2211 if2210 String Matching    pada 22/04/21"
s = "foobar"
print(get_prefixes(s))
print(get_suffixes(s[1:]))
# # ========= get index =========== #
# keyword = "praktikum"
# key = keyword.lower()
# rs = raw_string.lower() 
# print(re.match(key,rs).span())




# ========= find matkul code =========== #
# reg = r"[A-Z]{2}\d{4}"
# matkul = None
# for fm in re.findall(reg, raw_string.upper()):
#     matkul = fm
#     break
# print(matkul)


# ========= find task type =========== #
# raw_string = re.sub(r'\s', r'\s', raw_string)
# list_kata = raw_string.lower().split(' ')
# print(list_kata)
# list_kp = []
# prev_kata = ""
# for kata in list_kata:
#     if kata in KataPenting.list_kata_penting:
#         # print("in")
#         if prev_kata == "tugas":
#             print("in")
#             if kata == "kecil":
#                 list_kp.append("Tucil")
#             elif kata == "besar":
#                 list_kp.append("Tubes")
#             else:
#                 list_kp.append("Tugas")
#         if kata == "pr":
#             list_kp.append("PR")
#         elif kata != "kecil" and kata != "besar" and kata != "tugas":
#             list_kp.append(kata.capitalize())
        
#         prev_kata = kata
# print(list_kp)


# string = "IF2240 tubes basis data 22/04/2021"
# regex = "(\w{2}\d{4})|(tubes)|(tucil)|(\d{2}/\d{2}/\d{2})"

# print(re.findall(regex, string))

# txt = "The rain in Spain"
# x = re.findall("^The.*Spain$", txt) 
# print(x)
# from component.KataPenting import KataPenting as kp
# print(kp.list_kata_indikator)
# print(kp.list_kata_penting)

# months = ["jan", "feb", "mar", "apr", "mei", "jun", "jul", "agu", "sep", "okt", "nov", "des"]
# months_fullname = ["januari", "februari", "maret", "april", "mei", "juni", "juli", "agustus", "september", "oktober", "november", "desember"]

# s1  = "21 April 2020 1 jan 21 5 apr 20 22/2/23"
# reg = r"(\d{1,2})(\s*[a-zA-Z]{3,9}\s*|\s*/\s*\d{1,2}\s*/\s*)(\d{4}|\d{2})"
# for tr in re.findall(reg, s1):
#     temp_date = []
#     valid = True
#     for component in tr:
#         c = re.sub('\s', '', component)
#         c = re.sub('/', '', c)
#         if (len(c) >= 3):
#             if c[:3].lower() in months:
#                 c = str(months.index(c[:3].lower())+1)
#         elif (len(temp_date) == 2 and len(c) == 2):
#             c = "20"+c
#         try:
#             c = int(c)
#         except:
#             valid = False
#             # print("TANGGAL TIDAK VALID")
#         temp_date.append(c)
#     if valid:
#         print(temp_date)
#     else:
#         print(None)



