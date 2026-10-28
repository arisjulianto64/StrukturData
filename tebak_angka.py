rahasia = random.randint(1, 5)
tebakan = int(input("Tebak angka 1-5: "))

if tebakan == rahasia:
    print("Benar!")
else:
    print("Salah! Angkanya:", rahasia)