class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SistemAntrianBank:
    def __init__(self):
        self.front = None
        self.rear = None

    # 1. Operasi Enqueue (Tambah Antrian)
    def enqueue(self, nama):
        baru = Node(nama)
        if self.rear is None:
            self.front = self.rear = baru
        else:
            self.rear.next = baru
            self.rear = baru
        print(f"--- Nasabah '{nama}' berhasil masuk antrian ---")

    # 2. Operasi Dequeue (Panggil Antrian)
    def dequeue(self):
        if self.front is None:
            print("Peringatan: Antrian sudah kosong!")
            return
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"--- Memanggil Nasabah: {temp.data} ---")
        del temp

    # 3. Operasi Peek (Lihat Urutan Terdepan)
    def peek(self):
        if self.front:
            print(f"Nasabah urutan terdepan saat ini: {self.front.data}")
        else:
            print("Antrian kosong.")

    # 4. Operasi Display (Tampilkan Semua Antrian)
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

# Contoh Penggunaan
bank = SistemAntrianBank()
bank.enqueue("Andi")
bank.enqueue("Budi")
bank.enqueue("Citra")
bank.display()
bank.peek()
bank.dequeue()
bank.display()