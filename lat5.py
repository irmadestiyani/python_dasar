# percabangan: if - else
nilai = 80

if nilai >= 75:
    print("selamat, kamu lulus!")
else:
    print("ayo remedial dulu")

print("program selesai")

print()

# percabangan: if - elif - else
nilai = 78

if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 55:
    grade = "C"
else:
    grade = "D"

print(f"nilai {nilai} -> grade {grade}")

print()

# nested if (if di dalam if)
umur, ktp = 20, True
if umur >= 17:
    if ktp:
        print("boleh memilih")
    else:
        print("buat ktp dulu")

print()

# ternary (if dalam satu baris)
umur = 16
s = "dewasa" if umur >= 17 else "anak"
print(s)

print()

# match-case (python 3.10+)
hari = "sabtu"

match hari:
    case "sabtu" | "minggu":
        print("libur!")
    case "senin":
        print("semangat!")
    case _:
        print("hari kerja")