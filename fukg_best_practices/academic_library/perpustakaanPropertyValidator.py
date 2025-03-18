import csv
import re

def validate_perpustakaan_csv(csv_file):
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
            
            # Memeriksa kolom namaPerpustakaan
            nama_perpustakaan = row[0].strip()
            if ',' in nama_perpustakaan:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama perpustakaan tidak boleh mengandung koma")
            
            # Memeriksa kolom lokasiPerpustakaan
            lokasi_perpustakaan = row[1].strip()
            if ',' in lokasi_perpustakaan:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Lokasi perpustakaan tidak boleh mengandung koma")
            
            # Memeriksa kolom jamOperasionalPerpustakaan
            jam_operasional_perpustakaan = row[2].strip()
            if ',' in jam_operasional_perpustakaan:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jam operasional perpustakaan tidak boleh mengandung koma")
            
            # Memeriksa kolom jumlahKoleksiPerpustakaan
            jumlah_koleksi_perpustakaan = row[3].strip()
            if not jumlah_koleksi_perpustakaan.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jumlah koleksi perpustakaan harus berupa angka")
            
            # Memeriksa kolom fasilitasPerpustakaan
            fasilitas_perpustakaan = row[4].strip()
            if ',' in fasilitas_perpustakaan:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Fasilitas perpustakaan tidak boleh mengandung koma")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_perpustakaan_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_library\perpustakaan_attribute.csv'
validate_perpustakaan_csv(csv_path)
