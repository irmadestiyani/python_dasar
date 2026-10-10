# function dasar
print("> function dasar")
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

hasil = hitung_luas(5, 3)
print(hasil)
print(hitung_luas(10, 2))

print()

# parameter default
print("> parameter default")
def sapa(nama, salam="halo"):
    return f"{salam}, {nama}!"

print(sapa("ani"))
print(sapa(salam="hai", nama="budi"))

# argumen
def total(*angka):
    return sum(angka)

print(total(1, 2, 3, 4))

print()

# lambda: function anonim satu baris
print("> lambda")
kuadrat = lambda x: x ** 2
print(kuadrat(4))

siswa = [("ani", 80), ("budi", 95)]
print(max(siswa, key=lambda s: s[1]))

print()

# scope variabel
print("> scope")
x = "global"

def tes():
    x = "lokal"
    print(x)

tes()
print(x)