# Python Program to count Mr.Tavolta Wage
# Name	: Ahmad Bisyrul Hafi (11180910000122)
# Date	: 02 September 2021
# Courses	: Software Quality Testing


jam_normal = 40
gaji_normal = 15000
gaji_lembur = gaji_normal * 1.5

print(f'Gaji Normal (40 Jam/minggu) = Rp {gaji_normal}/jam')
print(f'Gaji Lembur (>40 Jam/minggu) = Rp {gaji_lembur}/jam')

print('=====================================================')

# Menghitung pemasukan dalam seminggu
jam_kerja = int(input("Berapa lama anda bekerja dalam seminggu? : "))

if jam_kerja>jam_normal:
	pemasukan = jam_normal * gaji_normal + (jam_kerja - jam_normal) * gaji_lembur
else:
	pemasukan = jam_kerja * gaji_normal


print('Pemasukan anda dalam seminggu adalah : Rp {pemasukan}')


#Menghitung pengeluaran

pengeluaran = int(input("Berapa banyak pengeluaran anda dalam seminggu? "))

# menghitung berapa banyak yang bisa ditabung
if pemasukan > pengeluaran:
	tabungan = pemasukan - pengeluaran
	print('Anda bisa menabung sebanyak Rp {tabungan}')
elif pemasukan == pengeluaran:
	print('Anda tidak bisa menabung')
else:
	print('Cari uang tambahan untuk menabung')