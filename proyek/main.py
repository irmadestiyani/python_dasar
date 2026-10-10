print("> modul py")
import math
from random import randint
import datetime as dt

print(math.sqrt(16))
print(math.pi)
print(randint(1, 6))
print(dt.date.today().year)

print()

print("> sendiri")
from utils.hitung import rata_rata

nilai = [80, 90, 70]
print(rata_rata(nilai))

from utils.teks import kapital
print(kapital("python"))