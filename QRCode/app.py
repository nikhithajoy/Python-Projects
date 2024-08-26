import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

def generate_qr_code(url: str) -> Image:
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the URL data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Streamlit app
st.title("QR Code Generator")

# User input for URL
url_input = st.text_input("Enter the URL to generate a QR code:")

if st.button("Generate QR Code"):
    if url_input:
        # Generate QR code
        qr_img = generate_qr_code(url_input)
        
        # Convert the PIL image to bytes for Streamlit display
        buffer = BytesIO()
        qr_img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()
        
        # Display the QR code image
        st.image(img_bytes, caption="Generated QR Code")
        
        # Option to download the QR code image
        st.download_button(
            label="Download QR Code",
            data=img_bytes,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.error("Please enter a valid URL.")
