import streamlit as st
import requests
from streamlit_mic_recorder import mic_recorder

# 1. Konfiqurasiya və Premium Dizayn
st.set_page_config(page_title="Mood AI Menu", layout="wide")

st.markdown("""
    <style>
        /* Premium Dark Mode Dizayn */
        .main { background-color: #121212; color: #ffffff; }
        .stApp { background-color: #121212; }
        
        .food-card {
            background: #1e1e1e;
            border-radius: 20px;
            padding: 20px;
            border: 1px solid #333;
            text-align: center;
            transition: transform 0.3s ease;
        }
        .food-card:hover { transform: scale(1.05); border-color: #D4AF37; }
        
        .food-img { border-radius: 15px; width: 100%; height: 200px; object-fit: cover; }
        .food-title { font-size: 1.5em; font-weight: bold; margin-top: 15px; color: #D4AF37; }
        .food-price { font-size: 1.2em; margin: 10px 0; }
        
        div.stButton > button {
            background-color: #D4AF37 !important;
            color: white !important;
            border: none;
            width: 100%;
            border-radius: 10px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Başlıq və Səsli Sifariş Paneli (Sidebar-da)
st.title("🍽️ MOOD AI DINING")
st.markdown("<p style='color:#888'>Sizinlə birlikdə hər zaman - Premium Restoran Sistemi</p>", unsafe_allow_html=True)

with st.sidebar:
    st.header("🎙️ Səsli Sifariş")
    st.write("Mikrofonu basın və sifarişinizi deyin:")
    audio_data = mic_recorder(start_prompt="DANIŞMAĞA BAŞLA", stop_prompt="GÖNDƏR", key="voice_order")
    if audio_data:
        st.write("Sifariş işlənir...")
        files = {"file": ("audio.wav", audio_data['bytes'], "audio/wav")}
        requests.post("https://o2nynum8.rcsrv.net/webhook/6eb72414-2f64-45bb-88e9-e58000725f9d", 
                      files=files, data={"type": "audio"})
        st.success("Sifarişiniz mətbəxə çatdı! ✅")

# 3. Menyu Grid-i
st.subheader("Bütün Menyu")
menu = [
    {"ad": "Truffle Burger", "qiymet": "15 AZN", "sekil": "https://img.freepik.com/free-photo/gourmet-burger-with-cheese-toppings-flame-grilled-beef-patty-with-fresh-vegetables_1258-29904.jpg"},
    {"ad": "Pizza Margherita", "qiymet": "12 AZN", "sekil": "https://img.freepik.com/free-photo/top-view-pepperoni-pizza-with-mushroom-sausages-bell-pepper-olive-onion_141793-2158.jpg"},
    {"ad": "Sushi Set", "qiymet": "25 AZN", "sekil": "https://img.freepik.com/free-photo/sushi-set-with-salmon-tuna-avocado_141793-2158.jpg"}
]

cols = st.columns(3)
for i, item in enumerate(menu):
    with cols[i]:
        st.markdown(f"""
            <div class="food-card">
                <img src="{item['sekil']}" class="food-img">
                <div class="food-title">{item['ad']}</div>
                <div class="food-price">{item['qiymet']}</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"SİFARİŞ ET", key=item["ad"]):
            requests.post("https://o2nynum8.rcsrv.net/webhook/6eb72414-2f64-45bb-88e9-e58000725f9d", 
                          json={"type": "text", "message": f"Sifariş: {item['ad']}"})
            st.toast(f"{item['ad']} sifariş edildi! 🎉", icon="✅")
