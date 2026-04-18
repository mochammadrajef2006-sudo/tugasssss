def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(b, end=" ")
        a, b = b, a + b
    print()

def perkalian(m, n):
    hasil = 0
    for i in range(n):
        hasil += m
    return hasil

# Program Utama
while True:
    print("Nim Genap")
    print("Menu pilihan")
    print("1. Barisan Fibonacci")
    print("2. M Kali N")
    print("0. Keluar")
    
    pilih = int(input("Pilih Menu : "))

    if pilih == 1:
        n = int(input("Masukkan jumlah N : "))
        fibonacci(n)

    elif pilih == 2:
        m = int(input("Masukkan nilai M : "))
        n = int(input("Masukkan nilai N : "))
        print("Hasil :", perkalian(m, n))

    elif pilih == 0:
        print("Program selesai")
        break

    else:
        print("Pilihan tidak tersedia")