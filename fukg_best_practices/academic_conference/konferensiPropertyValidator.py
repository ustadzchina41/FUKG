import csv
import re
from datetime import datetime

def validate_conference_csv(csv_file):
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
            
            # Memeriksa kolom namaKonferensi
            nama_konferensi = row[0].strip()
            if ',' in nama_konferensi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama konferensi tidak boleh mengandung koma")
            
            # Memeriksa kolom tanggal
            tanggal = row[1].strip()
            try:
                datetime.strptime(tanggal, '%d %B %Y')
            except ValueError:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Format tanggal harus DD MMMM YYYY (contoh: 20 April 2024)")
            
            # Memeriksa kolom lokasi
            lokasi = row[2].strip()
            if ',' in lokasi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Lokasi tidak boleh mengandung koma")
            
            # Memeriksa kolom jumlahPeserta
            jumlah_peserta = row[3].strip()
            if not jumlah_peserta.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jumlah peserta harus berupa angka")
            
            # Memeriksa kolom topik
            topik = row[4].strip()
            if ',' in topik:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Topik tidak boleh mengandung koma")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_conference_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_conference\konferensi_attribute.csv'
validate_conference_csv(csv_path)
