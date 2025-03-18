import csv
import re

def validate_publikasi_csv(csv_file):
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
            
            # Memeriksa kolom judulPublikasi
            judul_publikasi = row[0].strip()
            if ',' in judul_publikasi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Judul publikasi tidak boleh mengandung koma")
            
            # Memeriksa kolom penulis
            penulis = row[1].strip()
            if not penulis.isupper():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama penulis harus huruf besar semua")
            if '.' in penulis:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama penulis tidak boleh mengandung titik")

            # Memeriksa kolom tahunTerbit
            tahun_terbit = row[2].strip()
            if not tahun_terbit.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Tahun terbit harus angka")
            
            # Memeriksa kolom jenisPublikasi
            jenis_publikasi = row[3].strip()
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', jenis_publikasi):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jenis publikasi harus Kapital setiap kata")
            
            # Memeriksa kolom topik
            topik = row[4].strip()
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', topik):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Topik harus Kapital setiap kata")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_penelitian_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\publication\publikasi_attribute.csv'
validate_publikasi_csv(csv_path)
