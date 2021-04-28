import re
from component.KataPenting import KataPenting
from component.string_match import kmp, boyer_moore

months = ["jan", "feb", "mar", "apr", "mei", "jun", "jul", "agu", "sep", "okt", "nov", "des"]
months_fullname = ["januari", "februari", "maret", "april", "mei", "juni", "juli", "agustus", "september", "oktober", "november", "desember"]

def clean_and_mark(raw_string):
    c = str(raw_string.lower())
    for i_waktu in KataPenting.list_indikator_waktu:
        c = c.replace(i_waktu, "|"*len(i_waktu))
        
    c.strip()
    c = " ".join(c.split())
    return c.capitalize()


def find_date_index_of(date, raw_string):
    date = date[1:-1].split(', ')
    for i in range(len(date)):
        date[i] = int(date[i])
    
    list_date = []

    raw_string = clean_and_mark(raw_string)
    reg1 = r"(\d{1,2})(\s*/\s*\d{1,2}\s*/\s*)(\d{4}|\d{2})"
    reg2 = r"(\d{1,2})(\s*[a-zA-Z]{3,9}\s*)(\d{4}|\d{2})"
    for tr in (re.findall(reg1, raw_string) + re.findall(reg2, raw_string)):
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
            temp_date.append(c)
        if valid and temp_date == date:
            list_date.append(tr)
    
    fd = list_date[0][0]+list_date[0][1]+list_date[0][2]
    i = re.search(fd, raw_string).span()
    return i[0]

def findall_date(raw_string):
    list_date = []
    raw_string = clean_and_mark(raw_string)
    reg1 = r"(\d{1,2})(\s*/\s*\d{1,2}\s*/\s*)(\d{4}|\d{2})"
    reg2 = r"(\d{1,2})(\s*[a-zA-Z]{3,9}\s*)(\d{4}|\d{2})"
    for tr in (re.findall(reg1, raw_string) + re.findall(reg2, raw_string)):
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
        #     print("")
    return list_date

def findall_tugas_type(raw_string):
    list_kata = raw_string.lower().split(' ')
    list_kp = []
    prev_kata = ""
    for kata in list_kata:
        if kata in KataPenting.list_kata_penting:
            if prev_kata == "tugas":
                if kata == "kecil":
                    list_kp.append("Tucil")
                elif kata == "besar":
                    list_kp.append("Tubes")
            if kata == "pr":
                list_kp.append("PR")
            elif kata != "kecil" and kata != "besar" and kata != "tugas":
                list_kp.append(kata.capitalize())
            
            prev_kata = kata
        elif prev_kata == "tugas":
            list_kp.append("Tugas")
            prev_kata = ""
    return list_kp

def find_first_tugas_type(raw_string):
    list_kp = findall_tugas_type(raw_string)
    if len(list_kp) == 0:
        return ""
    return list_kp[0]

def findall_matkul_code(raw_string):
    reg = r"[A-Z]{2}\d{4}"
    list_matkul = []
    for fm in re.findall(reg, raw_string.upper()):
        list_matkul.append(fm)
    return list_matkul

def find_first_matkul_code(raw_string):
    list_matkul = findall_matkul_code(raw_string)
    if len(list_matkul) == 0:
        return ""
    return list_matkul[0]

def clean_nama_tugas(raw_nama_tugas):
    c = str(raw_nama_tugas.lower())
    for i_waktu in KataPenting.list_indikator_waktu:
        c = c.replace(i_waktu, "")
        
    c.strip()
    c = " ".join(c.split())
    return c.capitalize()


def find_nama_tugas(raw_string):
    rs = raw_string.lower()
    list_matkul_code = findall_matkul_code(raw_string)
    list_tugas_type = findall_tugas_type(raw_string)
    list_all_date = findall_date(raw_string)

    nama_tugas = ""

    if len(list_all_date) > 0 and len(list_matkul_code) > 0 and len(list_tugas_type) > 0:
        fd = str(list_all_date[0])
        lmc = list_matkul_code[-1]
        ltt = list_tugas_type[-1]
        imc = kmp(rs, lmc.lower())+len(lmc)
        itt = boyer_moore(rs, ltt.lower())+len(ltt)
        i = 0
        if imc>itt:
            i=imc
        else:
            i = itt
        ifd = find_date_index_of(fd,rs)
        nama_tugas = clean_nama_tugas(rs[i:ifd])

    return nama_tugas

def is_dl_keyword_exist(raw_string):
    exist = False
    rs = raw_string.lower()
    rs = " ".join(rs.split())
    list_kata = rs.split(' ')
    for dl in KataPenting.list_deadline_keyword:
        code = rs.find(dl)
        if (code >= 0):
            exist = True
            break
    return exist

def is_waktu_exist(raw_string):
    exist = False
    rs = raw_string.lower()
    rs = " ".join(rs.split())
    list_kata = rs.split(' ')
    for kw in KataPenting.list_time_keyword:
        code = rs.find(kw)
        if (code >= 0):
            exist = True
            break
    return exist

def find_keyword_update_task(raw_string):
    rs = raw_string.lower()
    kata = ""
    for keyword in KataPenting.list_update_task_keyword:
        i = kmp(rs, keyword)
        if i>=0:
            kata = keyword
            break
    return kata

def is_task_done_exist(raw_string):
    rs = raw_string.lower()
    kata = ""
    for keyword in KataPenting.list_task_done_keyword:
        i = kmp(rs, keyword)
        if i>=0:
            kata = keyword
            break
    if (kata == ""):
        return False
    return True

def is_help_keyword_exist(raw_string):
    rs = raw_string.lower()
    kata = ""
    for keyword in KataPenting.list_help_keyword:
        i = kmp(rs, keyword)
        if i>=0:
            kata = keyword
            break
    if (kata == ""):
        return False
    return True


    
