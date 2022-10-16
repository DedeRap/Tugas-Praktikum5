# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:26:45 2022

@author: ASUS
"""
print("===== Harga Tiket =====")

ul = 1
h = 0

while(ul == 1):
    
    Um = int(input('Masukkan umur(Tekan -1 untuk berhenti) = '))
    
    if (Um <= 2 and Um >= 0):
        n = 0.00
        print("Gratis")
    elif (Um >= 3 and Um <= 12):
        n = 14.00
        print("Harga $14 dollar")
    elif (Um >= 65):
        n = 18.00
        print("Harga $18 dollar")
    elif (Um >= 13 and Um <= 64):
        n = 23.00
        print("Harga $23 dollar")
    else :
        ul = 0
        n = 0.00
        
    h = h + n
    print("Total = $",h)
    
b = int(input("Masukkan jumlah uang = $"))

if (b >= h):
    t = b - h
    print("Kembalian anda = $", t)
else :
    i = 1
    t = h - b
    print("Maaf, anda kekurangan = $",t)
    
    while (i == 1):
        c = int(input("\nMasukkan uang anda dengan jumlah yang benar = $"))
        b = b + c
        
        if (b == h):
            print("Uang anda sudah cukup")
            i = 0
        elif (b >= h):
            t = b - h
            print("Kembalian anda = $", t)
            i = 0
        else :
            print("Uang anda masih kurang.")
            print("Mohon memasukkan uang yang sesuai dengan harga total")
            
print("\nTerima kasih atas pembayarannya.")
print("Saya atas nama Radea Aji Prasojo denga NIM 064002200016.")