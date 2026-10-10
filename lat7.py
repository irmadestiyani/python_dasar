# list: koleksi berurutan yang bisa diubah
print("> list")
nilai = [80, 65, 90]
nilai.append(75)
nilai.remove(65)
nilai[0] = 85

print(nilai)
print(nilai[-1], len(nilai))
print(sorted(nilai))

print()

# tuple: seperti list tapi gak bisa diubah (immutable)
print("> tuple")
titik = (3, 7)
warna = (255, 128, 0)

x, y = titik   # unpacking
print(f"x={x}, y={y}")
print(warna[0], len(warna))

# titik[0] = 10   # TypeError, tuple gak bisa diubah

print()

# set: kumpulan nilai unik, duplikat otomatis dibuang
print("> set")
angka = {1, 2, 2, 3, 3, 3}
print(angka)

ipa = {"ani", "budi", "citra"}
ips = {"budi", "dodi"}

print(ipa | ips)
print(ipa & ips)
print(ipa - ips)

print()

# dictionary: pasangan key - value
print("> dictionary")
siswa = {"nama": "sari", "umur": 19}
siswa["kota"] = "bandung"
siswa["umur"] = 20
print(siswa["nama"])
print(siswa.get("hobi", "-"))

for k, v in siswa.items():
    print(f"{k}: {v}")