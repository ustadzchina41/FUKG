import csv
from datetime import datetime

def validate_ekstrakurikuler_csv(csv_file):
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
            
            # Memeriksa kolom namaKegiatanEkstrakurikuler
            nama_kegiatan = row[0].strip()
            if ',' in nama_kegiatan:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama kegiatan ekstrakurikuler tidak boleh mengandung koma")
            
            # Memeriksa kolom organisasiPenyelenggara
            penyelenggara = row[1].strip()
            if ',' in penyelenggara:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Organisasi penyelenggara tidak boleh mengandung koma")
            if not penyelenggara.istitle():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Organisasi penyelenggara harus diawali dengan huruf kapital")
            
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
            
            # Memeriksa kolom deskripsi
            deskripsi = row[4].strip()
            if ',' in deskripsi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Deskripsi tidak boleh mengandung koma")
            if len(deskripsi.split()) > 40:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Deskripsi maksimal 40 kata")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_ekstrakurikuler_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\extracurricular_activity\kegiatanEkstrakurikuler_attribute.csv'
validate_ekstrakurikuler_csv(csv_path)
