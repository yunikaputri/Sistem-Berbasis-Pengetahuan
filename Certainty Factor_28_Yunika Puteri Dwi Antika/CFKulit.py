# SISTEM PAKAR DIAGNOSA JENIS KULIT WAJAH
print("NAMA    : YUNIKA PUTERI DWI ANTIKA")
print("NIM     : 2241760048")
print("KELAS   : SIB2D")
print("NO ABSEN: 28")


rule_penyakit = {
    'P01': ['G01', 'G02', 'G03', 'G04', 'G05', 'G06', 'G11'],
    'P02': ['G07', 'G08', 'G09', 'G16'],
    'P03': ['G01', 'G05', 'G10', 'G11', 'G12'],
    'P04': ['G07', 'G14', 'G15', 'G16', 'G17'],
    'P05': ['G12', 'G18', 'G19', 'G20']
}

data_nilai_pakar = {
    ('P01', 'G01'): 0.8,
    ('P01', 'G02'): 0.8,
    ('P01', 'G03'): 0.8,
    ('P01', 'G04'): 0.8,
    ('P01', 'G05'): 0.8,
    ('P01', 'G06'): 0.8,
    ('P01', 'G11'): 0.8,
    ('P02', 'G07'): 0.8,
    ('P02', 'G08'): 0.8,
    ('P02', 'G09'): 0.8,
    ('P02', 'G16'): 0.8,
    ('P03', 'G01'): 0.6,
    ('P03', 'G05'): 0.6,
    ('P03', 'G10'): 0.8,
    ('P03', 'G11'): 0.6,
    ('P03', 'G12'): 0.6,
    ('P04', 'G07'): 0.6,
    ('P04', 'G14'): 0.4,
    ('P04', 'G15'): 0.6,
    ('P04', 'G16'): 0.4,
    ('P04', 'G17'): 0.6,
    ('P05', 'G12'): 0.8,
    ('P05', 'G18'): 0.8,
    ('P05', 'G19'): 0.8,
    ('P05', 'G20'): 0.8,
}

data_gejala = {
    'G01': 'Tidak berminyak',
    'G02': 'Segar dan halus',
    'G03': 'Bahan-bahan kosmetik mudah menempel di kulit',
    'G04': 'Terlihat sehat',
    'G05': 'Tidak berjerawat',
    'G06': 'Mudah dalam memilih kosmetik',
    'G07': 'Pori-pori kulit besar terutama di area hidung, pipi, dagu',
    'G08': 'Kulit di bagian wajah terlihat mengkilat',
    'G09': 'Sering ditumbuhi jerawat',
    'G10': 'Kulit kelihatan kering sekali',
    'G11': 'Pori-pori halus',
    'G12': 'Tekstur kulit wajah tipis',
    'G13': 'Cepat menampakkan kerutan-kerutan',
    'G14': 'Sebagian kulit kelihatan berminyak',
    'G15': 'Sebagian kulit kelihatan kering',
    'G16': 'Kadang berjerawat',
    'G17': 'Susah mendapat hasil polesan kosmetik yang sempurna',
    'G18': 'Mudah alergi',
    'G19': 'Mudah iritasi dan terluka',
    'G20': 'Kulit mudah terlihat kemerahan'
}

data_penyakit = {
    'P01': 'Kulit Normal',
    'P02': 'Kulit Beminyak',
    'P03': 'Kulit Kering',
    'P04': 'Kulit Kombinasi',
    'P05': 'Kulit Sensitif'
}

# Fungsi untuk menghitung CF kombinasi
def hitung_cf_kombinasi(nilai_user, nilai_pakar):
    return nilai_user * nilai_pakar

# Fungsi untuk menghitung CF gabungan
def hitung_cf_gabungan(cf1, cf2):
    return cf1 + cf2 - (cf1 * cf2)

# Menampilkan keterangan gejala
print("\nKeterangan Gejala:")
for kode_gejala, nama_gejala in data_gejala.items():
    print(f"{kode_gejala}: {nama_gejala}")
print()

# Menampilkan keterangan penyakit
print("Keterangan Penyakit:")
for kode_penyakit, nama_penyakit in data_penyakit.items():
    print(f"{kode_penyakit}: {nama_penyakit}")
print()


# Input gejala dari pengguna
gejala_input = []
while True:
    kode_gejala = input("Masukkan kode gejala yang Anda alami (atau tekan Enter untuk selesai): ")
    if kode_gejala == "":
        break
    nilai_gejala = float(input(f"Masukkan nilai untuk gejala {data_gejala.get(kode_gejala, 'tidak valid')} (0-1): "))
    gejala_input.append((kode_gejala, nilai_gejala))

# Output
for penyakit, gejala_list in rule_penyakit.items():
    for gejala, nilai_user in gejala_input:
        if gejala in gejala_list:
            nilai_pakar = data_nilai_pakar.get((penyakit, gejala), 0)
            cf_kombinasi = hitung_cf_kombinasi(nilai_user, nilai_pakar)
            print(f"Kode Penyakit: {penyakit}, Kode Gejala: {gejala}, CF Kombinasi: {cf_kombinasi}")
    if all(data_nilai_pakar.get((penyakit, gejala), 0) == 0 for gejala, _ in gejala_input):
        print(f"Kode Penyakit: {penyakit}, CF Kombinasi: 0")

# Menampilkan hasil kesimpulan
print("\nBeberapa Tipe Kulit yang mungkin Anda miliki:")
for penyakit in rule_penyakit:
    cf_gabungan = 0
    count = 0
    for gejala, nilai_user in gejala_input:
        if gejala in rule_penyakit[penyakit]:
            nilai_pakar = data_nilai_pakar.get((penyakit, gejala), 0)
            cf_kombinasi = hitung_cf_kombinasi(nilai_user, nilai_pakar)
            if cf_gabungan == 0:
                cf_gabungan = cf_kombinasi
            else:
                cf_gabungan = hitung_cf_gabungan(cf_gabungan, cf_kombinasi)
            count += 1
    if count > 0:
        print(f"- {data_penyakit[penyakit]} ({penyakit}): {cf_gabungan * 100}%")
