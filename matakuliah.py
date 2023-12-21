import sqlite3

# Fungsi untuk membuat tabel matakuliah jika belum ada
def create_table():
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()

    # Membuat tabel matakuliah
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matakuliah (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kode TEXT NOT NULL,
            nama TEXT NOT NULL,
            sks INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

# Fungsi untuk menambahkan matakuliah baru
def tambah_matakuliah(kode, nama, sks):
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()
  
    # Menambahkan matakuliah baru
    # Perintah SQL untuk menambahkan matakuliah baru
    cursor.execute("INSERT INTO matakuliah (kode, nama, sks) VALUES ('MK001', 'Matematika Teknik', '3'), ('MK002', 'Teknologi Komputer', '3'), ('MK003', 'Logika Matematika', '3');")
    
    connection.commit()
    connection.close()
  
# Fungsi untuk menampilkan semua matakuliah
def tampilkan_semua_matakuliah(kode, nama, sks):
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()

    # Menampilkan semua matakuliah
    # Perintah SQL untuk menampilkan matakuliah
    cursor.execute("SELECT * FROM matakuliah;")
    rows = cursor.fetchall()

    for row in rows:
        print(f"{row[1]}, {row[2]}, {row[3]}")

    connection.close()

# Fungsi untuk mengupdate data matakuliah
def update_matakuliah(kode, new_nama, new_sks):
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()

    # Mengupdate data matakuliah berdasarkan kode
    # Perintah SQL untuk updated data matakuliah
    cursor.execute("UPDATE matakuliah SET (nama, sks) = ('Teknologi Komputasi', '4') WHERE (nama, sks) = ('Teknologi Komputer', '3');")    
    
    connection.commit()
    connection.close()

# Fungsi untuk menghapus matakuliah berdasarkan kode
def hapus_matakuliah(kode):
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()

    # Menghapus matakuliah berdasarkan kode
    # Perintah SQL untuk menghapus data matakuliah
    cursor.execute("DELETE FROM matakuliah WHERE kode = 'MK003'")

    connection.commit()
    connection.close()

connection = sqlite3.connect("matakuliah.db")
cursor = connection.cursor()    

kode = "kode"
nama = "nama"
sks = "sks"

# Membuat tabel jika belum ada
create_table()

# Menambahkan beberapa matakuliah
tambah_matakuliah(kode, nama, sks)

# Menampilkan semua matakuliah
print("Daftar Mata Kuliah:")
tampilkan_semua_matakuliah(kode, nama, sks)

# Mengupdate data matakuliah
update_matakuliah(kode, nama, sks)

# Menampilkan semua matakuliah setelah diupdate
print("\nDaftar Mata Kuliah setelah Update:")
tampilkan_semua_matakuliah(kode, nama, sks)

# Menghapus matakuliah berdasarkan kode
hapus_matakuliah(kode)

# Menampilkan semua matakuliah setelah dihapus
print("\nDaftar Mata Kuliah setelah Hapus:")
tampilkan_semua_matakuliah(kode, nama, sks)

