import streamlit as st
import requests
from streamlit_mic_recorder import mic_recorder

# Səhifəni hazırla
st.set_page_config(page_title="Mood AI Menu", layout="wide")

st.title("🍽️ Mood AI Restaurant - Premium")

# Menyunu göstər
menu = [
    {"ad": "Truffle Burger", "qiymet": "15 AZN", "sekil": "https://img.freepik.com/free-photo/gourmet-burger-with-cheese-toppings-flame-grilled-beef-patty-with-fresh-vegetables_1258-29904.jpg"},
    {"ad": "Pizza Margherita", "qiymet": "12 AZN", "sekil": "https://img.freepik.com/free-photo/top-view-pepperoni-pizza-with-mushroom-sausages-bell-pepper-olive-onion_141793-2158.jpg"},
    {"ad": "Sushi Set", "qiymet": "25 AZN", "sekil": "https://img.freepik.com/free-photo/sushi-set-with-salmon-tuna-avocado_141793-2158.jpg"}
]

cols = st.columns(3)
for i, item in enumerate(menu):
    with cols[i]:
        st.image(item["sekil"], use_container_width=True)
        st.subheader(item["ad"])
        if st.button(f"Sifariş et: {item['ad']}", key=item["ad"]):
            requests.post("https://o2nynum8.rcsrv.net/webhook/6eb72414-2f64-45bb-88e9-e58000725f9d", 
                          json={"type": "text", "message": f"Sifariş: {item['ad']}"})
            st.success("Səbətə əlavə olundu!")

st.divider()

# Səsli Sifariş (Yeni stabil metod)
st.subheader("🎙️ Səslə Sifariş")
audio_data = mic_recorder(start_prompt="🎙️ Səsi yaz", stop_prompt="⏹️ Göndər")

if audio_data:
    st.write("Səs göndərilir...")
    # Səsi n8n-ə göndər
    files = {"file": ("audio.wav", audio_data['bytes'], "audio/wav")}
    requests.post("https://o2nynum8.rcsrv.net/webhook/6eb72414-2f64-45bb-88e9-e58000725f9d", 
                  files=files, data={"type": "audio"})
    st.success("Sifarişiniz mətbəxə çatdı! ✅")
