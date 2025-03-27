# Project: QR Code Encoder/Decoder
# Yeh project QR code generate aur decode karne ke liye hai.

# Required Libraries:
# is project ke liye aapko `qrcode`, `pyzbar` aur `PIL` install karni hogi.
# Install karne ke liye terminal me yeh command chalayein:
# pip install qrcode[pil] pyzbar pillow

import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def generate_qr(data, filename):
    """Diye gaye data ka QR code generate kar ke save karega."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR code '{filename}' me save ho gaya hai.")

def decode_qr(filename):
    """Diye gaye QR code image ko decode karega aur data return karega."""
    img = Image.open(filename)
    decoded_objects = decode(img)
    
    for obj in decoded_objects:
        print(f"Decoded Data: {obj.data.decode('utf-8')}")

if __name__ == "__main__":
    choice = input("QR code generate karna hai (G) ya decode karna hai (D)? ")
    if choice.lower() == 'g':
        data = input("Enter data for QR code: ")
        filename = input("Enter filename to save QR code (e.g., qr.png): ")
        generate_qr(data, filename)
    elif choice.lower() == 'd':
        filename = input("Enter QR code image filename to decode: ")
        decode_qr(filename)
    else:
        print("Invalid choice!")
