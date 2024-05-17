import numpy as np

print("NAMA    : YUNIKA PUTERI DWI ANTIKA")
print("NIM     : 2241760048")
print("KELAS   : SIB2D")
print("NO ABSEN: 28")


# Data kriteria, alternatif, dan evaluasi
kriteria = [
    ('Luas Lahan', 0.133, 'benefit'),
    ('Jarak ke Pusat Kota', 0.053, 'cost'),
    ('Sistem Informasi Pendukung', 0.080, 'benefit'),
    ('Keunggulan Transportasi Umum dibanding Angkutan Pribadi', 0.067, 'benefit'),
    ('Promosi oleh Institusi Umum', 0.027, 'benefit'),
    ('Frekuensi Angkutan Umum di lokasi', 0.093, 'benefit'),
    ('Harga Tempat Parkir', 0.187, 'cost'),
    ('Trafik Angkutan Umum di Lokasi', 0.107, 'cost'),
    ('Lokasi Parkir Gratis di Pusat Kota', 0.040, 'cost'),
    ('Total Biaya Parkir dan Angkutan Umum', 0.160, 'cost'),
]

alternatif = [
    'Lot 51', 'Petak 61', 'Petak 77', 'Area 51', 'Lot 61', 'Petak 57', 'Komplek 51'
]

evaluasi = [
    [4, 3, 7, 6, 8, 6, 4, 4, 5, 4],  # Lot 51
    [2, 4, 4, 8, 5, 6, 5, 2, 3, 3],  # Petak 61
    [4, 3, 7, 9, 7, 4, 5, 3, 4, 3],  # Petak 77
    [4, 5, 8, 8, 8, 3, 5, 4, 3, 3],  # Area 51
    [4, 4, 4, 9, 6, 3, 3, 3, 5, 3],  # Lot 61
    [2, 3, 6, 8, 7, 3, 3, 4, 5, 3],  # Petak 57
    [4, 5, 4, 9, 5, 6, 4, 3, 3, 4]   # Komplek 51
]

# Konversi ke numpy array
evaluasi = np.array(evaluasi)

# Menghitung nilai solusi rata-rata (AV)
AV = evaluasi.mean(axis=0)

# Inisialisasi array untuk PDA dan NDA
PDA = np.zeros_like(evaluasi, dtype=float)
NDA = np.zeros_like(evaluasi, dtype=float)

# Menghitung PDA dan NDA berdasarkan tipe kriteria (benefit/cost)
for j in range(len(kriteria)):
    if kriteria[j][2] == 'benefit':
        PDA[:, j] = np.maximum(0, (evaluasi[:, j] - AV[j]) / AV[j])
        NDA[:, j] = np.maximum(0, (AV[j] - evaluasi[:, j]) / AV[j])
    else:
        PDA[:, j] = np.maximum(0, (AV[j] - evaluasi[:, j]) / AV[j])
        NDA[:, j] = np.maximum(0, (evaluasi[:, j] - AV[j]) / AV[j])

# Menghitung jumlah terbobot PDA dan NDA
bobot = np.array([k[1] for k in kriteria])
SP = PDA @ bobot
SN = NDA @ bobot

# Normalisasi SP dan SN
NSP = SP / SP.max()
NSN = 1 - (SN / SN.max())

# Menghitung nilai skor penilaian (AS)
AS = 0.5 * (NSP + NSN)

# Perankingan
ranking = np.argsort(AS)[::-1]

# Menampilkan hasil nilai solusi rata-rata (AV) dalam bentuk tabel
print("\nNilai Solusi Rata-rata (AV) : ")
print("+--------------------------------------------------------------+---------+")
print("|                      Kriteria                                |   AV    |")
print("+------------------------------------------------------------- +---------+")
for i, nilai in enumerate(AV):
    print(f"| {kriteria[i][0]:<60} | {nilai:<7.4f} |")
print("+--------------------------------------------------------------+---------+")

# Menampilkan PDA dan NDA 
print("\nMenghitung Jarak Positif / Negatif dari Rata-rata (PDA / NDA) : ")
print("+------------------------------------------------------------------------------+------------------------------------------------------------------------------+")
print("|                                  PDA                                         |                                 NDA                                          |")
print("+------------------------------------------------------------------------------+------------------------------------------------------------------------------+")
for i in range(len(kriteria)):
    print("|", end=" ")
    for val in PDA[:, i]:
        print("{:<10.6f}".format(val), end=" ")
    print("|", end=" ")
    for val in NDA[:, i]:
        print("{:<10.6f}".format(val), end=" ")
    print("|")
print("+------------------------------------------------------------------------------+------------------------------------------------------------------------------+")

# Menampilkan hasil SP, SN, NSP, NSN, dan AS dalam bentuk tabel
print("\nMenghitung jumlah terbobot PDA / NDA (SP / SN) : ")
print("+----------------------+----------------------+")
print("|          SP          |           SN         |")
print("+----------------------+----------------------+")
max_len = max(len(max(map(str, SP), key=len)), len(max(map(str, SN), key=len)))
for sp_val, sn_val in zip(SP, SN):
    print(f"| {sp_val:<{max_len}} | {sn_val:<{max_len}} |")
print("+----------------------+----------------------+")


print("\nMenghitung nilai normalisasi SP / SN (NSP / NSN) : ")
print("+----------------------+----------------------+")
print("|         NSP          |          NSN         |")
print("+----------------------+----------------------+")
max_len = max(len(max(map(str, NSP), key=len)), len(max(map(str, NSN), key=len)))
for nsp_val, nsn_val in zip(NSP, NSN):
    print(f"| {nsp_val:<{max_len}} | {nsn_val:<{max_len}} |")
print("+----------------------+----------------------+")


print("\nMenghitung nilai skor penilaian (AS) : ")
print("+---------------------+")
print("|         AS          |")
print("+---------------------+")
max_len = max(len('AS'), len(max(map(str, AS), key=len)))
for val in AS:
    print(f"| {val:<{max_len}} |")
print("+---------------------+")

# Menampilkan hasil perangkingan
print("\nPerangkingan : ")
print("+----------+-----------------+-----------------+")
print("| Rangking |    Alternatif   |     NILAI AS    |")
print("+----------+-----------------+-----------------+")
for i, rank in enumerate(ranking):
    print(f"|    {i+1:<3}   | {alternatif[rank]:<15} | {AS[rank]:<15.8f} |")
print("+----------+-----------------+-----------------+")

