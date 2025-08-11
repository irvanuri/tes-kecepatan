import speedtest
import time
import csv
from datetime import datetime
import os

CSV_FILE = "hasil_speedtest.csv"

def simpan_hasil(timestamp, ping, download, upload):
    file_exists = os.path.isfile(CSV_FILE)
    
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Waktu", "Ping (ms)", "Download (Mbps)", "Upload (Mbps)"])
        writer.writerow([timestamp, f"{ping:.2f}", f"{download:.2f}", f"{upload:.2f}"])

def test_speed():
    print("Mengukur kecepatan internet...\n")
    st = speedtest.Speedtest()

    try:
        # Cari server terbaik
        print("Mencari server terbaik...")
        st.get_best_server()
        
        # Tes download
        print("Mengukur kecepatan download...")
        download_speed = st.download() / 1_000_000  # Mbps
        
        # Tes upload
        print("Mengukur kecepatan upload...")
        upload_speed = st.upload() / 1_000_000  # Mbps
        
        # Tes ping
        ping_result = st.results.ping

        # Tampilkan hasil
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n=== Hasil Speed Test ===")
        print(f"Waktu   : {timestamp}")
        print(f"Ping    : {ping_result:.2f} ms")
        print(f"Download: {download_speed:.2f} Mbps")
        print(f"Upload  : {upload_speed:.2f} Mbps")

        # Simpan ke CSV
        simpan_hasil(timestamp, ping_result, download_speed, upload_speed)
        print(f"Hasil tes tersimpan di '{CSV_FILE}'\n")
    
    except speedtest.ConfigRetrievalError:
        print("Gagal mengambil konfigurasi speedtest. Pastikan koneksi internet aktif.")
    except speedtest.NoMatchedServers:
        print("Tidak ada server speedtest yang cocok ditemukan.")
    except speedtest.ShareResultsConnectFailure:
        print("Gagal membagikan hasil speedtest.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def main():
    while True:
        test_speed()
        repeat = input("Ulangi pengujian? (y/n): ").strip().lower()
        while repeat not in ("y", "n"):
            repeat = input("Masukkan hanya 'y' atau 'n': ").strip().lower()
        if repeat == 'n':
            print("Terima kasih telah menggunakan pengukur kecepatan internet!")
            break
        print("\nMengulangi pengujian...\n")
        time.sleep(2)

if __name__ == "__main__":
    main()
