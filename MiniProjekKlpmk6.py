total_pulsa = 0
total_Ewallet = 0
hargaakesoris = 0
nominal = 0
itp = []
list_hp = []
list_nominalhp = []
listnowallet = []
listwallertnominal = []
listnamawallet = []
Tharga_aksesoris = []
nama_aksesoris = []
jumlah_aksesoris = []


while True:
    print("====Zhamet Cell====")
    print("1.Isi Pulsa")
    print("2.Isi E-Wallet")
    print("3.Aksesoris")
    print("4.Selesai")
    pilihan = input("Pilih Layanan: ")
    if pilihan.isdigit():
        pilihan = int(pilihan)
        if pilihan == 1:
            while True:
                print("====Pulsa====")
                print("Ketik Batal Untuk Membatalkan")
                no_hp = input("Masukkan Nomor Pulsa (12 Digit): ").lower()
                if no_hp == "Batal":
                    break
                elif no_hp.isdigit() and len(no_hp) ==12:
                    nominal = input("Masukkan Nominal: ")
                    if nominal.isdigit():
                        list_hp.append(no_hp)
                        nominal = int(nominal)
                        list_nominalhp.append(nominal)
                        total_pulsa += nominal
                        break
                    else:
                        print("Nominal Harus Berupa Angka")
                else:
                    print("Nomor Tidak Valid")
        elif pilihan == 2:
            while True:
                print("====E-Wallet====")
                print("1.Dana")
                print("2.GoPay")
                print("3.ShopeePay")
                print("4.Batal")
                pilihan = input("Pilih E-Wallet: ")
                if pilihan.isdigit():
                    pilihan = int(pilihan)
                    if pilihan == 1:
                        namawallet = "Dana"
                        while True:
                            print("====Dana====")
                            print("Ketik Batal Untuk Membatalkan")
                            dana = input("Masukkan Nomor Dana (12 Digit): ").lower()
                            if dana == "Batal":
                                break
                            elif dana.isdigit() and len(dana) == 12:
                                while True:
                                    nominal = input("Masukkan Nominal: ")
                                    if nominal.isdigit():
                                        nominal = int(nominal)
                                        if nominal > 0:
                                            total_Ewallet += nominal
                                            listnowallet.append(dana)
                                            listwallertnominal.append(nominal)
                                            listnamawallet.append(namawallet)
                                            break
                                        else:
                                            print("Nominal Harus Berupa Angka")
                                    else:
                                        print("Nominal Tidak Valid")
                                break
                            else:
                                print("Nomor Tidak Valid")
                    elif pilihan == 2:
                        namawallet = "GoPay"
                        while True:
                            print("====GoPay====")
                            print("Ketik Batal Untuk Membatalkan")
                            gopay = input("Masukkan Nomor GoPay (12 Digit): ").lower()
                            if gopay == "Batal":
                                break
                            elif gopay.isdigit() and len(gopay) == 12:
                                nominal = input("Masukkan Nominal: ")
                                if nominal.isdigit():
                                    nominal = int(nominal)
                                    if nominal > 0:
                                        total_Ewallet += nominal
                                        listnowallet.append(gopay)
                                        listwallertnominal.append(nominal)
                                        listnamawallet.append(namawallet)
                                        break
                                    else:
                                        print("Nominal Harus Berupa Angka")
                                else:
                                    print("Hanya Berupa Angka")
                            else:
                                print("Nomor Tidak Valid")
                    elif pilihan == 3:
                        namawallet = "ShopeePay"
                        while True:
                            print("====ShopeePay====")
                            print("Ketik Batal Untuk Membatalkan")
                            shopeepay = input("Masukkan Nomor ShopeePay (12 Digit): ").lower()
                            if shopeepay == "Batal":
                                break
                            elif shopeepay.isdigit() and len(shopeepay) == 12:
                                nominal = input("Masukkan Nominal: ")
                                if nominal.isdigit():
                                    nominal = int(nominal)
                                    if nominal > 0:
                                        total_Ewallet += nominal
                                        listnowallet.append(shopeepay)
                                        listwallertnominal.append(nominal)
                                        listnamawallet.append(namawallet)
                                        break
                                    else:
                                        print("Nominal Harus Berupa Angka")
                                else:
                                    print("Harus Berupa Angka")
                            else:
                                print("Nomor Tidak Valid")
                    elif pilihan == 4:
                        break
                    else:
                        print("Tidak Ada Pilihan Tersebut")
                else:
                    print("Pilihan Berupa Angka")
        elif pilihan == 3:
            while True:
                print("====Aksesoris====")
                print("1.Kabel Data")
                print("2.Earphone")
                print("3.Casing Hp")
                print("4.Batal")
                pilihan = input("Pilih Aksesoris: ")
                if pilihan.isdigit():
                    pilihan = int(pilihan)
                    if pilihan == 1:
                        while True:
                            print("1.Type C - Rp 10.000")
                            print("2.Micro USB - Rp 7.500")
                            print("3.Batal")
                            pilihan = input("Pilih Tipe Kabel: ")
                            if pilihan.isdigit():
                                pilihan = int(pilihan)
                                if pilihan == 1:
                                    namaakse = "Type C"
                                    harga = 10000
                                    while True:
                                        jumlah = input("Beli Berapa Banyak: ").lower()
                                        if jumlah == "Batal":
                                            break
                                        elif jumlah.isdigit():
                                            jumlah = int(jumlah)
                                            hargaakesoris += jumlah * harga
                                            nama_aksesoris.append(namaakse)
                                            Tharga_aksesoris.append(jumlah * harga)
                                            jumlah_aksesoris.append(jumlah)
                                            break
                                        else:
                                            print("Hanya Menggunakan Angka")
                                elif pilihan == 2:
                                    namaakse = "Type Micro USB"
                                    harga = 7500
                                    while True:
                                        jumlah = input("Beli Berapa Banyak: ").lower()
                                        if jumlah == "Batal":
                                            break
                                        elif jumlah.isdigit():
                                            jumlah = int(jumlah)
                                            hargaakesoris += jumlah * harga
                                            nama_aksesoris.append(namaakse)
                                            Tharga_aksesoris.append(jumlah * harga)
                                            jumlah_aksesoris.append(jumlah)
                                            break
                                        else:
                                            print("Hanya Menggunakan Angka")
                                elif pilihan == 3:
                                    break
                                else:
                                    print("Tidak Ada Pilihan")
                            else:
                                print("Harus Berupa Angka")
                    elif pilihan == 2:
                        while True:
                            print("1.Low Budget - Rp 10.000")
                            print("2.Mid Budget - Rp 25.000")
                            print("3.High Budget - Rp 50.000")
                            print("4.Batal")
                            pilihan = input("Pilih Earphone:")
                            if pilihan.isdigit():
                                pilihan = int(pilihan)
                                if pilihan == 1:
                                    namaakse = "Low Budget Earphone"
                                    harga = 10000
                                    jumlah = input("Beli Berapa Banyak: ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        hargaakesoris += jumlah * harga
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        break
                                    else:
                                        print("Harus Berupa Angka")
                                elif pilihan == 2:
                                    namaakse = "Mid Budget Earphone"
                                    harga = 25000
                                    jumlah = input("Beli Berapa Banyak: ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        hargaakesoris += jumlah * harga
                                        break
                                    else:
                                        print("Harus Berupa Angka")
                                elif pilihan == 3:
                                    namaakse = "High Budget Earphone"
                                    harga = 50000
                                    jumlah = input("Beli Berapa Banyak: ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        hargaakesoris += jumlah * harga
                                        break
                                    else:
                                        print("Harus Berupa Angka")
                                elif pilihan == 4:
                                    break
                                else:
                                    print("Tidak Ada Pilihan")
                            else:
                                print("Harus Berupa Angka")
                    elif pilihan == 3:
                        while True:
                            print("1.Xiaomi - Rp 5.000")
                            print("2.Realme - Rp 4.500")
                            print("3.iPhone - Rp 5.500")
                            print("4.Batal")
                            pilihan = input("Pilih Merek: ")
                            if pilihan.isdigit():
                                pilihan = int(pilihan)
                                if pilihan == 1:
                                    namaakse = "Case Xiaomi"
                                    harga = 5000
                                    jumlah = input("Beli Berapa Banyak: ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        hargaakesoris += jumlah * harga
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        break
                                    else:
                                        print("Jumlah Harus Angka")
                                elif pilihan == 2:
                                    namaakse = "Case Realme"
                                    harga = 4500
                                    jumlah = input("Beli Berapa Banyak: ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        hargaakesoris += jumlah * harga
                                        break
                                    else:
                                        print("Jumlah Harus Berupa Angka")
                                elif pilihan == 3:
                                    namaakse = "Case iPhone"
                                    harga = 5500
                                    jumlah = input("Beli Berapa Banyak: ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        hargaakesoris += jumlah * harga
                                        break
                                    else:
                                        print("Harus Berupa Angka")
                                elif pilihan == 4:
                                    break
                            else:
                                print("Harus Berupa Angka")
                    elif pilihan == 4:
                        break
                    else:
                        print("Tidak Ada Pilihan")
        elif pilihan == 4:
            total = hargaakesoris + total_Ewallet + total_pulsa
            print("=" * 11)
            print("Zhamet Cell")
            print("=" * 11)
            for p in range (len(list_hp)):
                print("Pulsa")
                print(                          "No:", list_hp[p], "Nominal:", list_nominalhp[p])
            print("-" * 10)
            print("E-Wallet:")
            for e in range(len(listnowallet)):
                print(e+1 , listnamawallet[e] ," No:", listnowallet[e], "Nominal:", listwallertnominal[e])
            print("-" * 10)
            print("Aksesoris")
            print("-" * 10)
            for a in range (len(nama_aksesoris)):
                print(a+1, nama_aksesoris[a], "|", jumlah_aksesoris[a], "|" , "Rp",Tharga_aksesoris[a])
            print("-" * 10)
            print("Total: ", total)
            print("-" * 10)
            print("ありがとうございました")
            print("Thank You")
            print("Terima Kasih")
            break
        else:
            print("Tidak Ada Pilihan")
    else:
        print("Harus Berupa Angka")

