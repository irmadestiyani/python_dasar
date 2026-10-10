# try - except - else - finally
print("> try - except")
try:
    angka = int(input("masukkan angka: "))
    hasil = 100 / angka
except ValueError:
    print("harus berupa angka!")
except ZeroDivisionError:
    print("tidak bisa dibagi nol!")
else:
    print(f"hasil: {hasil}")
finally:
    print("selesai.")

print()

# raise: memunculkan error sendiri
print("> raise")
def set_umur(umur):
    if umur < 0:
        raise ValueError("umur tidak valid")
    return umur

try:
    set_umur(-5)
except ValueError as e:
    print(f"error: {e}")