import csv
import re
from datetime import datetime

def validate_workshop_csv(csv_file):
    # Membuka file CSV
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # List untuk menyimpan pesan kesalahan
        errors = []
        
        # Lewati baris pertama (judul kolom)
        next(csvreader, None)
        
        # Iterasi setiap baris data dalam CSV mulai dari baris kedua
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 5:
                errors.append(f"Jumlah kolom tidak sesuai pada baris {line_num}")
                continue
            
            # Memeriksa kolom judulWorkshop
            judul_workshop = row[0].strip()
            if ',' in judul_workshop:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Judul workshop tidak boleh mengandung koma")
            
            # Memeriksa kolom pembicara
            pembicara = row[1].strip()
            if ',' in pembicara:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama pembicara tidak boleh mengandung koma")
            
            # Memeriksa kolom tanggal
            tanggal = row[2].strip()
            try:
                datetime.strptime(tanggal, '%d %B %Y')
            except ValueError:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Format tanggal harus DD MMMM YYYY (contoh: 20 Agustus 2023)")
            
            # Memeriksa kolom lokasi
            lokasi = row[3].strip()
            if ',' in lokasi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Lokasi tidak boleh mengandung koma")
            
            # Memeriksa kolom fokus
            fokus = row[4].strip()
            if ',' in fokus:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Fokus tidak boleh mengandung koma")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_workshop_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_workshop\workshop_attribute.csv'
validate_workshop_csv(csv_path)