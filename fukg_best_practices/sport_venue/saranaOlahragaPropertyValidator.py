import csv

def validate_sarana_olahraga_csv(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        errors = []
        
        next(csvreader, None)  # Skip header
        
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 5:
                errors.append(f"Jumlah kolom tidak sesuai pada baris {line_num}")
                continue
            
            # Validasi namaFasilitas
            nama_fasilitas = row[0].strip()
            if ',' in nama_fasilitas:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama fasilitas tidak boleh mengandung koma")
            
            # Validasi lokasi
            lokasi = row[1].strip()
            if ',' in lokasi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Lokasi tidak boleh mengandung koma")
            
            # Validasi jenisOlahraga
            jenis_olahraga = row[2].strip()
            if not jenis_olahraga.istitle():  # Memastikan setiap kata diawali kapital
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jenis olahraga harus diawali dengan huruf kapital")
            
            # Validasi jamOperasional (boleh kata, angka atau karakter selain koma)
            jam_operasional = row[3].strip()
            if ',' in jam_operasional:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jam operasional tidak boleh mengandung koma")
            
            # Validasi kapasitas
            kapasitas = row[4].strip()
            if not kapasitas.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Kapasitas harus berupa angka")
        
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Ganti dengan path file CSV sarana olahraga Anda
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\sport_venue\saranaOlahraga_attribute.csv'
validate_sarana_olahraga_csv(csv_path)
