import time
start_time = time.time()

print("Mohon isikan jawaban Anda untuk mendaftar kursus")
print(" ")

usia = int(input("Berapakah usia Anda: "))

print("Apakah Anda lulus ujian kualifikasi? (Y/T)")
lulus = input().upper()

syaratusia = usia >= 21
syaratujian = lulus == "Y"

hasil = syaratusia and syaratujian
print(" ")
if hasil == True:
    print("Anda dapat mendaftar di kursus.")
else:
    print("Anda tidak dapat mendaftar di kursus.")
print("-"*35)


print("Runtime =",time.time() - start_time, "detik")