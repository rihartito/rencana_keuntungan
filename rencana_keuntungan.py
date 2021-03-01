
'''Seorang penjual roti mengeluarkan modal sebesar Rp 1.000.000 untuk menjalankan usahanya. 
Dia mematok harga untuk satu rotinya adalah Rp 6.000 Jika ia merencanakanan 
ingin mendapatkan keuntungan Rp 200.000 dari usaha rotinya tersebut, maka berapa  minimal roti yang harus dibuat agar mendapat keuntungan ?

pendapatan = ingin_raih + pemasukan
jumlah = pendapatan / harga

#inputan :
pemasukan = harga jual,untung ; ingin_raih = keuntungan yang ingin dicapai oleh user 
harga = harga barang
 
#proses :
cari tahu yang mana pemasukan,ingin_raih,harga
mencari keuntungan yang ingin dicapai oleh user

#output :
menampilkan jumlah barang yang ingin dicapai oleh user untuk mendapatkan keuntungan 
'''

def rencana_keuntungan(pemasukan,ingin_raih,harga):
    pendapatan = ingin_raih + pemasukan
    jumlah = pendapatan // harga
    return jumlah

def tampilan():
    print("=====Selamat datang=====")
    print("    semoga membantu  ")
    pemasukan = int(input("masukkan keuntungan : "))
    ingin_raih = int(input("masukkan keuntungan yang ingin diraih : "))
    harga = int(input("masukkan harga : "))
    print("banyak roti yang harus dibuat adalah :",rencana_keuntungan(pemasukan,ingin_raih,harga))

tampilan()