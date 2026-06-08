import streamlit as st
from audiorecorder import audiorecorder
import requests

# Saytın ümumi görünüşü
st.set_page_config(page_title="Mood AI Menu", layout="wide")

# CSS ilə Premium Görünüş (Dizaynı göz oxşayan edən hissə)
st.markdown("""
    <style>
        .menu-card {
            border-radius: 20px;
            padding: 20px;
            background-color: #ffffff;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: 0.3s;
            margin-bottom: 20px;
            border: 1px solid #eee;
        }
        .menu-card:hover { box-shadow: 0 8px 25px rgba(0,0,0,0.2); }
        .price { color: #D4AF37; font-weight: bold; font-size: 1.2em; }
    </style>
""", unsafe_allow_html=True)

st.title("🍽️ Mood AI Restaurant Premium Menu")
st.markdown("---")

# Menyu Məlumatları
menu = [
    {"ad": "Truffle Burger", "qiymet": "15 AZN", "sekil": "https://img.freepik.com/free-photo/gourmet-burger-with-cheese-toppings-flame-grilled-beef-patty-with-fresh-vegetables_1258-29904.jpg"},
    {"ad": "Pizza Margherita", "qiymet": "12 AZN", "sekil": "https://img.freepik.com/free-photo/top-view-pepperoni-pizza-with-mushroom-sausages-bell-pepper-olive-onion_141793-2158.jpg"},
    {"ad": "Sushi Set", "qiymet": "25 AZN", "sekil": "https://img.freepik.com/free-photo/sushi-set-with-salmon-tuna-avocado_141793-2158.jpg"},
    {"ad": "Coca-Cola", "qiymet": "3 AZN", "sekil": "https://img.freepik.com/free-photo/glass-cola-with-ice-cubes_114579-459.jpg"}
]

# Grid Layout (4 sütunlu geniş görünüş)
cols = st.columns(4)
for i, item in enumerate(menu):
    with cols[i]:
        st.markdown(f"""
            <div class="menu-card">
                <img src="{item['sekil']}" style="width:100%; border-radius:15px;">
                <h3 style="margin-top:15px;">{item['ad']}</h3>
                <p class="price">{item['qiymet']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Sifariş et", key=item["ad"]):
            requests.post("https://o2nynum8.rcsrv.net/webhook/6eb72414-2f64-45bb-88e9-e58000725f9d", 
                          json={"type": "text", "message": f"Sifariş: {item['ad']}"})
            st.success("Səbətə əlavə olundu!")

st.divider()

# Səsli Sifariş (Sidebar-a keçirdik ki, əsas menyunu bağlamasın)
with st.sidebar:
    st.header("🎙️ Səslə Sifariş")
    audio = audiorecorder("Mikrofonu aktivləşdir", "Yazılır...")
    if len(audio) > 0:
        st.write("Səs göndərilir...")
        files = {"file": ("audio.wav", audio.export().read(), "audio/wav")}
        requests.post("https://o2nynum8.rcsrv.net/webhook/6eb72414-2f64-45bb-88e9-e58000725f9d", 
                      files=files, data={"type": "audio"})
        st.success("Sifarişiniz mətbəxə çatdı! ✅")
