# DATA COLLECTION TERSEDIA
dataYellowPages = [
    [1,'Restoran','Burger Blenger','Tangerang','082120221000'],
    [2,'Perhotelan','Glory Hotel','Jakarta Pusat','082120222000'],
    [3,'Elektronik','AC Service','Jakarta Utara','082120223000'],
    [4,'Restoran','Golden Pizza','Tangerang','082150005000']
]
# dataYellowPages = []

# PROGRAM YELLOW PAGES
def yellowPages():
    while True:
        pilihanMainMenu = input('''
        Selamat Datang di Yellow Pages Indonesia\n
        Menu Utama Yellow Pages:\n
        1. Menampilkan Daftar Perusahaan 
        2. Menambah Data Perusahaan
        3. Mengupdate Data Perusahaan
        4. Menghapus Data Perusahaan
        5. Exit\n
        Masukkan nomor menu yang ingin dijalankan:''')
    
        if pilihanMainMenu == '1':
            def menuShowData():
                # MENU READ
                while True:
                    pilihanShowData = input('''
                    Menu Show Data\n
                    1) Menampilkan Seluruh Data
                    2) Menampilkan Data sesuai ID
                    3) Kembali ke Menu Utama\n
                    Masukkan nomor menu yang ingin dijalankan:''')

                    if pilihanShowData == '1':
                        if len(dataYellowPages) == 0:
                            print('Data Tidak Tersedia')
                        else:
                            print('Daftar Perusahaan:\n')
                            print('ID\t|Kategori Bisnis|Nama Perusahaan\t|Alamat\t\t|Nomor Telepon')
                            for i in range(len(dataYellowPages)):
                                print(f'{dataYellowPages[i][0]}\t|{dataYellowPages[i][1]}\t|{dataYellowPages[i][2]}\t\t|{dataYellowPages[i][3]}\t|{dataYellowPages[i][4]}')
                    elif pilihanShowData == '2':
                        while True:
                            checkID = input('Masukkan ID perusahaan yang ingin ditampilkan:')
                            if checkID.isdigit():
                                checkID = int(checkID)
                                if any(checkID in i for i in dataYellowPages):
                                    print('Daftar Perusahaan:\n')
                                    print('ID\t|Kategori Bisnis|Nama Perusahaan\t|Alamat\t\t|Nomor Telepon')
                                    for i in range(len(dataYellowPages)):
                                        print(f'{checkID}\t|{dataYellowPages[checkID-1][1]}\t|{dataYellowPages[checkID-1][2]}\t\t|{dataYellowPages[checkID-1][3]}\t|{dataYellowPages[checkID-1][4]}')
                                        break
                                else:
                                    print('Data Tidak Tersedia')
                                break
                            else:
                                print('ID harus angka')
                    elif pilihanShowData == '3':
                        break
                    else:
                        print('Pilihan yang anda masukkan salah')
            menuShowData()
        elif pilihanMainMenu == '2':
            def menuCreateData():
                # MENU CREATE
                while True:
                    pilihanCreateData = input('''
                    Menu Create Data\n
                    1) Menambah Data
                    2) Kembali ke Menu Utama\n
                    Masukkan nomor menu yang ingin dijalankan:''')

                    if pilihanCreateData == '1':
                        while True:
                            checkID = input('Masukkan ID perusahaan yang ingin ditambah ke Data Yellow Pages:')
                            if checkID.isdigit():
                                checkID = int(checkID)
                                if any(checkID in i for i in dataYellowPages):
                                    print('Data Sudah Tersedia')
                                else:
                                    print('Data baru, silahkan mengisi kelengkapan data:')
                                    while True:
                                        ID = input('ID:')
                                        if ID.isdigit():
                                            ID = int(ID)
                                            while True:
                                                kategoriBisnis = input('Kategori Bisnis:')
                                                if len(kategoriBisnis)>1:
                                                    while True:
                                                        namaPerusahaan = input('Nama Perusahaan:')
                                                        if len(namaPerusahaan)>1:
                                                            while True:
                                                                alamat = input('Alamat Perusahaan:')
                                                                if len(alamat)>1:
                                                                    while True:
                                                                        nomorTelepon = input('Nomor Telepon:')
                                                                        if nomorTelepon.isdigit() and len(nomorTelepon)>=10 and len(nomorTelepon)<=13:

                                                                            # MENU SIMPAN
                                                                            while True:
                                                                                option1 = input('Apakah anda ingin menyimpan data?(ya/tidak):')
                                                                                option1 = option1.upper()
                                                                                if option1 == 'TIDAK':
                                                                                    break
                                                                                elif option1 == 'YA':
                                                                                    dataYellowPages.append([ID,kategoriBisnis,namaPerusahaan,alamat,nomorTelepon])
                                                                                    print('Daftar Perusahaan:\n')
                                                                                    print('ID\t|Kategori Bisnis|Nama Perusahaan\t|Alamat\t\t|Nomor Telepon')
                                                                                    for i in range(len(dataYellowPages)):
                                                                                        print(f'{dataYellowPages[i][0]}\t|{dataYellowPages[i][1]}\t|{dataYellowPages[i][2]}\t\t|{dataYellowPages[i][3]}\t|{dataYellowPages[i][4]}')
                                                                                    break
                                                                                else:
                                                                                    print('Pilihan yang anda masukkan salah')
                                                                            break
                                                                        else:
                                                                            print('nomor telepon tidak valid')
                                                                    break
                                                                else:
                                                                    print('input harus lebih dari 1 karakter')
                                                            break
                                                        else:
                                                            print('input harus lebih dari 1 karakter')
                                                    break
                                                else:
                                                    print('input harus lebih dari 1 karakter')
                                            break
                                        else:            
                                            print('input harus angka')
                                break
                            else:
                                print('ID harus angka')    
                    elif pilihanCreateData == '2':
                        break
                    else:
                        print('Pilihan yang anda masukkan salah')
            menuCreateData()
        elif pilihanMainMenu == '3':
            def menuUpdateData():
                while True:
                    pilihanUpdateData = input('''
                    Menu Update Data\n
                    1) Mengupdate Data
                    2) Kembali ke Menu Utama\n
                    Masukkan nomor menu yang ingin dijalankan:''')

                    if pilihanUpdateData == '1':
                        while True:
                            checkID = input('Masukkan ID perusahaan yang ingin diupdate:')
                            if checkID.isdigit():
                                checkID = int(checkID)
                                if any(checkID in i for i in dataYellowPages):
                                    while True:
                                        option1 = input(f'Ingin lanjut mengupdate data dengan ID {checkID}?(ya/tidak):')
                                        option1 = option1.lower()
                                        if option1 == 'ya':
                                            # UPDATE FUNCTION
                                            while True:
                                                kolomUpdate = input('''
                                                Daftar nomor kolom\n
                                                1) ID
                                                2) Kategori Bisnis
                                                3) Nama Perusahaan
                                                4) Alamat
                                                5) Nomor Telepon\n
                                                Masukkan nomor kolom yang ingin diedit:''')

                                                if kolomUpdate == '1':
                                                    while True:
                                                        updateID = input('Masukkan ID baru:')
                                                        if updateID.isdigit():
                                                            updateID = int(updateID)
                                                            while True:
                                                                option2 = input('Simpan update?(ya/tidak):')
                                                                option2 = option2.upper()
                                                                if option2 == 'YA':
                                                                    dataYellowPages[checkID-1][0] = updateID
                                                                    print('Data Terupdate')
                                                                    print('ID\t|Kategori Bisnis|Nama Perusahaan\t|Alamat\t\t|Nomor Telepon')
                                                                    for i in range(len(dataYellowPages)):
                                                                        print(f'{dataYellowPages[checkID-1][0]}\t|{dataYellowPages[checkID-1][1]}\t|{dataYellowPages[checkID-1][2]}\t\t|{dataYellowPages[checkID-1][3]}\t|{dataYellowPages[checkID-1][4]}')
                                                                        break
                                                                    break
                                                                elif option2 == 'TIDAK':
                                                                    break
                                                                else:
                                                                    print('Pilihan yang anda masukkan salah')
                                                            break
                                                        else:
                                                            print('input harus angka')
                                                    break
                                                elif kolomUpdate == '2':
                                                    while True:
                                                        updateKategoriBisnis = input('Masukkan kategori bisnis baru:')
                                                        if len(updateKategoriBisnis)>1:
                                                            while True:
                                                                option2 = input('Simpan update?(ya/tidak):')
                                                                option2 = option2.upper()
                                                                if option2 == 'YA':
                                                                    dataYellowPages[checkID-1][1] = updateKategoriBisnis
                                                                    print('Data Terupdate')
                                                                    print('ID\t|Kategori Bisnis|Nama Perusahaan\t|Alamat\t\t|Nomor Telepon')
                                                                    for i in range(len(dataYellowPages)):
                                                                        print(f'{dataYellowPages[checkID-1][0]}\t|{dataYellowPages[checkID-1][1]}\t|{dataYellowPages[checkID-1][2]}\t\t|{dataYellowPages[checkID-1][3]}\t|{dataYellowPages[checkID-1][4]}')
                                                                        break
                                                                    break                                                                
                                                                elif option2 == 'TIDAK':
                                                                    break
                                                                else:
                                                                    print('Pilihan yang anda masukkan salah')
                                                            break
                                                        else:
                                                            print('input harus lebih dari 1 karakter')
                                                    break
                                                elif kolomUpdate == '3':
                                                    while True:
                                                        updateNamaPerusahaan = input('Masukkan nama perusahaan baru:')
                                                        if len(updateNamaPerusahaan)>1:
                                                            while True:
                                                                option2 = input('Simpan update?(ya/tidak):')
                                                                option2 = option2.upper()
                                                                if option2 == 'YA':
                                                                    dataYellowPages[checkID-1][2] = updateNamaPerusahaan
                                                                    print('Data Terupdate')
                                                                    print('ID\t|Kategori Bisnis|Nama Perusahaan\t|Alamat\t\t|Nomor Telepon')
                                                                    for i in range(len(dataYellowPages)):
                                                                        print(f'{dataYellowPages[checkID-1][0]}\t|{dataYellowPages[checkID-1][1]}\t|{dataYellowPages[checkID-1][2]}\t\t|{dataYellowPages[checkID-1][3]}\t|{dataYellowPages[checkID-1][4]}')
                                                                        break
                                                                    break                                                                
                                                                elif option2 == 'TIDAK':
                                                                    break
                                                                else:
                                                                    print('Pilihan yang anda masukkan salah')
                                                            break
                                                        else:
                                                            print('input harus lebih dari 1 karakter')
                                                    break
                                                elif kolomUpdate == '4':
                                                    while True:
                                                        updateAlamat = input('Masukkan alamat baru:')
                                                        if len(updateAlamat)>1:
                                                            while True:
                                                                option2 = input('Simpan update?(ya/tidak):')
                                                                option2 = option2.upper()
                                                                if option2 == 'YA':
                                                                    dataYellowPages[checkID-1][3] = updateAlamat
                                                                    print('Data Terupdate')
                                                                    print('ID\t|Kategori Bisnis|Nama Perusahaan\t|Alamat\t\t|Nomor Telepon')
                                                                    for i in range(len(dataYellowPages)):
                                                                        print(f'{dataYellowPages[checkID-1][0]}\t|{dataYellowPages[checkID-1][1]}\t|{dataYellowPages[checkID-1][2]}\t\t|{dataYellowPages[checkID-1][3]}\t|{dataYellowPages[checkID-1][4]}')
                                                                        break
                                                                    break                                                                
                                                                elif option2 == 'TIDAK':
                                                                    break
                                                                else:
                                                                    print('Pilihan yang anda masukkan salah')
                                                            break
                                                        else:
                                                            print('input harus lebih dari 1 karakter')
                                                    break
                                                elif kolomUpdate == '5':
                                                    while True:
                                                        updateNomorTelepon = input('Masukkan nomor telepon baru:')
                                                        if updateNomorTelepon.isdigit() and len(updateNomorTelepon)>=10 and len(updateNomorTelepon)<=13:
                                                            while True:
                                                                option2 = input('Simpan update?(ya/tidak):')
                                                                option2 = option2.upper()
                                                                if option2 == 'YA':
                                                                    dataYellowPages[checkID-1][4] = updateNomorTelepon
                                                                    print('Data Terupdate')
                                                                    print('ID\t|Kategori Bisnis|Nama Perusahaan\t|Alamat\t\t|Nomor Telepon')
                                                                    for i in range(len(dataYellowPages)):
                                                                        print(f'{dataYellowPages[checkID-1][0]}\t|{dataYellowPages[checkID-1][1]}\t|{dataYellowPages[checkID-1][2]}\t\t|{dataYellowPages[checkID-1][3]}\t|{dataYellowPages[checkID-1][4]}')
                                                                        break
                                                                    break                                                                
                                                                elif option2 == 'TIDAK':
                                                                    break
                                                                else:
                                                                    print('Pilihan yang anda masukkan salah')
                                                            break
                                                        else:
                                                            print('nomor telepon tidak valid')
                                                    break
                                                else:
                                                    print('Pilihan yang anda masukkan salah')
                                                
                                            break                           
                                        elif option1 == 'tidak':
                                            break
                                        else:
                                            print('Pilihan yang anda masukkan salah')
                                    break
                                else:
                                    print('Data tidak tersedia')
                                break
                            else:
                                print('ID harus angka')
                    elif pilihanUpdateData == '2':
                        break
                    else:
                        print('Pilihan yang anda masukkan salah')
            menuUpdateData()
        elif pilihanMainMenu == '4':
            def menuDeleteData():
                while True:
                    pilihanDeleteData = input('''
                    Menu Delete Data\n
                    1) Menghapus Data
                    2) Kembali ke Menu Utama\n
                    Masukkan nomor menu yang ingin dijalankan:''')

                    if pilihanDeleteData == '1':
                        while True:
                            checkID = input('Masukkan ID perusahaan yang ingin dihapus:')
                            if checkID.isdigit():
                                checkID = int(checkID)
                                if any(checkID in i for i in dataYellowPages):
                                    while True:
                                        option1 = input(f'Ingin menghapus data dengan ID {checkID}?(ya/tidak):')
                                        option1 = option1.upper()

                                        if option1 == 'YA':
                                            while True:
                                                option2 = input('Apakah anda yakin?(ya/tidak):')
                                                option2 = option2.upper()
                                                if option2 == 'YA':
                                                    checkID = checkID - 1
                                                    del dataYellowPages[checkID]
                                                    print('Data Terhapus')
                                                    print('Daftar Perusahaan:\n')
                                                    print('ID\t|Kategori Bisnis|Nama Perusahaan\t|Alamat\t\t|Nomor Telepon')
                                                    for i in range(len(dataYellowPages)):
                                                        print(f'{dataYellowPages[i][0]}\t|{dataYellowPages[i][1]}\t|{dataYellowPages[i][2]}\t\t|{dataYellowPages[i][3]}\t|{dataYellowPages[i][4]}')
                                                    break
                                                elif option2 == 'TIDAK':
                                                    print('Daftar Perusahaan:\n')
                                                    print('ID\t|Kategori Bisnis|Nama Perusahaan\t|Alamat\t\t|Nomor Telepon')
                                                    for i in range(len(dataYellowPages)):
                                                        print(f'{dataYellowPages[i][0]}\t|{dataYellowPages[i][1]}\t|{dataYellowPages[i][2]}\t\t|{dataYellowPages[i][3]}\t|{dataYellowPages[i][4]}')
                                                    break
                                                else:
                                                    print('Pilihan yang anda masukkan salah')
                                            break
                                        elif option1 == 'TIDAK':
                                            break
                                        else:
                                            print('Pilihan yang anda masukkan salah') 
                                else:
                                    print('Data tidak tersedia')
                                break
                            else:
                                print('ID harus angka')
                    elif pilihanDeleteData == '2':
                        break
                    else:
                        print('Pilihan yang anda masukkan salah')
            menuDeleteData()
        elif pilihanMainMenu == '5':
            print('Anda telah keluar dari program')
            break
        else:
            print('Pilihan yang anda masukkan salah')
yellowPages()

# NOTE:
# code yang sama bisa disimpan didalam function dulu nanti tinggal dipanggil jika dibutuhkan, function ditaruh diluar
# penamaan variabel sebaiknya bahasa inggris dan konsisten formnya, jika camel case, camel case terus
# penyimpanan data sebaiknya menggunakan dictionary bukan list. karena pemanggilan data dengan primary key bukan index
# codingan terlalu ke kanan kurang baik