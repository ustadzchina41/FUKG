import csv
from datetime import datetime

def validate_upacara_wisuda_csv(csv_file):
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
            
            # Memeriksa kolom tanggalWisuda
            tanggal_wisuda = row[0].strip()
            try:
                datetime.strptime(tanggal_wisuda, '%d %B %Y')
            except ValueError:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Format tanggal harus DD MMMM YYYY (contoh: 20 Agustus 2023)")
            
            # Memeriksa kolom lokasi
            lokasi = row[1].strip()
            if ',' in lokasi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Lokasi tidak boleh mengandung koma")
            
            # Memeriksa kolom jumlahWisudawan
            jumlah_wisudawan = row[2].strip()
            if not jumlah_wisudawan.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jumlah wisudawan harus berupa angka")
            
            # Memeriksa kolom pembicara
            pembicara = row[3].strip()
            if ',' in pembicara:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Pembicara tidak boleh mengandung koma")
            if not pembicara.istitle():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Pembicara harus diawali dengan huruf kapital")
            
            # Memeriksa kolom agenda
            agenda = row[4].strip()
            if ',' in agenda:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Agenda tidak boleh mengandung koma")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_upacara_wisuda_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\graduation_ceremony\upacaraWisuda_attribute.csv'
validate_upacara_wisuda_csv(csv_path)
