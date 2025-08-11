import streamlit as st
import speedtest

st.set_page_config(page_title="Speed Test Internet", page_icon="🌐", layout="centered")

st.title("🌐 Internet Speed Test")
st.write("Klik tombol di bawah untuk mengetes kecepatan internet kamu.")

if st.button("🚀 Mulai Test Kecepatan"):
    st.write("Sedang melakukan pengujian... mohon tunggu 🙏")
    
    try:
        stt = speedtest.Speedtest()
        stt.get_best_server()
        
        download_speed = stt.download() / 1_000_000   # Mbps
        upload_speed = stt.upload() / 1_000_000       # Mbps
        ping_result = stt.results.ping                # ms
        
        st.success("✅ Tes selesai!")
        st.metric("Ping", f"{ping_result:.1f} ms")
        st.metric("Download", f"{download_speed:.1f} Mbps")
        st.metric("Upload", f"{upload_speed:.1f} Mbps")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

st.write("---")
st.caption("Dibuat dengan Ai tinggal copy-paste wkwk")

