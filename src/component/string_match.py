def get_prefixes(s):
    return [s[:i] for i in range (1, len(s)+1)]

def get_suffixes(s):
    return [s[-i:] for i in range (1, len(s)+1)]

def last_occurence(s):
    lo = {}
    i = len(s)-1
    while i>=0:
        if s[i] not in lo:
            lo[s[i]] = i
        i-=1
    # print(lo)
    return lo

def get_border_table(pattern):
    k = 0
    border_table = []
    while (k < len(pattern)-1):
        pf = get_prefixes(pattern[0:k+1])
        sf = get_suffixes(pattern[1:k+1])
        x = 0
        fail_k = 0
        while x < len(sf):
            if pf[x] == sf[x]:
                fail_k = x+1
            x+=1
        border_table.append(fail_k)
        k+=1
    return border_table


def kmp(text,pattern):
    x=-1
    n = len(text)
    m = len(pattern)
    border_table = get_border_table(pattern) 
    i=0 # index text
    j=0 # index pattern
    while (i<n):
        if text[i] == pattern[j]:
            if j == m-1:
                return i - m + 1
            i+=1
            j+=1
        elif j>0:
            j=border_table[j-1]
        else:
            i+=1
            
    return x

def boyer_moore(text,pattern):
    lo = last_occurence(pattern)
    m = len(pattern)
    x=-1
    if m>0:
        match = False
        all_char_checked = False
        j=m-1
        i=j
        while i<=len(text) and not match and not all_char_checked:
            mismatch = False
            while not mismatch and j>=0 and i<len(text):
                if text[i] != pattern[j]:
                    mismatch = True
                j-=1
                i-=1
            if i>=len(text):
                all_char_checked = True
            elif mismatch:
                # kasus 3: text[i] not in pattern -> lo
                if text[i] not in lo:
                    l = -1
                    i = (i + m - (l+1))
                    j = m-1
                # kasus 1: lo[text[i]] < j
                elif lo[text[i]] < j:
                    l = lo[text[i]]
                    i = (i + m - (l+1))
                    j = m-1
                # kasus 2: lo[text[i]] > j
                else:
                    i = i+m-j
                    j = m-1
            else:
                match = True
                x = i+1
                    
    return x
