import csv
import re

def validate_asrama_csv(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        errors = []
        
        next(csvreader, None)  # Skip header
        
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 5:
                errors.append(f"Jumlah kolom tidak sesuai pada baris {line_num}")
                continue
            
            # Validasi namaAsrama
            nama_asrama = row[0].strip()
            if ',' in nama_asrama:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama asrama tidak boleh mengandung koma")
            
            # Validasi lokasi
            lokasi = row[1].strip()
            if ',' in lokasi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Lokasi tidak boleh mengandung koma")
            
            # Validasi kapasitas
            kapasitas = row[2].strip()
            if not kapasitas.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Kapasitas harus berupa angka")
            
            # Validasi fasilitas
            fasilitas = row[3].strip()
            if ',' in fasilitas:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Fasilitas tidak boleh mengandung koma")
            
            # Validasi biaya
            biaya = row[4].strip()
            if not re.match(r'^[a-zA-Z]+ [\d.,]+$', biaya):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Biaya harus dimulai dengan kode mata uang dan diikuti dengan angka (contoh: Rp 5.000.000.000)")
        
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")


# Ganti dengan path file CSV asrama Anda
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_dormitory\asrama_attribute.csv'
validate_asrama_csv(csv_path)
