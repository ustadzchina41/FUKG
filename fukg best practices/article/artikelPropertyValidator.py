import csv
import re

def validate_artikel_csv(csv_file):
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
            
            # Memeriksa kolom judulArtikel
            judul_artikel = row[0].strip()
            if ',' in judul_artikel:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Judul artikel tidak boleh mengandung koma")
            
            # Memeriksa kolom penulis
            penulis = row[1].strip()
            if ',' in penulis:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Penulis tidak boleh mengandung koma")
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', penulis):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Penulis harus Kapital setiap kata")
            
            # Memeriksa kolom jurnal
            jurnal = row[2].strip()
            if ',' in jurnal:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jurnal tidak boleh mengandung koma")
            
            # Memeriksa kolom tahunTerbit
            tahun_terbit = row[3].strip()
            if not tahun_terbit.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Tahun terbit harus angka")
            
            # Memeriksa kolom topik
            topik = row[4].strip()
            if ',' in topik:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Topik tidak boleh mengandung koma")
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', topik):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Topik harus Kapital setiap kata")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_artikel_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\article\artikel_attribute.csv'
validate_artikel_csv(csv_path)