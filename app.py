import streamlit as st
import requests
from streamlit_mic_recorder import mic_recorder

st.set_page_config(page_title="Mood AI Menu", layout="wide")

# CSS Dizayn
st.markdown("""
    <style>
        .food-card { background: #1e1e1e; border-radius: 15px; padding: 15px; text-align: center; border: 1px solid #333; }
        .food-img { border-radius: 10px; width: 100%; }
        .stButton button { background-color: #D4AF37; color: white; width: 100%; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# Yaddaş (Söhbət tarixçəsi)
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Salam! Mən Mood AI restoranının köməkçisiyəm. Sizə necə kömək edə bilərəm?"}]

st.title("🍽️ MOOD AI - İnteraktiv Kiosk")

# Tablar: Menyu vs Çat
tab1, tab2 = st.tabs(["📋 Menyu", "💬 Müştəri Dəstəyi"])

with tab1:
    # Menyu Grid-i (əvvəlki kimi)
    cols = st.columns(3)
    menu = [
        {"ad": "Truffle Burger", "qiymet": "15 AZN", "sekil": "https://img.freepik.com/free-photo/gourmet-burger-with-cheese-toppings-flame-grilled-beef-patty-with-fresh-vegetables_1258-29904.jpg"},
        {"ad": "Pizza Margherita", "qiymet": "12 AZN", "sekil": "https://img.freepik.com/free-photo/top-view-pepperoni-pizza-with-mushroom-sausages-bell-pepper-olive-onion_141793-2158.jpg"},
        {"ad": "Sushi Set", "qiymet": "25 AZN", "sekil": "https://img.freepik.com/free-photo/sushi-set-with-salmon-tuna-avocado_141793-2158.jpg"}
    ]
    for i, item in enumerate(menu):
        with cols[i]:
            st.image(item["sekil"], use_container_width=True)
            if st.button(f"Sifariş et: {item['ad']}"):
                requests.post("https://o2nynum8.rcsrv.net/webhook/6eb72414-2f64-45bb-88e9-e58000725f9d", json={"type": "text", "message": f"Sifariş: {item['ad']}"})
                st.toast(f"{item['ad']} sifariş edildi!", icon="✅")

with tab2:
    # Çat interfeysi
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # İstifadəçi girişi
    if prompt := st.chat_input("Sualınızı yazın..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # n8n-ə göndər və cavabı al
        with st.chat_message("assistant"):
            response = requests.post("https://o2nynum8.rcsrv.net/webhook/6eb72414-2f64-45bb-88e9-e58000725f9d", 
                                    json={"type": "text", "message": prompt})
            
            # n8n-dən gələn cavabı al (n8n "Respond to Webhook" nodu ilə cavab göndərməlidir)
            ai_reply = response.text if response.text else "Bağlantıda xəta baş verdi."
            st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
