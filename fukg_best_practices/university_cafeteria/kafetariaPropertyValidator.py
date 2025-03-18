import csv

def validate_kafetaria_csv(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        errors = []
        
        next(csvreader, None)  # Skip header
        
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 5:
                errors.append(f"Jumlah kolom tidak sesuai pada baris {line_num}")
                continue
            
            # Validasi namaKafetaria
            nama_kafetaria = row[0].strip()
            if ',' in nama_kafetaria:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama kafetaria tidak boleh mengandung koma")
            
            # Validasi lokasi
            lokasi = row[1].strip()
            if ',' in lokasi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Lokasi tidak boleh mengandung koma")
            
            # Validasi jamOperasional
            jam_operasional = row[2].strip()
            if ',' in jam_operasional:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jam operasional tidak boleh mengandung koma")
            
            # Validasi menu
            menu = row[3].strip()
            if ',' in menu:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Menu tidak boleh mengandung koma")
            
            # Validasi kapasitas
            kapasitas = row[4].strip()
            if not kapasitas.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Kapasitas harus berupa angka")
        
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Ganti dengan path file CSV kafetaria Anda
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_cafeteria\kafetaria_attribute.csv'
validate_kafetaria_csv(csv_path)
