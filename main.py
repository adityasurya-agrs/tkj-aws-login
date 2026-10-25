import random

angka_tersembunyi = random.randint(1, 25)
kesempatan_ke = 0



while True:
    tebakan = int(input("Tebak angka: "))
    kesempatan_ke += 1

    if tebakan < angka_tersembunyi:
        print("Terlalu kecil")
    elif tebakan > angka_tersembunyi:
        print("Terlalu besar")
    else:
        print(f"Benar! Jawabannya {angka_tersembunyi}")
        print(f"Jumlah percobaan: {kesempatan_ke}")
        break
