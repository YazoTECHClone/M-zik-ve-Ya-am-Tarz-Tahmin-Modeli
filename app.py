import streamlit as st
import random
import time

# Sayfa ayarları
st.set_page_config(page_title="Sanal Mining", layout="centered", page_icon="💻")
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: #00ff00;
    }
    .stButton > button {
        color: black;
        background-color: #00ff00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Başlangıç durumları
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "main_menu" not in st.session_state:
    st.session_state.main_menu = False
if "puan" not in st.session_state:
    st.session_state.puan = 0
if "loglar" not in st.session_state:
    st.session_state.loglar = []
if "auto_mining" not in st.session_state:
    st.session_state.auto_mining = False

# Giriş ekranı
if not st.session_state.authenticated:
    st.title("🔐 Giriş Ekranı")
    username = st.text_input("Kullanıcı Adı")
    password = st.text_input("Şifre", type="password")
    if st.button("Giriş Yap"):
        if username == "root" and password == "1234":
            st.session_state.authenticated = True
            st.session_state.main_menu = True
            st.rerun()
        else:
            st.error("❌ Hatalı giriş.")
    st.stop()

# Ana Menü
if st.session_state.main_menu:
    st.title("📡 Ana Menü")
    st.markdown("### Seçenekler:")
    if st.button("🔓 IP Sız"):
        st.session_state.main_menu = False
        st.rerun()
    if st.button("🚪 Çıkış"):
        st.session_state.authenticated = False
        st.session_state.main_menu = False
        st.session_state.puan = 0
        st.session_state.loglar = []
        st.rerun()
    st.stop()

# IP üretici
def generate_fake_ip():
    return f"{random.randint(10, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

# Kazma fonksiyonu
def mine_ip():
    fake_ip = generate_fake_ip()
    st.session_state.puan += 1
    st.session_state.loglar.insert(0, f"[+] IP kazıldı: {fake_ip} | Puan: {st.session_state.puan}")

# Oyun başlığı
st.title("💰 IP Mining Paneli")

# Elle kaz
if st.button("💎 Elle Kaz (Tıkla Kaz)"):
    mine_ip()

# Otomatik kazıcı kontrol
col1, col2 = st.columns(2)
with col1:
    if st.button("⛏️ Auto Kazmaya Başla"):
        st.session_state.auto_mining = True
with col2:
    if st.button("🛑 Durdur"):
        st.session_state.auto_mining = False

# Auto mining çalışıyorsa...
if st.session_state.auto_mining:
    mine_ip()
    time.sleep(0.5)
    st.rerun()

# Loglar
st.markdown("## 📜 Kazım Logları")
for log in st.session_state.loglar[:10]:  # son 10 log
    st.code(log)

# Puan
st.markdown(f"### 🧮 Toplam Puan: `{st.session_state.puan}`")

# Ana menüye dön
if st.button("⬅️ Ana Menü"):
    st.session_state.main_menu = True
    st.rerun()
