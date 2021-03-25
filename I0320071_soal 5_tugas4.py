s = "hey there! what should this string be?"

# panjangnya harus 20
print("panjang dari s = %d" % len(s))

# huruf pertama 'a' harusnya di index no 8
print("kemunculan pertama a = %d" % s.index("a"))

# jumlah huruf a harusnya 2
print("a muncul sebanyak %d kali" % s.count("a"))
# memotong string berdasarkan index
print("lima karakter pertama adalah '%s' " % s[:5]) # start to 5
print("lima karakter berikutnya adalah '%s" % s[5:10]) # 5 to 10
print("karakter ketiga bels adalah '%s'" % s[12])
print("karakter dengan index ganjil adalah'%s'" %s[1::2])
print("lima karakter terakhir adalah '%s'" % s[-5:])

# konversikan ke upercase
print("string dalam huruf besar : %s" % s.upper())

# konversikan ke upercase
print("string dalam huruf besar: %s" % s.lower())

# cek bagaimana string itu dimulai
if s.startswith("str"):
    print("string dimulai dengan 'str'. Good!")
# cek bagaimana string itu diakhiri
if s.endswith("ome!"):
    print("string diakhri dengan 'ome!'. 'Good' ")

# pisahkan string menjadi tiga string yang terpisah,
#masing-masing hanya berisi satu kata
print("pisahkan kata-kata dari string tersebut: %s" % s.split(" "))