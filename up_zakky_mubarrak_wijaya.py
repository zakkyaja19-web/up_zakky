print("===== kasir kantin =====")
total = 0

while True:
    print("\n---- daftar makanan ----")
    print("1. nasi goreng sultan - 60.000")
    print("2. gorengan - 5.000")
    print("0. selesai memilih makanan")

    pilihan = int(input("mau beli makanan yang mana? (0-2):"))

    if pilihan == 0:
        break
    elif pilihan == 1:
        total = 60000
        nama_makanan = "nasi goreng sultan"
    elif pilihan == 2:
        total = 5000
        nama_makanan = "gorengan"
    else:
        print("pilihan tidak valid, silahkan pilih lagi")
        continue

    jumlah = int(input(f"mau tambahan makanan ini {nama_makanan}:"))
    subtotal = total * jumlah
    total += subtotal
    print(f"subtotal {nama_makanan} ({jumlah}x):,Rp{subtotal:,}")

    if total > 100000:
        diskon_persen = 10
        total_diskon = total * 0.10
    else:
        diskon_persen = 0
        total_diskon = 0
 
total_bayar = total -total_diskon

print("\n=========================")
print("      struk pembayaran     ")
print("==========================")
print(f"total belanja : RP{total:,}")
print(f"diskon : {diskon_persen}%")
print(f"potongan : RP{total_diskon:,}")
print("--------------------------")
print(f"total bayar : RP{total_bayar:,}")
print("==========================")
print("        trima kasih      ")
print("==========================")