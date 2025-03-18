import csv
import re

def validate_ruang_kelas_csv(csv_file):
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
            
            # Memeriksa kolom nomorRuangan
            nomor_ruangan = row[0].strip()
            if ',' in nomor_ruangan:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nomor ruangan tidak boleh mengandung koma")
            
            # Memeriksa kolom gedung
            gedung = row[1].strip()
            if ',' in gedung:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Gedung tidak boleh mengandung koma")
            
            # Memeriksa kolom kapasitas
            kapasitas = row[2].strip()
            if not kapasitas.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Kapasitas harus berupa angka")
            
            # Memeriksa kolom fasilitas
            fasilitas = row[3].strip()
            if ',' in fasilitas:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Fasilitas tidak boleh mengandung koma")
            
            # Memeriksa kolom jadwalPenggunaan
            jadwal_penggunaan = row[4].strip()
            if ',' in jadwal_penggunaan:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jadwal penggunaan tidak boleh mengandung koma")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_laboratorium_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\classroom\ruanganKelas_attribute.csv'
validate_ruang_kelas_csv(csv_path)
