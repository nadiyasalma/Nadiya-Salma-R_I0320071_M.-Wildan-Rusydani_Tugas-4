#program rencana pengujian
usia_min= 21
usia_pengguna = int(input("berapa usia anda : "))
if usia_min <= usia_pengguna :
    print("anda sudah cukup umur")
    a = str(input("apakah anda sudah lulus dalam ujian kulaifikasi: (Y/T) "))
    if a == "T" :
        print("anda tidak dapat mendaftar di kursus ")
    elif a == "T" :
        print("anda belom boleh mengikuti kursus")
else :
    print("anda belum cukup umur")

