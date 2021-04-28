import re
from component.KataPenting import KataPenting

months = ["jan", "feb", "mar", "apr", "mei", "jun", "jul", "agu", "sep", "okt", "nov", "des"]
months_fullname = ["januari", "februari", "maret", "april", "mei", "juni", "juli", "agustus", "september", "oktober", "november", "desember"]

def findall_date(raw_string):
    list_date = []
    reg = r"(\d{1,2})(\s*[a-zA-Z]{3,9}\s*|\s*/\s*\d{1,2}\s*/\s*)(\d{4}|\d{2})"
    for tr in re.findall(reg, raw_string):
        temp_date = []
        valid = True
        for component in tr:
            c = re.sub('\s', '', component)
            c = re.sub('/', '', c)
            if (len(c) >= 3):
                if c[:3].lower() in months:
                    if len(c)>3:
                        if c.lower() in months_fullname:
                            c = str(months_fullname.index(c.lower())+1)
                    else:
                        c = str(months.index(c[:3].lower())+1)
            elif (len(temp_date) == 2 and len(c) == 2):
                c = "20"+c
            try:
                c = int(c)
            except:
                valid = False
                # print("TANGGAL TIDAK VALID")
            temp_date.append(c)
        if valid:
            list_date.append(temp_date)
            # print(temp_date)
        # else:
        #     print(None)
    # untuk validasi kebenaran tanggal
    # for tggl in list_date:
    #     if (tggl[0]):
    #         # jan mar mei jul agt okt des = 31
    #         # apr jun sept nov = 30
    #         # feb = 29 every four years else feb = 28
    #         if (int(tggl[2]) % 4 == 0 and tggl[0] == 29 and tggl[1] == 2):
    #             valid = True
    #         elif(tggl[0] == 28 and tggl[1] == 2):
    #             valid = True
    #         elif(tggl[0] == 30 and tggl[1] == 4 or tggl[1] == 6 or tggl[1] == 9 or tggl[1] == 11):
    #             valid = True
    #         elif(tggl[0] == 31):
    #             valid = True
    #         else :
    #             valid = False
    # if (valid):
    #     return list_date
    # else:
    #     list_date.clear
    #     return list_date
    return list_date
    

def find_first_tugas_type(raw_string):
    list_kata = raw_string.lower().split(' ')
    list_kp = []
    prev_kata = ""
    for kata in list_kata:
        if kata in KataPenting.list_kata_penting:
            # print("in")
            if prev_kata == "tugas":
                # print("in")
                if kata == "kecil":
                    list_kp.append("Tucil")
                elif kata == "besar":
                    list_kp.append("Tubes")
                else:
                    list_kp.append("Tugas")
            if kata == "pr":
                list_kp.append("PR")
            elif kata != "kecil" and kata != "besar" and kata != "tugas":
                list_kp.append(kata.capitalize())
            
            prev_kata = kata
    if len(list_kp) == 0:
        return None
    return list_kp[0]

def find_first_matkul_code(raw_string):
    reg = r"[A-Z]{2}\d{4}"
    matkul = None
    for fm in re.findall(reg, raw_string.upper()):
        matkul = fm
        break
    return matkul
