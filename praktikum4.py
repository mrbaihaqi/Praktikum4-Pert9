#Membuat variable perulangan while
data = []
while True : 
	nama	= input	("Nama           : ")
	nim		= input ("NIM            : ")
	tugas	= int(input("Nilai Tugas    : "))
	uts 	= int(input("Nilai UTS      : "))
	uas 	= int(input("Nilai UAS      : "))
	nilaiakhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100 
	data.append ([nama,nim,tugas,uts,uas,nilaiakhir])
	lagi = input ("Tambah lagi (y/t)?")
	if lagi.lower() =="t":
		break
#prosess hasil dari lopping
print ("========================|=======DATA MAHASISWA==========|==============================")
print ("=======================================================================================")
print ("| No |	 Nama 	|  NIM 	| TUGAS |  UTS 	|     UAS 	|	 NILAI AKHIR 	|")
print ("=======================================================================================")
i=0
for x in data:
	i+=1
	print ("|{6:3d} | {0:9s}|  {1:5s}|{2:4d}   |{3:5d}  |    {4:4d}	| 	{5:10.2f} 	|"\
		.format (x[0][:9],x[1][:6],x[2],x[3],x[4],x[5],i))
print ("=======================================================================================")
