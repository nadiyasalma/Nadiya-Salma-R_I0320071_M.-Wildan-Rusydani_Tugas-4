#program rencana pengujian
usia_min = 21
usia_pengguna = int(input("berapa usia anda : "))
if usia_min <= usia_pengguna :
    print("anda sudah cukup umur")
    x = str(input("apakah anda sudah lulus dalam ujian kualifikasi: (Y/T) "))
    if x == "Y" :
        print("anda dapat mengikuti kursus")
    elif x == "T" :
        print("anda tidak dapat mengikuti kursus")
else :
    print("anda belum cukup umur")

