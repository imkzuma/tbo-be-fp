# GUNG KRISNA 
# 2108561021

RESULT = {} # ini adalah dictionary yang berisi hasil dari proses CNF

def remove_unit_production(keyList): # fungsi untuk menghapus produksi unit
    global RESULT # mengakses variabel global
    for key, value in RESULT.items(): # perulangan untuk setiap key dan value pada dictionary
        if key in keyList: # jika key ada pada list keyList
            tempList = [] # buat list kosong temporary
            for prod in value: # perulangan untuk setiap produksi pada value
                if len(prod.split(" ")) == 2: # jika panjang produksi adalah 2
                    tempList.append(prod) # tambahkan produksi ke list temporary
                else: # jika panjang produksi bukan 2
                    for i in RESULT[prod]: # perulangan untuk setiap produksi pada value dari key
                        if i not in tempList: # jika produksi belum ada di list temporary
                            tempList.append(i) # tambahkan produksi ke list temporary
            RESULT[key] = tempList # set value dari key dengan list temporary

def get_set_of_production(): # fungsi untuk mengambil set produksi
    global RESULT # mengakses variabel global
    
    RESULT.clear() # menghapus semua isi dictionary
    f = open("./variable_list1.txt", "r", encoding="utf-8") # membuka file variable_list.txt
    
    for lines in f: # perulangan untuk setiap baris pada file
        line = lines.splitlines() # memisahkan baris dengan newline
        line = line[0].split(" -> ") # memisahkan baris dengan ->
        lhs = line[0] # mengambil bagian kiri
        rhs = line[1].split(" | ") # mengambil bagian kanan dan memisahkan dengan |
        if lhs in RESULT.keys(): # jika key sudah ada di dictionaryya
            RESULT[lhs].extend(rhs) # tambahkan value ke list value
        else: # jika key belum ada di dictionary
            RESULT[lhs] = rhs # buat key baru dengan value baru
    f.close() # menutup file
    for key, value in RESULT.items(): # perulangan untuk setiap key dan value pada dictionary
        if key == "PropNoun": # jika key adalah PropNoun 
            tempList = [] # buat list kosong temporary
            for val in value: # perulangan untuk setiap produksi pada value
                if val not in tempList: # jika produksi belum ada di list temporary
                    tempList.append(val.lower()) # tambahkan produksi ke list temporary dengan huruf kecil
            RESULT[key] = tempList # set value dari key dengan list temporary
    
    phrases = ["NumP", "AdvP", "AdjP", "PP", "NP", "VP"] # list key yang akan dihapus produksi unitnya 
    
    remove_unit_production(phrases) # panggil fungsi untuk menghapus produksi unit
    patterns = ["S", "P", "O", "Pel", "Ket"] # list key yang akan dihapus produksi unitnya
    
    remove_unit_production(patterns) # panggil fungsi untuk menghapus produksi unit
    
    tempList = [] # buat list kosong temporary
    tempDict = {} # buat dictionary kosong temporary
    counter = 1 # buat counter untuk key baru
    
    for key, value in RESULT.items(): # perulangan untuk setiap key dan value pada dictionary
        if key == "K": # jika key adalah K
            for val in value:  # perulangan untuk setiap produksi pada value
                if len(val.split(" ")) > 2: # jika panjang produksi lebih dari 2
                    temp = val.split(" ") # pisahkan produksi dengan spasi
                    while len(temp) > 2: # perulangan selama panjang produksi lebih dari 2
                        checkStr = temp[0] + " " + temp[1] # buat string untuk dicek
                        isFound = False # buat boolean untuk mengecek apakah string sudah ada di dictionary
                        for k, v in tempDict.items(): # perulangan untuk setiap key dan value pada dictionary temporary
                            if checkStr == v: # jika string sudah ada di dictionary
                                isFound = True # set boolean menjadi True
                                temp.pop(0) # hapus produksi yang sudah dicek
                                temp.pop(0) # hapus produksi yang sudah dicek
                                temp.insert(0, k) # tambahkan key baru ke produksi
                                break # hentikan perulangan
                        if not isFound: # jika string belum ada di dictionary
                            tempDict["K" + str(counter)] = checkStr # tambahkan key baru dengan value baru ke dictionary temporary
                            temp.pop(0) # hapus produksi yang sudah dicek
                            temp.pop(0) # hapus produksi yang sudah dicek
                            temp.insert(0, "K" + str(counter)) # tambahkan key baru ke produksi
                            counter += 1 # tambahkan counter
                    tempList.append(" ".join(temp)) # tambahkan produksi ke list temporary
                else: # jika panjang produksi tidak lebih dari 2
                    tempList.append(val) # tambahkan produksi ke list temporary
            RESULT[key] = tempList # set value dari key dengan list temporary
    for key, value in tempDict.items(): # perulangan untuk setiap key dan value pada dictionary temporary
        RESULT[key] = [value] # set value dari key dengan value baru
    return RESULT # kembalikan dictionary
