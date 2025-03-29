import streamlit as st
import qrcode
from PIL import Image
import io

def create_QR_CODE(stringDataList,urlLink, bool_add_string=False):
    '''
    stringList example: stringlist=["GT-Andy\n","Email: andy_zhu@gt-global.net\n"]
    '''
    image_path=r"C:\Andy\Software_Icon\Andy1.png"
    image = Image.open(image_path)
    image = image.resize((120, 120))
    qr_code = qrcode.QRCode(version=6, box_size=20, border=10)
    # qr_code.add_data(f"GT-Andy\nEmail: andy_zhu@gt-global.net\n")  
    if bool_add_string==True:
        for s in stringDataList:
            qr_code.add_data(s)
    # for s in stringDataList:
    #     qr_code.add_data(s)
    qr_code.add_data(urlLink)
    qr_code.make(fit=True)
    qr_image = qr_code.make_image(fill_color="black", back_color="white")
    qr_image.paste(image, (80, 80))
    return qr_image
    # qr_image.save(qrcodeSavePath)   

def create_QR_CODE(urlLink):
    '''
    stringList example: stringlist=["GT-Andy\n","Email: andy_zhu@gt-global.net\n"]
    '''
    image_path=r"C:\Andy\Software_Icon\Andy1.png"
    image = Image.open(image_path)
    image = image.resize((120, 120))
    qr_code = qrcode.QRCode(version=5, box_size=20, border=10)
    # qr_code.add_data(f"GT-Andy\nEmail: andy_zhu@gt-global.net\n")  
    # if bool_add_string==True:
    #     for s in stringDataList:
    #         qr_code.add_data(s)
    # for s in stringDataList:
    #     qr_code.add_data(s)
    qr_code.add_data(urlLink)
    qr_code.make(fit=True)
    qr_image = qr_code.make_image(fill_color="black", back_color="white")
    qr_image.paste(image, (80, 80))
    return qr_image

st.set_page_config(layout="wide")

st.title("QR Code Generator")
text=st.text_input("input your text or website here")

if text:
    qr=qrcode.make(text)
    image = create_QR_CODE(urlLink=text)
    
    # Convert PIL Image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    # Display the QR code with logo
    st.image(img_byte_arr, caption="QR Code with Logo",width=400)
    
    # Convert and display the simple QR code
    # qr_byte_arr = io.BytesIO()
    # qr.get_image().save(qr_byte_arr, format='PNG')
    # qr_byte_arr = qr_byte_arr.getvalue()
    # st.image(qr_byte_arr, caption="Simple QR Code",width=200)










