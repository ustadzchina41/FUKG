import csv

def validate_klinik_csv(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        errors = []
        
        next(csvreader, None)  # Skip header
        
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 5:
                errors.append(f"Jumlah kolom tidak sesuai pada baris {line_num}")
                continue
            
            # Validasi namaKlinik
            nama_klinik = row[0].strip()
            if ',' in nama_klinik:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama klinik tidak boleh mengandung koma")
            
            # Validasi lokasi
            lokasi = row[1].strip()
            if ',' in lokasi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Lokasi tidak boleh mengandung koma")
            
            # Validasi jamOperasional
            jam_operasional = row[2].strip()
            if ',' in jam_operasional:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jam operasional tidak boleh mengandung koma")
            
            # Validasi layanan
            layanan = row[3].strip()
            if ',' in layanan:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Layanan tidak boleh mengandung koma")
            
            # Validasi stafMedis
            staf_medis = row[4].strip()
            if ',' in staf_medis:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Staf medis tidak boleh mengandung koma")
        
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Ganti dengan path file CSV klinik Anda
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\medical_facility\klinikKampus_attribute.csv'
validate_klinik_csv(csv_path)
