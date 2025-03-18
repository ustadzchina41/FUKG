import csv
import re

def validate_organisasi_mahasiswa_csv(csv_file):
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
            
            # Memeriksa kolom namaOrganisasi
            nama_organisasi = row[0].strip()
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', nama_organisasi):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama organisasi harus Kapital setiap kata")
            
            # Memeriksa kolom ketua
            ketua = row[1].strip()
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', ketua):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama ketua harus Kapital setiap kata, tanpa gelar")
            
            # Memeriksa kolom jumlahAnggota
            jumlah_anggota = row[2].strip()
            if not jumlah_anggota.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jumlah anggota harus angka")
            
            # Memeriksa kolom bidangKegiatan
            bidang_kegiatan = row[3].strip()
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', bidang_kegiatan):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Bidang kegiatan harus Kapital setiap kata")
            
            # Memeriksa kolom tahunBerdiri
            tahun_berdiri = row[4].strip()
            if not tahun_berdiri.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Tahun berdiri harus angka")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_organisasi_mahasiswa_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\student_organization\organisasiMahasiswa_Attribute.csv'
validate_organisasi_mahasiswa_csv(csv_path)
