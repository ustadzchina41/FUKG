import csv
import re

def validate_departemen_csv(csv_file):
    # Definisikan path lengkap ke file CSV
    csv_path = csv_file
    
    # Membuka file CSV
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
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
            
            # Memeriksa kolom namaDepartemen
            nama_departemen = row[0].strip()
            if not re.match(r'^Departemen [A-Z][a-z]*(\s[A-Z][a-z]*)*$', nama_departemen):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama departemen harus diawali dengan 'Departemen' dan Kapital setiap kata")
            
            # Memeriksa kolom kepalaDepartemen
            kepala_departemen = row[1].strip()
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', kepala_departemen):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama kepala departemen harus Kapital setiap kata, tanpa gelar")
            
            # Memeriksa kolom lokasi
            lokasi = row[2].strip()
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', lokasi):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Lokasi harus Kapital setiap kata")
            
            # Memeriksa kolom jumlahStaf
            jumlah_staf = row[3].strip()
            if not jumlah_staf.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jumlah staf harus angka")
            
            # Memeriksa kolom bidangStudi
            bidang_studi = row[4].strip()
            if not re.match(r'^([A-Z][a-z]*(\s[A-Z][a-z]*)*)|([a-z]*(\s[a-z]*)*)$', bidang_studi):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Bidang studi harus kapital setiap kata atau kecil semua")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_departemen_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\departemen_attribute.csv'
validate_departemen_csv(csv_path)
