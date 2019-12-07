data=[]
while(True):
    nim=input("Masukan Nim :")
    nama=input("Masukan Nama :")
    nilaitugas=int(input("masukan nilai tugas:"))
    uts=int(input("masukan nilai uts:"))
    uas=int(input("masukan nilai uas:"))
    akhir=int (30 * nilaitugas / 100) + (30 * uts / 100) + (30 * uas / 100)
    data.append([nim, nama, nilaitugas, uts, uas, akhir,])
    ulangi=input("Tambah data (y/t)?")
    if ulangi.lower() == 't' :
        break;

print("\nDAFTAR NAMA\n")
print("====================================================================================")
print("|   NIM   |   Nama   |   Nilai Tugas   |   Nilai UTS   |   Nilai UAS   |   Akhir   |")
print("====================================================================================")
for x in data:
    print ("| {0:7} | {1:8} | {2:15} | {3:13} | {4:13} | {5:9} |" .format(x[0], x[1], x[2], x[3], x[4], x[5]))