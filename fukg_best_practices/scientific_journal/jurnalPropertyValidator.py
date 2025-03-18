import csv
import re

def validate_jurnal_csv(csv_file):
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
            
            # Memeriksa kolom namaJurnal
            nama_jurnal = row[0].strip()
            if ',' in nama_jurnal:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama jurnal tidak boleh mengandung koma")
            
            # Memeriksa kolom editor
            editor = row[1].strip()
            if not editor.isupper():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama Editor harus huruf besar semua")
            if '.' in editor:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama Editor tidak boleh mengandung titik")

            # Memeriksa kolom frekuensiTerbit
            frekuensi_terbit = row[2].strip()
            if not frekuensi_terbit.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Frekuensi terbit harus angka")
            
            # Memeriksa kolom issn
            issn = row[3].strip()
            if ',' in issn:
                errors.append(f"Data salah pada baris {line_num}, informasi error: ISSN tidak boleh mengandung koma")
            
            # Memeriksa kolom bidangStudi
            bidang_studi = row[4].strip()
            if ',' in bidang_studi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Bidang studi tidak boleh mengandung koma")
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', bidang_studi):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Bidang studi harus Kapital setiap kata")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_jurnal_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\scientific_journal\jurnal_attribute.csv'
validate_jurnal_csv(csv_path)
