import streamlit as st
import qrcode
from PIL import Image
import io



st.set_page_config(layout="wide")

st.title("QR Code Generator")
text=st.text_input("input your text or website here")

if text:
    qr=qrcode.make(text)

    st.image(qr.get_image())










