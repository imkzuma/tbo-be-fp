from modules.cnf import get_set_of_production
# GUNG KRISNA 
# 2108561021

#  ini adalah library yang digunakan untuk mengimport fungsi get_set_of_production

TRIANGULAR_TABLE = {} # ini adalah tabel yang digunakan untuk menyimpan hasil perhitungan CYK
# g = None # ini adalah variabel global yang digunakan untuk menyimpan graf yang dibangun dari inputan user
# previousNode = None # ini adalah variabel global yang digunakan untuk menyimpan node sebelumnya

def cekString(inputString): # ini adalah fungsi yang digunakan untuk mengecek apakah inputan user diterima atau tidak
    global TRIANGULAR_TABLE # ini adalah variabel global yang digunakan untuk menyimpan tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    TRIANGULAR_TABLE.clear() # ini adalah fungsi yang digunakan untuk menghapus isi dari tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    
    prodRules = get_set_of_production() # ini adalah variabel yang digunakan untuk menyimpan hasil dari fungsi get_set_of_production
    temp = inputString.lower().split(" ") # ini adalah variabel yang digunakan untuk menyimpan hasil dari fungsi get_set_of_production
    
    inputString = temp # ini adalah variabel yang digunakan untuk menyimpan hasil dari fungsi get_set_of_production
    
    for i in range(1,len(inputString)+1): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
        for j in range(i, len(inputString)+1): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
            TRIANGULAR_TABLE[(i,j)] = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    
    for i in reversed(range(1, len(inputString)+1)): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
        for j in range(1, i+1): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
            if (j == j + len(inputString) - i): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                tempList = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                for key, value in prodRules.items(): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    for val in value: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                        if (val == inputString[j-1] and key not in tempList): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                            tempList.append(key) # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                TRIANGULAR_TABLE[(j, j + len(inputString) - i)] = tempList # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
            
            else: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                tempList = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                resultList = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                
                for k in range(len(inputString) - i): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    first = TRIANGULAR_TABLE[(j,j+k)] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    second = TRIANGULAR_TABLE[(j+k+1,j+len(inputString) - i)] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    for fi in first: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                        for se in second: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                            if (fi + " " + se not in tempList): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                                tempList.append(fi + " " + se) # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                
                for key, value in prodRules.items(): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    for val in value: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                        if (val in tempList and key not in resultList): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                            resultList.append(key) # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                
                TRIANGULAR_TABLE[(j,j+len(inputString) - i)] = resultList # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK

    if "K" in TRIANGULAR_TABLE[(1, len(inputString))]: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
        return True # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    else: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
        return False # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK


#arr = ["Sang Penyair sedang menulis sebait puisi", "Adik saya sedang mencuci sepatu baru", "Kakak saya sudah membeli nasi goreng", "Ibu sedang menyapu lantai", "Sita baru saja membersihkan kamar mandi", "Vina sedang mendengarkan lagu galau", "Nenek mengirim sepucuk surat", "Kakek sedang menanam padi di sawah", "Kelinci itu sedang melompati pagar bambu", "Mereka sedang melempar batu kerikil", "Roni sedang menendang bola di halaman sekolah", "Kakak saya menuang susu di gelas besar", "Yoni baru saja mengambil mainan adik saya", "Leo selalu mengagumi kecantikan Naura", "Kinan sedang memetik bunga melati di taman", "Lini sedang membaca buku novel di kamar tidur", "Kakek sedang membajak sawah", "Rina sedang melukis pemandangan di kebun bunga", "Raka sedang menyetir mobil ke rumah baru", "Polisi itu sedang menangkap penjahat di hutan", "Ibu memasakkan saya sayur enak", "Ibu sedang membuatkan bapak itu teh daun di dapur", "Intan menyanyikan lagu  indah sebagai pelengkap", "Agnita memberikan teman saya sebuah buku baru", "Yoni membelikan adik saya mainan baru", "Kakak saya menuangi gelas saya dengan susu", "Pak Agus sedang menebangi pohon dengan gergaji listrik", "Ayah membelikan adik saya mainan baru", "Kinan sedang memetikkan ibu saya bunga melati di kebun kakek", "Raka sedang menyetir mobil baru dengan hati-hati", "Lini membacakan adik saya cerita pendek di perpustakaan", "Ibu sedang menyapu lantai hingga bersih", "Kakek membajak sawah itu dengan traktor", "Rina sedang melukis pemandangan dengan sangat indah", "Diah sudah mengirim sepucuk surat untuk kerabat saya di kampung", "Ayah sedang menangkap anjing dengan semangat tinggi", "Kakak saya sedang membuatkan adik saya mainan baru", "Ibu Dewi sedang menjahitkan adik saya celana sekolah baru", "Intan sedang meminjamkan Agnita pensil warna", "Krisna sedang menberikan adik saya motor bekas", "Kakak sedang membaca buku", "Carlos sedang menonton televisi", "Kakek sedang menembak burung", "Adik sedang menggambar bunga", "Andi sedang menulis artikel", "Gung Wah berjalan sempoyongan", "Intan membeli sepatu baru", "Dhandy bekerja siang malam", "Seorang tahanan melarikan diri", "Monika menginap di rumah teman", "Aldo menangis sesenggukan", "Rebecca berlari kencang", "Ayu bernyanyi dengan merdu", "Krisna berdiri tegak", "Kucing itu bergerak lincah", "HP Toni bergetar di kantong", "Adik berteriak hingga suaranya serak", "Ibu berbelanja di pasar", "Pohon itu tersambar petir", "Maling itu tertangkap polisi"]


def cekKebenaranKata(inputString): # ini adalah fungsi yang digunakan untuk mengecek apakah inputan user diterima atau tidak
    global TRIANGULAR_TABLE # ini adalah variabel global yang digunakan untuk menyimpan tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    TRIANGULAR_TABLE.clear() # ini adalah fungsi yang digunakan untuk menghapus isi dari tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    
    prodRules = get_set_of_production() # ini adalah variabel yang digunakan untuk menyimpan hasil dari fungsi get_set_of_production
    temp = inputString.lower().split(" ") # ini adalah variabel yang digunakan untuk menyimpan hasil dari fungsi get_set_of_production
    
    inputString = temp # ini adalah variabel yang digunakan untuk menyimpan hasil dari fungsi get_set_of_production

    kalimatChecker = list()
    
    for i in range(1,len(inputString)+1): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
        for j in range(i, len(inputString)+1): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
            TRIANGULAR_TABLE[(i,j)] = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    
    for i in reversed(range(1, len(inputString)+1)): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
        for j in range(1, i+1): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
            if (j == j + len(inputString) - i): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                tempList = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                for key, value in prodRules.items(): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    for val in value: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                        if (val == inputString[j-1] and key not in tempList): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                            tempList.append(key) # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                            kalimatChecker.append(inputString[j-1])
                TRIANGULAR_TABLE[(j, j + len(inputString) - i)] = tempList # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
            
            else: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                tempList = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                resultList = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                
                for k in range(len(inputString) - i): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    first = TRIANGULAR_TABLE[(j,j+k)] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    second = TRIANGULAR_TABLE[(j+k+1,j+len(inputString) - i)] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    for fi in first: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                        for se in second: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                            if (fi + " " + se not in tempList): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                                tempList.append(fi + " " + se) # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                
                for key, value in prodRules.items(): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    for val in value: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                        if (val in tempList and key not in resultList): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                            resultList.append(key) # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                
                TRIANGULAR_TABLE[(j,j+len(inputString) - i)] = resultList # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    
    kalimatChecker = list(dict.fromkeys(kalimatChecker))
    newList = list()

    for i in range(len(inputString)):
        if inputString[i] not in kalimatChecker:
            newList.append(inputString[i])
    
    return newList

def printTable(inputString):
    global TRIANGULAR_TABLE

    null = "\u2205"
    result = list()
    n = len(inputString.split(" "))

    for i in range(1, n+1):
        tempArr = list()
        for j in range(i):
            temp = TRIANGULAR_TABLE[(j+1, n-i+j+1)]
            if len(temp) == 0:
                tempArr.append(null)
            else:
                tempArr.append(temp)

        result.append(tempArr)

    result.append(inputString.split(" "))
    return result

string = "kakak suka bermain sawah"

print(cekString(string))
print(cekKebenaranKata(string))

