import qrcode

# URL to be encoded
url = "https://www.example.com"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in the QR code grid
    border=4,  # thickness of the border (in boxes)
)

# Add the URL data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR code created and saved as 'qrcode.png'.")