# perulangan for + range
print("> for + range")
for i in range(1, 4):
    print(f"putaran ke-{i}")

buah = ["apel", "jeruk", "mangga"]
for b in buah:
    print(b.upper())

print()

# perulangan while
print("> while")
hitung = 3
while hitung > 0:
    print(f"hitung mundur: {hitung}")
    hitung -= 1
print("meluncur!")

print()

# break, continue, pass
print("> break, continue, pass")
for n in range(1, 10):
    if n == 3:
        continue   
    if n == 6:
        break
    print(n)

for i in range(3):
    pass