# UTS-Struktur-Data

I Made Pasek Bagaskara Sugiana - 2501010014 - Baagaaskaaraa
Henry Ersya Tryas Putra - 2501010237 - HenryErsyaTryasPutra
I Putu Aditya Perdana - 2501010008 - Adyc-f

BAB I

1.1 Rumusan Masalah
Rumusan Masalah:
Bagaimana struktur data Queue dapat memastikan keadilan pelayanan (nasabah yang datang duluan dilayani duluan)?
Mengapa implementasi menggunakan Linked List lebih menguntungkan untuk antrian pelayanan bank yang jumlahnya fluktuatif?
Bagaimana operasi Enqueue dan Dequeue mempermudah petugas dalam mengelola transisi antrian tanpa kesalahan manual?

1.2 Solusi:
Sistem ini menyediakan manajemen antrian digital yang menerapkan prinsip FIFO (First In, First Out). Dengan menggunakan Linked List, sistem tidak akan mengalami kendala overflow (antrian penuh) selama memori komputer masih tersedia. Solusi ini memastikan setiap nasabah memiliki nomor urut yang pasti dan petugas cukup menekan satu tombol (Dequeue) untuk memanggil urutan berikutnya secara akurat.

BAB II

2.1 Landasan Teori

Struktur data merupakan cara sistematis untuk menyimpan dan mengorganisir data agar dapat diakses secara efisien. Menurut Horowitz (2008), pemilihan struktur data yang tepat sangat krusial karena berdampak langsung pada kecepatan pemrosesan data dan penggunaan memori pada aplikasi.

Queue (antrian) adalah struktur data linear di mana penambahan elemen dilakukan di ujung belakang (Rear) dan penghapusan dilakukan di ujung depan (Front). Operasi ini mengikuti prinsip FIFO (First In, First Out), yang berarti data yang pertama kali dimasukkan akan menjadi yang pertama kali dikeluarkan (Sitorus, 2015). Konsep ini adalah representasi paling akurat untuk sistem pelayanan publik.

Dalam implementasinya, Linked List sering dipilih untuk membangun Queue karena sifatnya yang dinamis. Berbeda dengan Array yang membutuhkan alokasi memori statis di awal, Linked List menggunakan node-node yang saling terhubung melalui pointer. Menurut Tenenbaum (2020), penggunaan Linked List menghilangkan kebutuhan untuk menggeser elemen data saat elemen terdepan dihapus, sehingga meningkatkan performa sistem secara signifikan.

BAB III

3.1 Desain Sistem dan Implementasi

Dalam sistem ini digunakan metode Queue (FIFO) untuk mengatur antrian pemesananmakanan. Berikut adalah pseudocode dari sistem yang dibuat:

    1. Bikin cetakan buat Nasabah (Node)
    Struktur Orang:
    nama = ""
    orang_berikutnya = kosong

    2. Siapin sistem antriannya
    SistemAntrian:
    paling_depan = kosong
    paling_belakang = kosong

    Fungsi nambahin orang ke antrian
    Fungsi Tambah(nama_nasabah):
    orang_baru = bikin Orang(nama_nasabah)
    
    kalau paling_belakang == kosong:
      // Kalo masih sepi, dia jadi yang pertama sekaligus terakhir
      paling_depan = orang_baru
      paling_belakang = orang_baru
    kalau nggak:
      // Kalo udah ada yang ngantri, taruh dia di belakangnya orang terakhir
      paling_belakang.orang_berikutnya = orang_baru
      paling_belakang = orang_baru // update posisi terakhir
      
    tampilin "Sip, " + nama_nasabah + " udah masuk antrian."

    Fungsi manggil orang terdepan (Hapus dari antrian)
    Fungsi Panggil():
    kalau paling_depan == kosong:
      tampilin "Antrian lagi sepi nih."
      keluar_dari_fungsi
      
    yang_dipanggil = paling_depan
    paling_depan = paling_depan.orang_berikutnya // Geser maju
    
    // Kalo abis digeser ternyata antriannya jadi abis
    kalau paling_depan == kosong:
      paling_belakang = kosong
      
    tampilin "Panggilan buat: " + yang_dipanggil.nama
    lupain(yang_dipanggil) // hapus dari memori

    Fungsi ngintip siapa yang paling depan
    Fungsi Ngintip():
    kalau paling_depan != kosong:
      tampilin "Yang lagi paling depan: " + paling_depan.nama
    kalau nggak:
      tampilin "Nggak ada orang."

    Fungsi liat seluruh barisan antrian
    Fungsi LiatSemua():
    kalau paling_depan == kosong:
      tampilin "Antrian kosong melompong."
      keluar_dari_fungsi
      
    tampilin "Barisan antrian sekarang:"
    orang_cek = paling_depan
    
    selama orang_cek != kosong:
      tampilin "[" + orang_cek.nama + "] -> "
      orang_cek = orang_cek.orang_berikutnya // geser ngeceknya ke belakang
      
    tampilin "Selesai."

3.2 Alur Sistem (Input → Proses → Output)

Input: Petugas/Mesin memasukkan nama atau nomor 
identitas nasabah ke sistem. 

Proses: 
Enqueue: Menambahkan node baru berisi data nasabah 
ke posisi Rear. 

Dequeue: Menghapus node di posisi Front (nasabah 
selesai dilayani). 

Peek: Melihat nama nasabah yang berada di urutan 
paling depan. 

Output: Menampilkan daftar seluruh nasabah yang 
masih berada dalam antrian. 

3.3 Sistem Antrian Bank (queue - FIFO)

    # Definisi Node untuk Linked List
    class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan nama nasabah
        self.next = None  # Pointer ke nasabah selanjutnya

    # Kelas utama untuk manajemen Queue
    class SistemAntrianBank:
    def __init__(self):
        self.front = None # Penanda nasabah terdepan
        self.rear = None  # Penanda nasabah terakhir

    # 1. Operasi Enqueue (Menambah Antrian)
    def enqueue(self, nama):
        baru = Node(nama)
        if self.rear is None:
            self.front = self.rear = baru
        else:
            self.rear.next = baru
            self.rear = baru
        print(f"--- Nasabah '{nama}' berhasil masuk antrian ---")

    # 2. Operasi Dequeue (Memanggil/Menghapus Antrian Terdepan)
    def dequeue(self):
        if self.front is None:
            print("Peringatan: Antrian sudah kosong!")
            return
        temp = self.front
        self.front = self.front.next
        # Jika setelah dihapus antrian jadi kosong
        if self.front is None:
            self.rear = None
        print(f"--- Memanggil Nasabah: {temp.data} ---")
        del temp

    # 3. Operasi Peek (Melihat Nasabah Terdepan Tanpa Menghapus)
    def peek(self):
        if self.front:
            print(f"Nasabah urutan terdepan saat ini: {self.front.data}")
        else:
            print("Antrian kosong.")

    # 4. Operasi Display (Menampilkan Seluruh Isi Antrian)
    def display(self):
        if self.front is None:
            print("Antrian Kosong.")
            return
        print("\n=== DAFTAR ANTRIAN SAAT INI ===")
        sekarang = self.front
        while sekarang:
            print(f"[{sekarang.data}]", end=" -> ")
            sekarang = sekarang.next
        print("Selesai\n")

    # --- Contoh Eksekusi Program ---
    bank = SistemAntrianBank()
    bank.enqueue("Andi")
    bank.enqueue("Budi")
    bank.enqueue("Citra")
    bank.display() # Menampilkan: Andi -> Budi -> Citra
    bank.peek()    # Menampilkan: Andi
    bank.dequeue() # Andi dipanggil
    bank.display() # Menampilkan: Budi -> Citra

BAB IV

4.1 Kesimpulan

Berdasarkan hasil rancangan dan implementasi sistem 
antrian pelayanan ini, dapat disimpulkan bahwa: 
Rumusan Masalah Terjawab: Sistem berhasil 
menerapkan prinsip keadilan pelayanan melalui konsep 
FIFO, di mana nasabah Andi yang datang pertama tetap 
menjadi yang pertama dilayani. 
Sesuai Teori: Implementasi Queue menggunakan 
Linked List terbukti sangat efektif karena sistem dapat 
terus bertambah sesuai jumlah nasabah tanpa dibatasi 
ukuran array di awal. 
Manfaat Kasus: Sistem ini meminimalkan risiko 
"penyerobotan" antrian dan memberikan kemudahan 
bagi manajemen bank untuk memantau beban kerja 
teller secara real-time. 
