import csv
import re

def validate_universitas_csv(csv_file):
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
            
            # Memeriksa kolom namaUniversitas
            nama_universitas = row[0].strip()
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', nama_universitas):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama universitas harus Kapital setiap kata")
            
            # Memeriksa kolom rektor
            rektor = row[1].strip()
            if not rektor.isupper():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama rektor harus huruf besar semua")
            if '.' in rektor:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama rektor tidak boleh mengandung titik")
          
            # Memeriksa kolom lokasi
            lokasi = row[2].strip()
            # Tidak ada aturan validasi khusus untuk lokasi, asumsi validasi lolos
            
            # Memeriksa kolom tahunBerdiri
            tahun_berdiri = row[3].strip()
            if not tahun_berdiri.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Tahun berdiri harus angka")
            
            # Memeriksa kolom jumlahFakultas
            jumlah_fakultas = row[4].strip()
            if not jumlah_fakultas.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jumlah fakultas harus angka")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_universitas_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'
validate_universitas_csv(csv_path)
