import csv
import re

def validate_laboratorium_csv(csv_file):
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
            
            # Memeriksa kolom namaLaboratorium
            nama_laboratorium = row[0].strip()
            if ',' in nama_laboratorium:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama laboratorium tidak boleh mengandung koma")
            
            # Memeriksa kolom lokasi
            lokasi = row[1].strip()
            if ',' in lokasi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Lokasi tidak boleh mengandung koma")
            
            # Memeriksa kolom kepalaLaboratorium
             # Memeriksa kolom kepalaLaboratorium
            kepala_laboratorium = row[2].strip()
            if not kepala_laboratorium.isupper():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama kepala laboratorium harus huruf besar semua")
            if '.' in kepala_laboratorium:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama kepala laboratorium tidak boleh mengandung titik")

            # Memeriksa kolom fasilitas
            fasilitas = row[3].strip()
            if ',' in fasilitas:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Fasilitas tidak boleh mengandung koma")
            
            # Memeriksa kolom bidangPenelitian
            bidang_penelitian = row[4].strip()
            if ',' in bidang_penelitian:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Bidang penelitian tidak boleh mengandung koma")
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', bidang_penelitian):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Bidang penelitian harus Kapital setiap kata")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_laboratorium_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_laboratory\laboratorium_attribute.csv'
validate_laboratorium_csv(csv_path)
