import streamlit as st
import qrcode





st.set_page_config(layout="wide")

st.title("QR Code Generator")
text=st.text_input("input your text or website here")

if text:
    qr=qrcode.make(text)

    st.image(qr.get_image())










