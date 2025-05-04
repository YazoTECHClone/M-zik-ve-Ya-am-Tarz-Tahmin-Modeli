import streamlit as st
import pandas as pd
from joblib import load



# Sayfa başlığı
st.set_page_config(page_title="Müzik ve Yaşam Tarzı Tahmin")
st.title("Müzik Türüne Göre Yaşam Tarzı Tahmini")

# st.markdown("## **Müzik Türüne Göre Yaşam Tarzı ölçme Modeli**")
# st.markdown("Bu site Müzik Türüne Göre Yaşam Tarzı ölçme  ile alakalı tahmin yapmak için tasarlanmıştır. Bunu yapmak için sınıflandırma modeli kullanacağız")

st.markdown("""# **Müzik ve Yaşam Tarzı Tahmin Modeli**

Bu site Müzik ve Yaşam Tarzı Tahmin ile alakalı tahmin yapmak için tasarlanmıştır. Bunu yapmak için sınıflandırma modeli kullanacağız.

### **Ne kullandık:**
- Web: `streamlit`
- Veri Bilimi: `numpy`, `pandas`, `matplotlib` , `seaborn`
- Model Kütüphaneleri: `scikit-learn`, 
""")


# 1. Bölüm: Kullanıcı Bilgileri
st.markdown("### **Kişisel Bilgiler**")
age = st.slider("Yaşınız", 10, 100, 30)
gender = st.radio("Cinsiyetiniz", ["Kadın", "Erkek"])

# 2. Bölüm: Müzik Alışkanlıkları
st.markdown("### **Müzik Alışkanlıklarınız**")
music_genre = st.radio("Hangi müzik türünü tercih edersiniz?", ["Oyun Müzikleri", "Phonk", "Rap", "Hip Hop", "Jazz", "Pop", "Rock"])
music_habit = st.selectbox("Müzik dinleme sıklığınız?", ["Hiçbir zaman", "Bazen", "Sık sık", "Her zaman"])

# 3. Bölüm: Oyun ve Müzik
st.markdown("### **Oyun ve Müzik İlişkisi**")
game_music = st.radio("Oyun oynarken müzik dinler misiniz?", ["Evet", "Hayır"])
game_duration = st.slider("Günlük oyun oynama süreniz (saat)", 0, 20, 4)

# 4. Bölüm: Uyku ve Müzik
st.markdown("### **Uyku ve Müzik Alışkanlıklarınız**")
sleep_music = st.radio("Uyurken müzik dinler misiniz?", ["Evet", "Hayır"])
sleep_duration = st.slider("Günlük uyku süreniz (saat)", 4, 12, 8)

# 5. Bölüm: Sosyal Aktivite ve Teknoloji Kullanımı
st.markdown("### **Sosyal Aktivite ve Teknoloji Kullanımı**")
social_activity = st.radio("Sosyal aktivitelerde yer alır mısınız?", ["Evet", "Hayır"])
tech_use = st.slider("Günlük teknoloji kullanımı (saat)", 0, 12, 3)

# 6. Bölüm: Fiziksel Aktivite
st.markdown("### **Fiziksel Aktivite Durumunuz**")
exercise = st.radio("Fiziksel aktivite yapar mısınız?", ["Evet", "Hayır"])
exercise_type = st.selectbox("Yaptığınız fiziksel aktivite türü", ["Koşu", "Yüzme", "Fitness", "Yoga", "Bisiklet", "Diğer"])



# 7. Bölüm: Sosyal Medya Kullanımı
st.markdown("### **Sosyal Medya Kullanımı**")
social_media = st.radio("Sosyal medya kullanıyor musunuz?", ["Evet", "Hayır"])
social_media_time = st.slider("Günlük sosyal medya kullanımı (saat)", 0, 12, 3)

# 8. Bölüm: Genel Yaşam Tarzı
st.markdown("### **Genel Yaşam Tarzı**")
lifestyle = st.radio("Genel yaşam tarzınızı nasıl tanımlarsınız?", ["Sosyal", "Aktif", "Sakin", "Durgun"])

# 9. Bölüm: Ekstra Bilgiler
st.markdown("### **Ekstra Bilgiler**")
hobby = st.text_input("Hobileriniz nelerdir?", "Müzik, Spor")
tech_interests = st.radio("Teknolojiye ilginiz var mı?", ["Evet", "Hayır"])


# Veri işleme: Kullanıcının verdiği verileri sayısal hale getirme
gender_mapping = {"Kadın": 0, "Erkek": 1}
music_genre_mapping = {"Oyun Müzikleri": 0, "Phonk": 1, "Rap": 2, "Hip Hop": 3, "Jazz": 4, "Pop": 5, "Rock": 6}
music_habit_mapping = {"Hiçbir zaman": 0, "Bazen": 1, "Sık sık": 2, "Her zaman": 3}
yes_no_mapping = {"Evet": 1, "Hayır": 0}
lifestyle_mapping = {"Sosyal": 0, "Aktif": 1, "Sakin": 2, "Durgun": 3}

# Kullanıcı verilerini sayısal forma dönüştürme
user_data = {
    "age": age,
    "gender": gender_mapping[gender],
    "music_genre": music_genre_mapping[music_genre],
    "music_habit": music_habit_mapping[music_habit],
    "game_music": yes_no_mapping[game_music],
    "game_duration": game_duration,
    "sleep_music": yes_no_mapping[sleep_music],
    "sleep_duration": sleep_duration,
    "social_activity": yes_no_mapping[social_activity],
    "tech_use": tech_use,
    "exercise": yes_no_mapping[exercise],
    "exercise_type": exercise_type,
    "social_media": yes_no_mapping[social_media],
    "social_media_time": social_media_time,
    "lifestyle": lifestyle_mapping[lifestyle],
    "hobby": hobby,
    "tech_interests": yes_no_mapping[tech_interests]
}

# Veriyi DataFrame'e dönüştürme
user_df = pd.DataFrame(user_data, index=[0])

# Veriyi DataFrame'e dönüştürme
user_df = pd.DataFrame(user_data, index=[0])

# CSV olarak indirme seçeneği
csv = user_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Tahmin Yapmak İçin Veriyi İndirin Excel",
    data=csv,
    file_name='kullanici_verisi.csv',
    mime='text/csv',
)

# Not: Model yükleme ve tahmin kaldırıldı
# model = load('music_lifestyle_model.pkl')
# prediction = model.predict(user_df)

with st.sidebar:
    st.markdown("## **Repository'miz**:")
    st.markdown("Kaynak kodu ve daha fazla bilgi için Repositroy'mize bakabilirsiniz")
    st.link_button("GitHub", "https://github.com/yazotech142")
    st.markdown("## **Biz Kimiz**")
    st.markdown("Ben Yağız Gülbe Bu Proje İnsanların Müziğe göre hayatı nasıl onu test etmek için yapılmıştır.")