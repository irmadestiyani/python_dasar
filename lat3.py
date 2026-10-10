#menampilkan output dengan print
print("halo", "dunia")
print("a", "b", "c", sep="-")
print("loading", end="...")
print("selesai")

harga = 15000 / 7
print(f"harga: rp{harga:.2f}")
print(f"total: {1500000:,}")

print() 

#membaca input dari pengguna
nama = input("siapa namamu? ")
umur = int(input("berapa umurmu? "))

tahun_depan = umur + 1
print(f"halo {nama}!")
print(f"tahun depan kamu {tahun_depan} tahun")