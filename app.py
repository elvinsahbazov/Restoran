import streamlit as st
from audiorecorder import audiorecorder
import requests

st.set_page_config(page_title="Mood AI Kiosk", page_icon="🎙️")
st.title("🎙️ Mood AI - Səsli Sifariş")

# Səs yazıcı (buna ehtiyac yoxdur, birbaşa aktivləşir)
audio = audiorecorder("Mikrofonu aktivləşdir", "Sifarişi yazmaq üçün bas")

if len(audio) > 0:
    st.success("Sifariş qeydə alındı, mətbəxə göndərilir...")
    # n8n Webhook-un bura yapışdır
    n8n_url = "https://o2nynum8.rcsrv.net/webhook/6eb72414-2f64-45bb-88e9-e58000725f9d"
    files = {"file": ("audio.wav", audio.export().read(), "audio/wav")}
    
    try:
        response = requests.post(n8n_url, files=files)
        st.balloons() # Uğurlu olduqda şık animasiya
        st.write("Sifarişiniz mətbəxdədir! ✅")
    except Exception as e:
        st.error("Bağlantı xətası baş verdi.")
