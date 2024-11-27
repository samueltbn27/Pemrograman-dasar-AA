# Data panen
data_panen = { 
    'lokasi1': { 'nama_lokasi': 'Kebun A', 'hasil_panen': { 'padi': 1200, 'jagung': 800, 'kedelai': 500 } }, 
    'lokasi2': { 'nama_lokasi': 'Kebun B', 'hasil_panen': { 'padi': 1500, 'jagung': 900, 'kedelai': 450 } }, 
    'lokasi3': { 'nama_lokasi': 'Kebun C', 'hasil_panen': { 'padi': 1100, 'jagung': 750, 'kedelai': 600 } }, 
    'lokasi4': { 'nama_lokasi': 'Kebun D', 'hasil_panen': { 'padi': 1300, 'jagung': 850, 'kedelai': 550 } }, 
    'lokasi5': { 'nama_lokasi': 'Kebun E', 'hasil_panen': { 'padi': 1400, 'jagung': 950, 'kedelai': 480 } } 
}

# 1. Menampilkan seluruh data panen
print("1. Data Panen:")
for lokasi, detail in data_panen.items():
    print(f"{detail['nama_lokasi']} - Padi: {detail['hasil_panen']['padi']}, Jagung: {detail['hasil_panen']['jagung']}, Kedelai: {detail['hasil_panen']['kedelai']}")

# 2. Hasil panen jagung di lokasi2
print("\n2. Hasil Jagung Lokasi 2:", data_panen['lokasi2']['hasil_panen']['jagung'])

# 3. Nama lokasi dari lokasi3
print("\n3. Nama Lokasi 3:", data_panen['lokasi3']['nama_lokasi'])

# 4. Variabel untuk hasil panen padi dan kedelai
hasil_panen_padi = {lokasi: detail['hasil_panen']['padi'] for lokasi, detail in data_panen.items()}
hasil_panen_kedelai = {lokasi: detail['hasil_panen']['kedelai'] for lokasi, detail in data_panen.items()}

print("\n4. Hasil Panen Padi:", hasil_panen_padi)
print("Hasil Panen Kedelai:", hasil_panen_kedelai)

# 5. Mengecek lokasi yang butuh perhatian
print("\n5. Status Lokasi:")
for lokasi, detail in data_panen.items():
    status = "memerlukan perhatian khusus" if detail['hasil_panen']['padi'] > 1300 or detail['hasil_panen']['jagung'] > 800 else "kondisi baik"
    print(f"{detail['nama_lokasi']} {status}")