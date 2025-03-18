import csv
import re

def validate_penelitian_csv(csv_file):
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
            
            # Memeriksa kolom judulPenelitian
            # Memeriksa kolom judulPenelitian
            judul_penelitian = row[0].strip()
            if ',' in judul_penelitian:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Judul penelitian tidak boleh mengandung koma")
            
            # Memeriksa kolom penelitiUtama
            peneliti_utama = row[1].strip()
            if not peneliti_utama.isupper():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama peneliti utama harus huruf besar semua")
            if '.' in peneliti_utama:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama peneliti utama tidak boleh mengandung titik")

            
            # Memeriksa kolom bidangStudi
            bidang_studi = row[2].strip()
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', bidang_studi):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Bidang studi harus Kapital setiap kata")
            
            # Memeriksa kolom tahunPenelitian
            tahun_penelitian = row[3].strip()
            if not tahun_penelitian.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Tahun penelitian harus angka")
            
            # Memeriksa kolom hasilPenelitian
            hasil_penelitian = row[4].strip()
            if ',' in hasil_penelitian:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Hasil penelitian tidak boleh mengandung koma")
            if len(hasil_penelitian.split()) > 40:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Hasil penelitian harus maksimal 40 kata")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_penelitian_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\research\penelitian_attribute.csv'
validate_penelitian_csv(csv_path)
